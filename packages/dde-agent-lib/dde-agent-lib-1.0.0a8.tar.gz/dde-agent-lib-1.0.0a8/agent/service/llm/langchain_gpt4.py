import os
from io import StringIO

from langchain.schema import (
    HumanMessage,
    SystemMessage,
    AIMessage
)

from langchain_openai import ChatOpenAI


class LangchainGpt4:

    def __init__(self, endpoint, *, streaming=True, model="gpt-4", history=None, retrieve_doc_context: str):
        os.environ["OPENAI_API_KEY"] = "sk-jDj1xziPIhDVP54e1c0cCcB4429640Fe9aCc3990357bF802"
        # os.environ["OPENAI_BASE_URL"] = "https://openai.sohoyo.io/v1"
        os.environ["OPENAI_BASE_URL"] = endpoint.strip()
        llm = ChatOpenAI(temperature=0.7, streaming=streaming)
        llm.model_name = model
        self.llm = llm
        self.input = "Please answer the professional question: {} \n in the field of geoscience based on " \
                     "following reference: " + retrieve_doc_context + ". \n If the reference is not relevant to the " \
                     "question, answer according to your own expertise. "
        messages = []
        system = SystemMessage(
            content="You are an expert and an assistant in geoscience. You have the following conversation with "
                    "the user, please continue. ")
        messages.append(system)
        if history is None:
            history = []
        for item in history:
            if item[1] is not None:
                hum_msg = HumanMessage(item[0])
                ass_msg = AIMessage(item[1])
                messages.append(hum_msg)
                messages.append(ass_msg)
        self.messages = messages

    is_ok: bool = False

    def invoke(self, prompt: str):
        self.deal_prompt(prompt)
        return self.llm.invoke(self.messages)

    async def astream(self, prompt: str):
        self.deal_prompt(prompt)
        with StringIO() as str_io:
            async for msg in self.llm.astream(self.messages):
                msg = msg.content
                str_io.write(msg)
                # if self.is_target(msg):
                yield str_io.getvalue()

    def is_target(self, msg: str) -> bool:
        target = [".", "!", "?", "。", "！", "？"]
        return msg in target

    def deal_prompt(self, prompt):
        hum_msg = HumanMessage(self.input.format(prompt))
        ass_msg = AIMessage("")
        self.messages.append(hum_msg)
        self.messages.append(ass_msg)


if __name__ == '__main__':
    # # llm = LangchainGeoGPT(streaming=False, endpoint="http://3.238.17.153:8001/llm/generate")
    os.environ["OPENAI_API_KEY"] = "sk-jDj1xziPIhDVP54e1c0cCcB4429640Fe9aCc3990357bF802"
    os.environ["OPENAI_BASE_URL"] = "https://openai.sohoyo.io/v1"
    llm = ChatOpenAI(temperature=0)
    llm.model_name = "gpt-4"

    messages = [
        SystemMessage(content="你是一个很棒的智能助手"),
        HumanMessage(content="请给我的花店起个名")
    ]

    print(llm.invoke(messages))