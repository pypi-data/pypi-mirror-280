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

__all__ = ['NamedCredentialArgs', 'NamedCredential']

@pulumi.input_type
class NamedCredentialArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 content: pulumi.Input['NamedCredentialContentArgs'],
                 scope: pulumi.Input[str],
                 type: pulumi.Input[str],
                 associated_resource: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamedCredential resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        :param pulumi.Input['NamedCredentialContentArgs'] content: (Updatable) The details of the named credential.
        :param pulumi.Input[str] scope: (Updatable) The scope of the named credential.
        :param pulumi.Input[str] type: The type of resource associated with the named credential.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] associated_resource: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) The information specified by the user about the named credential.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] name: The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "type", type)
        if associated_resource is not None:
            pulumi.set(__self__, "associated_resource", associated_resource)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input['NamedCredentialContentArgs']:
        """
        (Updatable) The details of the named credential.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input['NamedCredentialContentArgs']):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        (Updatable) The scope of the named credential.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of resource associated with the named credential.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="associatedResource")
    def associated_resource(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        """
        return pulumi.get(self, "associated_resource")

    @associated_resource.setter
    def associated_resource(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associated_resource", value)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The information specified by the user about the named credential.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NamedCredentialState:
    def __init__(__self__, *,
                 associated_resource: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input['NamedCredentialContentArgs']] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NamedCredential resources.
        :param pulumi.Input[str] associated_resource: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        :param pulumi.Input['NamedCredentialContentArgs'] content: (Updatable) The details of the named credential.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) The information specified by the user about the named credential.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] lifecycle_details: The details of the lifecycle state.
        :param pulumi.Input[str] name: The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        :param pulumi.Input[str] scope: (Updatable) The scope of the named credential.
        :param pulumi.Input[str] state: The current lifecycle state of the named credential.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the named credential was created.
        :param pulumi.Input[str] time_updated: The date and time the named credential was last updated.
        :param pulumi.Input[str] type: The type of resource associated with the named credential.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if associated_resource is not None:
            pulumi.set(__self__, "associated_resource", associated_resource)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="associatedResource")
    def associated_resource(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        """
        return pulumi.get(self, "associated_resource")

    @associated_resource.setter
    def associated_resource(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associated_resource", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input['NamedCredentialContentArgs']]:
        """
        (Updatable) The details of the named credential.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input['NamedCredentialContentArgs']]):
        pulumi.set(self, "content", value)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The information specified by the user about the named credential.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        The details of the lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The scope of the named credential.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current lifecycle state of the named credential.
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
        The date and time the named credential was created.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the named credential was last updated.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of resource associated with the named credential.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class NamedCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_resource: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['NamedCredentialContentArgs']]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Named Credential resource in Oracle Cloud Infrastructure Database Management service.

        Creates a named credential.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_named_credential = oci.database_management.NamedCredential("test_named_credential",
            compartment_id=compartment_id,
            content=oci.database_management.NamedCredentialContentArgs(
                credential_type=named_credential_content_credential_type,
                password_secret_access_mode=named_credential_content_password_secret_access_mode,
                password_secret_id=test_secret["id"],
                role=named_credential_content_role,
                user_name=test_user["name"],
            ),
            name=named_credential_name,
            scope=named_credential_scope,
            type=named_credential_type,
            associated_resource=named_credential_associated_resource,
            defined_tags={
                "Operations.CostCenter": "42",
            },
            description=named_credential_description,
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        NamedCredentials can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DatabaseManagement/namedCredential:NamedCredential test_named_credential "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] associated_resource: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        :param pulumi.Input[pulumi.InputType['NamedCredentialContentArgs']] content: (Updatable) The details of the named credential.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) The information specified by the user about the named credential.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] name: The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        :param pulumi.Input[str] scope: (Updatable) The scope of the named credential.
        :param pulumi.Input[str] type: The type of resource associated with the named credential.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamedCredentialArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Named Credential resource in Oracle Cloud Infrastructure Database Management service.

        Creates a named credential.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_named_credential = oci.database_management.NamedCredential("test_named_credential",
            compartment_id=compartment_id,
            content=oci.database_management.NamedCredentialContentArgs(
                credential_type=named_credential_content_credential_type,
                password_secret_access_mode=named_credential_content_password_secret_access_mode,
                password_secret_id=test_secret["id"],
                role=named_credential_content_role,
                user_name=test_user["name"],
            ),
            name=named_credential_name,
            scope=named_credential_scope,
            type=named_credential_type,
            associated_resource=named_credential_associated_resource,
            defined_tags={
                "Operations.CostCenter": "42",
            },
            description=named_credential_description,
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        NamedCredentials can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DatabaseManagement/namedCredential:NamedCredential test_named_credential "id"
        ```

        :param str resource_name: The name of the resource.
        :param NamedCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamedCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_resource: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['NamedCredentialContentArgs']]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamedCredentialArgs.__new__(NamedCredentialArgs)

            __props__.__dict__["associated_resource"] = associated_resource
            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["name"] = name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(NamedCredential, __self__).__init__(
            'oci:DatabaseManagement/namedCredential:NamedCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            associated_resource: Optional[pulumi.Input[str]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[pulumi.InputType['NamedCredentialContentArgs']]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'NamedCredential':
        """
        Get an existing NamedCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] associated_resource: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        :param pulumi.Input[pulumi.InputType['NamedCredentialContentArgs']] content: (Updatable) The details of the named credential.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) The information specified by the user about the named credential.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] lifecycle_details: The details of the lifecycle state.
        :param pulumi.Input[str] name: The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        :param pulumi.Input[str] scope: (Updatable) The scope of the named credential.
        :param pulumi.Input[str] state: The current lifecycle state of the named credential.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the named credential was created.
        :param pulumi.Input[str] time_updated: The date and time the named credential was last updated.
        :param pulumi.Input[str] type: The type of resource associated with the named credential.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamedCredentialState.__new__(_NamedCredentialState)

        __props__.__dict__["associated_resource"] = associated_resource
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["content"] = content
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["name"] = name
        __props__.__dict__["scope"] = scope
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        __props__.__dict__["type"] = type
        return NamedCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedResource")
    def associated_resource(self) -> pulumi.Output[Optional[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        """
        return pulumi.get(self, "associated_resource")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the named credential resides.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output['outputs.NamedCredentialContent']:
        """
        (Updatable) The details of the named credential.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) The information specified by the user about the named credential.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        The details of the lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the named credential. Valid characters are uppercase or lowercase letters, numbers, and "_". The name of the named credential cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        (Updatable) The scope of the named credential.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of the named credential.
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
        The date and time the named credential was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The date and time the named credential was last updated.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of resource associated with the named credential.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "type")

