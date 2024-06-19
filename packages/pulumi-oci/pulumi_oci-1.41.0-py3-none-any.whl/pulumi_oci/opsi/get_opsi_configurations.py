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
    'GetOpsiConfigurationsResult',
    'AwaitableGetOpsiConfigurationsResult',
    'get_opsi_configurations',
    'get_opsi_configurations_output',
]

@pulumi.output_type
class GetOpsiConfigurationsResult:
    """
    A collection of values returned by getOpsiConfigurations.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, opsi_config_types=None, opsi_configurations_collections=None, states=None):
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
        if opsi_config_types and not isinstance(opsi_config_types, list):
            raise TypeError("Expected argument 'opsi_config_types' to be a list")
        pulumi.set(__self__, "opsi_config_types", opsi_config_types)
        if opsi_configurations_collections and not isinstance(opsi_configurations_collections, list):
            raise TypeError("Expected argument 'opsi_configurations_collections' to be a list")
        pulumi.set(__self__, "opsi_configurations_collections", opsi_configurations_collections)
        if states and not isinstance(states, list):
            raise TypeError("Expected argument 'states' to be a list")
        pulumi.set(__self__, "states", states)

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
        User-friendly display name for the OPSI configuration. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetOpsiConfigurationsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="opsiConfigTypes")
    def opsi_config_types(self) -> Optional[Sequence[str]]:
        """
        OPSI configuration type.
        """
        return pulumi.get(self, "opsi_config_types")

    @property
    @pulumi.getter(name="opsiConfigurationsCollections")
    def opsi_configurations_collections(self) -> Sequence['outputs.GetOpsiConfigurationsOpsiConfigurationsCollectionResult']:
        """
        The list of opsi_configurations_collection.
        """
        return pulumi.get(self, "opsi_configurations_collections")

    @property
    @pulumi.getter
    def states(self) -> Optional[Sequence[str]]:
        """
        OPSI configuration resource lifecycle state.
        """
        return pulumi.get(self, "states")


class AwaitableGetOpsiConfigurationsResult(GetOpsiConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOpsiConfigurationsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            opsi_config_types=self.opsi_config_types,
            opsi_configurations_collections=self.opsi_configurations_collections,
            states=self.states)


def get_opsi_configurations(compartment_id: Optional[str] = None,
                            display_name: Optional[str] = None,
                            filters: Optional[Sequence[pulumi.InputType['GetOpsiConfigurationsFilterArgs']]] = None,
                            opsi_config_types: Optional[Sequence[str]] = None,
                            states: Optional[Sequence[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOpsiConfigurationsResult:
    """
    This data source provides the list of Opsi Configurations in Oracle Cloud Infrastructure Opsi service.

    Gets a list of OPSI configuration resources based on the query parameters specified.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_opsi_configurations = oci.Opsi.get_opsi_configurations(compartment_id=compartment_id,
        display_name=opsi_configuration_display_name,
        opsi_config_types=opsi_configuration_opsi_config_type,
        states=opsi_configuration_state)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: Filter to return based on resources that match the entire display name.
    :param Sequence[str] opsi_config_types: Filter to return based on configuration type of OPSI configuration.
    :param Sequence[str] states: Filter to return based on Lifecycle state of OPSI configuration.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['opsiConfigTypes'] = opsi_config_types
    __args__['states'] = states
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Opsi/getOpsiConfigurations:getOpsiConfigurations', __args__, opts=opts, typ=GetOpsiConfigurationsResult).value

    return AwaitableGetOpsiConfigurationsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        opsi_config_types=pulumi.get(__ret__, 'opsi_config_types'),
        opsi_configurations_collections=pulumi.get(__ret__, 'opsi_configurations_collections'),
        states=pulumi.get(__ret__, 'states'))


@_utilities.lift_output_func(get_opsi_configurations)
def get_opsi_configurations_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                   display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetOpsiConfigurationsFilterArgs']]]]] = None,
                                   opsi_config_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                   states: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOpsiConfigurationsResult]:
    """
    This data source provides the list of Opsi Configurations in Oracle Cloud Infrastructure Opsi service.

    Gets a list of OPSI configuration resources based on the query parameters specified.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_opsi_configurations = oci.Opsi.get_opsi_configurations(compartment_id=compartment_id,
        display_name=opsi_configuration_display_name,
        opsi_config_types=opsi_configuration_opsi_config_type,
        states=opsi_configuration_state)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: Filter to return based on resources that match the entire display name.
    :param Sequence[str] opsi_config_types: Filter to return based on configuration type of OPSI configuration.
    :param Sequence[str] states: Filter to return based on Lifecycle state of OPSI configuration.
    """
    ...
