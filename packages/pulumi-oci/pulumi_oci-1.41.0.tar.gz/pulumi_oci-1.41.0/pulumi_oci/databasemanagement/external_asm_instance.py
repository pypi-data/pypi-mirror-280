# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExternalAsmInstanceArgs', 'ExternalAsmInstance']

@pulumi.input_type
class ExternalAsmInstanceArgs:
    def __init__(__self__, *,
                 external_asm_instance_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a ExternalAsmInstance resource.
        :param pulumi.Input[str] external_asm_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "external_asm_instance_id", external_asm_instance_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="externalAsmInstanceId")
    def external_asm_instance_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        """
        return pulumi.get(self, "external_asm_instance_id")

    @external_asm_instance_id.setter
    def external_asm_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_asm_instance_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _ExternalAsmInstanceState:
    def __init__(__self__, *,
                 adr_home_directory: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 component_name: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 external_asm_id: Optional[pulumi.Input[str]] = None,
                 external_asm_instance_id: Optional[pulumi.Input[str]] = None,
                 external_db_node_id: Optional[pulumi.Input[str]] = None,
                 external_db_system_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExternalAsmInstance resources.
        :param pulumi.Input[str] adr_home_directory: The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        :param pulumi.Input[str] component_name: The name of the external ASM instance.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: The user-friendly name for the ASM instance. The name does not have to be unique.
        :param pulumi.Input[str] external_asm_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM that the ASM instance belongs to.
        :param pulumi.Input[str] external_asm_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        :param pulumi.Input[str] external_db_node_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node on which the ASM instance is running.
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM instance is a part of.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] host_name: The name of the host on which the ASM instance is running.
        :param pulumi.Input[str] lifecycle_details: Additional information about the current lifecycle state.
        :param pulumi.Input[str] state: The current lifecycle state of the external ASM instance.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the external ASM instance was created.
        :param pulumi.Input[str] time_updated: The date and time the external ASM instance was last updated.
        """
        if adr_home_directory is not None:
            pulumi.set(__self__, "adr_home_directory", adr_home_directory)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if component_name is not None:
            pulumi.set(__self__, "component_name", component_name)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if external_asm_id is not None:
            pulumi.set(__self__, "external_asm_id", external_asm_id)
        if external_asm_instance_id is not None:
            pulumi.set(__self__, "external_asm_instance_id", external_asm_instance_id)
        if external_db_node_id is not None:
            pulumi.set(__self__, "external_db_node_id", external_db_node_id)
        if external_db_system_id is not None:
            pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if host_name is not None:
            pulumi.set(__self__, "host_name", host_name)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="adrHomeDirectory")
    def adr_home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.
        """
        return pulumi.get(self, "adr_home_directory")

    @adr_home_directory.setter
    def adr_home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adr_home_directory", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the external ASM instance.
        """
        return pulumi.get(self, "component_name")

    @component_name.setter
    def component_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_name", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-friendly name for the ASM instance. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="externalAsmId")
    def external_asm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM that the ASM instance belongs to.
        """
        return pulumi.get(self, "external_asm_id")

    @external_asm_id.setter
    def external_asm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_asm_id", value)

    @property
    @pulumi.getter(name="externalAsmInstanceId")
    def external_asm_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        """
        return pulumi.get(self, "external_asm_instance_id")

    @external_asm_instance_id.setter
    def external_asm_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_asm_instance_id", value)

    @property
    @pulumi.getter(name="externalDbNodeId")
    def external_db_node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node on which the ASM instance is running.
        """
        return pulumi.get(self, "external_db_node_id")

    @external_db_node_id.setter
    def external_db_node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_db_node_id", value)

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM instance is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @external_db_system_id.setter
    def external_db_system_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_db_system_id", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the host on which the ASM instance is running.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current lifecycle state of the external ASM instance.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the external ASM instance was created.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the external ASM instance was last updated.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class ExternalAsmInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 external_asm_instance_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        This resource provides the External Asm Instance resource in Oracle Cloud Infrastructure Database Management service.

        Updates the external ASM instance specified by `externalAsmInstanceId`.

        ## Import

        ExternalAsmInstances can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DatabaseManagement/externalAsmInstance:ExternalAsmInstance test_external_asm_instance "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] external_asm_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExternalAsmInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the External Asm Instance resource in Oracle Cloud Infrastructure Database Management service.

        Updates the external ASM instance specified by `externalAsmInstanceId`.

        ## Import

        ExternalAsmInstances can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DatabaseManagement/externalAsmInstance:ExternalAsmInstance test_external_asm_instance "id"
        ```

        :param str resource_name: The name of the resource.
        :param ExternalAsmInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalAsmInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 external_asm_instance_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExternalAsmInstanceArgs.__new__(ExternalAsmInstanceArgs)

            __props__.__dict__["defined_tags"] = defined_tags
            if external_asm_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_asm_instance_id'")
            __props__.__dict__["external_asm_instance_id"] = external_asm_instance_id
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["adr_home_directory"] = None
            __props__.__dict__["compartment_id"] = None
            __props__.__dict__["component_name"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["external_asm_id"] = None
            __props__.__dict__["external_db_node_id"] = None
            __props__.__dict__["external_db_system_id"] = None
            __props__.__dict__["host_name"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(ExternalAsmInstance, __self__).__init__(
            'oci:DatabaseManagement/externalAsmInstance:ExternalAsmInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            adr_home_directory: Optional[pulumi.Input[str]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            component_name: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            external_asm_id: Optional[pulumi.Input[str]] = None,
            external_asm_instance_id: Optional[pulumi.Input[str]] = None,
            external_db_node_id: Optional[pulumi.Input[str]] = None,
            external_db_system_id: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            host_name: Optional[pulumi.Input[str]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'ExternalAsmInstance':
        """
        Get an existing ExternalAsmInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adr_home_directory: The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        :param pulumi.Input[str] component_name: The name of the external ASM instance.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: The user-friendly name for the ASM instance. The name does not have to be unique.
        :param pulumi.Input[str] external_asm_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM that the ASM instance belongs to.
        :param pulumi.Input[str] external_asm_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        :param pulumi.Input[str] external_db_node_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node on which the ASM instance is running.
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM instance is a part of.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] host_name: The name of the host on which the ASM instance is running.
        :param pulumi.Input[str] lifecycle_details: Additional information about the current lifecycle state.
        :param pulumi.Input[str] state: The current lifecycle state of the external ASM instance.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the external ASM instance was created.
        :param pulumi.Input[str] time_updated: The date and time the external ASM instance was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalAsmInstanceState.__new__(_ExternalAsmInstanceState)

        __props__.__dict__["adr_home_directory"] = adr_home_directory
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["component_name"] = component_name
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["external_asm_id"] = external_asm_id
        __props__.__dict__["external_asm_instance_id"] = external_asm_instance_id
        __props__.__dict__["external_db_node_id"] = external_db_node_id
        __props__.__dict__["external_db_system_id"] = external_db_system_id
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["host_name"] = host_name
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return ExternalAsmInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adrHomeDirectory")
    def adr_home_directory(self) -> pulumi.Output[str]:
        """
        The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.
        """
        return pulumi.get(self, "adr_home_directory")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Output[str]:
        """
        The name of the external ASM instance.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-friendly name for the ASM instance. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalAsmId")
    def external_asm_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM that the ASM instance belongs to.
        """
        return pulumi.get(self, "external_asm_id")

    @property
    @pulumi.getter(name="externalAsmInstanceId")
    def external_asm_instance_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM instance.
        """
        return pulumi.get(self, "external_asm_instance_id")

    @property
    @pulumi.getter(name="externalDbNodeId")
    def external_db_node_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node on which the ASM instance is running.
        """
        return pulumi.get(self, "external_db_node_id")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM instance is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The name of the host on which the ASM instance is running.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of the external ASM instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the external ASM instance was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The date and time the external ASM instance was last updated.
        """
        return pulumi.get(self, "time_updated")

