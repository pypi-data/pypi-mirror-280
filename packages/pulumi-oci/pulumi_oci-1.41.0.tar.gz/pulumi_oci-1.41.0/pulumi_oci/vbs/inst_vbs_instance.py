# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstVbsInstanceArgs', 'InstVbsInstance']

@pulumi.input_type
class InstVbsInstanceArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 idcs_access_token: Optional[pulumi.Input[str]] = None,
                 is_resource_usage_agreement_granted: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_compartment_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstVbsInstance resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier. It can only be the root compartment
        :param pulumi.Input[str] display_name: (Updatable) Display Name
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] idcs_access_token: IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        :param pulumi.Input[bool] is_resource_usage_agreement_granted: (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        :param pulumi.Input[str] name: Service Instance Name
        :param pulumi.Input[str] resource_compartment_id: (Updatable) Compartment where VBS may create additional resources for the service instance
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "display_name", display_name)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if idcs_access_token is not None:
            pulumi.set(__self__, "idcs_access_token", idcs_access_token)
        if is_resource_usage_agreement_granted is not None:
            pulumi.set(__self__, "is_resource_usage_agreement_granted", is_resource_usage_agreement_granted)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_compartment_id is not None:
            pulumi.set(__self__, "resource_compartment_id", resource_compartment_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) Compartment Identifier. It can only be the root compartment
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        (Updatable) Display Name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="idcsAccessToken")
    def idcs_access_token(self) -> Optional[pulumi.Input[str]]:
        """
        IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        """
        return pulumi.get(self, "idcs_access_token")

    @idcs_access_token.setter
    def idcs_access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idcs_access_token", value)

    @property
    @pulumi.getter(name="isResourceUsageAgreementGranted")
    def is_resource_usage_agreement_granted(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        """
        return pulumi.get(self, "is_resource_usage_agreement_granted")

    @is_resource_usage_agreement_granted.setter
    def is_resource_usage_agreement_granted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_resource_usage_agreement_granted", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Service Instance Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceCompartmentId")
    def resource_compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment where VBS may create additional resources for the service instance


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "resource_compartment_id")

    @resource_compartment_id.setter
    def resource_compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_compartment_id", value)


@pulumi.input_type
class _InstVbsInstanceState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 idcs_access_token: Optional[pulumi.Input[str]] = None,
                 is_resource_usage_agreement_granted: Optional[pulumi.Input[bool]] = None,
                 lifecyle_details: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_compartment_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None,
                 vbs_access_url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstVbsInstance resources.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier. It can only be the root compartment
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display Name
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] idcs_access_token: IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        :param pulumi.Input[bool] is_resource_usage_agreement_granted: (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        :param pulumi.Input[str] lifecyle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] name: Service Instance Name
        :param pulumi.Input[str] resource_compartment_id: (Updatable) Compartment where VBS may create additional resources for the service instance
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of the VbsInstance.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the the VbsInstance was created. An RFC3339 formatted datetime string
        :param pulumi.Input[str] time_updated: The time the VbsInstance was updated. An RFC3339 formatted datetime string
        :param pulumi.Input[str] vbs_access_url: Public web URL for accessing the VBS service instance
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if idcs_access_token is not None:
            pulumi.set(__self__, "idcs_access_token", idcs_access_token)
        if is_resource_usage_agreement_granted is not None:
            pulumi.set(__self__, "is_resource_usage_agreement_granted", is_resource_usage_agreement_granted)
        if lifecyle_details is not None:
            pulumi.set(__self__, "lifecyle_details", lifecyle_details)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_compartment_id is not None:
            pulumi.set(__self__, "resource_compartment_id", resource_compartment_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)
        if vbs_access_url is not None:
            pulumi.set(__self__, "vbs_access_url", vbs_access_url)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment Identifier. It can only be the root compartment
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Display Name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="idcsAccessToken")
    def idcs_access_token(self) -> Optional[pulumi.Input[str]]:
        """
        IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        """
        return pulumi.get(self, "idcs_access_token")

    @idcs_access_token.setter
    def idcs_access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idcs_access_token", value)

    @property
    @pulumi.getter(name="isResourceUsageAgreementGranted")
    def is_resource_usage_agreement_granted(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        """
        return pulumi.get(self, "is_resource_usage_agreement_granted")

    @is_resource_usage_agreement_granted.setter
    def is_resource_usage_agreement_granted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_resource_usage_agreement_granted", value)

    @property
    @pulumi.getter(name="lifecyleDetails")
    def lifecyle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecyle_details")

    @lifecyle_details.setter
    def lifecyle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecyle_details", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Service Instance Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceCompartmentId")
    def resource_compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment where VBS may create additional resources for the service instance


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "resource_compartment_id")

    @resource_compartment_id.setter
    def resource_compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_compartment_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the VbsInstance.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the the VbsInstance was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the VbsInstance was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)

    @property
    @pulumi.getter(name="vbsAccessUrl")
    def vbs_access_url(self) -> Optional[pulumi.Input[str]]:
        """
        Public web URL for accessing the VBS service instance
        """
        return pulumi.get(self, "vbs_access_url")

    @vbs_access_url.setter
    def vbs_access_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vbs_access_url", value)


class InstVbsInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 idcs_access_token: Optional[pulumi.Input[str]] = None,
                 is_resource_usage_agreement_granted: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_compartment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Vbs Instance resource in Oracle Cloud Infrastructure Vbs Inst service.

        Creates a new VbsInstance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_vbs_instance = oci.vbs.InstVbsInstance("test_vbs_instance",
            compartment_id=compartment_id,
            display_name=vbs_instance_display_name,
            name=vbs_instance_name,
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            freeform_tags={
                "bar-key": "value",
            },
            idcs_access_token=vbs_instance_idcs_access_token,
            is_resource_usage_agreement_granted=vbs_instance_is_resource_usage_agreement_granted,
            resource_compartment_id=resource_compartment_id)
        ```

        ## Import

        VbsInstances can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Vbs/instVbsInstance:InstVbsInstance test_vbs_instance "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier. It can only be the root compartment
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display Name
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] idcs_access_token: IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        :param pulumi.Input[bool] is_resource_usage_agreement_granted: (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        :param pulumi.Input[str] name: Service Instance Name
        :param pulumi.Input[str] resource_compartment_id: (Updatable) Compartment where VBS may create additional resources for the service instance
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstVbsInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Vbs Instance resource in Oracle Cloud Infrastructure Vbs Inst service.

        Creates a new VbsInstance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_vbs_instance = oci.vbs.InstVbsInstance("test_vbs_instance",
            compartment_id=compartment_id,
            display_name=vbs_instance_display_name,
            name=vbs_instance_name,
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            freeform_tags={
                "bar-key": "value",
            },
            idcs_access_token=vbs_instance_idcs_access_token,
            is_resource_usage_agreement_granted=vbs_instance_is_resource_usage_agreement_granted,
            resource_compartment_id=resource_compartment_id)
        ```

        ## Import

        VbsInstances can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Vbs/instVbsInstance:InstVbsInstance test_vbs_instance "id"
        ```

        :param str resource_name: The name of the resource.
        :param InstVbsInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstVbsInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 idcs_access_token: Optional[pulumi.Input[str]] = None,
                 is_resource_usage_agreement_granted: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_compartment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstVbsInstanceArgs.__new__(InstVbsInstanceArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["idcs_access_token"] = idcs_access_token
            __props__.__dict__["is_resource_usage_agreement_granted"] = is_resource_usage_agreement_granted
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_compartment_id"] = resource_compartment_id
            __props__.__dict__["lifecyle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
            __props__.__dict__["vbs_access_url"] = None
        super(InstVbsInstance, __self__).__init__(
            'oci:Vbs/instVbsInstance:InstVbsInstance',
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
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            idcs_access_token: Optional[pulumi.Input[str]] = None,
            is_resource_usage_agreement_granted: Optional[pulumi.Input[bool]] = None,
            lifecyle_details: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_compartment_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None,
            vbs_access_url: Optional[pulumi.Input[str]] = None) -> 'InstVbsInstance':
        """
        Get an existing InstVbsInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier. It can only be the root compartment
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display Name
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] idcs_access_token: IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        :param pulumi.Input[bool] is_resource_usage_agreement_granted: (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        :param pulumi.Input[str] lifecyle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] name: Service Instance Name
        :param pulumi.Input[str] resource_compartment_id: (Updatable) Compartment where VBS may create additional resources for the service instance
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of the VbsInstance.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the the VbsInstance was created. An RFC3339 formatted datetime string
        :param pulumi.Input[str] time_updated: The time the VbsInstance was updated. An RFC3339 formatted datetime string
        :param pulumi.Input[str] vbs_access_url: Public web URL for accessing the VBS service instance
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstVbsInstanceState.__new__(_InstVbsInstanceState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["idcs_access_token"] = idcs_access_token
        __props__.__dict__["is_resource_usage_agreement_granted"] = is_resource_usage_agreement_granted
        __props__.__dict__["lifecyle_details"] = lifecyle_details
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_compartment_id"] = resource_compartment_id
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        __props__.__dict__["vbs_access_url"] = vbs_access_url
        return InstVbsInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment Identifier. It can only be the root compartment
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Display Name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="idcsAccessToken")
    def idcs_access_token(self) -> pulumi.Output[str]:
        """
        IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        """
        return pulumi.get(self, "idcs_access_token")

    @property
    @pulumi.getter(name="isResourceUsageAgreementGranted")
    def is_resource_usage_agreement_granted(self) -> pulumi.Output[bool]:
        """
        (Updatable) Whether VBS is authorized to create and use resources in the customer tenancy
        """
        return pulumi.get(self, "is_resource_usage_agreement_granted")

    @property
    @pulumi.getter(name="lifecyleDetails")
    def lifecyle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecyle_details")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Service Instance Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceCompartmentId")
    def resource_compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment where VBS may create additional resources for the service instance


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "resource_compartment_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the VbsInstance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the the VbsInstance was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the VbsInstance was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="vbsAccessUrl")
    def vbs_access_url(self) -> pulumi.Output[str]:
        """
        Public web URL for accessing the VBS service instance
        """
        return pulumi.get(self, "vbs_access_url")

