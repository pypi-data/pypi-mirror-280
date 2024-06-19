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
    'GetAnalyticsInstancePrivateAccessChannelResult',
    'AwaitableGetAnalyticsInstancePrivateAccessChannelResult',
    'get_analytics_instance_private_access_channel',
    'get_analytics_instance_private_access_channel_output',
]

@pulumi.output_type
class GetAnalyticsInstancePrivateAccessChannelResult:
    """
    A collection of values returned by getAnalyticsInstancePrivateAccessChannel.
    """
    def __init__(__self__, analytics_instance_id=None, display_name=None, egress_source_ip_addresses=None, id=None, ip_address=None, key=None, network_security_group_ids=None, private_access_channel_key=None, private_source_dns_zones=None, private_source_scan_hosts=None, subnet_id=None, vcn_id=None):
        if analytics_instance_id and not isinstance(analytics_instance_id, str):
            raise TypeError("Expected argument 'analytics_instance_id' to be a str")
        pulumi.set(__self__, "analytics_instance_id", analytics_instance_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if egress_source_ip_addresses and not isinstance(egress_source_ip_addresses, list):
            raise TypeError("Expected argument 'egress_source_ip_addresses' to be a list")
        pulumi.set(__self__, "egress_source_ip_addresses", egress_source_ip_addresses)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if network_security_group_ids and not isinstance(network_security_group_ids, list):
            raise TypeError("Expected argument 'network_security_group_ids' to be a list")
        pulumi.set(__self__, "network_security_group_ids", network_security_group_ids)
        if private_access_channel_key and not isinstance(private_access_channel_key, str):
            raise TypeError("Expected argument 'private_access_channel_key' to be a str")
        pulumi.set(__self__, "private_access_channel_key", private_access_channel_key)
        if private_source_dns_zones and not isinstance(private_source_dns_zones, list):
            raise TypeError("Expected argument 'private_source_dns_zones' to be a list")
        pulumi.set(__self__, "private_source_dns_zones", private_source_dns_zones)
        if private_source_scan_hosts and not isinstance(private_source_scan_hosts, list):
            raise TypeError("Expected argument 'private_source_scan_hosts' to be a list")
        pulumi.set(__self__, "private_source_scan_hosts", private_source_scan_hosts)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)

    @property
    @pulumi.getter(name="analyticsInstanceId")
    def analytics_instance_id(self) -> str:
        return pulumi.get(self, "analytics_instance_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display Name of the Private Access Channel.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="egressSourceIpAddresses")
    def egress_source_ip_addresses(self) -> Sequence[str]:
        """
        The list of IP addresses from the customer subnet connected to private access channel, used as a source Ip by Private Access Channel for network traffic from the AnalyticsInstance to Private Sources.
        """
        return pulumi.get(self, "egress_source_ip_addresses")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        IP Address of the Private Access channel.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Private Access Channel unique identifier key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="networkSecurityGroupIds")
    def network_security_group_ids(self) -> Sequence[str]:
        """
        Network Security Group OCIDs for an Analytics instance.
        """
        return pulumi.get(self, "network_security_group_ids")

    @property
    @pulumi.getter(name="privateAccessChannelKey")
    def private_access_channel_key(self) -> str:
        return pulumi.get(self, "private_access_channel_key")

    @property
    @pulumi.getter(name="privateSourceDnsZones")
    def private_source_dns_zones(self) -> Sequence['outputs.GetAnalyticsInstancePrivateAccessChannelPrivateSourceDnsZoneResult']:
        """
        List of Private Source DNS zones registered with Private Access Channel, where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance. Min of 1 is required and Max of 30 Private Source DNS zones can be registered.
        """
        return pulumi.get(self, "private_source_dns_zones")

    @property
    @pulumi.getter(name="privateSourceScanHosts")
    def private_source_scan_hosts(self) -> Sequence['outputs.GetAnalyticsInstancePrivateAccessChannelPrivateSourceScanHostResult']:
        """
        List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.
        """
        return pulumi.get(self, "private_source_scan_hosts")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        OCID of the customer subnet connected to private access channel.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> str:
        """
        OCID of the customer VCN peered with private access channel.
        """
        return pulumi.get(self, "vcn_id")


