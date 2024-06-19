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
from ._inputs import *

__all__ = [
    'GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult',
    'AwaitableGetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult',
    'get_managed_database_optimizer_statistics_advisor_executions',
    'get_managed_database_optimizer_statistics_advisor_executions_output',
]

@pulumi.output_type
class GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult:
    """
    A collection of values returned by getManagedDatabaseOptimizerStatisticsAdvisorExecutions.
    """
    def __init__(__self__, end_time_less_than_or_equal_to=None, filters=None, id=None, managed_database_id=None, optimizer_statistics_advisor_executions_collections=None, start_time_greater_than_or_equal_to=None):
        if end_time_less_than_or_equal_to and not isinstance(end_time_less_than_or_equal_to, str):
            raise TypeError("Expected argument 'end_time_less_than_or_equal_to' to be a str")
        pulumi.set(__self__, "end_time_less_than_or_equal_to", end_time_less_than_or_equal_to)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if optimizer_statistics_advisor_executions_collections and not isinstance(optimizer_statistics_advisor_executions_collections, list):
            raise TypeError("Expected argument 'optimizer_statistics_advisor_executions_collections' to be a list")
        pulumi.set(__self__, "optimizer_statistics_advisor_executions_collections", optimizer_statistics_advisor_executions_collections)
        if start_time_greater_than_or_equal_to and not isinstance(start_time_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'start_time_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "start_time_greater_than_or_equal_to", start_time_greater_than_or_equal_to)

    @property
    @pulumi.getter(name="endTimeLessThanOrEqualTo")
    def end_time_less_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "end_time_less_than_or_equal_to")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> str:
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter(name="optimizerStatisticsAdvisorExecutionsCollections")
    def optimizer_statistics_advisor_executions_collections(self) -> Sequence['outputs.GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsOptimizerStatisticsAdvisorExecutionsCollectionResult']:
        """
        The list of optimizer_statistics_advisor_executions_collection.
        """
        return pulumi.get(self, "optimizer_statistics_advisor_executions_collections")

    @property
    @pulumi.getter(name="startTimeGreaterThanOrEqualTo")
    def start_time_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "start_time_greater_than_or_equal_to")


class AwaitableGetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult(GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult(
            end_time_less_than_or_equal_to=self.end_time_less_than_or_equal_to,
            filters=self.filters,
            id=self.id,
            managed_database_id=self.managed_database_id,
            optimizer_statistics_advisor_executions_collections=self.optimizer_statistics_advisor_executions_collections,
            start_time_greater_than_or_equal_to=self.start_time_greater_than_or_equal_to)


def get_managed_database_optimizer_statistics_advisor_executions(end_time_less_than_or_equal_to: Optional[str] = None,
                                                                 filters: Optional[Sequence[pulumi.InputType['GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsFilterArgs']]] = None,
                                                                 managed_database_id: Optional[str] = None,
                                                                 start_time_greater_than_or_equal_to: Optional[str] = None,
                                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult:
    """
    This data source provides the list of Managed Database Optimizer Statistics Advisor Executions in Oracle Cloud Infrastructure Database Management service.

    Lists the details of the Optimizer Statistics Advisor task executions, such as their duration, and the number of findings, if any.
    Optionally, you can specify a date-time range (of seven days) to obtain the list of executions that fall within the specified time range.
    If the date-time range is not specified, then the executions in the last seven days are listed.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_optimizer_statistics_advisor_executions = oci.DatabaseManagement.get_managed_database_optimizer_statistics_advisor_executions(managed_database_id=test_managed_database["id"],
        end_time_less_than_or_equal_to=managed_database_optimizer_statistics_advisor_execution_end_time_less_than_or_equal_to,
        start_time_greater_than_or_equal_to=managed_database_optimizer_statistics_advisor_execution_start_time_greater_than_or_equal_to)
    ```


    :param str end_time_less_than_or_equal_to: The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is "yyyy-MM-dd'T'hh:mm:ss.sss'Z'".
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str start_time_greater_than_or_equal_to: The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is "yyyy-MM-dd'T'hh:mm:ss.sss'Z'".
    """
    __args__ = dict()
    __args__['endTimeLessThanOrEqualTo'] = end_time_less_than_or_equal_to
    __args__['filters'] = filters
    __args__['managedDatabaseId'] = managed_database_id
    __args__['startTimeGreaterThanOrEqualTo'] = start_time_greater_than_or_equal_to
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseOptimizerStatisticsAdvisorExecutions:getManagedDatabaseOptimizerStatisticsAdvisorExecutions', __args__, opts=opts, typ=GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult).value

    return AwaitableGetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult(
        end_time_less_than_or_equal_to=pulumi.get(__ret__, 'end_time_less_than_or_equal_to'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        optimizer_statistics_advisor_executions_collections=pulumi.get(__ret__, 'optimizer_statistics_advisor_executions_collections'),
        start_time_greater_than_or_equal_to=pulumi.get(__ret__, 'start_time_greater_than_or_equal_to'))


@_utilities.lift_output_func(get_managed_database_optimizer_statistics_advisor_executions)
def get_managed_database_optimizer_statistics_advisor_executions_output(end_time_less_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsFilterArgs']]]]] = None,
                                                                        managed_database_id: Optional[pulumi.Input[str]] = None,
                                                                        start_time_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseOptimizerStatisticsAdvisorExecutionsResult]:
    """
    This data source provides the list of Managed Database Optimizer Statistics Advisor Executions in Oracle Cloud Infrastructure Database Management service.

    Lists the details of the Optimizer Statistics Advisor task executions, such as their duration, and the number of findings, if any.
    Optionally, you can specify a date-time range (of seven days) to obtain the list of executions that fall within the specified time range.
    If the date-time range is not specified, then the executions in the last seven days are listed.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_optimizer_statistics_advisor_executions = oci.DatabaseManagement.get_managed_database_optimizer_statistics_advisor_executions(managed_database_id=test_managed_database["id"],
        end_time_less_than_or_equal_to=managed_database_optimizer_statistics_advisor_execution_end_time_less_than_or_equal_to,
        start_time_greater_than_or_equal_to=managed_database_optimizer_statistics_advisor_execution_start_time_greater_than_or_equal_to)
    ```


    :param str end_time_less_than_or_equal_to: The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is "yyyy-MM-dd'T'hh:mm:ss.sss'Z'".
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str start_time_greater_than_or_equal_to: The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is "yyyy-MM-dd'T'hh:mm:ss.sss'Z'".
    """
    ...
