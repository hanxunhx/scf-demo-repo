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
from taifucloudcloud.tav.v20190118 import models


class TavClient(AbstractClient):
    _apiVersion = '2019-01-18'
    _endpoint = 'tav.taifucloudcloudapi.com'


    def GetLocalEngine(self, request):
        """獲取TAV本地引擎

        :param request: Request instance for GetLocalEngine.
        :type request: :class:`taifucloudcloud.tav.v20190118.models.GetLocalEngineRequest`
        :rtype: :class:`taifucloudcloud.tav.v20190118.models.GetLocalEngineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLocalEngine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLocalEngineResponse()
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


    def GetScanResult(self, request):
        """tav文件上傳掃描結果查詢

        :param request: Request instance for GetScanResult.
        :type request: :class:`taifucloudcloud.tav.v20190118.models.GetScanResultRequest`
        :rtype: :class:`taifucloudcloud.tav.v20190118.models.GetScanResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetScanResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetScanResultResponse()
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


    def ScanFile(self, request):
        """tav文件上傳掃描

        :param request: Request instance for ScanFile.
        :type request: :class:`taifucloudcloud.tav.v20190118.models.ScanFileRequest`
        :rtype: :class:`taifucloudcloud.tav.v20190118.models.ScanFileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanFileResponse()
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


    def ScanFileHash(self, request):
        """通過文件哈希值獲取文件黑白屬性

        :param request: Request instance for ScanFileHash.
        :type request: :class:`taifucloudcloud.tav.v20190118.models.ScanFileHashRequest`
        :rtype: :class:`taifucloudcloud.tav.v20190118.models.ScanFileHashResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanFileHash", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanFileHashResponse()
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