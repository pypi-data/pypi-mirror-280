# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SetSecurityAssessmentBaselineArgs', 'SetSecurityAssessmentBaseline']

@pulumi.input_type
class SetSecurityAssessmentBaselineArgs:
    def __init__(__self__, *,
                 security_assessment_id: pulumi.Input[str],
                 assessment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SetSecurityAssessmentBaseline resource.
        :param pulumi.Input[str] security_assessment_id: The OCID of the security assessment.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assessment_ids: The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        """
        pulumi.set(__self__, "security_assessment_id", security_assessment_id)
        if assessment_ids is not None:
            pulumi.set(__self__, "assessment_ids", assessment_ids)

    @property
    @pulumi.getter(name="securityAssessmentId")
    def security_assessment_id(self) -> pulumi.Input[str]:
        """
        The OCID of the security assessment.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "security_assessment_id")

    @security_assessment_id.setter
    def security_assessment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_assessment_id", value)

    @property
    @pulumi.getter(name="assessmentIds")
    def assessment_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        """
        return pulumi.get(self, "assessment_ids")

    @assessment_ids.setter
    def assessment_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "assessment_ids", value)


@pulumi.input_type
class _SetSecurityAssessmentBaselineState:
    def __init__(__self__, *,
                 assessment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_assessment_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SetSecurityAssessmentBaseline resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assessment_ids: The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        :param pulumi.Input[str] security_assessment_id: The OCID of the security assessment.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if assessment_ids is not None:
            pulumi.set(__self__, "assessment_ids", assessment_ids)
        if security_assessment_id is not None:
            pulumi.set(__self__, "security_assessment_id", security_assessment_id)

    @property
    @pulumi.getter(name="assessmentIds")
    def assessment_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        """
        return pulumi.get(self, "assessment_ids")

    @assessment_ids.setter
    def assessment_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "assessment_ids", value)

    @property
    @pulumi.getter(name="securityAssessmentId")
    def security_assessment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the security assessment.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "security_assessment_id")

    @security_assessment_id.setter
    def security_assessment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_assessment_id", value)


class SetSecurityAssessmentBaseline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_assessment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Set Security Assessment Baseline resource in Oracle Cloud Infrastructure Data Safe service.

        Sets the saved security assessment as the baseline in the compartment where the the specified assessment resides. The security assessment needs to be of type 'SAVED'.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_set_security_assessment_baseline = oci.data_safe.SetSecurityAssessmentBaseline("test_set_security_assessment_baseline",
            security_assessment_id=test_security_assessment["id"],
            assessment_ids=set_security_assessment_baseline_assessment_ids)
        ```

        ## Import

        SetSecurityAssessmentBaseline can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DataSafe/setSecurityAssessmentBaseline:SetSecurityAssessmentBaseline test_set_security_assessment_baseline "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assessment_ids: The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        :param pulumi.Input[str] security_assessment_id: The OCID of the security assessment.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SetSecurityAssessmentBaselineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Set Security Assessment Baseline resource in Oracle Cloud Infrastructure Data Safe service.

        Sets the saved security assessment as the baseline in the compartment where the the specified assessment resides. The security assessment needs to be of type 'SAVED'.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_set_security_assessment_baseline = oci.data_safe.SetSecurityAssessmentBaseline("test_set_security_assessment_baseline",
            security_assessment_id=test_security_assessment["id"],
            assessment_ids=set_security_assessment_baseline_assessment_ids)
        ```

        ## Import

        SetSecurityAssessmentBaseline can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DataSafe/setSecurityAssessmentBaseline:SetSecurityAssessmentBaseline test_set_security_assessment_baseline "id"
        ```

        :param str resource_name: The name of the resource.
        :param SetSecurityAssessmentBaselineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SetSecurityAssessmentBaselineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_assessment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SetSecurityAssessmentBaselineArgs.__new__(SetSecurityAssessmentBaselineArgs)

            __props__.__dict__["assessment_ids"] = assessment_ids
            if security_assessment_id is None and not opts.urn:
                raise TypeError("Missing required property 'security_assessment_id'")
            __props__.__dict__["security_assessment_id"] = security_assessment_id
        super(SetSecurityAssessmentBaseline, __self__).__init__(
            'oci:DataSafe/setSecurityAssessmentBaseline:SetSecurityAssessmentBaseline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            assessment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            security_assessment_id: Optional[pulumi.Input[str]] = None) -> 'SetSecurityAssessmentBaseline':
        """
        Get an existing SetSecurityAssessmentBaseline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assessment_ids: The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        :param pulumi.Input[str] security_assessment_id: The OCID of the security assessment.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SetSecurityAssessmentBaselineState.__new__(_SetSecurityAssessmentBaselineState)

        __props__.__dict__["assessment_ids"] = assessment_ids
        __props__.__dict__["security_assessment_id"] = security_assessment_id
        return SetSecurityAssessmentBaseline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assessmentIds")
    def assessment_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of OCIDs for the security assessments that need to be updated while setting the baseline.
        """
        return pulumi.get(self, "assessment_ids")

    @property
    @pulumi.getter(name="securityAssessmentId")
    def security_assessment_id(self) -> pulumi.Output[str]:
        """
        The OCID of the security assessment.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "security_assessment_id")

