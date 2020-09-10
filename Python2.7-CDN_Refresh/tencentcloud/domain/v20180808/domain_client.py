# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.domain.v20180808 import models


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.taifucloudcloudapi.com'


    def CheckDomain(self, request):
        """檢查域名是否可以注冊

        :param request: Request instance for CheckDomain.
        :type request: :class:`taifucloudcloud.domain.v20180808.models.CheckDomainRequest`
        :rtype: :class:`taifucloudcloud.domain.v20180808.models.CheckDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDomainPriceList(self, request):
        """按照域名後綴獲取對應的價格清單

        :param request: Request instance for DescribeDomainPriceList.
        :type request: :class:`taifucloudcloud.domain.v20180808.models.DescribeDomainPriceListRequest`
        :rtype: :class:`taifucloudcloud.domain.v20180808.models.DescribeDomainPriceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainPriceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainPriceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)