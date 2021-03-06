# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SensorEventApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sensor_event_all_by_participant(self, participant_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_all_by_participant  # noqa: E501

        Get the set of all sensor events produced by the given participant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_all_by_participant(participant_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str participant_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sensor_event_all_by_participant_with_http_info(participant_id, origin, _from, to, **kwargs)  # noqa: E501

    def sensor_event_all_by_participant_with_http_info(self, participant_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_all_by_participant  # noqa: E501

        Get the set of all sensor events produced by the given participant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_all_by_participant_with_http_info(participant_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str participant_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[object], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['participant_id', 'origin', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensor_event_all_by_participant" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'participant_id' is set
        if self.api_client.client_side_validation and ('participant_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['participant_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `participant_id` when calling `sensor_event_all_by_participant`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if self.api_client.client_side_validation and ('origin' not in local_var_params or  # noqa: E501
                                                        local_var_params['origin'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `origin` when calling `sensor_event_all_by_participant`")  # noqa: E501
        # verify the required parameter '_from' is set
        if self.api_client.client_side_validation and ('_from' not in local_var_params or  # noqa: E501
                                                        local_var_params['_from'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `_from` when calling `sensor_event_all_by_participant`")  # noqa: E501
        # verify the required parameter 'to' is set
        if self.api_client.client_side_validation and ('to' not in local_var_params or  # noqa: E501
                                                        local_var_params['to'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to` when calling `sensor_event_all_by_participant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'participant_id' in local_var_params:
            path_params['participant_id'] = local_var_params['participant_id']  # noqa: E501

        query_params = []
        if 'origin' in local_var_params and local_var_params['origin'] is not None:  # noqa: E501
            query_params.append(('origin', local_var_params['origin']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/participant/{participant_id}/sensor_event', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensor_event_all_by_researcher(self, researcher_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_all_by_researcher  # noqa: E501

        Get the set of all sensor events produced by participants  of any study conducted by a researcher, by researcher identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_all_by_researcher(researcher_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str researcher_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sensor_event_all_by_researcher_with_http_info(researcher_id, origin, _from, to, **kwargs)  # noqa: E501

    def sensor_event_all_by_researcher_with_http_info(self, researcher_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_all_by_researcher  # noqa: E501

        Get the set of all sensor events produced by participants  of any study conducted by a researcher, by researcher identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_all_by_researcher_with_http_info(researcher_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str researcher_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[object], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['researcher_id', 'origin', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensor_event_all_by_researcher" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'researcher_id' is set
        if self.api_client.client_side_validation and ('researcher_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['researcher_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `researcher_id` when calling `sensor_event_all_by_researcher`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if self.api_client.client_side_validation and ('origin' not in local_var_params or  # noqa: E501
                                                        local_var_params['origin'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `origin` when calling `sensor_event_all_by_researcher`")  # noqa: E501
        # verify the required parameter '_from' is set
        if self.api_client.client_side_validation and ('_from' not in local_var_params or  # noqa: E501
                                                        local_var_params['_from'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `_from` when calling `sensor_event_all_by_researcher`")  # noqa: E501
        # verify the required parameter 'to' is set
        if self.api_client.client_side_validation and ('to' not in local_var_params or  # noqa: E501
                                                        local_var_params['to'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to` when calling `sensor_event_all_by_researcher`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'researcher_id' in local_var_params:
            path_params['researcher_id'] = local_var_params['researcher_id']  # noqa: E501

        query_params = []
        if 'origin' in local_var_params and local_var_params['origin'] is not None:  # noqa: E501
            query_params.append(('origin', local_var_params['origin']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/researcher/{researcher_id}/sensor_event', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensor_event_all_by_study(self, study_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_all_by_study  # noqa: E501

        Get the set of all sensor events produced by participants  participants of a single study, by study identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_all_by_study(study_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str study_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sensor_event_all_by_study_with_http_info(study_id, origin, _from, to, **kwargs)  # noqa: E501

    def sensor_event_all_by_study_with_http_info(self, study_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_all_by_study  # noqa: E501

        Get the set of all sensor events produced by participants  participants of a single study, by study identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_all_by_study_with_http_info(study_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str study_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[object], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['study_id', 'origin', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensor_event_all_by_study" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'study_id' is set
        if self.api_client.client_side_validation and ('study_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['study_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `study_id` when calling `sensor_event_all_by_study`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if self.api_client.client_side_validation and ('origin' not in local_var_params or  # noqa: E501
                                                        local_var_params['origin'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `origin` when calling `sensor_event_all_by_study`")  # noqa: E501
        # verify the required parameter '_from' is set
        if self.api_client.client_side_validation and ('_from' not in local_var_params or  # noqa: E501
                                                        local_var_params['_from'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `_from` when calling `sensor_event_all_by_study`")  # noqa: E501
        # verify the required parameter 'to' is set
        if self.api_client.client_side_validation and ('to' not in local_var_params or  # noqa: E501
                                                        local_var_params['to'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to` when calling `sensor_event_all_by_study`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']  # noqa: E501

        query_params = []
        if 'origin' in local_var_params and local_var_params['origin'] is not None:  # noqa: E501
            query_params.append(('origin', local_var_params['origin']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/study/{study_id}/sensor_event', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensor_event_create(self, participant_id, sensor_event, **kwargs):  # noqa: E501
        """sensor_event_create  # noqa: E501

        Create a new SensorEvent for the given Participant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_create(participant_id, sensor_event, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str participant_id: (required)
        :param SensorEvent sensor_event: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sensor_event_create_with_http_info(participant_id, sensor_event, **kwargs)  # noqa: E501

    def sensor_event_create_with_http_info(self, participant_id, sensor_event, **kwargs):  # noqa: E501
        """sensor_event_create  # noqa: E501

        Create a new SensorEvent for the given Participant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_create_with_http_info(participant_id, sensor_event, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str participant_id: (required)
        :param SensorEvent sensor_event: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['participant_id', 'sensor_event']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensor_event_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'participant_id' is set
        if self.api_client.client_side_validation and ('participant_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['participant_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `participant_id` when calling `sensor_event_create`")  # noqa: E501
        # verify the required parameter 'sensor_event' is set
        if self.api_client.client_side_validation and ('sensor_event' not in local_var_params or  # noqa: E501
                                                        local_var_params['sensor_event'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sensor_event` when calling `sensor_event_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'participant_id' in local_var_params:
            path_params['participant_id'] = local_var_params['participant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensor_event' in local_var_params:
            body_params = local_var_params['sensor_event']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/participant/{participant_id}/sensor_event', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensor_event_delete(self, participant_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_delete  # noqa: E501

        Delete a sensor event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_delete(participant_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str participant_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sensor_event_delete_with_http_info(participant_id, origin, _from, to, **kwargs)  # noqa: E501

    def sensor_event_delete_with_http_info(self, participant_id, origin, _from, to, **kwargs):  # noqa: E501
        """sensor_event_delete  # noqa: E501

        Delete a sensor event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensor_event_delete_with_http_info(participant_id, origin, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str participant_id: (required)
        :param str origin: (required)
        :param float _from: (required)
        :param float to: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['participant_id', 'origin', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensor_event_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'participant_id' is set
        if self.api_client.client_side_validation and ('participant_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['participant_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `participant_id` when calling `sensor_event_delete`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if self.api_client.client_side_validation and ('origin' not in local_var_params or  # noqa: E501
                                                        local_var_params['origin'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `origin` when calling `sensor_event_delete`")  # noqa: E501
        # verify the required parameter '_from' is set
        if self.api_client.client_side_validation and ('_from' not in local_var_params or  # noqa: E501
                                                        local_var_params['_from'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `_from` when calling `sensor_event_delete`")  # noqa: E501
        # verify the required parameter 'to' is set
        if self.api_client.client_side_validation and ('to' not in local_var_params or  # noqa: E501
                                                        local_var_params['to'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to` when calling `sensor_event_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'participant_id' in local_var_params:
            path_params['participant_id'] = local_var_params['participant_id']  # noqa: E501

        query_params = []
        if 'origin' in local_var_params and local_var_params['origin'] is not None:  # noqa: E501
            query_params.append(('origin', local_var_params['origin']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/participant/{participant_id}/sensor_event', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
