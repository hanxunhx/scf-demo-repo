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
from taifucloudcloud.yunsou.v20191115 import models


class YunsouClient(AbstractClient):
    _apiVersion = '2019-11-15'
    _endpoint = 'yunsou.taifucloudcloudapi.com'


    def DataManipulation(self, request):
        """上傳雲搜數據的API介面。

        :param request: Request instance for DataManipulation.
        :type request: :class:`taifucloudcloud.yunsou.v20191115.models.DataManipulationRequest`
        :rtype: :class:`taifucloudcloud.yunsou.v20191115.models.DataManipulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DataManipulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DataManipulationResponse()
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


    def DataSearch(self, request):
        """用于檢索雲搜中的數據。

        :param request: Request instance for DataSearch.
        :type request: :class:`taifucloudcloud.yunsou.v20191115.models.DataSearchRequest`
        :rtype: :class:`taifucloudcloud.yunsou.v20191115.models.DataSearchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DataSearch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DataSearchResponse()
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