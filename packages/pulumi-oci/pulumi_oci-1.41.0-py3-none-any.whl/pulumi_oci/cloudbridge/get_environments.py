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
    'GetEnvironmentsResult',
    'AwaitableGetEnvironmentsResult',
    'get_environments',
    'get_environments_output',
]

@pulumi.output_type
class GetEnvironmentsResult:
    """
    A collection of values returned by getEnvironments.
    """
    def __init__(__self__, compartment_id=None, display_name=None, environment_collections=None, environment_id=None, filters=None, id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if environment_collections and not isinstance(environment_collections, list):
            raise TypeError("Expected argument 'environment_collections' to be a list")
        pulumi.set(__self__, "environment_collections", environment_collections)
        if environment_id and not isinstance(environment_id, str):
            raise TypeError("Expected argument 'environment_id' to be a str")
        pulumi.set(__self__, "environment_id", environment_id)
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
        Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Environment identifier, which can be renamed.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="environmentCollections")
    def environment_collections(self) -> Sequence['outputs.GetEnvironmentsEnvironmentCollectionResult']:
        """
        The list of environment_collection.
        """
        return pulumi.get(self, "environment_collections")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[str]:
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetEnvironmentsFilterResult']]:
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
        The current state of the source environment.
        """
        return pulumi.get(self, "state")


class AwaitableGetEnvironmentsResult(GetEnvironmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            environment_collections=self.environment_collections,
            environment_id=self.environment_id,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_environments(compartment_id: Optional[str] = None,
                     display_name: Optional[str] = None,
                     environment_id: Optional[str] = None,
                     filters: Optional[Sequence[pulumi.InputType['GetEnvironmentsFilterArgs']]] = None,
                     state: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentsResult:
    """
    This data source provides the list of Environments in Oracle Cloud Infrastructure Cloud Bridge service.

    Returns a list of source environments.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_environments = oci.CloudBridge.get_environments(compartment_id=compartment_id,
        display_name=environment_display_name,
        environment_id=test_environment["id"],
        state=environment_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str environment_id: A filter to return only resources that match the given environment ID.
    :param str state: A filter to return only resources where their lifecycleState matches the given lifecycleState.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['environmentId'] = environment_id
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudBridge/getEnvironments:getEnvironments', __args__, opts=opts, typ=GetEnvironmentsResult).value

    return AwaitableGetEnvironmentsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        environment_collections=pulumi.get(__ret__, 'environment_collections'),
        environment_id=pulumi.get(__ret__, 'environment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_environments)
def get_environments_output(compartment_id: Optional[pulumi.Input[str]] = None,
                            display_name: Optional[pulumi.Input[Optional[str]]] = None,
                            environment_id: Optional[pulumi.Input[Optional[str]]] = None,
                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetEnvironmentsFilterArgs']]]]] = None,
                            state: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentsResult]:
    """
    This data source provides the list of Environments in Oracle Cloud Infrastructure Cloud Bridge service.

    Returns a list of source environments.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_environments = oci.CloudBridge.get_environments(compartment_id=compartment_id,
        display_name=environment_display_name,
        environment_id=test_environment["id"],
        state=environment_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str environment_id: A filter to return only resources that match the given environment ID.
    :param str state: A filter to return only resources where their lifecycleState matches the given lifecycleState.
    """
    ...
