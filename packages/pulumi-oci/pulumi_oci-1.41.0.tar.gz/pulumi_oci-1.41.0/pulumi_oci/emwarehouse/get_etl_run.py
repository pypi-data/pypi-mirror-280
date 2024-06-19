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

__all__ = [
    'GetEtlRunResult',
    'AwaitableGetEtlRunResult',
    'get_etl_run',
    'get_etl_run_output',
]

@pulumi.output_type
class GetEtlRunResult:
    """
    A collection of values returned by getEtlRun.
    """
    def __init__(__self__, compartment_id=None, display_name=None, em_warehouse_id=None, id=None, items=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if em_warehouse_id and not isinstance(em_warehouse_id, str):
            raise TypeError("Expected argument 'em_warehouse_id' to be a str")
        pulumi.set(__self__, "em_warehouse_id", em_warehouse_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The name of the ETLRun.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="emWarehouseId")
    def em_warehouse_id(self) -> str:
        return pulumi.get(self, "em_warehouse_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetEtlRunItemResult']:
        """
        List of runs
        """
        return pulumi.get(self, "items")


class AwaitableGetEtlRunResult(GetEtlRunResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEtlRunResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            em_warehouse_id=self.em_warehouse_id,
            id=self.id,
            items=self.items)


def get_etl_run(compartment_id: Optional[str] = None,
                display_name: Optional[str] = None,
                em_warehouse_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEtlRunResult:
    """
    This data source provides details about a specific Em Warehouse Etl Run resource in Oracle Cloud Infrastructure Em Warehouse service.

    Gets a list of runs of an EmWarehouseResource by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_em_warehouse_etl_run = oci.EmWarehouse.get_etl_run(em_warehouse_id=test_em_warehouse["id"],
        compartment_id=compartment_id,
        display_name=em_warehouse_etl_run_display_name)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str em_warehouse_id: unique EmWarehouse identifier
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['emWarehouseId'] = em_warehouse_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:EmWarehouse/getEtlRun:getEtlRun', __args__, opts=opts, typ=GetEtlRunResult).value

    return AwaitableGetEtlRunResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        em_warehouse_id=pulumi.get(__ret__, 'em_warehouse_id'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'))


@_utilities.lift_output_func(get_etl_run)
def get_etl_run_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                       em_warehouse_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEtlRunResult]:
    """
    This data source provides details about a specific Em Warehouse Etl Run resource in Oracle Cloud Infrastructure Em Warehouse service.

    Gets a list of runs of an EmWarehouseResource by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_em_warehouse_etl_run = oci.EmWarehouse.get_etl_run(em_warehouse_id=test_em_warehouse["id"],
        compartment_id=compartment_id,
        display_name=em_warehouse_etl_run_display_name)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str em_warehouse_id: unique EmWarehouse identifier
    """
    ...
