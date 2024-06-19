# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NatGatewayArgs', 'NatGateway']

@pulumi.input_type
class NatGatewayArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 vcn_id: pulumi.Input[str],
                 block_traffic: Optional[pulumi.Input[bool]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 public_ip_id: Optional[pulumi.Input[str]] = None,
                 route_table_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NatGateway resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        :param pulumi.Input[str] vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[bool] block_traffic: (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] public_ip_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        :param pulumi.Input[str] route_table_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.
               
               If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "vcn_id", vcn_id)
        if block_traffic is not None:
            pulumi.set(__self__, "block_traffic", block_traffic)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if public_ip_id is not None:
            pulumi.set(__self__, "public_ip_id", public_ip_id)
        if route_table_id is not None:
            pulumi.set(__self__, "route_table_id", route_table_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "vcn_id")

    @vcn_id.setter
    def vcn_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vcn_id", value)

    @property
    @pulumi.getter(name="blockTraffic")
    def block_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        """
        return pulumi.get(self, "block_traffic")

    @block_traffic.setter
    def block_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "block_traffic", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        """
        return pulumi.get(self, "public_ip_id")

    @public_ip_id.setter
    def public_ip_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_id", value)

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.

        If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        """
        return pulumi.get(self, "route_table_id")

    @route_table_id.setter
    def route_table_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_table_id", value)


@pulumi.input_type
class _NatGatewayState:
    def __init__(__self__, *,
                 block_traffic: Optional[pulumi.Input[bool]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 nat_ip: Optional[pulumi.Input[str]] = None,
                 public_ip_id: Optional[pulumi.Input[str]] = None,
                 route_table_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 vcn_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NatGateway resources.
        :param pulumi.Input[bool] block_traffic: (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] nat_ip: The IP address associated with the NAT gateway.
        :param pulumi.Input[str] public_ip_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        :param pulumi.Input[str] route_table_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.
               
               If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        :param pulumi.Input[str] state: The NAT gateway's current state.
        :param pulumi.Input[str] time_created: The date and time the NAT gateway was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        :param pulumi.Input[str] vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if block_traffic is not None:
            pulumi.set(__self__, "block_traffic", block_traffic)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if nat_ip is not None:
            pulumi.set(__self__, "nat_ip", nat_ip)
        if public_ip_id is not None:
            pulumi.set(__self__, "public_ip_id", public_ip_id)
        if route_table_id is not None:
            pulumi.set(__self__, "route_table_id", route_table_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if vcn_id is not None:
            pulumi.set(__self__, "vcn_id", vcn_id)

    @property
    @pulumi.getter(name="blockTraffic")
    def block_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        """
        return pulumi.get(self, "block_traffic")

    @block_traffic.setter
    def block_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "block_traffic", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="natIp")
    def nat_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address associated with the NAT gateway.
        """
        return pulumi.get(self, "nat_ip")

    @nat_ip.setter
    def nat_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nat_ip", value)

    @property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        """
        return pulumi.get(self, "public_ip_id")

    @public_ip_id.setter
    def public_ip_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_id", value)

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.

        If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        """
        return pulumi.get(self, "route_table_id")

    @route_table_id.setter
    def route_table_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_table_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The NAT gateway's current state.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the NAT gateway was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "vcn_id")

    @vcn_id.setter
    def vcn_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vcn_id", value)


class NatGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_traffic: Optional[pulumi.Input[bool]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 public_ip_id: Optional[pulumi.Input[str]] = None,
                 route_table_id: Optional[pulumi.Input[str]] = None,
                 vcn_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Nat Gateway resource in Oracle Cloud Infrastructure Core service.

        Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the
        NAT gateway as the rule's target. See [Route Table](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_nat_gateway = oci.core.NatGateway("test_nat_gateway",
            compartment_id=compartment_id,
            vcn_id=test_vcn["id"],
            block_traffic=nat_gateway_block_traffic,
            defined_tags={
                "Operations.CostCenter": "42",
            },
            display_name=nat_gateway_display_name,
            freeform_tags={
                "Department": "Finance",
            },
            public_ip_id=test_public_ip["id"],
            route_table_id=test_route_table["id"])
        ```

        ## Import

        NatGateways can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Core/natGateway:NatGateway test_nat_gateway "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] block_traffic: (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] public_ip_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        :param pulumi.Input[str] route_table_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.
               
               If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        :param pulumi.Input[str] vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NatGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Nat Gateway resource in Oracle Cloud Infrastructure Core service.

        Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the
        NAT gateway as the rule's target. See [Route Table](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_nat_gateway = oci.core.NatGateway("test_nat_gateway",
            compartment_id=compartment_id,
            vcn_id=test_vcn["id"],
            block_traffic=nat_gateway_block_traffic,
            defined_tags={
                "Operations.CostCenter": "42",
            },
            display_name=nat_gateway_display_name,
            freeform_tags={
                "Department": "Finance",
            },
            public_ip_id=test_public_ip["id"],
            route_table_id=test_route_table["id"])
        ```

        ## Import

        NatGateways can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Core/natGateway:NatGateway test_nat_gateway "id"
        ```

        :param str resource_name: The name of the resource.
        :param NatGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NatGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_traffic: Optional[pulumi.Input[bool]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 public_ip_id: Optional[pulumi.Input[str]] = None,
                 route_table_id: Optional[pulumi.Input[str]] = None,
                 vcn_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NatGatewayArgs.__new__(NatGatewayArgs)

            __props__.__dict__["block_traffic"] = block_traffic
            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["public_ip_id"] = public_ip_id
            __props__.__dict__["route_table_id"] = route_table_id
            if vcn_id is None and not opts.urn:
                raise TypeError("Missing required property 'vcn_id'")
            __props__.__dict__["vcn_id"] = vcn_id
            __props__.__dict__["nat_ip"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(NatGateway, __self__).__init__(
            'oci:Core/natGateway:NatGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            block_traffic: Optional[pulumi.Input[bool]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            nat_ip: Optional[pulumi.Input[str]] = None,
            public_ip_id: Optional[pulumi.Input[str]] = None,
            route_table_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            vcn_id: Optional[pulumi.Input[str]] = None) -> 'NatGateway':
        """
        Get an existing NatGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] block_traffic: (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] nat_ip: The IP address associated with the NAT gateway.
        :param pulumi.Input[str] public_ip_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        :param pulumi.Input[str] route_table_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.
               
               If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        :param pulumi.Input[str] state: The NAT gateway's current state.
        :param pulumi.Input[str] time_created: The date and time the NAT gateway was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        :param pulumi.Input[str] vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NatGatewayState.__new__(_NatGatewayState)

        __props__.__dict__["block_traffic"] = block_traffic
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["nat_ip"] = nat_ip
        __props__.__dict__["public_ip_id"] = public_ip_id
        __props__.__dict__["route_table_id"] = route_table_id
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["vcn_id"] = vcn_id
        return NatGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blockTraffic")
    def block_traffic(self) -> pulumi.Output[bool]:
        """
        (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`
        """
        return pulumi.get(self, "block_traffic")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="natIp")
    def nat_ip(self) -> pulumi.Output[str]:
        """
        The IP address associated with the NAT gateway.
        """
        return pulumi.get(self, "nat_ip")

    @property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
        """
        return pulumi.get(self, "public_ip_id")

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.

        If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.
        """
        return pulumi.get(self, "route_table_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The NAT gateway's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the NAT gateway was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "vcn_id")

