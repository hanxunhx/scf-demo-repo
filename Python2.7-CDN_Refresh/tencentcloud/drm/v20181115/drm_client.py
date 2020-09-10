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
from taifucloudcloud.drm.v20181115 import models


class DrmClient(AbstractClient):
    _apiVersion = '2018-11-15'
    _endpoint = 'drm.taifucloudcloudapi.com'


    def AddFairPlayPem(self, request):
        """本介面用來設置fairplay方案所需的私鑰、私鑰金鑰、ask等訊息。
        如需使用fairplay方案，請務必先設置私鑰。

        :param request: Request instance for AddFairPlayPem.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.AddFairPlayPemRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.AddFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddFairPlayPem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddFairPlayPemResponse()
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


    def CreateEncryptKeys(self, request):
        """該介面用來設置加密的金鑰。注意，同一個content id，只能設置一次！

        :param request: Request instance for CreateEncryptKeys.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.CreateEncryptKeysRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.CreateEncryptKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEncryptKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEncryptKeysResponse()
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


    def CreateLicense(self, request):
        """本介面用來生成DRM方案對應的播放許可證，開發者需提供DRM方案類型、内容類型參數，後台将生成許可證後返回許可證數據
        開發者需要轉發終端設備發出的許可證請求訊息。

        :param request: Request instance for CreateLicense.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.CreateLicenseRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.CreateLicenseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLicense", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLicenseResponse()
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


    def DeleteFairPlayPem(self, request):
        """本介面用來删除fairplay方案的私鑰、ask等訊息
        注：高風險操作，删除後，您将無法使用Top Cloud DRM提供的fairplay服務。
        由于快取，删除操作需要約半小時生效

        :param request: Request instance for DeleteFairPlayPem.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.DeleteFairPlayPemRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.DeleteFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFairPlayPem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFairPlayPemResponse()
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


    def DescribeAllKeys(self, request):
        """本介面用來查詢指定DRM類型、ContentType的所有加密金鑰

        :param request: Request instance for DescribeAllKeys.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.DescribeAllKeysRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.DescribeAllKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllKeysResponse()
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


    def DescribeFairPlayPem(self, request):
        """該介面用來查詢設置的FairPlay私鑰校驗訊息。可用該介面校驗設置的私鑰與本身的私鑰是否一緻。

        :param request: Request instance for DescribeFairPlayPem.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.DescribeFairPlayPemRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.DescribeFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFairPlayPem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFairPlayPemResponse()
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


    def DescribeKeys(self, request):
        """開發者需要指定使用的DRM類型、和需要加密的Track類型，後台返回加密使用的金鑰
        如果加密使用的ContentID沒有關聯的金鑰訊息，後台會自動生成新的金鑰返回

        :param request: Request instance for DescribeKeys.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.DescribeKeysRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.DescribeKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeysResponse()
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


    def ModifyFairPlayPem(self, request):
        """本介面用來設置fairplay方案所需的私鑰、私鑰金鑰、ask等訊息。
        如需使用fairplay方案，請務必先設置私鑰。

        :param request: Request instance for ModifyFairPlayPem.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.ModifyFairPlayPemRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.ModifyFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyFairPlayPem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFairPlayPemResponse()
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


    def StartEncryption(self, request):
        """開發者調用該介面，啓動一次内容文件的DRM加密工作流

        :param request: Request instance for StartEncryption.
        :type request: :class:`taifucloudcloud.drm.v20181115.models.StartEncryptionRequest`
        :rtype: :class:`taifucloudcloud.drm.v20181115.models.StartEncryptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartEncryption", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartEncryptionResponse()
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