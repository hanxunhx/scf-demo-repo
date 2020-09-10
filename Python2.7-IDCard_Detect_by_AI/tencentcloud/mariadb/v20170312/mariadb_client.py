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
from taifucloudcloud.mariadb.v20170312 import models


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.taifucloudcloudapi.com'


    def CloneAccount(self, request):
        """本介面（CloneAccount）用于複製實例帳戶。

        :param request: 調用CloneAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.CloneAccountRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloneAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneAccountResponse()
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


    def CloseDBExtranetAccess(self, request):
        """本介面(CloseDBExtranetAccess)用于關閉雲資料庫實例的外網訪問。關閉外網訪問後，外網網址将不可訪問，查詢實例清單介面将不返回對應實例的外網域名和端口訊息。

        :param request: 調用CloseDBExtranetAccess所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseDBExtranetAccessResponse()
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


    def CopyAccountPrivileges(self, request):
        """本介面（CopyAccountPrivileges）用于複制雲資料庫賬号的權限。
        注意：相同用戶名，不同Host是不同的賬号，Readonly屬性相同的賬号之間才能複制權限。

        :param request: 調用CopyAccountPrivileges所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyAccountPrivilegesResponse()
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


    def CreateAccount(self, request):
        """本介面（CreateAccount）用于創建雲資料庫賬号。一個實例可以創建多個不同的賬号，相同的用戶名+不同的host是不同的賬号。

        :param request: 調用CreateAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.CreateAccountRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
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


    def CreateDBInstance(self, request):
        """本介面（CreateDBInstance）用于創建包年包月的雲資料庫實例，可通過傳入實例規格、資料庫版本号、購買時長和數量等訊息創建雲資料庫實例。

        :param request: 調用CreateDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.CreateDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceResponse()
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


    def DeleteAccount(self, request):
        """本介面（DeleteAccount）用于删除雲資料庫賬号。用戶名+host唯一确定一個賬号。

        :param request: 調用DeleteAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DeleteAccountRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
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


    def DescribeAccountPrivileges(self, request):
        """本介面（DescribeAccountPrivileges）用于查詢雲資料庫賬号權限。
        注意：注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用DescribeAccountPrivileges所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
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


    def DescribeAccounts(self, request):
        """本介面（DescribeAccounts）用于查詢指定雲資料庫實例的賬号清單。

        :param request: 調用DescribeAccounts所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeBackupTime(self, request):
        """本介面（DescribeBackupTime）用于獲取雲資料庫的備份時間。後台系統将根據此配置定期進行實例備份。

        :param request: 調用DescribeBackupTime所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeBackupTimeRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeBackupTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupTimeResponse()
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


    def DescribeDBInstanceSpecs(self, request):
        """本介面(DescribeDBInstanceSpecs)用于查詢可創建的雲資料庫可售賣的規格配置。

        :param request: 調用DescribeDBInstanceSpecs所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBInstanceSpecsRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceSpecs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceSpecsResponse()
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


    def DescribeDBInstances(self, request):
        """本介面（DescribeDBInstances）用于查詢雲資料庫實例清單，支援通過項目ID、實例ID、内網網址、實例名稱等來篩選實例。
        如果不指定任何篩選條件，則預設返回20條實例記錄，單次請求最多支援返回100條實例記錄。

        :param request: 調用DescribeDBInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
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


    def DescribeDBLogFiles(self, request):
        """本介面(DescribeDBLogFiles)用于獲取資料庫的各種日志清單，包括冷備、binlog、errlog和slowlog。

        :param request: 調用DescribeDBLogFiles所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBLogFilesRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBLogFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBLogFilesResponse()
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


    def DescribeDBParameters(self, request):
        """本介面(DescribeDBParameters)用于獲取資料庫的當前參數設置。

        :param request: 調用DescribeDBParameters所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBParametersRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBParametersResponse()
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


    def DescribeDBPerformance(self, request):
        """本介面(DescribeDBPerformance)用于檢視資料庫實例當前效能數據。

        :param request: 調用DescribeDBPerformance所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBPerformanceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBPerformanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPerformance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPerformanceResponse()
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


    def DescribeDBPerformanceDetails(self, request):
        """本介面(DescribeDBPerformanceDetails)用于檢視實例效能數據詳情。

        :param request: 調用DescribeDBPerformanceDetails所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBPerformanceDetailsRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBPerformanceDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPerformanceDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPerformanceDetailsResponse()
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


    def DescribeDBResourceUsage(self, request):
        """本介面(DescribeDBResourceUsage)用于檢視資料庫實例資源的使用情況。

        :param request: 調用DescribeDBResourceUsage所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBResourceUsageRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBResourceUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBResourceUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBResourceUsageResponse()
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


    def DescribeDBResourceUsageDetails(self, request):
        """本介面(DescribeDBResourceUsageDetails)用于檢視資料庫實例當前效能數據。

        :param request: 調用DescribeDBResourceUsageDetails所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBResourceUsageDetailsRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBResourceUsageDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBResourceUsageDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBResourceUsageDetailsResponse()
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


    def DescribeDBSlowLogs(self, request):
        """本介面(DescribeDBSlowLogs)用于查詢慢查詢日志清單。

        :param request: 調用DescribeDBSlowLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeDBSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowLogsResponse()
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


    def DescribeFlow(self, request):
        """本介面（DescribeFlow）用于查詢流程狀态。

        :param request: 調用DescribeFlow所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeFlowRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowResponse()
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


    def DescribeLogFileRetentionPeriod(self, request):
        """本介面(DescribeLogFileRetentionPeriod)用于檢視資料庫備份日志的備份天數的設置情況。

        :param request: 調用DescribeLogFileRetentionPeriod所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogFileRetentionPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogFileRetentionPeriodResponse()
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


    def DescribeOrders(self, request):
        """本介面（DescribeOrders）用于查詢雲資料庫訂單訊息。傳入訂單Id來查詢訂單關聯的雲資料庫實例，和對應的任務流程ID。

        :param request: 調用DescribeOrders所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrdersResponse()
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


    def DescribePrice(self, request):
        """本介面（DescribePrice）用于在購買實例前，查詢實例的價格。

        :param request: 調用DescribePrice所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribePriceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribePriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePriceResponse()
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


    def DescribeRenewalPrice(self, request):
        """本介面（DescribeRenewalPrice）用于在續約雲資料庫實例時，查詢續約的價格。

        :param request: 調用DescribeRenewalPrice所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeRenewalPriceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRenewalPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRenewalPriceResponse()
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


    def DescribeSaleInfo(self, request):
        """本介面(DescribeSaleInfo)用于查詢雲資料庫可售賣的地域和可用區訊息。

        :param request: 調用DescribeSaleInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeSaleInfoRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeSaleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSaleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSaleInfoResponse()
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


    def DescribeSqlLogs(self, request):
        """本介面（DescribeSqlLogs）用于獲取實例SQL日志。

        :param request: 調用DescribeSqlLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeSqlLogsRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeSqlLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSqlLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSqlLogsResponse()
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


    def DescribeUpgradePrice(self, request):
        """本介面（DescribeUpgradePrice）用于在擴容雲資料庫實例時，查詢擴容的價格。

        :param request: 調用DescribeUpgradePrice所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeUpgradePriceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.DescribeUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUpgradePrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUpgradePriceResponse()
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


    def GrantAccountPrivileges(self, request):
        """本介面（GrantAccountPrivileges）用于給雲資料庫賬号賦權。
        注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用GrantAccountPrivileges所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GrantAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantAccountPrivilegesResponse()
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


    def InitDBInstances(self, request):
        """本介面(InitDBInstances)用于初始化雲資料庫實例，包括設置預設字元集、表名大小寫敏感等。

        :param request: 調用InitDBInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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


    def ModifyAccountDescription(self, request):
        """本介面（ModifyAccountDescription）用于修改雲資料庫賬号備注。
        注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用ModifyAccountDescription所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
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


    def ModifyBackupTime(self, request):
        """本介面（ModifyBackupTime）用于設置雲資料庫實例的備份時間。後台系統将根據此配置定期進行實例備份。

        :param request: 調用ModifyBackupTime所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyBackupTimeRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyBackupTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupTimeResponse()
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


    def ModifyDBInstanceName(self, request):
        """本介面（ModifyDBInstanceName）用于修改雲資料庫實例的名稱。

        :param request: 調用ModifyDBInstanceName所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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


    def ModifyDBInstancesProject(self, request):
        """本介面（ModifyDBInstancesProject）用于修改雲資料庫實例所屬項目。

        :param request: 調用ModifyDBInstancesProject所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstancesProjectResponse()
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


    def ModifyDBParameters(self, request):
        """本介面(ModifyDBParameters)用于修改資料庫參數。

        :param request: 調用ModifyDBParameters所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyDBParametersRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBParametersResponse()
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


    def ModifyLogFileRetentionPeriod(self, request):
        """本介面(ModifyLogFileRetentionPeriod)用于修改資料庫備份日志保存天數。

        :param request: 調用ModifyLogFileRetentionPeriod所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLogFileRetentionPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLogFileRetentionPeriodResponse()
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


    def OpenDBExtranetAccess(self, request):
        """本介面（OpenDBExtranetAccess）用于開通雲資料庫實例的外網訪問。開通外網訪問後，您可通過外網域名和端口訪問實例，可使用查詢實例清單介面獲取外網域名和端口訊息。

        :param request: 調用OpenDBExtranetAccess所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBExtranetAccessResponse()
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


    def RenewDBInstance(self, request):
        """本介面（RenewDBInstance）用于續約雲資料庫實例。

        :param request: 調用RenewDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.RenewDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstanceResponse()
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


    def ResetAccountPassword(self, request):
        """本介面（ResetAccountPassword）用于重置雲資料庫賬号的密碼。
        注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用ResetAccountPassword所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
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


    def UpgradeDBInstance(self, request):
        """本介面(UpgradeDBInstance)用于擴容雲資料庫實例。本介面完成下單和支付兩個動作，如果發生支付失敗的錯誤，調用用戶帳戶相關介面中的支付訂單介面（PayDeals）重新支付即可。

        :param request: 調用UpgradeDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.mariadb.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.mariadb.v20170312.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
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