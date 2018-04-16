# coding: utf-8

"""
    Swagger Petstore

    This is a sample Petstore server.  You can find  out more about Swagger at  [http://swagger.io](http://swagger.io) or on  [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_pets_by_status(self, status, **kwargs):  # noqa: E501
        """Finds Pets by status  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_pets_by_status(status, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_pets_by_status_with_http_info(status, **kwargs)  # noqa: E501
        else:
            (data) = self.find_pets_by_status_with_http_info(status, **kwargs)  # noqa: E501
            return data

    def find_pets_by_status_with_http_info(self, status, **kwargs):  # noqa: E501
        """Finds Pets by status  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_pets_by_status_with_http_info(status, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_pets_by_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `find_pets_by_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
            collection_formats['status'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/test', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Pet]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
