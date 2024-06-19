# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AutonomousContainerDatabaseDataguardRoleChangeArgs', 'AutonomousContainerDatabaseDataguardRoleChange']

@pulumi.input_type
class AutonomousContainerDatabaseDataguardRoleChangeArgs:
    def __init__(__self__, *,
                 autonomous_container_database_dataguard_association_id: pulumi.Input[str],
                 autonomous_container_database_id: pulumi.Input[str],
                 role: pulumi.Input[str],
                 connection_strings_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutonomousContainerDatabaseDataguardRoleChange resource.
        """
        pulumi.set(__self__, "autonomous_container_database_dataguard_association_id", autonomous_container_database_dataguard_association_id)
        pulumi.set(__self__, "autonomous_container_database_id", autonomous_container_database_id)
        pulumi.set(__self__, "role", role)
        if connection_strings_type is not None:
            pulumi.set(__self__, "connection_strings_type", connection_strings_type)

    @property
    @pulumi.getter(name="autonomousContainerDatabaseDataguardAssociationId")
    def autonomous_container_database_dataguard_association_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "autonomous_container_database_dataguard_association_id")

    @autonomous_container_database_dataguard_association_id.setter
    def autonomous_container_database_dataguard_association_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "autonomous_container_database_dataguard_association_id", value)

    @property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "autonomous_container_database_id")

    @autonomous_container_database_id.setter
    def autonomous_container_database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "autonomous_container_database_id", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="connectionStringsType")
    def connection_strings_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "connection_strings_type")

    @connection_strings_type.setter
    def connection_strings_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_strings_type", value)


@pulumi.input_type
class _AutonomousContainerDatabaseDataguardRoleChangeState:
    def __init__(__self__, *,
                 autonomous_container_database_dataguard_association_id: Optional[pulumi.Input[str]] = None,
                 autonomous_container_database_id: Optional[pulumi.Input[str]] = None,
                 connection_strings_type: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AutonomousContainerDatabaseDataguardRoleChange resources.
        """
        if autonomous_container_database_dataguard_association_id is not None:
            pulumi.set(__self__, "autonomous_container_database_dataguard_association_id", autonomous_container_database_dataguard_association_id)
        if autonomous_container_database_id is not None:
            pulumi.set(__self__, "autonomous_container_database_id", autonomous_container_database_id)
        if connection_strings_type is not None:
            pulumi.set(__self__, "connection_strings_type", connection_strings_type)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter(name="autonomousContainerDatabaseDataguardAssociationId")
    def autonomous_container_database_dataguard_association_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "autonomous_container_database_dataguard_association_id")

    @autonomous_container_database_dataguard_association_id.setter
    def autonomous_container_database_dataguard_association_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "autonomous_container_database_dataguard_association_id", value)

    @property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "autonomous_container_database_id")

    @autonomous_container_database_id.setter
    def autonomous_container_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "autonomous_container_database_id", value)

    @property
    @pulumi.getter(name="connectionStringsType")
    def connection_strings_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "connection_strings_type")

    @connection_strings_type.setter
    def connection_strings_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_strings_type", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


class AutonomousContainerDatabaseDataguardRoleChange(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autonomous_container_database_dataguard_association_id: Optional[pulumi.Input[str]] = None,
                 autonomous_container_database_id: Optional[pulumi.Input[str]] = None,
                 connection_strings_type: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AutonomousContainerDatabaseDataguardRoleChange resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutonomousContainerDatabaseDataguardRoleChangeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AutonomousContainerDatabaseDataguardRoleChange resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AutonomousContainerDatabaseDataguardRoleChangeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutonomousContainerDatabaseDataguardRoleChangeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autonomous_container_database_dataguard_association_id: Optional[pulumi.Input[str]] = None,
                 autonomous_container_database_id: Optional[pulumi.Input[str]] = None,
                 connection_strings_type: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AutonomousContainerDatabaseDataguardRoleChangeArgs.__new__(AutonomousContainerDatabaseDataguardRoleChangeArgs)

            if autonomous_container_database_dataguard_association_id is None and not opts.urn:
                raise TypeError("Missing required property 'autonomous_container_database_dataguard_association_id'")
            __props__.__dict__["autonomous_container_database_dataguard_association_id"] = autonomous_container_database_dataguard_association_id
            if autonomous_container_database_id is None and not opts.urn:
                raise TypeError("Missing required property 'autonomous_container_database_id'")
            __props__.__dict__["autonomous_container_database_id"] = autonomous_container_database_id
            __props__.__dict__["connection_strings_type"] = connection_strings_type
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
        super(AutonomousContainerDatabaseDataguardRoleChange, __self__).__init__(
            'oci:Database/autonomousContainerDatabaseDataguardRoleChange:AutonomousContainerDatabaseDataguardRoleChange',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            autonomous_container_database_dataguard_association_id: Optional[pulumi.Input[str]] = None,
            autonomous_container_database_id: Optional[pulumi.Input[str]] = None,
            connection_strings_type: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'AutonomousContainerDatabaseDataguardRoleChange':
        """
        Get an existing AutonomousContainerDatabaseDataguardRoleChange resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AutonomousContainerDatabaseDataguardRoleChangeState.__new__(_AutonomousContainerDatabaseDataguardRoleChangeState)

        __props__.__dict__["autonomous_container_database_dataguard_association_id"] = autonomous_container_database_dataguard_association_id
        __props__.__dict__["autonomous_container_database_id"] = autonomous_container_database_id
        __props__.__dict__["connection_strings_type"] = connection_strings_type
        __props__.__dict__["role"] = role
        return AutonomousContainerDatabaseDataguardRoleChange(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autonomousContainerDatabaseDataguardAssociationId")
    def autonomous_container_database_dataguard_association_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "autonomous_container_database_dataguard_association_id")

    @property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "autonomous_container_database_id")

    @property
    @pulumi.getter(name="connectionStringsType")
    def connection_strings_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "connection_strings_type")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role")

