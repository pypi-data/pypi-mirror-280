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
    'GetAssetSourcesResult',
    'AwaitableGetAssetSourcesResult',
    'get_asset_sources',
    'get_asset_sources_output',
]

@pulumi.output_type
class GetAssetSourcesResult:
    """
    A collection of values returned by getAssetSources.
    """
    def __init__(__self__, asset_source_collections=None, asset_source_id=None, compartment_id=None, display_name=None, filters=None, id=None, state=None):
        if asset_source_collections and not isinstance(asset_source_collections, list):
            raise TypeError("Expected argument 'asset_source_collections' to be a list")
        pulumi.set(__self__, "asset_source_collections", asset_source_collections)
        if asset_source_id and not isinstance(asset_source_id, str):
            raise TypeError("Expected argument 'asset_source_id' to be a str")
        pulumi.set(__self__, "asset_source_id", asset_source_id)
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
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="assetSourceCollections")
    def asset_source_collections(self) -> Sequence['outputs.GetAssetSourcesAssetSourceCollectionResult']:
        """
        The list of asset_source_collection.
        """
        return pulumi.get(self, "asset_source_collections")

    @property
    @pulumi.getter(name="assetSourceId")
    def asset_source_id(self) -> Optional[str]:
        return pulumi.get(self, "asset_source_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the resource.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAssetSourcesFilterResult']]:
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
        The current state of the asset source.
        """
        return pulumi.get(self, "state")


class AwaitableGetAssetSourcesResult(GetAssetSourcesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetSourcesResult(
            asset_source_collections=self.asset_source_collections,
            asset_source_id=self.asset_source_id,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_asset_sources(asset_source_id: Optional[str] = None,
                      compartment_id: Optional[str] = None,
                      display_name: Optional[str] = None,
                      filters: Optional[Sequence[pulumi.InputType['GetAssetSourcesFilterArgs']]] = None,
                      state: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetSourcesResult:
    """
    This data source provides the list of Asset Sources in Oracle Cloud Infrastructure Cloud Bridge service.

    Returns a list of asset sources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_asset_sources = oci.CloudBridge.get_asset_sources(compartment_id=compartment_id,
        asset_source_id=test_asset_source["id"],
        display_name=asset_source_display_name,
        state=asset_source_state)
    ```


    :param str asset_source_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the asset source.
    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: The current state of the asset source.
    """
    __args__ = dict()
    __args__['assetSourceId'] = asset_source_id
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudBridge/getAssetSources:getAssetSources', __args__, opts=opts, typ=GetAssetSourcesResult).value

    return AwaitableGetAssetSourcesResult(
        asset_source_collections=pulumi.get(__ret__, 'asset_source_collections'),
        asset_source_id=pulumi.get(__ret__, 'asset_source_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_asset_sources)
def get_asset_sources_output(asset_source_id: Optional[pulumi.Input[Optional[str]]] = None,
                             compartment_id: Optional[pulumi.Input[str]] = None,
                             display_name: Optional[pulumi.Input[Optional[str]]] = None,
                             filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAssetSourcesFilterArgs']]]]] = None,
                             state: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssetSourcesResult]:
    """
    This data source provides the list of Asset Sources in Oracle Cloud Infrastructure Cloud Bridge service.

    Returns a list of asset sources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_asset_sources = oci.CloudBridge.get_asset_sources(compartment_id=compartment_id,
        asset_source_id=test_asset_source["id"],
        display_name=asset_source_display_name,
        state=asset_source_state)
    ```


    :param str asset_source_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the asset source.
    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: The current state of the asset source.
    """
    ...
