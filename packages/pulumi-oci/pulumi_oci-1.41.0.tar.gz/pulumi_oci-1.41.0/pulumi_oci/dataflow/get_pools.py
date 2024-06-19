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
    'GetPoolsResult',
    'AwaitableGetPoolsResult',
    'get_pools',
    'get_pools_output',
]

@pulumi.output_type
class GetPoolsResult:
    """
    A collection of values returned by getPools.
    """
    def __init__(__self__, compartment_id=None, display_name=None, display_name_starts_with=None, filters=None, id=None, owner_principal_id=None, pool_collections=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if display_name_starts_with and not isinstance(display_name_starts_with, str):
            raise TypeError("Expected argument 'display_name_starts_with' to be a str")
        pulumi.set(__self__, "display_name_starts_with", display_name_starts_with)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if owner_principal_id and not isinstance(owner_principal_id, str):
            raise TypeError("Expected argument 'owner_principal_id' to be a str")
        pulumi.set(__self__, "owner_principal_id", owner_principal_id)
        if pool_collections and not isinstance(pool_collections, list):
            raise TypeError("Expected argument 'pool_collections' to be a list")
        pulumi.set(__self__, "pool_collections", pool_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of a compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="displayNameStartsWith")
    def display_name_starts_with(self) -> Optional[str]:
        return pulumi.get(self, "display_name_starts_with")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetPoolsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ownerPrincipalId")
    def owner_principal_id(self) -> Optional[str]:
        """
        The OCID of the user who created the resource.
        """
        return pulumi.get(self, "owner_principal_id")

    @property
    @pulumi.getter(name="poolCollections")
    def pool_collections(self) -> Sequence['outputs.GetPoolsPoolCollectionResult']:
        """
        The list of pool_collection.
        """
        return pulumi.get(self, "pool_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of this pool.
        """
        return pulumi.get(self, "state")


class AwaitableGetPoolsResult(GetPoolsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPoolsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            display_name_starts_with=self.display_name_starts_with,
            filters=self.filters,
            id=self.id,
            owner_principal_id=self.owner_principal_id,
            pool_collections=self.pool_collections,
            state=self.state)


def get_pools(compartment_id: Optional[str] = None,
              display_name: Optional[str] = None,
              display_name_starts_with: Optional[str] = None,
              filters: Optional[Sequence[pulumi.InputType['GetPoolsFilterArgs']]] = None,
              owner_principal_id: Optional[str] = None,
              state: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPoolsResult:
    """
    This data source provides the list of Pools in Oracle Cloud Infrastructure Data Flow service.

    Lists all pools in the specified compartment. The query must include compartmentId. The query may also include one other parameter. If the query does not include compartmentId, or includes compartmentId, but with two or more other parameters, an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_pools = oci.DataFlow.get_pools(compartment_id=compartment_id,
        display_name=pool_display_name,
        display_name_starts_with=pool_display_name_starts_with,
        owner_principal_id=test_owner_principal["id"],
        state=pool_state)
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str display_name: The query parameter for the Spark application name.
    :param str display_name_starts_with: The displayName prefix.
    :param str owner_principal_id: The OCID of the user who created the resource.
    :param str state: The LifecycleState of the pool.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['displayNameStartsWith'] = display_name_starts_with
    __args__['filters'] = filters
    __args__['ownerPrincipalId'] = owner_principal_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataFlow/getPools:getPools', __args__, opts=opts, typ=GetPoolsResult).value

    return AwaitableGetPoolsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        display_name_starts_with=pulumi.get(__ret__, 'display_name_starts_with'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        owner_principal_id=pulumi.get(__ret__, 'owner_principal_id'),
        pool_collections=pulumi.get(__ret__, 'pool_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_pools)
def get_pools_output(compartment_id: Optional[pulumi.Input[str]] = None,
                     display_name: Optional[pulumi.Input[Optional[str]]] = None,
                     display_name_starts_with: Optional[pulumi.Input[Optional[str]]] = None,
                     filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetPoolsFilterArgs']]]]] = None,
                     owner_principal_id: Optional[pulumi.Input[Optional[str]]] = None,
                     state: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPoolsResult]:
    """
    This data source provides the list of Pools in Oracle Cloud Infrastructure Data Flow service.

    Lists all pools in the specified compartment. The query must include compartmentId. The query may also include one other parameter. If the query does not include compartmentId, or includes compartmentId, but with two or more other parameters, an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_pools = oci.DataFlow.get_pools(compartment_id=compartment_id,
        display_name=pool_display_name,
        display_name_starts_with=pool_display_name_starts_with,
        owner_principal_id=test_owner_principal["id"],
        state=pool_state)
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str display_name: The query parameter for the Spark application name.
    :param str display_name_starts_with: The displayName prefix.
    :param str owner_principal_id: The OCID of the user who created the resource.
    :param str state: The LifecycleState of the pool.
    """
    ...