class AwaitableGetAnalyticsInstancePrivateAccessChannelResult(GetAnalyticsInstancePrivateAccessChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnalyticsInstancePrivateAccessChannelResult(
            analytics_instance_id=self.analytics_instance_id,
            display_name=self.display_name,
            egress_source_ip_addresses=self.egress_source_ip_addresses,
            id=self.id,
            ip_address=self.ip_address,
            key=self.key,
            network_security_group_ids=self.network_security_group_ids,
            private_access_channel_key=self.private_access_channel_key,
            private_source_dns_zones=self.private_source_dns_zones,
            private_source_scan_hosts=self.private_source_scan_hosts,
            subnet_id=self.subnet_id,
            vcn_id=self.vcn_id)


def get_analytics_instance_private_access_channel(analytics_instance_id: Optional[str] = None,
                                                  private_access_channel_key: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnalyticsInstancePrivateAccessChannelResult:
    """
    This data source provides details about a specific Analytics Instance Private Access Channel resource in Oracle Cloud Infrastructure Analytics service.

    Retrieve private access channel in the specified Analytics Instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_analytics_instance_private_access_channel = oci.Analytics.get_analytics_instance_private_access_channel(analytics_instance_id=test_analytics_instance["id"],
        private_access_channel_key=analytics_instance_private_access_channel_private_access_channel_key)
    ```


    :param str analytics_instance_id: The OCID of the AnalyticsInstance.
    :param str private_access_channel_key: The unique identifier key of the Private Access Channel.
    """
    __args__ = dict()
    __args__['analyticsInstanceId'] = analytics_instance_id
    __args__['privateAccessChannelKey'] = private_access_channel_key
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Analytics/getAnalyticsInstancePrivateAccessChannel:getAnalyticsInstancePrivateAccessChannel', __args__, opts=opts, typ=GetAnalyticsInstancePrivateAccessChannelResult).value

    return AwaitableGetAnalyticsInstancePrivateAccessChannelResult(
        analytics_instance_id=pulumi.get(__ret__, 'analytics_instance_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        egress_source_ip_addresses=pulumi.get(__ret__, 'egress_source_ip_addresses'),
        id=pulumi.get(__ret__, 'id'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        key=pulumi.get(__ret__, 'key'),
        network_security_group_ids=pulumi.get(__ret__, 'network_security_group_ids'),
        private_access_channel_key=pulumi.get(__ret__, 'private_access_channel_key'),
        private_source_dns_zones=pulumi.get(__ret__, 'private_source_dns_zones'),
        private_source_scan_hosts=pulumi.get(__ret__, 'private_source_scan_hosts'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'))


@_utilities.lift_output_func(get_analytics_instance_private_access_channel)
def get_analytics_instance_private_access_channel_output(analytics_instance_id: Optional[pulumi.Input[str]] = None,
                                                         private_access_channel_key: Optional[pulumi.Input[str]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAnalyticsInstancePrivateAccessChannelResult]:
    """
    This data source provides details about a specific Analytics Instance Private Access Channel resource in Oracle Cloud Infrastructure Analytics service.

    Retrieve private access channel in the specified Analytics Instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_analytics_instance_private_access_channel = oci.Analytics.get_analytics_instance_private_access_channel(analytics_instance_id=test_analytics_instance["id"],
        private_access_channel_key=analytics_instance_private_access_channel_private_access_channel_key)
    ```


    :param str analytics_instance_id: The OCID of the AnalyticsInstance.
    :param str private_access_channel_key: The unique identifier key of the Private Access Channel.
    """
    ...
