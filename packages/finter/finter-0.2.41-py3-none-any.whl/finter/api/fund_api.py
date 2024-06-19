# coding: utf-8

"""
    FINTER API

    ## Finter API Document 1. Domain   - production      - https://api.finter.quantit.io/   - staging      - https://staging.api.finter.quantit.io/  2. Authorization <br><br/>(1) 토큰 발급<br/>curl -X POST https://api.finter.quantit.io/login -d {'username': '{finter_user_id}', 'password': '{finter_user_password}'<br> (2) username, password 로그인 (swagger ui 이용 시)<br/>  # noqa: E501

    OpenAPI spec version: 0.298
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from finter.api_client import ApiClient


class FundApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fund_identities_retrieve(self, **kwargs):  # noqa: E501
        """fund_identities_retrieve  # noqa: E501

        ## Flexible Fund Model identity name list API ### 입력변수  (없음)       |출력변수 |설명 |타입 |  |:-------|:--------|:--------|  |unix_timestamp||int| |ffm_identity_name_list|플렉서블 펀드 모델 identity name 리스트|List of string|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fund_identities_retrieve(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FundIdentitiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fund_identities_retrieve_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fund_identities_retrieve_with_http_info(**kwargs)  # noqa: E501
            return data

    def fund_identities_retrieve_with_http_info(self, **kwargs):  # noqa: E501
        """fund_identities_retrieve  # noqa: E501

        ## Flexible Fund Model identity name list API ### 입력변수  (없음)       |출력변수 |설명 |타입 |  |:-------|:--------|:--------|  |unix_timestamp||int| |ffm_identity_name_list|플렉서블 펀드 모델 identity name 리스트|List of string|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fund_identities_retrieve_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FundIdentitiesResponse
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
                    " to method fund_identities_retrieve" % key
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
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fund/identities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FundIdentitiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fund_model_retrieve(self, **kwargs):  # noqa: E501
        """fund_model_retrieve  # noqa: E501

        ## Fund Model Data API |입력변수              |설명                                                    |필수  |기본값      |  |:--------------------|:-------------------------------------------------------|:-----|:-----------|  |identity_name        |펀드 모델 identity name                                  |O     |            |  |end                  |받을 데이터의 마지막 인덱스(날짜)                          |X     |request 시점 | |code_format          |데이터 칼럼 형식: ccid, isin, short_code 중 택1           |X     |ccid        | |tail                 |받을 데이터의 row 개수: 마지막 인덱스부터 tail 값 만큼, 1 이상 1000 이하값으로 제한됨 |X     |20 |      |출력변수  |설명               |타입                 |  |:--------|:------------------|:--------------------|  |unix_timestamp||int| |fm       |펀드 모델 데이터    |string (json-string) | |meta     |출력값 메타 정보    |dict                 |   ### meta dict 구성  - identity_name - code_format - tail - start_date - last_date   ### 'fm'으로 받은 펀드 모델 문자열 데이터프레임 변환 - pd.read_json(fm, orient='index')  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fund_model_retrieve(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code_format: data column code format
        :param str end: data end date
        :param str identity_name: fund model identity name
        :param int tail: data tail row number
        :return: FundModelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fund_model_retrieve_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fund_model_retrieve_with_http_info(**kwargs)  # noqa: E501
            return data

    def fund_model_retrieve_with_http_info(self, **kwargs):  # noqa: E501
        """fund_model_retrieve  # noqa: E501

        ## Fund Model Data API |입력변수              |설명                                                    |필수  |기본값      |  |:--------------------|:-------------------------------------------------------|:-----|:-----------|  |identity_name        |펀드 모델 identity name                                  |O     |            |  |end                  |받을 데이터의 마지막 인덱스(날짜)                          |X     |request 시점 | |code_format          |데이터 칼럼 형식: ccid, isin, short_code 중 택1           |X     |ccid        | |tail                 |받을 데이터의 row 개수: 마지막 인덱스부터 tail 값 만큼, 1 이상 1000 이하값으로 제한됨 |X     |20 |      |출력변수  |설명               |타입                 |  |:--------|:------------------|:--------------------|  |unix_timestamp||int| |fm       |펀드 모델 데이터    |string (json-string) | |meta     |출력값 메타 정보    |dict                 |   ### meta dict 구성  - identity_name - code_format - tail - start_date - last_date   ### 'fm'으로 받은 펀드 모델 문자열 데이터프레임 변환 - pd.read_json(fm, orient='index')  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fund_model_retrieve_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code_format: data column code format
        :param str end: data end date
        :param str identity_name: fund model identity name
        :param int tail: data tail row number
        :return: FundModelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_format', 'end', 'identity_name', 'tail']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fund_model_retrieve" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_format' in params:
            query_params.append(('code_format', params['code_format']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'identity_name' in params:
            query_params.append(('identity_name', params['identity_name']))  # noqa: E501
        if 'tail' in params:
            query_params.append(('tail', params['tail']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fund/model', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FundModelResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
