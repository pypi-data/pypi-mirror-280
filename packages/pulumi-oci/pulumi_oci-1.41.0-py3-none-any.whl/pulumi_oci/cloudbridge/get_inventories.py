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
    'GetInventoriesResult',
    'AwaitableGetInventoriesResult',
    'get_inventories',
    'get_inventories_output',
]

@pulumi.output_type
class GetInventoriesResult:
    """
    A collection of values returned by getInventories.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, inventory_collections=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inventory_collections and not isinstance(inventory_collections, list):
            raise TypeError("Expected argument 'inventory_collections' to be a list")
        pulumi.set(__self__, "inventory_collections", inventory_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the tenantId.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetInventoriesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inventoryCollections")
    def inventory_collections(self) -> Sequence['outputs.GetInventoriesInventoryCollectionResult']:
        """
        The list of inventory_collection.
        """
        return pulumi.get(self, "inventory_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the inventory.
        """
        return pulumi.get(self, "state")


class AwaitableGetInventoriesResult(GetInventoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInventoriesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            inventory_collections=self.inventory_collections,
            state=self.state)


def get_inventories(compartment_id: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetInventoriesFilterArgs']]] = None,
                    state: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInventoriesResult:
    """
    This data source provides the list of Inventories in Oracle Cloud Infrastructure Cloud Bridge service.

    Returns a list of inventories.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_inventories = oci.CloudBridge.get_inventories(compartment_id=compartment_id,
        state=inventory_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str state: A filter to return inventory if the lifecycleState matches the given lifecycleState.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudBridge/getInventories:getInventories', __args__, opts=opts, typ=GetInventoriesResult).value

    return AwaitableGetInventoriesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        inventory_collections=pulumi.get(__ret__, 'inventory_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_inventories)
def get_inventories_output(compartment_id: Optional[pulumi.Input[str]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInventoriesFilterArgs']]]]] = None,
                           state: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInventoriesResult]:
    """
    This data source provides the list of Inventories in Oracle Cloud Infrastructure Cloud Bridge service.

    Returns a list of inventories.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_inventories = oci.CloudBridge.get_inventories(compartment_id=compartment_id,
        state=inventory_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str state: A filter to return inventory if the lifecycleState matches the given lifecycleState.
    """
    ...
