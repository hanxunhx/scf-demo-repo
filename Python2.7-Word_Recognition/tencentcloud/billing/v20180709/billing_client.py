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
from taifucloudcloud.billing.v20180709 import models


class BillingClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'billing.taifucloudcloudapi.com'


    def DescribeAccountBalance(self, request):
        """獲取雲帳戶餘額訊息。

        :param request: 調用DescribeAccountBalance所需參數的結構體。
        :type request: :class:`taifucloudcloud.billing.v20180709.models.DescribeAccountBalanceRequest`
        :rtype: :class:`taifucloudcloud.billing.v20180709.models.DescribeAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountBalanceResponse()
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


    def DescribeBillDetail(self, request):
        """查詢帳單明細數據

        :param request: 調用DescribeBillDetail所需參數的結構體。
        :type request: :class:`taifucloudcloud.billing.v20180709.models.DescribeBillDetailRequest`
        :rtype: :class:`taifucloudcloud.billing.v20180709.models.DescribeBillDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillDetailResponse()
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


    def DescribeBillResourceSummary(self, request):
        """查詢帳單資源匯總數據

        :param request: 調用DescribeBillResourceSummary所需參數的結構體。
        :type request: :class:`taifucloudcloud.billing.v20180709.models.DescribeBillResourceSummaryRequest`
        :rtype: :class:`taifucloudcloud.billing.v20180709.models.DescribeBillResourceSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillResourceSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillResourceSummaryResponse()
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


    def DescribeDealsByCond(self, request):
        """查詢訂單

        :param request: 調用DescribeDealsByCond所需參數的結構體。
        :type request: :class:`taifucloudcloud.billing.v20180709.models.DescribeDealsByCondRequest`
        :rtype: :class:`taifucloudcloud.billing.v20180709.models.DescribeDealsByCondResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDealsByCond", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDealsByCondResponse()
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


    def DescribeDosageDetailByDate(self, request):
        """按日期獲取産品用量明細

        :param request: 調用DescribeDosageDetailByDate所需參數的結構體。
        :type request: :class:`taifucloudcloud.billing.v20180709.models.DescribeDosageDetailByDateRequest`
        :rtype: :class:`taifucloudcloud.billing.v20180709.models.DescribeDosageDetailByDateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDosageDetailByDate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDosageDetailByDateResponse()
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


    def PayDeals(self, request):
        """支付訂單

        :param request: 調用PayDeals所需參數的結構體。
        :type request: :class:`taifucloudcloud.billing.v20180709.models.PayDealsRequest`
        :rtype: :class:`taifucloudcloud.billing.v20180709.models.PayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PayDealsResponse()
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