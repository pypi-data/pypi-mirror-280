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
    'GetAddressListsResult',
    'AwaitableGetAddressListsResult',
    'get_address_lists',
    'get_address_lists_output',
]

@pulumi.output_type
class GetAddressListsResult:
    """
    A collection of values returned by getAddressLists.
    """
    def __init__(__self__, address_lists=None, compartment_id=None, filters=None, id=None, ids=None, names=None, states=None, time_created_greater_than_or_equal_to=None, time_created_less_than=None):
        if address_lists and not isinstance(address_lists, list):
            raise TypeError("Expected argument 'address_lists' to be a list")
        pulumi.set(__self__, "address_lists", address_lists)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if states and not isinstance(states, list):
            raise TypeError("Expected argument 'states' to be a list")
        pulumi.set(__self__, "states", states)
        if time_created_greater_than_or_equal_to and not isinstance(time_created_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_created_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_created_greater_than_or_equal_to", time_created_greater_than_or_equal_to)
        if time_created_less_than and not isinstance(time_created_less_than, str):
            raise TypeError("Expected argument 'time_created_less_than' to be a str")
        pulumi.set(__self__, "time_created_less_than", time_created_less_than)

    @property
    @pulumi.getter(name="addressLists")
    def address_lists(self) -> Sequence['outputs.GetAddressListsAddressListResult']:
        """
        The list of address_lists.
        """
        return pulumi.get(self, "address_lists")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the address list's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAddressListsFilterResult']]:
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
    def ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def states(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "states")

    @property
    @pulumi.getter(name="timeCreatedGreaterThanOrEqualTo")
    def time_created_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeCreatedLessThan")
    def time_created_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_less_than")


class AwaitableGetAddressListsResult(GetAddressListsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressListsResult(
            address_lists=self.address_lists,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            names=self.names,
            states=self.states,
            time_created_greater_than_or_equal_to=self.time_created_greater_than_or_equal_to,
            time_created_less_than=self.time_created_less_than)


def get_address_lists(compartment_id: Optional[str] = None,
                      filters: Optional[Sequence[pulumi.InputType['GetAddressListsFilterArgs']]] = None,
                      ids: Optional[Sequence[str]] = None,
                      names: Optional[Sequence[str]] = None,
                      states: Optional[Sequence[str]] = None,
                      time_created_greater_than_or_equal_to: Optional[str] = None,
                      time_created_less_than: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddressListsResult:
    """
    This data source provides the list of Address Lists in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

    Gets a list of address lists that can be used in a WAAS policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_address_lists = oci.Waas.get_address_lists(compartment_id=compartment_id,
        ids=address_list_ids,
        names=address_list_names,
        states=address_list_states,
        time_created_greater_than_or_equal_to=address_list_time_created_greater_than_or_equal_to,
        time_created_less_than=address_list_time_created_less_than)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the compartment is created.
    :param Sequence[str] ids: Filter address lists using a list of address lists OCIDs.
    :param Sequence[str] names: Filter address lists using a list of names.
    :param Sequence[str] states: Filter address lists using a list of lifecycle states.
    :param str time_created_greater_than_or_equal_to: A filter that matches address lists created on or after the specified date-time.
    :param str time_created_less_than: A filter that matches address lists created before the specified date-time.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['ids'] = ids
    __args__['names'] = names
    __args__['states'] = states
    __args__['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to
    __args__['timeCreatedLessThan'] = time_created_less_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Waas/getAddressLists:getAddressLists', __args__, opts=opts, typ=GetAddressListsResult).value

    return AwaitableGetAddressListsResult(
        address_lists=pulumi.get(__ret__, 'address_lists'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        names=pulumi.get(__ret__, 'names'),
        states=pulumi.get(__ret__, 'states'),
        time_created_greater_than_or_equal_to=pulumi.get(__ret__, 'time_created_greater_than_or_equal_to'),
        time_created_less_than=pulumi.get(__ret__, 'time_created_less_than'))


@_utilities.lift_output_func(get_address_lists)
def get_address_lists_output(compartment_id: Optional[pulumi.Input[str]] = None,
                             filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAddressListsFilterArgs']]]]] = None,
                             ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             states: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             time_created_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                             time_created_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddressListsResult]:
    """
    This data source provides the list of Address Lists in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

    Gets a list of address lists that can be used in a WAAS policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_address_lists = oci.Waas.get_address_lists(compartment_id=compartment_id,
        ids=address_list_ids,
        names=address_list_names,
        states=address_list_states,
        time_created_greater_than_or_equal_to=address_list_time_created_greater_than_or_equal_to,
        time_created_less_than=address_list_time_created_less_than)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the compartment is created.
    :param Sequence[str] ids: Filter address lists using a list of address lists OCIDs.
    :param Sequence[str] names: Filter address lists using a list of names.
    :param Sequence[str] states: Filter address lists using a list of lifecycle states.
    :param str time_created_greater_than_or_equal_to: A filter that matches address lists created on or after the specified date-time.
    :param str time_created_less_than: A filter that matches address lists created before the specified date-time.
    """
    ...
