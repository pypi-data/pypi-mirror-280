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
    'GetExternalDatabaseConnectorsResult',
    'AwaitableGetExternalDatabaseConnectorsResult',
    'get_external_database_connectors',
    'get_external_database_connectors_output',
]

@pulumi.output_type
class GetExternalDatabaseConnectorsResult:
    """
    A collection of values returned by getExternalDatabaseConnectors.
    """
    def __init__(__self__, compartment_id=None, display_name=None, external_database_connectors=None, external_database_id=None, filters=None, id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_database_connectors and not isinstance(external_database_connectors, list):
            raise TypeError("Expected argument 'external_database_connectors' to be a list")
        pulumi.set(__self__, "external_database_connectors", external_database_connectors)
        if external_database_id and not isinstance(external_database_id, str):
            raise TypeError("Expected argument 'external_database_id' to be a str")
        pulumi.set(__self__, "external_database_id", external_database_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The user-friendly name for the [external database connector](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails). The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalDatabaseConnectors")
    def external_database_connectors(self) -> Sequence['outputs.GetExternalDatabaseConnectorsExternalDatabaseConnectorResult']:
        """
        The list of external_database_connectors.
        """
        return pulumi.get(self, "external_database_connectors")

    @property
    @pulumi.getter(name="externalDatabaseId")
    def external_database_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external database resource.
        """
        return pulumi.get(self, "external_database_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetExternalDatabaseConnectorsFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current lifecycle state of the external database connector resource.
        """
        return pulumi.get(self, "state")


class AwaitableGetExternalDatabaseConnectorsResult(GetExternalDatabaseConnectorsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalDatabaseConnectorsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            external_database_connectors=self.external_database_connectors,
            external_database_id=self.external_database_id,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_external_database_connectors(compartment_id: Optional[str] = None,
                                     display_name: Optional[str] = None,
                                     external_database_id: Optional[str] = None,
                                     filters: Optional[Sequence[pulumi.InputType['GetExternalDatabaseConnectorsFilterArgs']]] = None,
                                     state: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalDatabaseConnectorsResult:
    """
    This data source provides the list of External Database Connectors in Oracle Cloud Infrastructure Database service.

    Gets a list of the external database connectors in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_database_connectors = oci.Database.get_external_database_connectors(compartment_id=compartment_id,
        external_database_id=test_database["id"],
        display_name=external_database_connector_display_name,
        state=external_database_connector_state)
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the entire display name given. The match is not case sensitive.
    :param str external_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external database whose connectors will be listed.
    :param str state: A filter to return only resources that match the specified lifecycle state.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['externalDatabaseId'] = external_database_id
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getExternalDatabaseConnectors:getExternalDatabaseConnectors', __args__, opts=opts, typ=GetExternalDatabaseConnectorsResult).value

    return AwaitableGetExternalDatabaseConnectorsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_database_connectors=pulumi.get(__ret__, 'external_database_connectors'),
        external_database_id=pulumi.get(__ret__, 'external_database_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_external_database_connectors)
def get_external_database_connectors_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                            display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                            external_database_id: Optional[pulumi.Input[str]] = None,
                                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetExternalDatabaseConnectorsFilterArgs']]]]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalDatabaseConnectorsResult]:
    """
    This data source provides the list of External Database Connectors in Oracle Cloud Infrastructure Database service.

    Gets a list of the external database connectors in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_database_connectors = oci.Database.get_external_database_connectors(compartment_id=compartment_id,
        external_database_id=test_database["id"],
        display_name=external_database_connector_display_name,
        state=external_database_connector_state)
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the entire display name given. The match is not case sensitive.
    :param str external_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external database whose connectors will be listed.
    :param str state: A filter to return only resources that match the specified lifecycle state.
    """
    ...
