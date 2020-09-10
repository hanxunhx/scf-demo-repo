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
from taifucloudcloud.smpn.v20190822 import models


class SmpnClient(AbstractClient):
    _apiVersion = '2019-08-22'
    _endpoint = 'smpn.taifucloudcloudapi.com'


    def CreateSmpnEpa(self, request):
        """企業号碼認證

        :param request: Request instance for CreateSmpnEpa.
        :type request: :class:`taifucloudcloud.smpn.v20190822.models.CreateSmpnEpaRequest`
        :rtype: :class:`taifucloudcloud.smpn.v20190822.models.CreateSmpnEpaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSmpnEpa", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSmpnEpaResponse()
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


    def DescribeSmpnChp(self, request):
        """查詢号碼的标記和标記次數

        :param request: Request instance for DescribeSmpnChp.
        :type request: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnChpRequest`
        :rtype: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnChpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmpnChp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmpnChpResponse()
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


    def DescribeSmpnFnr(self, request):
        """虛假号碼識别

        :param request: Request instance for DescribeSmpnFnr.
        :type request: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnFnrRequest`
        :rtype: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnFnrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmpnFnr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmpnFnrResponse()
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


    def DescribeSmpnMhm(self, request):
        """号碼營銷監控

        :param request: Request instance for DescribeSmpnMhm.
        :type request: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnMhmRequest`
        :rtype: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnMhmResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmpnMhm", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmpnMhmResponse()
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


    def DescribeSmpnMrl(self, request):
        """查詢号碼惡意标記等級

        :param request: Request instance for DescribeSmpnMrl.
        :type request: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnMrlRequest`
        :rtype: :class:`taifucloudcloud.smpn.v20190822.models.DescribeSmpnMrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmpnMrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmpnMrlResponse()
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