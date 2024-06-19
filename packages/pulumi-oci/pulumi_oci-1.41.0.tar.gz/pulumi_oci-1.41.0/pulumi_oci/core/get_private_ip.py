# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPrivateIpResult',
    'AwaitableGetPrivateIpResult',
    'get_private_ip',
    'get_private_ip_output',
]

@pulumi.output_type
class GetPrivateIpResult:
    """
    A collection of values returned by getPrivateIp.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, hostname_label=None, id=None, ip_address=None, is_primary=None, is_reserved=None, private_ip_id=None, subnet_id=None, time_created=None, vlan_id=None, vnic_id=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if hostname_label and not isinstance(hostname_label, str):
            raise TypeError("Expected argument 'hostname_label' to be a str")
        pulumi.set(__self__, "hostname_label", hostname_label)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if is_primary and not isinstance(is_primary, bool):
            raise TypeError("Expected argument 'is_primary' to be a bool")
        pulumi.set(__self__, "is_primary", is_primary)
        if is_reserved and not isinstance(is_reserved, bool):
            raise TypeError("Expected argument 'is_reserved' to be a bool")
        pulumi.set(__self__, "is_reserved", is_reserved)
        if private_ip_id and not isinstance(private_ip_id, str):
            raise TypeError("Expected argument 'private_ip_id' to be a str")
        pulumi.set(__self__, "private_ip_id", private_ip_id)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if vlan_id and not isinstance(vlan_id, str):
            raise TypeError("Expected argument 'vlan_id' to be a str")
        pulumi.set(__self__, "vlan_id", vlan_id)
        if vnic_id and not isinstance(vnic_id, str):
            raise TypeError("Expected argument 'vnic_id' to be a str")
        pulumi.set(__self__, "vnic_id", vnic_id)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The private IP's availability domain. This attribute will be null if this is a *secondary* private IP assigned to a VNIC that is in a *regional* subnet.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the private IP.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="hostnameLabel")
    def hostname_label(self) -> str:
        """
        The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123).
        """
        return pulumi.get(self, "hostname_label")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The private IP's Oracle ID ([OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The private IP address of the `privateIp` object. The address is within the CIDR of the VNIC's subnet.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> bool:
        """
        Whether this private IP is the primary one on the VNIC. Primary private IPs are unassigned and deleted automatically when the VNIC is terminated.  Example: `true`
        """
        return pulumi.get(self, "is_primary")

    @property
    @pulumi.getter(name="isReserved")
    def is_reserved(self) -> bool:
        """
        true if the IP is reserved and can exist detached from vnic
        """
        return pulumi.get(self, "is_reserved")

    @property
    @pulumi.getter(name="privateIpId")
    def private_ip_id(self) -> str:
        return pulumi.get(self, "private_ip_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the VNIC is in.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the private IP was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> str:
        """
        Applicable only if the `PrivateIp` object is being used with a VLAN as part of the Oracle Cloud VMware Solution. The `vlanId` is the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN. See [Vlan](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/Vlan).
        """
        return pulumi.get(self, "vlan_id")

    @property
    @pulumi.getter(name="vnicId")
    def vnic_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VNIC the private IP is assigned to. The VNIC and private IP must be in the same subnet. However, if the `PrivateIp` object is being used with a VLAN as part of the Oracle Cloud VMware Solution, the `vnicId` is null.
        """
        return pulumi.get(self, "vnic_id")


class AwaitableGetPrivateIpResult(GetPrivateIpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateIpResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            hostname_label=self.hostname_label,
            id=self.id,
            ip_address=self.ip_address,
            is_primary=self.is_primary,
            is_reserved=self.is_reserved,
            private_ip_id=self.private_ip_id,
            subnet_id=self.subnet_id,
            time_created=self.time_created,
            vlan_id=self.vlan_id,
            vnic_id=self.vnic_id)


def get_private_ip(private_ip_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateIpResult:
    """
    This data source provides details about a specific Private Ip resource in Oracle Cloud Infrastructure Core service.

    Gets the specified private IP. You must specify the object's [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    Alternatively, you can get the object by using
    [ListPrivateIps](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps)
    with the private IP address (for example, 10.0.3.3) and subnet [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_ip = oci.Core.get_private_ip(private_ip_id=test_private_ip_oci_core_private_ip["id"])
    ```


    :param str private_ip_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private IP or IPv6.
    """
    __args__ = dict()
    __args__['privateIpId'] = private_ip_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getPrivateIp:getPrivateIp', __args__, opts=opts, typ=GetPrivateIpResult).value

    return AwaitableGetPrivateIpResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        hostname_label=pulumi.get(__ret__, 'hostname_label'),
        id=pulumi.get(__ret__, 'id'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        is_primary=pulumi.get(__ret__, 'is_primary'),
        is_reserved=pulumi.get(__ret__, 'is_reserved'),
        private_ip_id=pulumi.get(__ret__, 'private_ip_id'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        vlan_id=pulumi.get(__ret__, 'vlan_id'),
        vnic_id=pulumi.get(__ret__, 'vnic_id'))


@_utilities.lift_output_func(get_private_ip)
def get_private_ip_output(private_ip_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateIpResult]:
    """
    This data source provides details about a specific Private Ip resource in Oracle Cloud Infrastructure Core service.

    Gets the specified private IP. You must specify the object's [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    Alternatively, you can get the object by using
    [ListPrivateIps](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps)
    with the private IP address (for example, 10.0.3.3) and subnet [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_ip = oci.Core.get_private_ip(private_ip_id=test_private_ip_oci_core_private_ip["id"])
    ```


    :param str private_ip_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private IP or IPv6.
    """
    ...
