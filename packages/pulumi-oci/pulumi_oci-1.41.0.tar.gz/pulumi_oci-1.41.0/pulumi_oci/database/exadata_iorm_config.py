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

__all__ = ['ExadataIormConfigArgs', 'ExadataIormConfig']

@pulumi.input_type
class ExadataIormConfigArgs:
    def __init__(__self__, *,
                 db_plans: pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]],
                 db_system_id: pulumi.Input[str],
                 objective: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExadataIormConfig resource.
        :param pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]] db_plans: (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        :param pulumi.Input[str] db_system_id: (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] objective: (Updatable) Value for the IORM objective Default is "Auto" 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "db_plans", db_plans)
        pulumi.set(__self__, "db_system_id", db_system_id)
        if objective is not None:
            pulumi.set(__self__, "objective", objective)

    @property
    @pulumi.getter(name="dbPlans")
    def db_plans(self) -> pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]]:
        """
        (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        """
        return pulumi.get(self, "db_plans")

    @db_plans.setter
    def db_plans(self, value: pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]]):
        pulumi.set(self, "db_plans", value)

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "db_system_id")

    @db_system_id.setter
    def db_system_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_system_id", value)

    @property
    @pulumi.getter
    def objective(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Value for the IORM objective Default is "Auto" 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "objective")

    @objective.setter
    def objective(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "objective", value)


@pulumi.input_type
class _ExadataIormConfigState:
    def __init__(__self__, *,
                 db_plans: Optional[pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]]] = None,
                 db_system_id: Optional[pulumi.Input[str]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 objective: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExadataIormConfig resources.
        :param pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]] db_plans: (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        :param pulumi.Input[str] db_system_id: (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] lifecycle_details: Additional information about the current `lifecycleState`.
        :param pulumi.Input[str] objective: (Updatable) Value for the IORM objective Default is "Auto" 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of IORM configuration for the Exadata DB system.
        """
        if db_plans is not None:
            pulumi.set(__self__, "db_plans", db_plans)
        if db_system_id is not None:
            pulumi.set(__self__, "db_system_id", db_system_id)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if objective is not None:
            pulumi.set(__self__, "objective", objective)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="dbPlans")
    def db_plans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]]]:
        """
        (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        """
        return pulumi.get(self, "db_plans")

    @db_plans.setter
    def db_plans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExadataIormConfigDbPlanArgs']]]]):
        pulumi.set(self, "db_plans", value)

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "db_system_id")

    @db_system_id.setter
    def db_system_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_system_id", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        Additional information about the current `lifecycleState`.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def objective(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Value for the IORM objective Default is "Auto" 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "objective")

    @objective.setter
    def objective(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "objective", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of IORM configuration for the Exadata DB system.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class ExadataIormConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_plans: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExadataIormConfigDbPlanArgs']]]]] = None,
                 db_system_id: Optional[pulumi.Input[str]] = None,
                 objective: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Exadata Iorm Config resource in Oracle Cloud Infrastructure Database service.

        Updates IORM settings for the specified Exadata DB system.

        **Note:** Deprecated for Exadata Cloud Service systems. Use the [new resource model APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model) instead.

        For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See [Switching an Exadata DB System to the New Resource Model and APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm) for details on converting existing Exadata DB systems to the new resource model.

        The [UpdateCloudVmClusterIormConfig](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudVmCluster/UpdateCloudVmClusterIormConfig/) API is used for Exadata systems using the
        new resource model.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_exadata_iorm_config = oci.database.ExadataIormConfig("test_exadata_iorm_config",
            db_plans=[oci.database.ExadataIormConfigDbPlanArgs(
                db_name=exadata_iorm_config_db_plans_db_name,
                share=exadata_iorm_config_db_plans_share,
            )],
            db_system_id=test_db_system["id"],
            objective="AUTO")
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExadataIormConfigDbPlanArgs']]]] db_plans: (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        :param pulumi.Input[str] db_system_id: (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] objective: (Updatable) Value for the IORM objective Default is "Auto" 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExadataIormConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Exadata Iorm Config resource in Oracle Cloud Infrastructure Database service.

        Updates IORM settings for the specified Exadata DB system.

        **Note:** Deprecated for Exadata Cloud Service systems. Use the [new resource model APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model) instead.

        For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See [Switching an Exadata DB System to the New Resource Model and APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm) for details on converting existing Exadata DB systems to the new resource model.

        The [UpdateCloudVmClusterIormConfig](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudVmCluster/UpdateCloudVmClusterIormConfig/) API is used for Exadata systems using the
        new resource model.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_exadata_iorm_config = oci.database.ExadataIormConfig("test_exadata_iorm_config",
            db_plans=[oci.database.ExadataIormConfigDbPlanArgs(
                db_name=exadata_iorm_config_db_plans_db_name,
                share=exadata_iorm_config_db_plans_share,
            )],
            db_system_id=test_db_system["id"],
            objective="AUTO")
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param ExadataIormConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExadataIormConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_plans: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExadataIormConfigDbPlanArgs']]]]] = None,
                 db_system_id: Optional[pulumi.Input[str]] = None,
                 objective: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExadataIormConfigArgs.__new__(ExadataIormConfigArgs)

            if db_plans is None and not opts.urn:
                raise TypeError("Missing required property 'db_plans'")
            __props__.__dict__["db_plans"] = db_plans
            if db_system_id is None and not opts.urn:
                raise TypeError("Missing required property 'db_system_id'")
            __props__.__dict__["db_system_id"] = db_system_id
            __props__.__dict__["objective"] = objective
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
        super(ExadataIormConfig, __self__).__init__(
            'oci:Database/exadataIormConfig:ExadataIormConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            db_plans: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExadataIormConfigDbPlanArgs']]]]] = None,
            db_system_id: Optional[pulumi.Input[str]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            objective: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'ExadataIormConfig':
        """
        Get an existing ExadataIormConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExadataIormConfigDbPlanArgs']]]] db_plans: (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        :param pulumi.Input[str] db_system_id: (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] lifecycle_details: Additional information about the current `lifecycleState`.
        :param pulumi.Input[str] objective: (Updatable) Value for the IORM objective Default is "Auto" 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of IORM configuration for the Exadata DB system.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExadataIormConfigState.__new__(_ExadataIormConfigState)

        __props__.__dict__["db_plans"] = db_plans
        __props__.__dict__["db_system_id"] = db_system_id
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["objective"] = objective
        __props__.__dict__["state"] = state
        return ExadataIormConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbPlans")
    def db_plans(self) -> pulumi.Output[Sequence['outputs.ExadataIormConfigDbPlan']]:
        """
        (Updatable) Array of IORM Setting for all the database in this Exadata DB System
        """
        return pulumi.get(self, "db_plans")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        Additional information about the current `lifecycleState`.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def objective(self) -> pulumi.Output[str]:
        """
        (Updatable) Value for the IORM objective Default is "Auto" 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "objective")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of IORM configuration for the Exadata DB system.
        """
        return pulumi.get(self, "state")

