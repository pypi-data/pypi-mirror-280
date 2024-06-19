# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetManagedDatabaseSqlTuningAdvisorTasksFindingResult',
    'AwaitableGetManagedDatabaseSqlTuningAdvisorTasksFindingResult',
    'get_managed_database_sql_tuning_advisor_tasks_finding',
    'get_managed_database_sql_tuning_advisor_tasks_finding_output',
]

@pulumi.output_type
class GetManagedDatabaseSqlTuningAdvisorTasksFindingResult:
    """
    A collection of values returned by getManagedDatabaseSqlTuningAdvisorTasksFinding.
    """
    def __init__(__self__, begin_exec_id=None, end_exec_id=None, finding_filter=None, id=None, index_hash_filter=None, items=None, managed_database_id=None, search_period=None, sql_tuning_advisor_task_id=None, stats_hash_filter=None):
        if begin_exec_id and not isinstance(begin_exec_id, str):
            raise TypeError("Expected argument 'begin_exec_id' to be a str")
        pulumi.set(__self__, "begin_exec_id", begin_exec_id)
        if end_exec_id and not isinstance(end_exec_id, str):
            raise TypeError("Expected argument 'end_exec_id' to be a str")
        pulumi.set(__self__, "end_exec_id", end_exec_id)
        if finding_filter and not isinstance(finding_filter, str):
            raise TypeError("Expected argument 'finding_filter' to be a str")
        pulumi.set(__self__, "finding_filter", finding_filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if index_hash_filter and not isinstance(index_hash_filter, str):
            raise TypeError("Expected argument 'index_hash_filter' to be a str")
        pulumi.set(__self__, "index_hash_filter", index_hash_filter)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if search_period and not isinstance(search_period, str):
            raise TypeError("Expected argument 'search_period' to be a str")
        pulumi.set(__self__, "search_period", search_period)
        if sql_tuning_advisor_task_id and not isinstance(sql_tuning_advisor_task_id, str):
            raise TypeError("Expected argument 'sql_tuning_advisor_task_id' to be a str")
        pulumi.set(__self__, "sql_tuning_advisor_task_id", sql_tuning_advisor_task_id)
        if stats_hash_filter and not isinstance(stats_hash_filter, str):
            raise TypeError("Expected argument 'stats_hash_filter' to be a str")
        pulumi.set(__self__, "stats_hash_filter", stats_hash_filter)

    @property
    @pulumi.getter(name="beginExecId")
    def begin_exec_id(self) -> Optional[str]:
        return pulumi.get(self, "begin_exec_id")

    @property
    @pulumi.getter(name="endExecId")
    def end_exec_id(self) -> Optional[str]:
        return pulumi.get(self, "end_exec_id")

    @property
    @pulumi.getter(name="findingFilter")
    def finding_filter(self) -> Optional[str]:
        return pulumi.get(self, "finding_filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="indexHashFilter")
    def index_hash_filter(self) -> Optional[str]:
        return pulumi.get(self, "index_hash_filter")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetManagedDatabaseSqlTuningAdvisorTasksFindingItemResult']:
        """
        An array of the findings for a tuning task.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> str:
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter(name="searchPeriod")
    def search_period(self) -> Optional[str]:
        return pulumi.get(self, "search_period")

    @property
    @pulumi.getter(name="sqlTuningAdvisorTaskId")
    def sql_tuning_advisor_task_id(self) -> str:
        """
        The unique identifier of the SQL Tuning Advisor task. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "sql_tuning_advisor_task_id")

    @property
    @pulumi.getter(name="statsHashFilter")
    def stats_hash_filter(self) -> Optional[str]:
        return pulumi.get(self, "stats_hash_filter")


class AwaitableGetManagedDatabaseSqlTuningAdvisorTasksFindingResult(GetManagedDatabaseSqlTuningAdvisorTasksFindingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseSqlTuningAdvisorTasksFindingResult(
            begin_exec_id=self.begin_exec_id,
            end_exec_id=self.end_exec_id,
            finding_filter=self.finding_filter,
            id=self.id,
            index_hash_filter=self.index_hash_filter,
            items=self.items,
            managed_database_id=self.managed_database_id,
            search_period=self.search_period,
            sql_tuning_advisor_task_id=self.sql_tuning_advisor_task_id,
            stats_hash_filter=self.stats_hash_filter)


def get_managed_database_sql_tuning_advisor_tasks_finding(begin_exec_id: Optional[str] = None,
                                                          end_exec_id: Optional[str] = None,
                                                          finding_filter: Optional[str] = None,
                                                          index_hash_filter: Optional[str] = None,
                                                          managed_database_id: Optional[str] = None,
                                                          search_period: Optional[str] = None,
                                                          sql_tuning_advisor_task_id: Optional[str] = None,
                                                          stats_hash_filter: Optional[str] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseSqlTuningAdvisorTasksFindingResult:
    """
    This data source provides details about a specific Managed Database Sql Tuning Advisor Tasks Finding resource in Oracle Cloud Infrastructure Database Management service.

    Gets an array of the details of the findings that match specific filters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_sql_tuning_advisor_tasks_finding = oci.DatabaseManagement.get_managed_database_sql_tuning_advisor_tasks_finding(managed_database_id=test_managed_database["id"],
        sql_tuning_advisor_task_id=test_sql_tuning_advisor_task["id"],
        begin_exec_id=test_begin_exec["id"],
        end_exec_id=test_end_exec["id"],
        finding_filter=managed_database_sql_tuning_advisor_tasks_finding_finding_filter,
        index_hash_filter=managed_database_sql_tuning_advisor_tasks_finding_index_hash_filter,
        search_period=managed_database_sql_tuning_advisor_tasks_finding_search_period,
        stats_hash_filter=managed_database_sql_tuning_advisor_tasks_finding_stats_hash_filter)
    ```


    :param str begin_exec_id: The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task.
    :param str end_exec_id: The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task.
    :param str finding_filter: The filter used to display specific findings in the report.
    :param str index_hash_filter: The hash value of the index table name.
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str search_period: The search period during which the API will search for begin and end exec id, if not supplied. Unused if beginExecId and endExecId optional query params are both supplied.
    :param str sql_tuning_advisor_task_id: The SQL tuning task identifier. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str stats_hash_filter: The hash value of the object for the statistic finding search.
    """
    __args__ = dict()
    __args__['beginExecId'] = begin_exec_id
    __args__['endExecId'] = end_exec_id
    __args__['findingFilter'] = finding_filter
    __args__['indexHashFilter'] = index_hash_filter
    __args__['managedDatabaseId'] = managed_database_id
    __args__['searchPeriod'] = search_period
    __args__['sqlTuningAdvisorTaskId'] = sql_tuning_advisor_task_id
    __args__['statsHashFilter'] = stats_hash_filter
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseSqlTuningAdvisorTasksFinding:getManagedDatabaseSqlTuningAdvisorTasksFinding', __args__, opts=opts, typ=GetManagedDatabaseSqlTuningAdvisorTasksFindingResult).value

    return AwaitableGetManagedDatabaseSqlTuningAdvisorTasksFindingResult(
        begin_exec_id=pulumi.get(__ret__, 'begin_exec_id'),
        end_exec_id=pulumi.get(__ret__, 'end_exec_id'),
        finding_filter=pulumi.get(__ret__, 'finding_filter'),
        id=pulumi.get(__ret__, 'id'),
        index_hash_filter=pulumi.get(__ret__, 'index_hash_filter'),
        items=pulumi.get(__ret__, 'items'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        search_period=pulumi.get(__ret__, 'search_period'),
        sql_tuning_advisor_task_id=pulumi.get(__ret__, 'sql_tuning_advisor_task_id'),
        stats_hash_filter=pulumi.get(__ret__, 'stats_hash_filter'))


@_utilities.lift_output_func(get_managed_database_sql_tuning_advisor_tasks_finding)
def get_managed_database_sql_tuning_advisor_tasks_finding_output(begin_exec_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                                 end_exec_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                                 finding_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                                 index_hash_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                                 managed_database_id: Optional[pulumi.Input[str]] = None,
                                                                 search_period: Optional[pulumi.Input[Optional[str]]] = None,
                                                                 sql_tuning_advisor_task_id: Optional[pulumi.Input[str]] = None,
                                                                 stats_hash_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseSqlTuningAdvisorTasksFindingResult]:
    """
    This data source provides details about a specific Managed Database Sql Tuning Advisor Tasks Finding resource in Oracle Cloud Infrastructure Database Management service.

    Gets an array of the details of the findings that match specific filters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_sql_tuning_advisor_tasks_finding = oci.DatabaseManagement.get_managed_database_sql_tuning_advisor_tasks_finding(managed_database_id=test_managed_database["id"],
        sql_tuning_advisor_task_id=test_sql_tuning_advisor_task["id"],
        begin_exec_id=test_begin_exec["id"],
        end_exec_id=test_end_exec["id"],
        finding_filter=managed_database_sql_tuning_advisor_tasks_finding_finding_filter,
        index_hash_filter=managed_database_sql_tuning_advisor_tasks_finding_index_hash_filter,
        search_period=managed_database_sql_tuning_advisor_tasks_finding_search_period,
        stats_hash_filter=managed_database_sql_tuning_advisor_tasks_finding_stats_hash_filter)
    ```


    :param str begin_exec_id: The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task.
    :param str end_exec_id: The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task.
    :param str finding_filter: The filter used to display specific findings in the report.
    :param str index_hash_filter: The hash value of the index table name.
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str search_period: The search period during which the API will search for begin and end exec id, if not supplied. Unused if beginExecId and endExecId optional query params are both supplied.
    :param str sql_tuning_advisor_task_id: The SQL tuning task identifier. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str stats_hash_filter: The hash value of the object for the statistic finding search.
    """
    ...
