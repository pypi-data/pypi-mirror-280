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
    'GetOutboundConnectorsResult',
    'AwaitableGetOutboundConnectorsResult',
    'get_outbound_connectors',
    'get_outbound_connectors_output',
]

@pulumi.output_type
class GetOutboundConnectorsResult:
    """
    A collection of values returned by getOutboundConnectors.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, display_name=None, filters=None, id=None, outbound_connectors=None, state=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if outbound_connectors and not isinstance(outbound_connectors, list):
            raise TypeError("Expected argument 'outbound_connectors' to be a list")
        pulumi.set(__self__, "outbound_connectors", outbound_connectors)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain the outbound connector is in. May be unset as a blank or NULL value.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the outbound connector.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My outbound connector`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetOutboundConnectorsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the outbound connector.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="outboundConnectors")
    def outbound_connectors(self) -> Sequence['outputs.GetOutboundConnectorsOutboundConnectorResult']:
        """
        The list of outbound_connectors.
        """
        return pulumi.get(self, "outbound_connectors")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of this outbound connector.
        """
        return pulumi.get(self, "state")


class AwaitableGetOutboundConnectorsResult(GetOutboundConnectorsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOutboundConnectorsResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            outbound_connectors=self.outbound_connectors,
            state=self.state)


def get_outbound_connectors(availability_domain: Optional[str] = None,
                            compartment_id: Optional[str] = None,
                            display_name: Optional[str] = None,
                            filters: Optional[Sequence[pulumi.InputType['GetOutboundConnectorsFilterArgs']]] = None,
                            id: Optional[str] = None,
                            state: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOutboundConnectorsResult:
    """
    This data source provides the list of Outbound Connectors in Oracle Cloud Infrastructure File Storage service.

    Lists the outbound connector resources in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_outbound_connectors = oci.FileStorage.get_outbound_connectors(availability_domain=outbound_connector_availability_domain,
        compartment_id=compartment_id,
        display_name=outbound_connector_display_name,
        id=outbound_connector_id,
        state=outbound_connector_state)
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:FileStorage/getOutboundConnectors:getOutboundConnectors', __args__, opts=opts, typ=GetOutboundConnectorsResult).value

    return AwaitableGetOutboundConnectorsResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        outbound_connectors=pulumi.get(__ret__, 'outbound_connectors'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_outbound_connectors)
def get_outbound_connectors_output(availability_domain: Optional[pulumi.Input[str]] = None,
                                   compartment_id: Optional[pulumi.Input[str]] = None,
                                   display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetOutboundConnectorsFilterArgs']]]]] = None,
                                   id: Optional[pulumi.Input[Optional[str]]] = None,
                                   state: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOutboundConnectorsResult]:
    """
    This data source provides the list of Outbound Connectors in Oracle Cloud Infrastructure File Storage service.

    Lists the outbound connector resources in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_outbound_connectors = oci.FileStorage.get_outbound_connectors(availability_domain=outbound_connector_availability_domain,
        compartment_id=compartment_id,
        display_name=outbound_connector_display_name,
        id=outbound_connector_id,
        state=outbound_connector_state)
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
