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
from taifucloudcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.taifucloudcloudapi.com'


    def CreateInstance(self, request):
        """創建EMR實例

        :param request: Request instance for CreateInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceResponse()
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


    def DescribeClusterNodes(self, request):
        """查詢硬體節點訊息

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterNodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterNodesResponse()
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


    def DescribeInstances(self, request):
        """查詢EMR實例

        :param request: Request instance for DescribeInstances.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def InquiryPriceCreateInstance(self, request):
        """創建實例詢價

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateInstanceResponse()
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


    def InquiryPriceRenewInstance(self, request):
        """續約詢價。

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewInstanceResponse()
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


    def InquiryPriceScaleOutInstance(self, request):
        """擴容詢價. 當擴容時候，請通過該介面查詢價格。

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceScaleOutInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceScaleOutInstanceResponse()
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


    def InquiryPriceUpdateInstance(self, request):
        """變配詢價

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpdateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpdateInstanceResponse()
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


    def ScaleOutInstance(self, request):
        """實例擴容

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScaleOutInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleOutInstanceResponse()
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


    def TerminateInstance(self, request):
        """銷毀EMR實例。此介面僅支援彈性MapReduce正式計費版本。

        :param request: Request instance for TerminateInstance.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstanceResponse()
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


    def TerminateTasks(self, request):
        """縮容Task節點

        :param request: Request instance for TerminateTasks.
        :type request: :class:`taifucloudcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`taifucloudcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTasksResponse()
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