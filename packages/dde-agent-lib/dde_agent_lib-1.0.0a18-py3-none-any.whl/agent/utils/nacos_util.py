import os
from typing import Any
import yaml
import nacos

from agent.config.app_config import get_app_config
from agent.utils.dde_logger import dde_logger as logger

system_config_from_nacos = None
global_client_storage = None
global_client_cron = None


def get_the_new_nacos_config():
    """
    将启动的实例注册到nacos上，以供portal后端通过nacos调用
    """
    app_configs = get_app_config()
    # 先从环境变量中获取nacos信息，如果为None，则从配置文件yaml中获取nacos信息
    nacos_group = os.environ.get('dde_nacos_group')
    if nacos_group is None:
        nacos_group = app_configs['nacos']['dde_nacos_group']
    nacos_namespace = os.environ.get('dde_nacos_namespace')
    if nacos_namespace is None:
        nacos_namespace = app_configs['nacos']['dde_nacos_namespace']
    nacos_server_address = os.environ.get('dde_nacos_addr')
    if nacos_server_address is None:
        nacos_server_address = app_configs['nacos']['dde_nacos_addr']
    global global_client_storage
    if (global_client_storage is None):
        global_client_storage = nacos.NacosClient(nacos_server_address, namespace=nacos_namespace)
        logger.debug("Nacos global_client_storage为None，需要进行初始化")
    else:
        logger.debug(f"Nacos global_client_storage[{global_client_storage}]已经初始化，无需再次初始化")
    # client = nacos.NacosClient(nacos_server_address, namespace=nacos_namespace)
    logger.info('nacos addr: %s, nacos group: %s, nacos namespace: %s,', nacos_server_address, nacos_group,
                nacos_namespace)
    # 定义服务实例参数
    service_name = app_configs['nacos']['dde_instance_name']
    data_id = service_name + '.yaml'
    system_config = global_client_storage.get_config(data_id, nacos_group, 20, None)
    system_config_yaml = yaml.safe_load(system_config)
    return system_config_yaml


def get_system_config_from_nacos():
    """从全局安全变量config_from_nacos中，线程安全读取nacos系统配置"""
    global system_config_from_nacos
    if (system_config_from_nacos is None):
        system_config_from_nacos = get_the_new_nacos_config()
    return system_config_from_nacos


def get_config_from_nacos_every_10_seconds():
    try:
        """
        每10秒从nacos上拉取配置，然后推送到原本的system_config_from_nacos中
        """
        app_configs = get_app_config()
        # 先从环境变量中获取nacos信息，如果为None，则从配置文件yaml中获取nacos信息
        nacos_group = os.environ.get('dde_nacos_group')
        if nacos_group is None:
            nacos_group = app_configs['nacos']['dde_nacos_group']
        nacos_namespace = os.environ.get('dde_nacos_namespace')
        if nacos_namespace is None:
            nacos_namespace = app_configs['nacos']['dde_nacos_namespace']
        nacos_server_address = os.environ.get('dde_nacos_addr')
        if nacos_server_address is None:
            nacos_server_address = app_configs['nacos']['dde_nacos_addr']
        global global_client_cron
        if (global_client_cron is None):
            global_client_cron = nacos.NacosClient(nacos_server_address, namespace=nacos_namespace)
        service_name = app_configs['nacos']['dde_instance_name']
        data_id = service_name + '.yaml'
        system_config = global_client_cron.get_config(data_id, nacos_group, 20, None)
        if (system_config is not None):
            system_config_yaml = yaml.safe_load(system_config)
            insert_system_config_from_nacos(system_config_yaml)
    except Exception as e:
        logger.error(e)


def insert_system_config_from_nacos(config: Any):
    """系统配置信息放在nacos上，如果nacos配置修改，观察者的回调函数会将新的nacos配置放入全局安全变量中"""
    global system_config_from_nacos
    # with lock:
    system_config_from_nacos = config
