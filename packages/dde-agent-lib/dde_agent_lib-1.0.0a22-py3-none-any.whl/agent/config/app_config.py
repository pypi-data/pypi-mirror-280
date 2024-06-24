import os

import yaml

# 根据环境变量ENVIRONMENT区分加载的yaml配置文件
_app_config = None
_app_environment = None


def get_app_config():
    """
      根据环境变量ENVIRONMENT判断开发、测试、生产环境，并将对应的yaml文件加载为app_config配置
    返回值: yaml配置
    """
    global _app_config
    global _app_environment

    # 如果配置已经加载，且环境未发生变化，直接返回配置，避免每次加载配置
    environment = os.environ.get("ENVIRONMENT")
    if _app_config is not None and environment == _app_environment:
        return _app_config
    if environment == "dev":
        with open(__file__.replace("app_config.py", "app_dev.yaml")) as f:
            _app_config = yaml.safe_load(f)
    elif environment == "test":
        with open(__file__.replace("app_config.py", "app_test.yaml")) as f:
            _app_config = yaml.safe_load(f)
    elif environment == "prod":
        with open(__file__.replace("app_config.py", "app_prod.yaml")) as f:
            _app_config = yaml.safe_load(f)
    elif environment == "pre_prod":
        with open(__file__.replace("app_config.py", "app_pre_prod.yaml")) as f:
            _app_config = yaml.safe_load(f)
    else:
        raise ValueError("Unknown environment.")
    _app_environment = environment
    return _app_config
