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
    'GetManagedDatabaseAttentionLogCountsResult',
    'AwaitableGetManagedDatabaseAttentionLogCountsResult',
    'get_managed_database_attention_log_counts',
    'get_managed_database_attention_log_counts_output',
]

@pulumi.output_type
class GetManagedDatabaseAttentionLogCountsResult:
    """
    A collection of values returned by getManagedDatabaseAttentionLogCounts.
    """
    def __init__(__self__, attention_log_counts_collections=None, filters=None, group_by=None, id=None, is_regular_expression=None, log_search_text=None, managed_database_id=None, time_greater_than_or_equal_to=None, time_less_than_or_equal_to=None, type_filter=None, urgency_filter=None):
        if attention_log_counts_collections and not isinstance(attention_log_counts_collections, list):
            raise TypeError("Expected argument 'attention_log_counts_collections' to be a list")
        pulumi.set(__self__, "attention_log_counts_collections", attention_log_counts_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if group_by and not isinstance(group_by, str):
            raise TypeError("Expected argument 'group_by' to be a str")
        pulumi.set(__self__, "group_by", group_by)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_regular_expression and not isinstance(is_regular_expression, bool):
            raise TypeError("Expected argument 'is_regular_expression' to be a bool")
        pulumi.set(__self__, "is_regular_expression", is_regular_expression)
        if log_search_text and not isinstance(log_search_text, str):
            raise TypeError("Expected argument 'log_search_text' to be a str")
        pulumi.set(__self__, "log_search_text", log_search_text)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if time_greater_than_or_equal_to and not isinstance(time_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_greater_than_or_equal_to", time_greater_than_or_equal_to)
        if time_less_than_or_equal_to and not isinstance(time_less_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_less_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_less_than_or_equal_to", time_less_than_or_equal_to)
        if type_filter and not isinstance(type_filter, str):
            raise TypeError("Expected argument 'type_filter' to be a str")
        pulumi.set(__self__, "type_filter", type_filter)
        if urgency_filter and not isinstance(urgency_filter, str):
            raise TypeError("Expected argument 'urgency_filter' to be a str")
        pulumi.set(__self__, "urgency_filter", urgency_filter)

    @property
    @pulumi.getter(name="attentionLogCountsCollections")
    def attention_log_counts_collections(self) -> Sequence['outputs.GetManagedDatabaseAttentionLogCountsAttentionLogCountsCollectionResult']:
        """
        The list of attention_log_counts_collection.
        """
        return pulumi.get(self, "attention_log_counts_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedDatabaseAttentionLogCountsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="groupBy")
    def group_by(self) -> Optional[str]:
        return pulumi.get(self, "group_by")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isRegularExpression")
    def is_regular_expression(self) -> Optional[bool]:
        return pulumi.get(self, "is_regular_expression")

    @property
    @pulumi.getter(name="logSearchText")
    def log_search_text(self) -> Optional[str]:
        return pulumi.get(self, "log_search_text")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        """
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter(name="timeGreaterThanOrEqualTo")
    def time_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeLessThanOrEqualTo")
    def time_less_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_less_than_or_equal_to")

    @property
    @pulumi.getter(name="typeFilter")
    def type_filter(self) -> Optional[str]:
        return pulumi.get(self, "type_filter")

    @property
    @pulumi.getter(name="urgencyFilter")
    def urgency_filter(self) -> Optional[str]:
        return pulumi.get(self, "urgency_filter")


class AwaitableGetManagedDatabaseAttentionLogCountsResult(GetManagedDatabaseAttentionLogCountsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseAttentionLogCountsResult(
            attention_log_counts_collections=self.attention_log_counts_collections,
            filters=self.filters,
            group_by=self.group_by,
            id=self.id,
            is_regular_expression=self.is_regular_expression,
            log_search_text=self.log_search_text,
            managed_database_id=self.managed_database_id,
            time_greater_than_or_equal_to=self.time_greater_than_or_equal_to,
            time_less_than_or_equal_to=self.time_less_than_or_equal_to,
            type_filter=self.type_filter,
            urgency_filter=self.urgency_filter)


def get_managed_database_attention_log_counts(filters: Optional[Sequence[pulumi.InputType['GetManagedDatabaseAttentionLogCountsFilterArgs']]] = None,
                                              group_by: Optional[str] = None,
                                              is_regular_expression: Optional[bool] = None,
                                              log_search_text: Optional[str] = None,
                                              managed_database_id: Optional[str] = None,
                                              time_greater_than_or_equal_to: Optional[str] = None,
                                              time_less_than_or_equal_to: Optional[str] = None,
                                              type_filter: Optional[str] = None,
                                              urgency_filter: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseAttentionLogCountsResult:
    """
    This data source provides the list of Managed Database Attention Log Counts in Oracle Cloud Infrastructure Database Management service.

    Get the counts of attention logs for the specified Managed Database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_attention_log_counts = oci.DatabaseManagement.get_managed_database_attention_log_counts(managed_database_id=test_managed_database["id"],
        group_by=managed_database_attention_log_count_group_by,
        is_regular_expression=managed_database_attention_log_count_is_regular_expression,
        log_search_text=managed_database_attention_log_count_log_search_text,
        time_greater_than_or_equal_to=managed_database_attention_log_count_time_greater_than_or_equal_to,
        time_less_than_or_equal_to=managed_database_attention_log_count_time_less_than_or_equal_to,
        type_filter=managed_database_attention_log_count_type_filter,
        urgency_filter=managed_database_attention_log_count_urgency_filter)
    ```


    :param str group_by: The optional parameter used to group different attention logs.
    :param bool is_regular_expression: The flag to indicate whether the search text is regular expression or not.
    :param str log_search_text: The optional query parameter to filter the attention or alert logs by search text.
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str time_greater_than_or_equal_to: The optional greater than or equal to timestamp to filter the logs.
    :param str time_less_than_or_equal_to: The optional less than or equal to timestamp to filter the logs.
    :param str type_filter: The optional parameter to filter the attention or alert logs by type.
    :param str urgency_filter: The optional parameter to filter the attention logs by urgency.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['groupBy'] = group_by
    __args__['isRegularExpression'] = is_regular_expression
    __args__['logSearchText'] = log_search_text
    __args__['managedDatabaseId'] = managed_database_id
    __args__['timeGreaterThanOrEqualTo'] = time_greater_than_or_equal_to
    __args__['timeLessThanOrEqualTo'] = time_less_than_or_equal_to
    __args__['typeFilter'] = type_filter
    __args__['urgencyFilter'] = urgency_filter
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseAttentionLogCounts:getManagedDatabaseAttentionLogCounts', __args__, opts=opts, typ=GetManagedDatabaseAttentionLogCountsResult).value

    return AwaitableGetManagedDatabaseAttentionLogCountsResult(
        attention_log_counts_collections=pulumi.get(__ret__, 'attention_log_counts_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        group_by=pulumi.get(__ret__, 'group_by'),
        id=pulumi.get(__ret__, 'id'),
        is_regular_expression=pulumi.get(__ret__, 'is_regular_expression'),
        log_search_text=pulumi.get(__ret__, 'log_search_text'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        time_greater_than_or_equal_to=pulumi.get(__ret__, 'time_greater_than_or_equal_to'),
        time_less_than_or_equal_to=pulumi.get(__ret__, 'time_less_than_or_equal_to'),
        type_filter=pulumi.get(__ret__, 'type_filter'),
        urgency_filter=pulumi.get(__ret__, 'urgency_filter'))


@_utilities.lift_output_func(get_managed_database_attention_log_counts)
def get_managed_database_attention_log_counts_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedDatabaseAttentionLogCountsFilterArgs']]]]] = None,
                                                     group_by: Optional[pulumi.Input[Optional[str]]] = None,
                                                     is_regular_expression: Optional[pulumi.Input[Optional[bool]]] = None,
                                                     log_search_text: Optional[pulumi.Input[Optional[str]]] = None,
                                                     managed_database_id: Optional[pulumi.Input[str]] = None,
                                                     time_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                     time_less_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                     type_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                     urgency_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseAttentionLogCountsResult]:
    """
    This data source provides the list of Managed Database Attention Log Counts in Oracle Cloud Infrastructure Database Management service.

    Get the counts of attention logs for the specified Managed Database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_attention_log_counts = oci.DatabaseManagement.get_managed_database_attention_log_counts(managed_database_id=test_managed_database["id"],
        group_by=managed_database_attention_log_count_group_by,
        is_regular_expression=managed_database_attention_log_count_is_regular_expression,
        log_search_text=managed_database_attention_log_count_log_search_text,
        time_greater_than_or_equal_to=managed_database_attention_log_count_time_greater_than_or_equal_to,
        time_less_than_or_equal_to=managed_database_attention_log_count_time_less_than_or_equal_to,
        type_filter=managed_database_attention_log_count_type_filter,
        urgency_filter=managed_database_attention_log_count_urgency_filter)
    ```


    :param str group_by: The optional parameter used to group different attention logs.
    :param bool is_regular_expression: The flag to indicate whether the search text is regular expression or not.
    :param str log_search_text: The optional query parameter to filter the attention or alert logs by search text.
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str time_greater_than_or_equal_to: The optional greater than or equal to timestamp to filter the logs.
    :param str time_less_than_or_equal_to: The optional less than or equal to timestamp to filter the logs.
    :param str type_filter: The optional parameter to filter the attention or alert logs by type.
    :param str urgency_filter: The optional parameter to filter the attention logs by urgency.
    """
    ...
