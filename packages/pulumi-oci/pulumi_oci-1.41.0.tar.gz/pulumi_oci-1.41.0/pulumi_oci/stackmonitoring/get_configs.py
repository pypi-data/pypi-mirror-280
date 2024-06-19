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
    'GetConfigsResult',
    'AwaitableGetConfigsResult',
    'get_configs',
    'get_configs_output',
]

@pulumi.output_type
class GetConfigsResult:
    """
    A collection of values returned by getConfigs.
    """
    def __init__(__self__, compartment_id=None, config_collections=None, display_name=None, filters=None, id=None, state=None, type=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if config_collections and not isinstance(config_collections, list):
            raise TypeError("Expected argument 'config_collections' to be a list")
        pulumi.set(__self__, "config_collections", config_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the configuration.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="configCollections")
    def config_collections(self) -> Sequence['outputs.GetConfigsConfigCollectionResult']:
        """
        The list of config_collection.
        """
        return pulumi.get(self, "config_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetConfigsFilterResult']]:
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
        The current state of the configuration.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetConfigsResult(GetConfigsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigsResult(
            compartment_id=self.compartment_id,
            config_collections=self.config_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state,
            type=self.type)


def get_configs(compartment_id: Optional[str] = None,
                display_name: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetConfigsFilterArgs']]] = None,
                state: Optional[str] = None,
                type: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigsResult:
    """
    This data source provides the list of Configs in Oracle Cloud Infrastructure Stack Monitoring service.

    Get a list of configurations in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_configs = oci.StackMonitoring.get_configs(compartment_id=compartment_id,
        display_name=config_display_name,
        state=config_state,
        type=config_type)
    ```


    :param str compartment_id: The ID of the compartment in which data is listed.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: The current state of the Config.
    :param str type: A filter to return only configuration items for a given config type. The only valid config type is `"AUTO_PROMOTE"`
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:StackMonitoring/getConfigs:getConfigs', __args__, opts=opts, typ=GetConfigsResult).value

    return AwaitableGetConfigsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        config_collections=pulumi.get(__ret__, 'config_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_configs)
def get_configs_output(compartment_id: Optional[pulumi.Input[str]] = None,
                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetConfigsFilterArgs']]]]] = None,
                       state: Optional[pulumi.Input[Optional[str]]] = None,
                       type: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigsResult]:
    """
    This data source provides the list of Configs in Oracle Cloud Infrastructure Stack Monitoring service.

    Get a list of configurations in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_configs = oci.StackMonitoring.get_configs(compartment_id=compartment_id,
        display_name=config_display_name,
        state=config_state,
        type=config_type)
    ```


    :param str compartment_id: The ID of the compartment in which data is listed.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: The current state of the Config.
    :param str type: A filter to return only configuration items for a given config type. The only valid config type is `"AUTO_PROMOTE"`
    """
    ...
