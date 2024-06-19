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

__all__ = ['DefaultDhcpOptionsArgs', 'DefaultDhcpOptions']

@pulumi.input_type
class DefaultDhcpOptionsArgs:
    def __init__(__self__, *,
                 manage_default_resource_id: pulumi.Input[str],
                 options: pulumi.Input[Sequence[pulumi.Input['DefaultDhcpOptionsOptionArgs']]],
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name_type: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a DefaultDhcpOptions resource.
        """
        pulumi.set(__self__, "manage_default_resource_id", manage_default_resource_id)
        pulumi.set(__self__, "options", options)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if domain_name_type is not None:
            pulumi.set(__self__, "domain_name_type", domain_name_type)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="manageDefaultResourceId")
    def manage_default_resource_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "manage_default_resource_id")

    @manage_default_resource_id.setter
    def manage_default_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "manage_default_resource_id", value)

    @property
    @pulumi.getter
    def options(self) -> pulumi.Input[Sequence[pulumi.Input['DefaultDhcpOptionsOptionArgs']]]:
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: pulumi.Input[Sequence[pulumi.Input['DefaultDhcpOptionsOptionArgs']]]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="domainNameType")
    def domain_name_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_name_type")

    @domain_name_type.setter
    def domain_name_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name_type", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _DefaultDhcpOptionsState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name_type: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 manage_default_resource_id: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input['DefaultDhcpOptionsOptionArgs']]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DefaultDhcpOptions resources.
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if domain_name_type is not None:
            pulumi.set(__self__, "domain_name_type", domain_name_type)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if manage_default_resource_id is not None:
            pulumi.set(__self__, "manage_default_resource_id", manage_default_resource_id)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="domainNameType")
    def domain_name_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_name_type")

    @domain_name_type.setter
    def domain_name_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name_type", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="manageDefaultResourceId")
    def manage_default_resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "manage_default_resource_id")

    @manage_default_resource_id.setter
    def manage_default_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "manage_default_resource_id", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DefaultDhcpOptionsOptionArgs']]]]:
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DefaultDhcpOptionsOptionArgs']]]]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


class DefaultDhcpOptions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name_type: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 manage_default_resource_id: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefaultDhcpOptionsOptionArgs']]]]] = None,
                 __props__=None):
        """
        Create a DefaultDhcpOptions resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefaultDhcpOptionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DefaultDhcpOptions resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DefaultDhcpOptionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefaultDhcpOptionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name_type: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 manage_default_resource_id: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefaultDhcpOptionsOptionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefaultDhcpOptionsArgs.__new__(DefaultDhcpOptionsArgs)

            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["domain_name_type"] = domain_name_type
            __props__.__dict__["freeform_tags"] = freeform_tags
            if manage_default_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'manage_default_resource_id'")
            __props__.__dict__["manage_default_resource_id"] = manage_default_resource_id
            if options is None and not opts.urn:
                raise TypeError("Missing required property 'options'")
            __props__.__dict__["options"] = options
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(DefaultDhcpOptions, __self__).__init__(
            'oci:Core/defaultDhcpOptions:DefaultDhcpOptions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            domain_name_type: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            manage_default_resource_id: Optional[pulumi.Input[str]] = None,
            options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefaultDhcpOptionsOptionArgs']]]]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None) -> 'DefaultDhcpOptions':
        """
        Get an existing DefaultDhcpOptions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DefaultDhcpOptionsState.__new__(_DefaultDhcpOptionsState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["domain_name_type"] = domain_name_type
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["manage_default_resource_id"] = manage_default_resource_id
        __props__.__dict__["options"] = options
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        return DefaultDhcpOptions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainNameType")
    def domain_name_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_name_type")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="manageDefaultResourceId")
    def manage_default_resource_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "manage_default_resource_id")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Sequence['outputs.DefaultDhcpOptionsOption']]:
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        return pulumi.get(self, "time_created")

