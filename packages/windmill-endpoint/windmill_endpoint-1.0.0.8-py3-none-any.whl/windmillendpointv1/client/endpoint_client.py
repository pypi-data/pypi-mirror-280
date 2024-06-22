# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright(C) 2023 baidu, Inc. All Rights Reserved

# @Time : 2023/9/15 14:13
# @Author : yangtingyu01
# @Email: yangtingyu01@baidu.com
# @File : endpoint_client.py
# @Software: PyCharm
"""
import json
from multidict import MultiDict
from typing import Optional
from baidubce.http import http_methods
from bceinternalsdk.client.bce_internal_client import BceInternalClient
from bceinternalsdk.client.paging import PagingRequest
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration


class EndpointClient(BceInternalClient):
    """
    A client class for interacting with the endpoint service. Initializes with default configuration.

    This client provides an interface to interact with the endpoint service using BCE (Baidu Cloud Engine) API.
    It supports operations related to creating and retrieving endpoint within a specified workspace.

    Args:
        config (Optional[BceClientConfiguration]): The client configuration to use.
        ak (Optional[str]): Access key for authentication.
        sk (Optional[str]): Secret key for authentication.
        endpoint (Optional[str]): The service endpoint URL.
    """

    def __init__(self, config: Optional[BceClientConfiguration] = None, ak: Optional[str] = "",
                 sk: Optional[str] = "", endpoint: Optional[str] = ""):
        """
        init the client with default configuration
        """
        if config is None:
            config = BceClientConfiguration(credentials=BceCredentials(ak, sk), endpoint=endpoint)
        super(EndpointClient, self).__init__(config=config)

    def list_endpoint(self, workspace_id: str, endpoint_hub_name: str, kind: Optional[str] = "",
                      category: Optional[str] = "", tags: Optional[str] = "",
                      filter_param: Optional[str] = "", page_request: Optional[PagingRequest] = PagingRequest()):
        """

        Lists endpoint in the system.

        Args:
            workspace_id (str): 工作区 id
            endpoint_hub_name (str): 端点中心名称
            kind: 类型
            category (str, optional): 按类别筛选
            tags (str, optional): 按版本标签筛选
            filter_param (str, optional): 搜索条件，支持系统名称、模型名称、描述。
            page_request (PagingRequest, optional): 分页请求配置。默认为 PagingRequest()。
        Returns:
            HTTP request response
        """
        params = MultiDict()
        params.add("pageNo", str(page_request.get_page_no()))
        params.add("pageSize", str(page_request.get_page_size()))
        params.add("order", page_request.order)
        params.add("orderBy", page_request.orderby)
        params.add("filter", filter_param)
        params.add("kind", str(kind))
        if category:
            for i in category:
                params.add("categories", i)
        if tags:
            for i in tags:
                params.add("tags", i)
        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs/" + endpoint_hub_name + "/endpoints", encoding="utf-8"),
                                  params=params)

    def get_endpoint(self, workspace_id: str, endpoint_hub_name: str, local_name: str):
        """
        get endpoint in the system.

        Args:
            workspace_id (str): 工作区 id
            endpoint_hub_name (str): 端点中心名称
            local_name: 名称
        Returns:
            HTTP request response
        """
        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs/" + endpoint_hub_name + "/endpoints/"
                                             + local_name, encoding="utf-8"))

    """
    deploy_endpoint_job api
    """
    def get_deploy_endpoint_job(self, workspace_id: str, endpoint_hub_name: str, local_name: str):
        """
        get deploy endpoint job

        Args:
            workspace_id (str): 工作区 id
            endpoint_hub_name (str): 端点中心名称
            local_name: 名称
        Returns:
            HTTP request response
        """
        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs/" + endpoint_hub_name + "/jobs/" + local_name,
                                             encoding="utf-8"))

    def list_deployment(self, workspace_id: str,
                        endpoint_hub_name: str,
                        f: Optional[str] = "",
                        server_kind: Optional[str] = "",
                        spec_kind: Optional[str] = "",
                        page_request: Optional[PagingRequest] = PagingRequest()):
        """

        :param page_request:
        :param spec_kind:
        :param server_kind:
        :param f:
        :param workspace_id:
        :param endpoint_hub_name:
        :return:
        """
        params = MultiDict()
        params.add("pageNo", str(page_request.get_page_no()))
        params.add("pageSize", str(page_request.get_page_size()))
        params.add("order", page_request.order)
        params.add("orderBy", page_request.orderby)
        params.add("filter", f)
        params.add("specKind", str(spec_kind))

        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs/" + endpoint_hub_name +
                                             "/deployments", encoding="utf-8"),
                                  params=params)

    """
    endpoint_hub_api
    """
    def list_endpoint_hub(self, workspace_id: str,
                          f: Optional[str] = "",
                          page_request: Optional[PagingRequest] = PagingRequest()):
        """
        Lists endpoint hub in the system.
        Args:
            workspace_id (str): 工作区 id
            f (str): 过滤参数
            page_request: 分页参数
        Returns:
            HTTP request response
        """
        params = MultiDict()
        params.add("pageNo", str(page_request.get_page_no()))
        params.add("pageSize", str(page_request.get_page_size()))
        params.add("order", page_request.order)
        params.add("orderBy", page_request.orderby)
        params.add("filter", f)

        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs", encoding="utf-8"),
                                  params=params)

    def get_endpoint_hub(self, workspace_id: str, local_name: str):
        """
        get endpoint hub in the system.
        Args:
            workspace_id (str): 工作区 id
            local_name(str): 名称
        Returns:
            HTTP request response
        """

        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs/" + local_name, encoding="utf-8"))
    """
    deployment api
    """
    def get_deployment(self, workspace_id: str, endpoint_hub_name: str, local_name: str):
        """
        get deployment in the system.
         Args:
            workspace_id (str): 工作区 id
            endpoint_hub_name (str): 端点中心名称
            local_name: 名称
        Returns:
            HTTP request response
        """
        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/workspaces/" + workspace_id +
                                             "/endpointhubs/" + endpoint_hub_name + "/deployments/" + local_name,
                                             encoding="utf-8"))
