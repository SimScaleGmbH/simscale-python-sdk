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


class GeometriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_geometries(self, project_id, **kwargs): # noqa: E501
        """List geometries within a project  # noqa: E501

        Only valid geometries that can be used for a simulation setup are included.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometries(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param int limit: The number of items to return.
        :param int page: The page number. Use in combination with limit.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Geometries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_geometries_with_http_info(project_id, **kwargs)  # noqa: E501

    def get_geometries_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """List geometries within a project  # noqa: E501

        Only valid geometries that can be used for a simulation setup are included.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometries_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param int limit: The number of items to return.
        :param int page: The page number. Use in combination with limit.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Geometries, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'limit',
            'page'
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
                    " to method get_geometries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_geometries`")  # noqa: E501

        if self.api_client.client_side_validation and 'project_id' in local_var_params and not re.search(r'^\d+$', local_var_params['project_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project_id` when calling `get_geometries`, must conform to the pattern `/^\d+$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_geometries`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_geometries`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_geometries`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_geometries`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            '/projects/{projectId}/geometries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geometries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_geometry(self, project_id, geometry_id, **kwargs): # noqa: E501
        """Get information about the geometry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry(project_id, geometry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_id: The geometry ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Geometry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_geometry_with_http_info(project_id, geometry_id, **kwargs)  # noqa: E501

    def get_geometry_with_http_info(self, project_id, geometry_id, **kwargs):  # noqa: E501
        """Get information about the geometry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_with_http_info(project_id, geometry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_id: The geometry ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Geometry, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'geometry_id'
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
                    " to method get_geometry" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_geometry`")  # noqa: E501
        # verify the required parameter 'geometry_id' is set
        if self.api_client.client_side_validation and ('geometry_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry_id` when calling `get_geometry`")  # noqa: E501

        if self.api_client.client_side_validation and 'project_id' in local_var_params and not re.search(r'^\d+$', local_var_params['project_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project_id` when calling `get_geometry`, must conform to the pattern `/^\d+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501
        if 'geometry_id' in local_var_params:
            path_params['geometryId'] = local_var_params['geometry_id']  # noqa: E501

        query_params = []

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
            '/projects/{projectId}/geometries/{geometryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geometry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_geometry_mappings(self, project_id, geometry_id, **kwargs): # noqa: E501
        """Describe id mapping of the geometry  # noqa: E501

        Assignment of topological entities (faces, bodies) in the simulation setup is a non-trivial task. Complex models can consist of several assemblies which may contain multiple occurrences of bodies and their entities. In order to describe an assignment unambiguously the full path from the root part of the model to the actual topological entity is required.  SimScale generates unique internal names for all topological entities of a model during the geometry import which are used for assignments within the simulation spec. Examples of internal names are `B1_TE5` or `A1_I26_A5_I27_B102_TE196`.  This API endpoint allows to retrieve a mapping between the internal names and a detailed description of the entities which includes: * The topological entity class (body or face) * The original body and entity names * Entity attributes like `SDL/TYSA_NAME`, `SDL/TYSA_UNAME`, `ATTRIB_XPARASOLID_NAME` or `SDL/TYSA_COLOUR` * The path from the root of the model  Please note that during geometry import the model's topology can be modified (e.g. facet split and other import options) which means that there is no 1:1 mapping between the internal and original names.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_mappings(project_id, geometry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_id: The geometry ID (required)
        :param int limit: The number of items to return.
        :param int page: The page number. Use in combination with limit.
        :param str _class: The entity class to filter.
        :param list[str] bodies: The body names to filter. If multiple body names are provided any match.
        :param list[str] entities: The entity names to filter. If multiple entity names are provided any match.
        :param list[str] attributes: The attribute names to filter. If multiple attribute names are provided any match.
        :param list[str] values: The attribute values to filter. If multiple attribute values are provided any match.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GeometryMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_geometry_mappings_with_http_info(project_id, geometry_id, **kwargs)  # noqa: E501

    def get_geometry_mappings_with_http_info(self, project_id, geometry_id, **kwargs):  # noqa: E501
        """Describe id mapping of the geometry  # noqa: E501

        Assignment of topological entities (faces, bodies) in the simulation setup is a non-trivial task. Complex models can consist of several assemblies which may contain multiple occurrences of bodies and their entities. In order to describe an assignment unambiguously the full path from the root part of the model to the actual topological entity is required.  SimScale generates unique internal names for all topological entities of a model during the geometry import which are used for assignments within the simulation spec. Examples of internal names are `B1_TE5` or `A1_I26_A5_I27_B102_TE196`.  This API endpoint allows to retrieve a mapping between the internal names and a detailed description of the entities which includes: * The topological entity class (body or face) * The original body and entity names * Entity attributes like `SDL/TYSA_NAME`, `SDL/TYSA_UNAME`, `ATTRIB_XPARASOLID_NAME` or `SDL/TYSA_COLOUR` * The path from the root of the model  Please note that during geometry import the model's topology can be modified (e.g. facet split and other import options) which means that there is no 1:1 mapping between the internal and original names.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_mappings_with_http_info(project_id, geometry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_id: The geometry ID (required)
        :param int limit: The number of items to return.
        :param int page: The page number. Use in combination with limit.
        :param str _class: The entity class to filter.
        :param list[str] bodies: The body names to filter. If multiple body names are provided any match.
        :param list[str] entities: The entity names to filter. If multiple entity names are provided any match.
        :param list[str] attributes: The attribute names to filter. If multiple attribute names are provided any match.
        :param list[str] values: The attribute values to filter. If multiple attribute values are provided any match.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GeometryMappings, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'geometry_id',
            'limit',
            'page',
            '_class',
            'bodies',
            'entities',
            'attributes',
            'values'
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
                    " to method get_geometry_mappings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_geometry_mappings`")  # noqa: E501
        # verify the required parameter 'geometry_id' is set
        if self.api_client.client_side_validation and ('geometry_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry_id` when calling `get_geometry_mappings`")  # noqa: E501

        if self.api_client.client_side_validation and 'project_id' in local_var_params and not re.search(r'^\d+$', local_var_params['project_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project_id` when calling `get_geometry_mappings`, must conform to the pattern `/^\d+$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_geometry_mappings`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_geometry_mappings`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_geometry_mappings`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_geometry_mappings`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501
        if 'geometry_id' in local_var_params:
            path_params['geometryId'] = local_var_params['geometry_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if '_class' in local_var_params and local_var_params['_class'] is not None:  # noqa: E501
            query_params.append(('class', local_var_params['_class']))  # noqa: E501
        if 'bodies' in local_var_params and local_var_params['bodies'] is not None:  # noqa: E501
            query_params.append(('bodies', local_var_params['bodies']))  # noqa: E501
            collection_formats['bodies'] = 'multi'  # noqa: E501
        if 'entities' in local_var_params and local_var_params['entities'] is not None:  # noqa: E501
            query_params.append(('entities', local_var_params['entities']))  # noqa: E501
            collection_formats['entities'] = 'multi'  # noqa: E501
        if 'attributes' in local_var_params and local_var_params['attributes'] is not None:  # noqa: E501
            query_params.append(('attributes', local_var_params['attributes']))  # noqa: E501
            collection_formats['attributes'] = 'multi'  # noqa: E501
        if 'values' in local_var_params and local_var_params['values'] is not None:  # noqa: E501
            query_params.append(('values', local_var_params['values']))  # noqa: E501
            collection_formats['values'] = 'multi'  # noqa: E501

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
            '/projects/{projectId}/geometries/{geometryId}/mappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GeometryMappings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_geometry(self, project_id, geometry_id, geometry, **kwargs): # noqa: E501
        """Update geometry information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_geometry(project_id, geometry_id, geometry, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_id: The geometry ID (required)
        :param Geometry geometry: Geometry information to be updated (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_geometry_with_http_info(project_id, geometry_id, geometry, **kwargs)  # noqa: E501

    def update_geometry_with_http_info(self, project_id, geometry_id, geometry, **kwargs):  # noqa: E501
        """Update geometry information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_geometry_with_http_info(project_id, geometry_id, geometry, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_id: The geometry ID (required)
        :param Geometry geometry: Geometry information to be updated (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'geometry_id',
            'geometry'
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
                    " to method update_geometry" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `update_geometry`")  # noqa: E501
        # verify the required parameter 'geometry_id' is set
        if self.api_client.client_side_validation and ('geometry_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry_id` when calling `update_geometry`")  # noqa: E501
        # verify the required parameter 'geometry' is set
        if self.api_client.client_side_validation and ('geometry' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry` when calling `update_geometry`")  # noqa: E501

        if self.api_client.client_side_validation and 'project_id' in local_var_params and not re.search(r'^\d+$', local_var_params['project_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project_id` when calling `update_geometry`, must conform to the pattern `/^\d+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501
        if 'geometry_id' in local_var_params:
            path_params['geometryId'] = local_var_params['geometry_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'geometry' in local_var_params:
            body_params = local_var_params['geometry']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/geometries/{geometryId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
