# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSummarizeResourceInventoryResult',
    'AwaitableGetSummarizeResourceInventoryResult',
    'get_summarize_resource_inventory',
    'get_summarize_resource_inventory_output',
]

@pulumi.output_type
class GetSummarizeResourceInventoryResult:
    """
    A collection of values returned by getSummarizeResourceInventory.
    """
    def __init__(__self__, active_fleet_count=None, application_count=None, compartment_id=None, id=None, installation_count=None, jre_count=None, managed_instance_count=None, time_end=None, time_start=None):
        if active_fleet_count and not isinstance(active_fleet_count, int):
            raise TypeError("Expected argument 'active_fleet_count' to be a int")
        pulumi.set(__self__, "active_fleet_count", active_fleet_count)
        if application_count and not isinstance(application_count, int):
            raise TypeError("Expected argument 'application_count' to be a int")
        pulumi.set(__self__, "application_count", application_count)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if installation_count and not isinstance(installation_count, int):
            raise TypeError("Expected argument 'installation_count' to be a int")
        pulumi.set(__self__, "installation_count", installation_count)
        if jre_count and not isinstance(jre_count, int):
            raise TypeError("Expected argument 'jre_count' to be a int")
        pulumi.set(__self__, "jre_count", jre_count)
        if managed_instance_count and not isinstance(managed_instance_count, int):
            raise TypeError("Expected argument 'managed_instance_count' to be a int")
        pulumi.set(__self__, "managed_instance_count", managed_instance_count)
        if time_end and not isinstance(time_end, str):
            raise TypeError("Expected argument 'time_end' to be a str")
        pulumi.set(__self__, "time_end", time_end)
        if time_start and not isinstance(time_start, str):
            raise TypeError("Expected argument 'time_start' to be a str")
        pulumi.set(__self__, "time_start", time_start)

    @property
    @pulumi.getter(name="activeFleetCount")
    def active_fleet_count(self) -> int:
        """
        The number of _active_ fleets.
        """
        return pulumi.get(self, "active_fleet_count")

    @property
    @pulumi.getter(name="applicationCount")
    def application_count(self) -> int:
        """
        The number of applications.
        """
        return pulumi.get(self, "application_count")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installationCount")
    def installation_count(self) -> int:
        """
        The number of Java installations.
        """
        return pulumi.get(self, "installation_count")

    @property
    @pulumi.getter(name="jreCount")
    def jre_count(self) -> int:
        """
        The number of Java Runtimes.
        """
        return pulumi.get(self, "jre_count")

    @property
    @pulumi.getter(name="managedInstanceCount")
    def managed_instance_count(self) -> int:
        """
        The number of managed instances.
        """
        return pulumi.get(self, "managed_instance_count")

    @property
    @pulumi.getter(name="timeEnd")
    def time_end(self) -> Optional[str]:
        return pulumi.get(self, "time_end")

    @property
    @pulumi.getter(name="timeStart")
    def time_start(self) -> Optional[str]:
        return pulumi.get(self, "time_start")


class AwaitableGetSummarizeResourceInventoryResult(GetSummarizeResourceInventoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSummarizeResourceInventoryResult(
            active_fleet_count=self.active_fleet_count,
            application_count=self.application_count,
            compartment_id=self.compartment_id,
            id=self.id,
            installation_count=self.installation_count,
            jre_count=self.jre_count,
            managed_instance_count=self.managed_instance_count,
            time_end=self.time_end,
            time_start=self.time_start)


def get_summarize_resource_inventory(compartment_id: Optional[str] = None,
                                     time_end: Optional[str] = None,
                                     time_start: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSummarizeResourceInventoryResult:
    """
    This data source provides details about a specific Summarize Resource Inventory resource in Oracle Cloud Infrastructure Jms service.

    Retrieve the inventory of JMS resources in the specified compartment: a list of the number of _active_ fleets, managed instances, Java Runtimes, Java installations, and applications.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_summarize_resource_inventory = oci.Jms.get_summarize_resource_inventory(compartment_id=compartment_id,
        time_end=summarize_resource_inventory_time_end,
        time_start=summarize_resource_inventory_time_start)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param str time_end: The end of the time period during which resources are searched (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
    :param str time_start: The start of the time period during which resources are searched (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['timeEnd'] = time_end
    __args__['timeStart'] = time_start
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Jms/getSummarizeResourceInventory:getSummarizeResourceInventory', __args__, opts=opts, typ=GetSummarizeResourceInventoryResult).value

    return AwaitableGetSummarizeResourceInventoryResult(
        active_fleet_count=pulumi.get(__ret__, 'active_fleet_count'),
        application_count=pulumi.get(__ret__, 'application_count'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        installation_count=pulumi.get(__ret__, 'installation_count'),
        jre_count=pulumi.get(__ret__, 'jre_count'),
        managed_instance_count=pulumi.get(__ret__, 'managed_instance_count'),
        time_end=pulumi.get(__ret__, 'time_end'),
        time_start=pulumi.get(__ret__, 'time_start'))


@_utilities.lift_output_func(get_summarize_resource_inventory)
def get_summarize_resource_inventory_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            time_end: Optional[pulumi.Input[Optional[str]]] = None,
                                            time_start: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSummarizeResourceInventoryResult]:
    """
    This data source provides details about a specific Summarize Resource Inventory resource in Oracle Cloud Infrastructure Jms service.

    Retrieve the inventory of JMS resources in the specified compartment: a list of the number of _active_ fleets, managed instances, Java Runtimes, Java installations, and applications.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_summarize_resource_inventory = oci.Jms.get_summarize_resource_inventory(compartment_id=compartment_id,
        time_end=summarize_resource_inventory_time_end,
        time_start=summarize_resource_inventory_time_start)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param str time_end: The end of the time period during which resources are searched (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
    :param str time_start: The start of the time period during which resources are searched (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
    """
    ...
