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
    'GetNetworkSourcesResult',
    'AwaitableGetNetworkSourcesResult',
    'get_network_sources',
    'get_network_sources_output',
]

@pulumi.output_type
class GetNetworkSourcesResult:
    """
    A collection of values returned by getNetworkSources.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, network_sources=None, state=None):
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
        if network_sources and not isinstance(network_sources, list):
            raise TypeError("Expected argument 'network_sources' to be a list")
        pulumi.set(__self__, "network_sources", network_sources)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the tenancy containing the network source. The tenancy is the root compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNetworkSourcesFilterResult']]:
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
        The name you assign to the network source during creation. The name must be unique across the tenancy and cannot be changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSources")
    def network_sources(self) -> Sequence['outputs.GetNetworkSourcesNetworkSourceResult']:
        """
        The list of network_sources.
        """
        return pulumi.get(self, "network_sources")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The network source object's current state. After creating a network source, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.
        """
        return pulumi.get(self, "state")


class AwaitableGetNetworkSourcesResult(GetNetworkSourcesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSourcesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            network_sources=self.network_sources,
            state=self.state)


def get_network_sources(compartment_id: Optional[str] = None,
                        filters: Optional[Sequence[pulumi.InputType['GetNetworkSourcesFilterArgs']]] = None,
                        name: Optional[str] = None,
                        state: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSourcesResult:
    """
    This data source provides the list of Network Sources in Oracle Cloud Infrastructure Identity service.

    Lists the network sources in your tenancy. You must specify your tenancy's OCID as the value for
    the compartment ID (remember that the tenancy is simply the root compartment).
    See [Where to Get the Tenancy's OCID and User's OCID](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_sources = oci.Identity.get_network_sources(compartment_id=tenancy_ocid,
        name=network_source_name,
        state=network_source_state)
    ```


    :param str compartment_id: The OCID of the compartment (remember that the tenancy is simply the root compartment).
    :param str name: A filter to only return resources that match the given name exactly.
    :param str state: A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getNetworkSources:getNetworkSources', __args__, opts=opts, typ=GetNetworkSourcesResult).value

    return AwaitableGetNetworkSourcesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network_sources=pulumi.get(__ret__, 'network_sources'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_network_sources)
def get_network_sources_output(compartment_id: Optional[pulumi.Input[str]] = None,
                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNetworkSourcesFilterArgs']]]]] = None,
                               name: Optional[pulumi.Input[Optional[str]]] = None,
                               state: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSourcesResult]:
    """
    This data source provides the list of Network Sources in Oracle Cloud Infrastructure Identity service.

    Lists the network sources in your tenancy. You must specify your tenancy's OCID as the value for
    the compartment ID (remember that the tenancy is simply the root compartment).
    See [Where to Get the Tenancy's OCID and User's OCID](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_sources = oci.Identity.get_network_sources(compartment_id=tenancy_ocid,
        name=network_source_name,
        state=network_source_state)
    ```


    :param str compartment_id: The OCID of the compartment (remember that the tenancy is simply the root compartment).
    :param str name: A filter to only return resources that match the given name exactly.
    :param str state: A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
    """
    ...
