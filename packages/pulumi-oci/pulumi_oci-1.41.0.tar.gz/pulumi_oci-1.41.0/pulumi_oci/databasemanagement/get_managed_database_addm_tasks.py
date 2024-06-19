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
    'GetManagedDatabaseAddmTasksResult',
    'AwaitableGetManagedDatabaseAddmTasksResult',
    'get_managed_database_addm_tasks',
    'get_managed_database_addm_tasks_output',
]

@pulumi.output_type
class GetManagedDatabaseAddmTasksResult:
    """
    A collection of values returned by getManagedDatabaseAddmTasks.
    """
    def __init__(__self__, addm_tasks_collections=None, filters=None, id=None, managed_database_id=None, time_end=None, time_start=None):
        if addm_tasks_collections and not isinstance(addm_tasks_collections, list):
            raise TypeError("Expected argument 'addm_tasks_collections' to be a list")
        pulumi.set(__self__, "addm_tasks_collections", addm_tasks_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if time_end and not isinstance(time_end, str):
            raise TypeError("Expected argument 'time_end' to be a str")
        pulumi.set(__self__, "time_end", time_end)
        if time_start and not isinstance(time_start, str):
            raise TypeError("Expected argument 'time_start' to be a str")
        pulumi.set(__self__, "time_start", time_start)

    @property
    @pulumi.getter(name="addmTasksCollections")
    def addm_tasks_collections(self) -> Sequence['outputs.GetManagedDatabaseAddmTasksAddmTasksCollectionResult']:
        """
        The list of addm_tasks_collection.
        """
        return pulumi.get(self, "addm_tasks_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedDatabaseAddmTasksFilterResult']]:
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
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        """
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter(name="timeEnd")
    def time_end(self) -> str:
        return pulumi.get(self, "time_end")

    @property
    @pulumi.getter(name="timeStart")
    def time_start(self) -> str:
        return pulumi.get(self, "time_start")


class AwaitableGetManagedDatabaseAddmTasksResult(GetManagedDatabaseAddmTasksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseAddmTasksResult(
            addm_tasks_collections=self.addm_tasks_collections,
            filters=self.filters,
            id=self.id,
            managed_database_id=self.managed_database_id,
            time_end=self.time_end,
            time_start=self.time_start)


def get_managed_database_addm_tasks(filters: Optional[Sequence[pulumi.InputType['GetManagedDatabaseAddmTasksFilterArgs']]] = None,
                                    managed_database_id: Optional[str] = None,
                                    time_end: Optional[str] = None,
                                    time_start: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseAddmTasksResult:
    """
    This data source provides the list of Managed Database Addm Tasks in Oracle Cloud Infrastructure Database Management service.

    Lists the metadata for each ADDM task who's end snapshot time falls within the provided start and end time. Details include
    the name of the ADDM task, description, user, status and creation date time.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_addm_tasks = oci.DatabaseManagement.get_managed_database_addm_tasks(managed_database_id=test_managed_database["id"],
        time_end=managed_database_addm_task_time_end,
        time_start=managed_database_addm_task_time_start)
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str time_end: The end of the time range to search for ADDM tasks as defined by date-time RFC3339 format.
    :param str time_start: The beginning of the time range to search for ADDM tasks as defined by date-time RFC3339 format.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['managedDatabaseId'] = managed_database_id
    __args__['timeEnd'] = time_end
    __args__['timeStart'] = time_start
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseAddmTasks:getManagedDatabaseAddmTasks', __args__, opts=opts, typ=GetManagedDatabaseAddmTasksResult).value

    return AwaitableGetManagedDatabaseAddmTasksResult(
        addm_tasks_collections=pulumi.get(__ret__, 'addm_tasks_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        time_end=pulumi.get(__ret__, 'time_end'),
        time_start=pulumi.get(__ret__, 'time_start'))


@_utilities.lift_output_func(get_managed_database_addm_tasks)
def get_managed_database_addm_tasks_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedDatabaseAddmTasksFilterArgs']]]]] = None,
                                           managed_database_id: Optional[pulumi.Input[str]] = None,
                                           time_end: Optional[pulumi.Input[str]] = None,
                                           time_start: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseAddmTasksResult]:
    """
    This data source provides the list of Managed Database Addm Tasks in Oracle Cloud Infrastructure Database Management service.

    Lists the metadata for each ADDM task who's end snapshot time falls within the provided start and end time. Details include
    the name of the ADDM task, description, user, status and creation date time.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_addm_tasks = oci.DatabaseManagement.get_managed_database_addm_tasks(managed_database_id=test_managed_database["id"],
        time_end=managed_database_addm_task_time_end,
        time_start=managed_database_addm_task_time_start)
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str time_end: The end of the time range to search for ADDM tasks as defined by date-time RFC3339 format.
    :param str time_start: The beginning of the time range to search for ADDM tasks as defined by date-time RFC3339 format.
    """
    ...
