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

__all__ = [
    'GetProfileResult',
    'AwaitableGetProfileResult',
    'get_profile',
    'get_profile_output',
]

@pulumi.output_type
class GetProfileResult:
    """
    A collection of values returned by getProfile.
    """
    def __init__(__self__, arch_type=None, compartment_id=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, is_default_profile=None, is_service_provided_profile=None, lifecycle_environments=None, lifecycle_stage_id=None, lifecycle_stages=None, managed_instance_group_id=None, managed_instance_groups=None, management_station_id=None, os_family=None, profile_id=None, profile_type=None, registration_type=None, software_source_ids=None, software_sources=None, state=None, system_tags=None, time_created=None, vendor_name=None):
        if arch_type and not isinstance(arch_type, str):
            raise TypeError("Expected argument 'arch_type' to be a str")
        pulumi.set(__self__, "arch_type", arch_type)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_default_profile and not isinstance(is_default_profile, bool):
            raise TypeError("Expected argument 'is_default_profile' to be a bool")
        pulumi.set(__self__, "is_default_profile", is_default_profile)
        if is_service_provided_profile and not isinstance(is_service_provided_profile, bool):
            raise TypeError("Expected argument 'is_service_provided_profile' to be a bool")
        pulumi.set(__self__, "is_service_provided_profile", is_service_provided_profile)
        if lifecycle_environments and not isinstance(lifecycle_environments, list):
            raise TypeError("Expected argument 'lifecycle_environments' to be a list")
        pulumi.set(__self__, "lifecycle_environments", lifecycle_environments)
        if lifecycle_stage_id and not isinstance(lifecycle_stage_id, str):
            raise TypeError("Expected argument 'lifecycle_stage_id' to be a str")
        pulumi.set(__self__, "lifecycle_stage_id", lifecycle_stage_id)
        if lifecycle_stages and not isinstance(lifecycle_stages, list):
            raise TypeError("Expected argument 'lifecycle_stages' to be a list")
        pulumi.set(__self__, "lifecycle_stages", lifecycle_stages)
        if managed_instance_group_id and not isinstance(managed_instance_group_id, str):
            raise TypeError("Expected argument 'managed_instance_group_id' to be a str")
        pulumi.set(__self__, "managed_instance_group_id", managed_instance_group_id)
        if managed_instance_groups and not isinstance(managed_instance_groups, list):
            raise TypeError("Expected argument 'managed_instance_groups' to be a list")
        pulumi.set(__self__, "managed_instance_groups", managed_instance_groups)
        if management_station_id and not isinstance(management_station_id, str):
            raise TypeError("Expected argument 'management_station_id' to be a str")
        pulumi.set(__self__, "management_station_id", management_station_id)
        if os_family and not isinstance(os_family, str):
            raise TypeError("Expected argument 'os_family' to be a str")
        pulumi.set(__self__, "os_family", os_family)
        if profile_id and not isinstance(profile_id, str):
            raise TypeError("Expected argument 'profile_id' to be a str")
        pulumi.set(__self__, "profile_id", profile_id)
        if profile_type and not isinstance(profile_type, str):
            raise TypeError("Expected argument 'profile_type' to be a str")
        pulumi.set(__self__, "profile_type", profile_type)
        if registration_type and not isinstance(registration_type, str):
            raise TypeError("Expected argument 'registration_type' to be a str")
        pulumi.set(__self__, "registration_type", registration_type)
        if software_source_ids and not isinstance(software_source_ids, list):
            raise TypeError("Expected argument 'software_source_ids' to be a list")
        pulumi.set(__self__, "software_source_ids", software_source_ids)
        if software_sources and not isinstance(software_sources, list):
            raise TypeError("Expected argument 'software_sources' to be a list")
        pulumi.set(__self__, "software_sources", software_sources)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if vendor_name and not isinstance(vendor_name, str):
            raise TypeError("Expected argument 'vendor_name' to be a str")
        pulumi.set(__self__, "vendor_name", vendor_name)

    @property
    @pulumi.getter(name="archType")
    def arch_type(self) -> str:
        """
        The architecture type.
        """
        return pulumi.get(self, "arch_type")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the registration profile.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Software source description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Software source name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDefaultProfile")
    def is_default_profile(self) -> bool:
        """
        Indicates if the profile is set as the default. There is exactly one default profile for a specified architecture, OS family, registration type, and vendor. When registering an instance with the corresonding characteristics, the default profile is used, unless another profile is specified.
        """
        return pulumi.get(self, "is_default_profile")

    @property
    @pulumi.getter(name="isServiceProvidedProfile")
    def is_service_provided_profile(self) -> bool:
        """
        Indicates if the profile was created by the service. OS Management Hub provides a limited set of standardized profiles that can be used to register Autonomous Linux or Windows instances.
        """
        return pulumi.get(self, "is_service_provided_profile")

    @property
    @pulumi.getter(name="lifecycleEnvironments")
    def lifecycle_environments(self) -> Sequence['outputs.GetProfileLifecycleEnvironmentResult']:
        """
        Provides identifying information for the specified lifecycle environment.
        """
        return pulumi.get(self, "lifecycle_environments")

    @property
    @pulumi.getter(name="lifecycleStageId")
    def lifecycle_stage_id(self) -> str:
        return pulumi.get(self, "lifecycle_stage_id")

    @property
    @pulumi.getter(name="lifecycleStages")
    def lifecycle_stages(self) -> Sequence['outputs.GetProfileLifecycleStageResult']:
        """
        Provides identifying information for the specified lifecycle stage.
        """
        return pulumi.get(self, "lifecycle_stages")

    @property
    @pulumi.getter(name="managedInstanceGroupId")
    def managed_instance_group_id(self) -> str:
        return pulumi.get(self, "managed_instance_group_id")

    @property
    @pulumi.getter(name="managedInstanceGroups")
    def managed_instance_groups(self) -> Sequence['outputs.GetProfileManagedInstanceGroupResult']:
        """
        Provides identifying information for the specified managed instance group.
        """
        return pulumi.get(self, "managed_instance_groups")

    @property
    @pulumi.getter(name="managementStationId")
    def management_station_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station to associate with an instance once registered. Associating with a management station applies only to non-OCI instances.
        """
        return pulumi.get(self, "management_station_id")

    @property
    @pulumi.getter(name="osFamily")
    def os_family(self) -> str:
        """
        The operating system family.
        """
        return pulumi.get(self, "os_family")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> str:
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> str:
        """
        The type of profile.
        """
        return pulumi.get(self, "profile_type")

    @property
    @pulumi.getter(name="registrationType")
    def registration_type(self) -> str:
        """
        The type of instance to register.
        """
        return pulumi.get(self, "registration_type")

    @property
    @pulumi.getter(name="softwareSourceIds")
    def software_source_ids(self) -> Sequence[str]:
        return pulumi.get(self, "software_source_ids")

    @property
    @pulumi.getter(name="softwareSources")
    def software_sources(self) -> Sequence['outputs.GetProfileSoftwareSourceResult']:
        """
        The list of software sources that the registration profile will use.
        """
        return pulumi.get(self, "software_sources")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the registration profile.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the registration profile was created (in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) format).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> str:
        """
        The vendor of the operating system for the instance.
        """
        return pulumi.get(self, "vendor_name")


class AwaitableGetProfileResult(GetProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfileResult(
            arch_type=self.arch_type,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_default_profile=self.is_default_profile,
            is_service_provided_profile=self.is_service_provided_profile,
            lifecycle_environments=self.lifecycle_environments,
            lifecycle_stage_id=self.lifecycle_stage_id,
            lifecycle_stages=self.lifecycle_stages,
            managed_instance_group_id=self.managed_instance_group_id,
            managed_instance_groups=self.managed_instance_groups,
            management_station_id=self.management_station_id,
            os_family=self.os_family,
            profile_id=self.profile_id,
            profile_type=self.profile_type,
            registration_type=self.registration_type,
            software_source_ids=self.software_source_ids,
            software_sources=self.software_sources,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            vendor_name=self.vendor_name)


def get_profile(profile_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfileResult:
    """
    This data source provides details about a specific Profile resource in Oracle Cloud Infrastructure Os Management Hub service.

    Gets information about the specified registration profile.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_profile = oci.OsManagementHub.get_profile(profile_id=test_profile_oci_os_management_hub_profile["id"])
    ```


    :param str profile_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile.
    """
    __args__ = dict()
    __args__['profileId'] = profile_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagementHub/getProfile:getProfile', __args__, opts=opts, typ=GetProfileResult).value

    return AwaitableGetProfileResult(
        arch_type=pulumi.get(__ret__, 'arch_type'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_default_profile=pulumi.get(__ret__, 'is_default_profile'),
        is_service_provided_profile=pulumi.get(__ret__, 'is_service_provided_profile'),
        lifecycle_environments=pulumi.get(__ret__, 'lifecycle_environments'),
        lifecycle_stage_id=pulumi.get(__ret__, 'lifecycle_stage_id'),
        lifecycle_stages=pulumi.get(__ret__, 'lifecycle_stages'),
        managed_instance_group_id=pulumi.get(__ret__, 'managed_instance_group_id'),
        managed_instance_groups=pulumi.get(__ret__, 'managed_instance_groups'),
        management_station_id=pulumi.get(__ret__, 'management_station_id'),
        os_family=pulumi.get(__ret__, 'os_family'),
        profile_id=pulumi.get(__ret__, 'profile_id'),
        profile_type=pulumi.get(__ret__, 'profile_type'),
        registration_type=pulumi.get(__ret__, 'registration_type'),
        software_source_ids=pulumi.get(__ret__, 'software_source_ids'),
        software_sources=pulumi.get(__ret__, 'software_sources'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        vendor_name=pulumi.get(__ret__, 'vendor_name'))


@_utilities.lift_output_func(get_profile)
def get_profile_output(profile_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProfileResult]:
    """
    This data source provides details about a specific Profile resource in Oracle Cloud Infrastructure Os Management Hub service.

    Gets information about the specified registration profile.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_profile = oci.OsManagementHub.get_profile(profile_id=test_profile_oci_os_management_hub_profile["id"])
    ```


    :param str profile_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile.
    """
    ...
