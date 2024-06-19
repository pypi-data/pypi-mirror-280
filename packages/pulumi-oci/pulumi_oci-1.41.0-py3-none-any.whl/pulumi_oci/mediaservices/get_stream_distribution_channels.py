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
    'GetStreamDistributionChannelsResult',
    'AwaitableGetStreamDistributionChannelsResult',
    'get_stream_distribution_channels',
    'get_stream_distribution_channels_output',
]

@pulumi.output_type
class GetStreamDistributionChannelsResult:
    """
    A collection of values returned by getStreamDistributionChannels.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, state=None, stream_distribution_channel_collections=None):
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
        if stream_distribution_channel_collections and not isinstance(stream_distribution_channel_collections, list):
            raise TypeError("Expected argument 'stream_distribution_channel_collections' to be a list")
        pulumi.set(__self__, "stream_distribution_channel_collections", stream_distribution_channel_collections)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The compartment ID of the lock.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Stream Distribution Channel display name. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetStreamDistributionChannelsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Stream Distribution Channel.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="streamDistributionChannelCollections")
    def stream_distribution_channel_collections(self) -> Sequence['outputs.GetStreamDistributionChannelsStreamDistributionChannelCollectionResult']:
        """
        The list of stream_distribution_channel_collection.
        """
        return pulumi.get(self, "stream_distribution_channel_collections")


class AwaitableGetStreamDistributionChannelsResult(GetStreamDistributionChannelsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamDistributionChannelsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state,
            stream_distribution_channel_collections=self.stream_distribution_channel_collections)


def get_stream_distribution_channels(compartment_id: Optional[str] = None,
                                     display_name: Optional[str] = None,
                                     filters: Optional[Sequence[pulumi.InputType['GetStreamDistributionChannelsFilterArgs']]] = None,
                                     id: Optional[str] = None,
                                     state: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamDistributionChannelsResult:
    """
    This data source provides the list of Stream Distribution Channels in Oracle Cloud Infrastructure Media Services service.

    Lists the Stream Distribution Channels.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_stream_distribution_channels = oci.MediaServices.get_stream_distribution_channels(compartment_id=compartment_id,
        display_name=stream_distribution_channel_display_name,
        id=stream_distribution_channel_id,
        state=stream_distribution_channel_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only the resources that match the entire display name given.
    :param str id: Unique Stream Distribution Channel identifier.
    :param str state: A filter to return only the resources with lifecycleState matching the given lifecycleState.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:MediaServices/getStreamDistributionChannels:getStreamDistributionChannels', __args__, opts=opts, typ=GetStreamDistributionChannelsResult).value

    return AwaitableGetStreamDistributionChannelsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'),
        stream_distribution_channel_collections=pulumi.get(__ret__, 'stream_distribution_channel_collections'))


@_utilities.lift_output_func(get_stream_distribution_channels)
def get_stream_distribution_channels_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetStreamDistributionChannelsFilterArgs']]]]] = None,
                                            id: Optional[pulumi.Input[Optional[str]]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStreamDistributionChannelsResult]:
    """
    This data source provides the list of Stream Distribution Channels in Oracle Cloud Infrastructure Media Services service.

    Lists the Stream Distribution Channels.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_stream_distribution_channels = oci.MediaServices.get_stream_distribution_channels(compartment_id=compartment_id,
        display_name=stream_distribution_channel_display_name,
        id=stream_distribution_channel_id,
        state=stream_distribution_channel_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only the resources that match the entire display name given.
    :param str id: Unique Stream Distribution Channel identifier.
    :param str state: A filter to return only the resources with lifecycleState matching the given lifecycleState.
    """
    ...
