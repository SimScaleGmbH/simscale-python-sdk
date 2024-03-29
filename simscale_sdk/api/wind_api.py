# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from simscale_sdk.api_client import ApiClient
from simscale_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WindApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_wind_data(self, latitude, longitude, **kwargs): # noqa: E501
        """Get wind condition for given coordinates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wind_data(latitude, longitude, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str latitude: Latitude coordinate in WGS84 format (required)
        :param str longitude: Longitude coordinate in WGS84 format (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WindRoseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_wind_data_with_http_info(latitude, longitude, **kwargs)  # noqa: E501

    def get_wind_data_with_http_info(self, latitude, longitude, **kwargs):  # noqa: E501
        """Get wind condition for given coordinates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wind_data_with_http_info(latitude, longitude, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str latitude: Latitude coordinate in WGS84 format (required)
        :param str longitude: Longitude coordinate in WGS84 format (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WindRoseResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'latitude',
            'longitude'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wind_data" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'latitude' is set
        if self.api_client.client_side_validation and ('latitude' not in local_var_params or  # noqa: E501
                                                        local_var_params['latitude'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `latitude` when calling `get_wind_data`")  # noqa: E501
        # verify the required parameter 'longitude' is set
        if self.api_client.client_side_validation and ('longitude' not in local_var_params or  # noqa: E501
                                                        local_var_params['longitude'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `longitude` when calling `get_wind_data`")  # noqa: E501

        if self.api_client.client_side_validation and ('latitude' in local_var_params and  # noqa: E501
                                                        len(local_var_params['latitude']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `latitude` when calling `get_wind_data`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('longitude' in local_var_params and  # noqa: E501
                                                        len(local_var_params['longitude']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `longitude` when calling `get_wind_data`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'latitude' in local_var_params and local_var_params['latitude'] is not None:  # noqa: E501
            query_params.append(('latitude', local_var_params['latitude']))  # noqa: E501
        if 'longitude' in local_var_params and local_var_params['longitude'] is not None:  # noqa: E501
            query_params.append(('longitude', local_var_params['longitude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/winddata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WindRoseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
