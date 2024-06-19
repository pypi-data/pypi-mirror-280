import json
import re
from typing import (
    Any,
    AsyncIterator,
    Dict,
    Iterator,
    List,
    Optional, Union, Type,
)
import aiohttp
import httpx
import requests
from langchain_core.callbacks import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from langchain_core.language_models import LanguageModelInput
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk
from langchain_core.pydantic_v1 import Field
from langchain_core.runnables import Runnable
from pydantic import BaseModel
from ratelimit import limits, sleep_and_retry

from agent.exception.custom_exception import CommonException
from agent.service.llm.custom_model import CustomModel
from agent.utils.dde_logger import dde_logger as logger
from agent.utils.nacos_util import get_system_config_from_nacos
from agent.utils.http_util import async_http_post

global call_limits
global llm_call_period
try:
    system_config = get_system_config_from_nacos()
    call_limits = system_config['limits']['call_limits']
    llm_call_period = system_config['limits']['llm_call_period']
except Exception as e:
    call_limits = 25
    llm_call_period = 1


class LangchainGeoGPTNew(LLM, CustomModel):
    def __init__(self, endpoint: str, *, streaming: bool = True, model: str = "Geogpt", system: Optional[str] = None,
                 history: Optional[list[list[str]]] = None, max_output_length: int = 3000,
                 template_name: str = "geogpt", temperature: Optional[float] = None):
        if history is None:
            history = []
        kwargs = {"endpoint": endpoint, " streaming": streaming, "model": model, "system": system,
                  "history": history, "max_output_length": max_output_length,
                  "template_name": template_name, "temperature": temperature}
        super().__init__(**kwargs)
        self.endpoint = endpoint.strip()
        self.streaming = streaming
        self.model = model
        self.system = system
        self.max_output_length = max_output_length
        self.template_name = template_name
        history_format = []
        for item in history:
            if item[1] is not None:
                tmp_history = {
                    "user": item[0],
                    "bot": item[1]
                }
                history_format.append(tmp_history)
        self.history = history_format

    init_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """init kwargs for qianfan client init, such as `query_per_second` which is 
        associated with qianfan resource object to limit QPS"""

    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """extra params for model invoke using with `do`."""

    client: Any

    streaming: Optional[bool] = True
    """Whether to stream the results or not."""

    model: str
    """Model name. 
    `model` will be ignored if `endpoint` is set
    """
    is_ok: bool = False  # 是否正确返回reference
    endpoint: str
    """Endpoint of the GeoGPT LLM, required if custom model used."""

    request_timeout: Optional[int] = 60
    """request timeout for chat http requests"""
    prompt: Optional[str]
    system: Optional[str]
    history: list[list[str]]
    max_output_length: int
    template_name: str

    top_p: Optional[float] = 0.8
    temperature: Optional[float]
    frequency_penalty: Optional[float] = 0.0
    best_of: Optional[int] = 1
    use_beam_search: Optional[bool] = False
    presence_penalty: Optional[float] = 1.0
    top_k: Optional[int] = -1
    length_penalty: Optional[float] = 1.0

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            **{"endpoint": self.endpoint, "model": self.model},
            **super()._identifying_params,
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "GeoGPT"

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling Qianfan API."""
        normal_params = {
            "system": self.system,
            "history": self.history,
            "endpoint": self.endpoint,
            "stream": self.streaming,
            "max_output_length": self.max_output_length,
            "template_name": self.template_name,
            "temperature": self.temperature
        }

        return {**normal_params, **self.model_kwargs}

    def _convert_prompt_msg_params(
            self,
            prompt: str,
            **kwargs: Any,
    ) -> dict:
        if "streaming" in kwargs:
            kwargs["stream"] = kwargs.pop("streaming")
        return {
            **{"prompt": prompt},
            **self._default_params,
            **kwargs,
        }

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        """Call out to an LLM models endpoint for each generation with a prompt.
        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.
        Returns:
            The string generated by the model.
        """
        if self.streaming:
            return ""
        params = self._convert_prompt_msg_params(prompt, **kwargs)
        response_payload = self.http_request(**params)
        return response_payload["data"]["output"]

    @limits(calls=call_limits, period=llm_call_period, raise_on_limit=True)
    async def _acall(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        logger.info(
            f"current time for LangchainGeoGPTNew._acall limits {call_limits} in {llm_call_period}s")

        params = self._convert_prompt_msg_params(prompt, **kwargs)
        response_payload = await self.async_http_request(**params)
        return response_payload["data"]["output"]

    def _stream(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        logger.error("检查streaming接口传了没，streaming默认为True")
        yield GenerationChunk(text="")

    @limits(calls=call_limits, period=llm_call_period, raise_on_limit=True)
    async def _astream(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> AsyncIterator[GenerationChunk]:
        logger.info(f"current time for LangchainGeoGPTNew limits._astream limits {call_limits} in {llm_call_period}s")
        params = self._convert_prompt_msg_params(prompt, **{**kwargs, "stream": True})
        data = self.generate_parameters(**params)
        delimiter = b'\x00'
        buffer = b''
        # 使用httpx.AsyncClient进行异步请求
        async with httpx.AsyncClient() as client:
            try:
                async with client.stream('POST', self.endpoint, json=data) as response:
                    if response.status_code != 200:
                        logger.error(f"调用大模型{self.model}出错，返回为[{response}]")
                        raise CommonException()

                    # 异步迭代处理流式数据
                    async for chunk in response.aiter_bytes():
                        buffer += chunk
                        while delimiter in buffer:
                            message, buffer = buffer.split(delimiter, 1)
                            if message:
                                ret = json.loads(message.decode())
                                logger.debug(f'data: {ret}')
                                res = ret.get("output", "")

                                # 替换字符串中的[[citation:*]]为<sup>[*]</sup>
                                pattern = r"\[\[citation:(\d+)\]\]"
                                replacement = r"<sup>[\1]</sup>"  # 前端上标标签
                                res = re.sub(pattern, replacement, res)

                                logger.debug(res)
                                yield GenerationChunk(text=res)
            except httpx.HTTPError as e:
                logger.error(f'HTTP error occurred: {e}')
            except Exception as e:
                logger.error(f'An error occurred: {e}')

    @staticmethod
    def generate_parameters(prompt, system, history, endpoint, stream, max_output_length, template_name, temperature):
        model_params = {
        }
        service_params = {
            "promptTemplateName": template_name,
            "stream": stream,
            "maxOutputLength": max_output_length
        }
        if temperature is not None:
            model_params.update({"temperature": temperature})
        if system is not None:
            service_params.update({"system": system})
        data = {
            "input": prompt,
            "serviceParams": service_params,
            "history": history,
            "modelParams": model_params
        }
        data_log = {
            "input": prompt[:2000],
            "serviceParams": service_params,
            "history": history,
            "modelParams": model_params
        }
        logger.info(f"调用大模型的endpoint为：{endpoint},参数为：{data_log}")
        return data

    @staticmethod
    def http_request(prompt, system, history, endpoint, stream, max_output_length, template_name, temperature):
        model_params = {
        }
        service_params = {
            "promptTemplateName": template_name,
            "stream": stream,
            "maxOutputLength": max_output_length
        }
        if temperature is not None:
            model_params.update({"temperature": temperature})
        if system is not None:
            service_params.update({"system": system})
        data = {
            "input": prompt,
            "serviceParams": service_params,
            "history": history,
            "modelParams": model_params
        }
        data_log = {
            "input": prompt[:2000],
            "serviceParams": service_params,
            "history": history,
            "modelParams": model_params
        }
        logger.info(f"调用大模型的endpoint为：{endpoint},参数为：{data_log}")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'text/event-stream'
        }
        response = requests.post(endpoint, json=data, headers=headers, stream=stream)
        if stream:
            return response
        else:
            return json.loads(response.content)

    @staticmethod
    async def async_http_request(prompt, system, history, endpoint, stream, max_output_length, template_name,
                                 temperature):
        model_params = {
        }
        service_params = {
            "promptTemplateName": template_name,
            "stream": stream,
            "maxOutputLength": max_output_length
        }
        if temperature is not None:
            model_params.update({"temperature": temperature})
        if system is not None:
            service_params.update({"system": system})
        data = {
            "input": prompt,
            "serviceParams": service_params,
            "history": history,
            "modelParams": model_params
        }
        logger.info(f"调用大模型的endpoint为：{endpoint},参数为：{data}")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'text/event-stream'
        }
        response = await async_http_post(url=endpoint, data=data, headers=headers)
        return response

    @staticmethod
    def ahttp_request_stream(prompt, system, history, endpoint, stream, max_output_length, template_name, temperature):
        model_params = {
        }
        service_params = {
            "promptTemplateName": template_name,
            "stream": stream,
            "maxOutputLength": max_output_length
        }
        if temperature is not None:
            model_params.update({"temperature": temperature})
        if system is not None:
            service_params.update({"system": system})
        data = {
            "input": prompt,
            "serviceParams": service_params,
            "history": history,
            "modelParams": model_params
        }
        logger.info(f"调用大模型的endpoint为：{endpoint},参数为：{data}")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'text/event-stream'
        }
        sseresp = aiohttp.request("POST", endpoint, headers=headers, data=json.dumps(data))
        return sseresp

    def with_structured_output(self, schema: Union[Dict, Type[BaseModel]], **kwargs: Any) -> Runnable[
        LanguageModelInput, Union[Dict, BaseModel]]:
        pass

    # 新大模型默认不需要system和prompt改造
    @staticmethod
    def deal_prompt(prompt: str):
        # tem_prompt = prompt.split("#System#")[-1]
        # prompt_list = tem_prompt.split("#Input#")
        return None, None


def tets():
    cus = LangchainGeoGPTNew("http://47.242.190.148:8001/llm/generate")
    cus.streaming = True
    for chunk in cus.stream("tell me how to study English for Chinese"):
        yield chunk


#
# if __name__ == '__main__':
#     loop1 = asyncio.new_event_loop()  # 创建一个事件循环
#     asyncio.set_event_loop(loop1)
#     loop = asyncio.get_event_loop()  # 创建一个事件循环
#     loop.run_until_complete(tets())  # 将协程加入到事件循环loop
#     loop.close()

if __name__ == '__main__':
    cus = LangchainGeoGPTNew(endpoint="http://10.108.0.24:30292/llm/generate",
                             max_output_length=32768, template_name="geogpt_customized", temperature=0.0,
                             streaming=False)
    input = "who are you"
    rs = cus.invoke(input)
    print(rs)
    # from lan cus = LangchainGeoGPTNew("http://47.242.190.148:8001/llm/generate")gchain_openai import ChatOpenAI
    # # # llm = LangchainGeoGPT(streaming=False, endpoint="http://3.238.17.153:8001/llm/generate")
    # os.environ["OPENAI_API_KEY"] = "sk-jDj1xziPIhDVP54e1c0cCcB4429640Fe9aCc3990357bF802"
    # os.environ["OPENAI_BASE_URL"]="https://openai.sohoyo.io/v1"
    # llm = ChatOpenAI(temperature=0.9)
    # llm.model_name = "gpt-4"
    # print(llm.invoke("hello"))
