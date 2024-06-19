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
    'GetSchedulesResult',
    'AwaitableGetSchedulesResult',
    'get_schedules',
    'get_schedules_output',
]

@pulumi.output_type
class GetSchedulesResult:
    """
    A collection of values returned by getSchedules.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, schedule_collections=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schedule_collections and not isinstance(schedule_collections, list):
            raise TypeError("Expected argument 'schedule_collections' to be a list")
        pulumi.set(__self__, "schedule_collections", schedule_collections)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The customer tenancy.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSchedulesFilterResult']]:
        """
        The filter object for query usage.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The unique name of the schedule created by the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scheduleCollections")
    def schedule_collections(self) -> Sequence['outputs.GetSchedulesScheduleCollectionResult']:
        """
        The list of schedule_collection.
        """
        return pulumi.get(self, "schedule_collections")


class AwaitableGetSchedulesResult(GetSchedulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchedulesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            schedule_collections=self.schedule_collections)


def get_schedules(compartment_id: Optional[str] = None,
                  filters: Optional[Sequence[pulumi.InputType['GetSchedulesFilterArgs']]] = None,
                  name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchedulesResult:
    """
    This data source provides the list of Schedules in Oracle Cloud Infrastructure Metering Computation service.

    Returns the saved schedule list.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_schedules = oci.MeteringComputation.get_schedules(compartment_id=compartment_id,
        name=schedule_name)
    ```


    :param str compartment_id: The compartment ID in which to list resources.
    :param Sequence[pulumi.InputType['GetSchedulesFilterArgs']] filters: The filter object for query usage.
    :param str name: Query parameter for filtering by name
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:MeteringComputation/getSchedules:getSchedules', __args__, opts=opts, typ=GetSchedulesResult).value

    return AwaitableGetSchedulesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        schedule_collections=pulumi.get(__ret__, 'schedule_collections'))


@_utilities.lift_output_func(get_schedules)
def get_schedules_output(compartment_id: Optional[pulumi.Input[str]] = None,
                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSchedulesFilterArgs']]]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchedulesResult]:
    """
    This data source provides the list of Schedules in Oracle Cloud Infrastructure Metering Computation service.

    Returns the saved schedule list.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_schedules = oci.MeteringComputation.get_schedules(compartment_id=compartment_id,
        name=schedule_name)
    ```


    :param str compartment_id: The compartment ID in which to list resources.
    :param Sequence[pulumi.InputType['GetSchedulesFilterArgs']] filters: The filter object for query usage.
    :param str name: Query parameter for filtering by name
    """
    ...
