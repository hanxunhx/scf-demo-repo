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
from taifucloudcloud.aa.v20200224 import models


class AaClient(AbstractClient):
    _apiVersion = '2020-02-24'
    _endpoint = 'aa.taifucloudcloudapi.com'


    def QueryActivityAntiRush(self, request):
        """Top Cloud 活動防刷（ActivityAntiRush，AA）是針對電商、O2O、P2P、遊戲、支付等行業在促銷活動中遇到“羊毛黨”惡意刷取優惠福利的行爲時，通過防刷引擎，精準識别出“薅羊毛”惡意行爲的活動防刷服務，避免了企業被刷帶來的巨大經濟損失。

        :param request: Request instance for QueryActivityAntiRush.
        :type request: :class:`taifucloudcloud.aa.v20200224.models.QueryActivityAntiRushRequest`
        :rtype: :class:`taifucloudcloud.aa.v20200224.models.QueryActivityAntiRushResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryActivityAntiRush", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryActivityAntiRushResponse()
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