# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConfigurationArgs', 'Configuration']

@pulumi.input_type
class ConfigurationArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 retention_period_days: pulumi.Input[int]):
        """
        The set of arguments for constructing a Configuration resource.
        :param pulumi.Input[str] compartment_id: ID of the root compartment (tenancy)
        :param pulumi.Input[int] retention_period_days: (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "retention_period_days", retention_period_days)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        ID of the root compartment (tenancy)
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> pulumi.Input[int]:
        """
        (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "retention_period_days")

    @retention_period_days.setter
    def retention_period_days(self, value: pulumi.Input[int]):
        pulumi.set(self, "retention_period_days", value)


@pulumi.input_type
class _ConfigurationState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 retention_period_days: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Configuration resources.
        :param pulumi.Input[str] compartment_id: ID of the root compartment (tenancy)
        :param pulumi.Input[int] retention_period_days: (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if retention_period_days is not None:
            pulumi.set(__self__, "retention_period_days", retention_period_days)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the root compartment (tenancy)
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "retention_period_days")

    @retention_period_days.setter
    def retention_period_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_period_days", value)


class Configuration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 retention_period_days: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        This resource provides the Configuration resource in Oracle Cloud Infrastructure Audit service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_configuration = oci.audit.Configuration("test_configuration",
            compartment_id=tenancy_ocid,
            retention_period_days=configuration_retention_period_days)
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: ID of the root compartment (tenancy)
        :param pulumi.Input[int] retention_period_days: (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Configuration resource in Oracle Cloud Infrastructure Audit service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_configuration = oci.audit.Configuration("test_configuration",
            compartment_id=tenancy_ocid,
            retention_period_days=configuration_retention_period_days)
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param ConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 retention_period_days: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationArgs.__new__(ConfigurationArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            if retention_period_days is None and not opts.urn:
                raise TypeError("Missing required property 'retention_period_days'")
            __props__.__dict__["retention_period_days"] = retention_period_days
        super(Configuration, __self__).__init__(
            'oci:Audit/configuration:Configuration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            retention_period_days: Optional[pulumi.Input[int]] = None) -> 'Configuration':
        """
        Get an existing Configuration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: ID of the root compartment (tenancy)
        :param pulumi.Input[int] retention_period_days: (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigurationState.__new__(_ConfigurationState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["retention_period_days"] = retention_period_days
        return Configuration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        ID of the root compartment (tenancy)
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> pulumi.Output[int]:
        """
        (Updatable) The retention period setting, specified in days. The minimum is 90, the maximum 365.  Example: `90` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "retention_period_days")

