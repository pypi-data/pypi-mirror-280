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

__all__ = ['ModelArgs', 'Model']

@pulumi.input_type
class ModelArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 model_training_details: pulumi.Input['ModelModelTrainingDetailsArgs'],
                 project_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Model resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID for the ai model's compartment.
        :param pulumi.Input['ModelModelTrainingDetailsArgs'] model_training_details: Specifies the details of the MSET model during the create call.
        :param pulumi.Input[str] project_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A short description of the ai model.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "model_training_details", model_training_details)
        pulumi.set(__self__, "project_id", project_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The OCID for the ai model's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="modelTrainingDetails")
    def model_training_details(self) -> pulumi.Input['ModelModelTrainingDetailsArgs']:
        """
        Specifies the details of the MSET model during the create call.
        """
        return pulumi.get(self, "model_training_details")

    @model_training_details.setter
    def model_training_details(self, value: pulumi.Input['ModelModelTrainingDetailsArgs']):
        pulumi.set(self, "model_training_details", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A short description of the ai model.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
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


@pulumi.input_type
class _ModelState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 model_training_details: Optional[pulumi.Input['ModelModelTrainingDetailsArgs']] = None,
                 model_training_results: Optional[pulumi.Input[Sequence[pulumi.Input['ModelModelTrainingResultArgs']]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Model resources.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID for the ai model's compartment.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A short description of the ai model.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input['ModelModelTrainingDetailsArgs'] model_training_details: Specifies the details of the MSET model during the create call.
        :param pulumi.Input[Sequence[pulumi.Input['ModelModelTrainingResultArgs']]] model_training_results: Specifies the details for an Anomaly Detection model trained with MSET.
        :param pulumi.Input[str] project_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The state of the model.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the the Model was created. An RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the Model was updated. An RFC3339 formatted datetime string.
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if model_training_details is not None:
            pulumi.set(__self__, "model_training_details", model_training_details)
        if model_training_results is not None:
            pulumi.set(__self__, "model_training_results", model_training_results)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The OCID for the ai model's compartment.
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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A short description of the ai model.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
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
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="modelTrainingDetails")
    def model_training_details(self) -> Optional[pulumi.Input['ModelModelTrainingDetailsArgs']]:
        """
        Specifies the details of the MSET model during the create call.
        """
        return pulumi.get(self, "model_training_details")

    @model_training_details.setter
    def model_training_details(self, value: Optional[pulumi.Input['ModelModelTrainingDetailsArgs']]):
        pulumi.set(self, "model_training_details", value)

    @property
    @pulumi.getter(name="modelTrainingResults")
    def model_training_results(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelModelTrainingResultArgs']]]]:
        """
        Specifies the details for an Anomaly Detection model trained with MSET.
        """
        return pulumi.get(self, "model_training_results")

    @model_training_results.setter
    def model_training_results(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelModelTrainingResultArgs']]]]):
        pulumi.set(self, "model_training_results", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the model.
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
        The time the the Model was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the Model was updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class Model(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 model_training_details: Optional[pulumi.Input[pulumi.InputType['ModelModelTrainingDetailsArgs']]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Model resource in Oracle Cloud Infrastructure Ai Anomaly Detection service.

        Creates a new Model.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_model = oci.ai_anomaly_detection.Model("test_model",
            compartment_id=compartment_id,
            model_training_details=oci.ai_anomaly_detection.ModelModelTrainingDetailsArgs(
                data_asset_ids=model_model_training_details_data_asset_ids,
                algorithm_hint=model_model_training_details_algorithm_hint,
                target_fap=model_model_training_details_target_fap,
                training_fraction=model_model_training_details_training_fraction,
                window_size=model_model_training_details_window_size,
            ),
            project_id=test_project["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=model_description,
            display_name=model_display_name,
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        Models can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:AiAnomalyDetection/model:Model test_model "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID for the ai model's compartment.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A short description of the ai model.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[pulumi.InputType['ModelModelTrainingDetailsArgs']] model_training_details: Specifies the details of the MSET model during the create call.
        :param pulumi.Input[str] project_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Model resource in Oracle Cloud Infrastructure Ai Anomaly Detection service.

        Creates a new Model.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_model = oci.ai_anomaly_detection.Model("test_model",
            compartment_id=compartment_id,
            model_training_details=oci.ai_anomaly_detection.ModelModelTrainingDetailsArgs(
                data_asset_ids=model_model_training_details_data_asset_ids,
                algorithm_hint=model_model_training_details_algorithm_hint,
                target_fap=model_model_training_details_target_fap,
                training_fraction=model_model_training_details_training_fraction,
                window_size=model_model_training_details_window_size,
            ),
            project_id=test_project["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=model_description,
            display_name=model_display_name,
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        Models can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:AiAnomalyDetection/model:Model test_model "id"
        ```

        :param str resource_name: The name of the resource.
        :param ModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 model_training_details: Optional[pulumi.Input[pulumi.InputType['ModelModelTrainingDetailsArgs']]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModelArgs.__new__(ModelArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            if model_training_details is None and not opts.urn:
                raise TypeError("Missing required property 'model_training_details'")
            __props__.__dict__["model_training_details"] = model_training_details
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["model_training_results"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(Model, __self__).__init__(
            'oci:AiAnomalyDetection/model:Model',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            model_training_details: Optional[pulumi.Input[pulumi.InputType['ModelModelTrainingDetailsArgs']]] = None,
            model_training_results: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelModelTrainingResultArgs']]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'Model':
        """
        Get an existing Model resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID for the ai model's compartment.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A short description of the ai model.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[pulumi.InputType['ModelModelTrainingDetailsArgs']] model_training_details: Specifies the details of the MSET model during the create call.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelModelTrainingResultArgs']]]] model_training_results: Specifies the details for an Anomaly Detection model trained with MSET.
        :param pulumi.Input[str] project_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The state of the model.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the the Model was created. An RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the Model was updated. An RFC3339 formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ModelState.__new__(_ModelState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["model_training_details"] = model_training_details
        __props__.__dict__["model_training_results"] = model_training_results
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return Model(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The OCID for the ai model's compartment.
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
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) A short description of the ai model.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
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
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="modelTrainingDetails")
    def model_training_details(self) -> pulumi.Output['outputs.ModelModelTrainingDetails']:
        """
        Specifies the details of the MSET model during the create call.
        """
        return pulumi.get(self, "model_training_details")

    @property
    @pulumi.getter(name="modelTrainingResults")
    def model_training_results(self) -> pulumi.Output[Sequence['outputs.ModelModelTrainingResult']]:
        """
        Specifies the details for an Anomaly Detection model trained with MSET.
        """
        return pulumi.get(self, "model_training_results")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the model.
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
        The time the the Model was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the Model was updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

