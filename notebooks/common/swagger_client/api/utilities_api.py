# coding: utf-8

"""
    GSI Floating-Point 32 API

    **Introduction**<br> GSI Technology’s floating-point similarity search API provides an accessible gateway to running searches on GSI’s Gemini® Associative Processing Unit (APU).<br> It works in conjunction with the GSI system management solution which enables users to work with multiple APU boards simultaneously for improved performance.<br><br> **Dataset and Query Format**<br> Dataset embeddings can be in 32- or 64-bit floating point format, and any number of features, e.g. 256 or 512 (there is no upper limit).<br> Query embeddings must have the same floating-point format and number of features as used in the dataset.<br> GSI performs the search and delivers the top-k most similar results.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UtilitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def apis_clean_csv_result(self, num_of_files_to_keep, **kwargs):  # noqa: E501
        """Clean old CSV results  # noqa: E501

        Clean old CSV results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_clean_csv_result(num_of_files_to_keep, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_files_to_keep: Number of files to keep. (required)
        :return: StatusOkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_clean_csv_result_with_http_info(num_of_files_to_keep, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_clean_csv_result_with_http_info(num_of_files_to_keep, **kwargs)  # noqa: E501
            return data

    def apis_clean_csv_result_with_http_info(self, num_of_files_to_keep, **kwargs):  # noqa: E501
        """Clean old CSV results  # noqa: E501

        Clean old CSV results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_clean_csv_result_with_http_info(num_of_files_to_keep, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_files_to_keep: Number of files to keep. (required)
        :return: StatusOkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['num_of_files_to_keep']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_clean_csv_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'num_of_files_to_keep' is set
        if ('num_of_files_to_keep' not in params or
                params['num_of_files_to_keep'] is None):
            raise ValueError("Missing the required parameter `num_of_files_to_keep` when calling `apis_clean_csv_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'num_of_files_to_keep' in params:
            path_params['num_of_files_to_keep'] = params['num_of_files_to_keep']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/results/clean/{num_of_files_to_keep}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusOkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_create_ground_truth(self, body, **kwargs):  # noqa: E501
        """Create ground truth.  # noqa: E501

        Create ground truth.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_create_ground_truth(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateGTRequest body: (required)
        :return: CreateGTResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_create_ground_truth_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_create_ground_truth_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_create_ground_truth_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create ground truth.  # noqa: E501

        Create ground truth.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_create_ground_truth_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateGTRequest body: (required)
        :return: CreateGTResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_create_ground_truth" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_create_ground_truth`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/createGT', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateGTResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_create_random_queries_file(self, body, **kwargs):  # noqa: E501
        """Create random queries file.  # noqa: E501

        Create random queries file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_create_random_queries_file(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRandomQueriesFileRequest body: (required)
        :return: CreateRandomQueriesFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_create_random_queries_file_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_create_random_queries_file_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_create_random_queries_file_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create random queries file.  # noqa: E501

        Create random queries file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_create_random_queries_file_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRandomQueriesFileRequest body: (required)
        :return: CreateRandomQueriesFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_create_random_queries_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_create_random_queries_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/createrandomqueriesfile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateRandomQueriesFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_download_client_kit(self, **kwargs):  # noqa: E501
        """Download python client-kit.  # noqa: E501

        Download python client-kit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_download_client_kit(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_download_client_kit_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apis_download_client_kit_with_http_info(**kwargs)  # noqa: E501
            return data

    def apis_download_client_kit_with_http_info(self, **kwargs):  # noqa: E501
        """Download python client-kit.  # noqa: E501

        Download python client-kit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_download_client_kit_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_download_client_kit" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/download/clientkit', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_download_csv(self, csv_results_file_path, **kwargs):  # noqa: E501
        """Download a CSV file.  # noqa: E501

        Download CSV file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_download_csv(csv_results_file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str csv_results_file_path: CSV file path to download from. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_download_csv_with_http_info(csv_results_file_path, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_download_csv_with_http_info(csv_results_file_path, **kwargs)  # noqa: E501
            return data

    def apis_download_csv_with_http_info(self, csv_results_file_path, **kwargs):  # noqa: E501
        """Download a CSV file.  # noqa: E501

        Download CSV file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_download_csv_with_http_info(csv_results_file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str csv_results_file_path: CSV file path to download from. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['csv_results_file_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_download_csv" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'csv_results_file_path' is set
        if ('csv_results_file_path' not in params or
                params['csv_results_file_path'] is None):
            raise ValueError("Missing the required parameter `csv_results_file_path` when calling `apis_download_csv`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'csv_results_file_path' in params:
            query_params.append(('csv_results_file_path', params['csv_results_file_path']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/download/csv', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_generate_queries(self, body, **kwargs):  # noqa: E501
        """Generate random queries  # noqa: E501

        API will generate a random float32 queries based on inputs and will save it to a file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_generate_queries(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GenerateQueriesRequest body: (required)
        :return: GenerateQueriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_generate_queries_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_generate_queries_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_generate_queries_with_http_info(self, body, **kwargs):  # noqa: E501
        """Generate random queries  # noqa: E501

        API will generate a random float32 queries based on inputs and will save it to a file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_generate_queries_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GenerateQueriesRequest body: (required)
        :return: GenerateQueriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_generate_queries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_generate_queries`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/queries/generate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenerateQueriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_print_memory_dump(self, **kwargs):  # noqa: E501
        """Print a dump of python objects in memory  # noqa: E501

        Print a dump of python objects in memory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_print_memory_dump(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StatusOkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_print_memory_dump_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apis_print_memory_dump_with_http_info(**kwargs)  # noqa: E501
            return data

    def apis_print_memory_dump_with_http_info(self, **kwargs):  # noqa: E501
        """Print a dump of python objects in memory  # noqa: E501

        Print a dump of python objects in memory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_print_memory_dump_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StatusOkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_print_memory_dump" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/memory/dump', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusOkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_save_results(self, body, **kwargs):  # noqa: E501
        """Save json structured results to a file.  # noqa: E501

        Save json structured results to a file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_save_results(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SaveResultsRequest body: (required)
        :return: SaveResultsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_save_results_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_save_results_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_save_results_with_http_info(self, body, **kwargs):  # noqa: E501
        """Save json structured results to a file.  # noqa: E501

        Save json structured results to a file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_save_results_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SaveResultsRequest body: (required)
        :return: SaveResultsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_save_results" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_save_results`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/save/results', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResultsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_validate(self, body, **kwargs):  # noqa: E501
        """Validate search results against ground truth.  # noqa: E501

        Validate search results against ground truth.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_validate(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateRequest body: (required)
        :return: ValidateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_validate_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_validate_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_validate_with_http_info(self, body, **kwargs):  # noqa: E501
        """Validate search results against ground truth.  # noqa: E501

        Validate search results against ground truth.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_validate_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateRequest body: (required)
        :return: ValidateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_validate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_validate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
