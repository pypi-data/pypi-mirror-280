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
    'GetFusionEnvironmentResult',
    'AwaitableGetFusionEnvironmentResult',
    'get_fusion_environment',
    'get_fusion_environment_output',
]

@pulumi.output_type
class GetFusionEnvironmentResult:
    """
    A collection of values returned by getFusionEnvironment.
    """
    def __init__(__self__, additional_language_packs=None, applied_patch_bundles=None, compartment_id=None, create_fusion_environment_admin_user_details=None, defined_tags=None, display_name=None, dns_prefix=None, domain_id=None, freeform_tags=None, fusion_environment_family_id=None, fusion_environment_id=None, fusion_environment_type=None, id=None, idcs_domain_url=None, is_break_glass_enabled=None, kms_key_id=None, kms_key_infos=None, lifecycle_details=None, lockbox_id=None, maintenance_policies=None, public_url=None, refreshes=None, rules=None, state=None, subscription_ids=None, system_name=None, time_created=None, time_upcoming_maintenance=None, time_updated=None, version=None):
        if additional_language_packs and not isinstance(additional_language_packs, list):
            raise TypeError("Expected argument 'additional_language_packs' to be a list")
        pulumi.set(__self__, "additional_language_packs", additional_language_packs)
        if applied_patch_bundles and not isinstance(applied_patch_bundles, list):
            raise TypeError("Expected argument 'applied_patch_bundles' to be a list")
        pulumi.set(__self__, "applied_patch_bundles", applied_patch_bundles)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if create_fusion_environment_admin_user_details and not isinstance(create_fusion_environment_admin_user_details, list):
            raise TypeError("Expected argument 'create_fusion_environment_admin_user_details' to be a list")
        pulumi.set(__self__, "create_fusion_environment_admin_user_details", create_fusion_environment_admin_user_details)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if dns_prefix and not isinstance(dns_prefix, str):
            raise TypeError("Expected argument 'dns_prefix' to be a str")
        pulumi.set(__self__, "dns_prefix", dns_prefix)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if fusion_environment_family_id and not isinstance(fusion_environment_family_id, str):
            raise TypeError("Expected argument 'fusion_environment_family_id' to be a str")
        pulumi.set(__self__, "fusion_environment_family_id", fusion_environment_family_id)
        if fusion_environment_id and not isinstance(fusion_environment_id, str):
            raise TypeError("Expected argument 'fusion_environment_id' to be a str")
        pulumi.set(__self__, "fusion_environment_id", fusion_environment_id)
        if fusion_environment_type and not isinstance(fusion_environment_type, str):
            raise TypeError("Expected argument 'fusion_environment_type' to be a str")
        pulumi.set(__self__, "fusion_environment_type", fusion_environment_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_domain_url and not isinstance(idcs_domain_url, str):
            raise TypeError("Expected argument 'idcs_domain_url' to be a str")
        pulumi.set(__self__, "idcs_domain_url", idcs_domain_url)
        if is_break_glass_enabled and not isinstance(is_break_glass_enabled, bool):
            raise TypeError("Expected argument 'is_break_glass_enabled' to be a bool")
        pulumi.set(__self__, "is_break_glass_enabled", is_break_glass_enabled)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if kms_key_infos and not isinstance(kms_key_infos, list):
            raise TypeError("Expected argument 'kms_key_infos' to be a list")
        pulumi.set(__self__, "kms_key_infos", kms_key_infos)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if lockbox_id and not isinstance(lockbox_id, str):
            raise TypeError("Expected argument 'lockbox_id' to be a str")
        pulumi.set(__self__, "lockbox_id", lockbox_id)
        if maintenance_policies and not isinstance(maintenance_policies, list):
            raise TypeError("Expected argument 'maintenance_policies' to be a list")
        pulumi.set(__self__, "maintenance_policies", maintenance_policies)
        if public_url and not isinstance(public_url, str):
            raise TypeError("Expected argument 'public_url' to be a str")
        pulumi.set(__self__, "public_url", public_url)
        if refreshes and not isinstance(refreshes, list):
            raise TypeError("Expected argument 'refreshes' to be a list")
        pulumi.set(__self__, "refreshes", refreshes)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subscription_ids and not isinstance(subscription_ids, list):
            raise TypeError("Expected argument 'subscription_ids' to be a list")
        pulumi.set(__self__, "subscription_ids", subscription_ids)
        if system_name and not isinstance(system_name, str):
            raise TypeError("Expected argument 'system_name' to be a str")
        pulumi.set(__self__, "system_name", system_name)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_upcoming_maintenance and not isinstance(time_upcoming_maintenance, str):
            raise TypeError("Expected argument 'time_upcoming_maintenance' to be a str")
        pulumi.set(__self__, "time_upcoming_maintenance", time_upcoming_maintenance)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="additionalLanguagePacks")
    def additional_language_packs(self) -> Sequence[str]:
        """
        Language packs
        """
        return pulumi.get(self, "additional_language_packs")

    @property
    @pulumi.getter(name="appliedPatchBundles")
    def applied_patch_bundles(self) -> Sequence[str]:
        """
        Patch bundle names
        """
        return pulumi.get(self, "applied_patch_bundles")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createFusionEnvironmentAdminUserDetails")
    def create_fusion_environment_admin_user_details(self) -> Sequence['outputs.GetFusionEnvironmentCreateFusionEnvironmentAdminUserDetailResult']:
        return pulumi.get(self, "create_fusion_environment_admin_user_details")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        FusionEnvironment Identifier, can be renamed
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> str:
        """
        DNS prefix
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
        """
        The IDCS domain created for the fusion instance
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="fusionEnvironmentFamilyId")
    def fusion_environment_family_id(self) -> str:
        """
        FusionEnvironmentFamily Identifier
        """
        return pulumi.get(self, "fusion_environment_family_id")

    @property
    @pulumi.getter(name="fusionEnvironmentId")
    def fusion_environment_id(self) -> str:
        return pulumi.get(self, "fusion_environment_id")

    @property
    @pulumi.getter(name="fusionEnvironmentType")
    def fusion_environment_type(self) -> str:
        """
        Type of the FusionEnvironment.
        """
        return pulumi.get(self, "fusion_environment_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier that is immutable on creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsDomainUrl")
    def idcs_domain_url(self) -> str:
        """
        The IDCS Domain URL
        """
        return pulumi.get(self, "idcs_domain_url")

    @property
    @pulumi.getter(name="isBreakGlassEnabled")
    def is_break_glass_enabled(self) -> bool:
        """
        If it's true, then the Break Glass feature is enabled
        """
        return pulumi.get(self, "is_break_glass_enabled")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        BYOK key id
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="kmsKeyInfos")
    def kms_key_infos(self) -> Sequence['outputs.GetFusionEnvironmentKmsKeyInfoResult']:
        """
        BYOK key info
        """
        return pulumi.get(self, "kms_key_infos")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="lockboxId")
    def lockbox_id(self) -> str:
        """
        The lockbox Id of this fusion environment. If there's no lockbox id, this field will be null
        """
        return pulumi.get(self, "lockbox_id")

    @property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(self) -> Sequence['outputs.GetFusionEnvironmentMaintenancePolicyResult']:
        """
        The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see [Understanding Environment Maintenance](https://docs.cloud.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance).
        """
        return pulumi.get(self, "maintenance_policies")

    @property
    @pulumi.getter(name="publicUrl")
    def public_url(self) -> str:
        """
        Public URL
        """
        return pulumi.get(self, "public_url")

    @property
    @pulumi.getter
    def refreshes(self) -> Sequence['outputs.GetFusionEnvironmentRefreshResult']:
        """
        Describes a refresh of a fusion environment
        """
        return pulumi.get(self, "refreshes")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetFusionEnvironmentRuleResult']:
        """
        Network Access Control Rules
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the ServiceInstance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subscriptionIds")
    def subscription_ids(self) -> Sequence[str]:
        """
        List of subscription IDs.
        """
        return pulumi.get(self, "subscription_ids")

    @property
    @pulumi.getter(name="systemName")
    def system_name(self) -> str:
        """
        Environment Specific Guid/ System Name
        """
        return pulumi.get(self, "system_name")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the the FusionEnvironment was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpcomingMaintenance")
    def time_upcoming_maintenance(self) -> str:
        """
        The next maintenance for this environment
        """
        return pulumi.get(self, "time_upcoming_maintenance")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the FusionEnvironment was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of Fusion Apps used by this environment
        """
        return pulumi.get(self, "version")


class AwaitableGetFusionEnvironmentResult(GetFusionEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFusionEnvironmentResult(
            additional_language_packs=self.additional_language_packs,
            applied_patch_bundles=self.applied_patch_bundles,
            compartment_id=self.compartment_id,
            create_fusion_environment_admin_user_details=self.create_fusion_environment_admin_user_details,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            dns_prefix=self.dns_prefix,
            domain_id=self.domain_id,
            freeform_tags=self.freeform_tags,
            fusion_environment_family_id=self.fusion_environment_family_id,
            fusion_environment_id=self.fusion_environment_id,
            fusion_environment_type=self.fusion_environment_type,
            id=self.id,
            idcs_domain_url=self.idcs_domain_url,
            is_break_glass_enabled=self.is_break_glass_enabled,
            kms_key_id=self.kms_key_id,
            kms_key_infos=self.kms_key_infos,
            lifecycle_details=self.lifecycle_details,
            lockbox_id=self.lockbox_id,
            maintenance_policies=self.maintenance_policies,
            public_url=self.public_url,
            refreshes=self.refreshes,
            rules=self.rules,
            state=self.state,
            subscription_ids=self.subscription_ids,
            system_name=self.system_name,
            time_created=self.time_created,
            time_upcoming_maintenance=self.time_upcoming_maintenance,
            time_updated=self.time_updated,
            version=self.version)


def get_fusion_environment(fusion_environment_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFusionEnvironmentResult:
    """
    This data source provides details about a specific Fusion Environment resource in Oracle Cloud Infrastructure Fusion Apps service.

    Gets a FusionEnvironment by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment = oci.Functions.get_fusion_environment(fusion_environment_id=test_fusion_environment_oci_fusion_apps_fusion_environment["id"])
    ```


    :param str fusion_environment_id: unique FusionEnvironment identifier
    """
    __args__ = dict()
    __args__['fusionEnvironmentId'] = fusion_environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getFusionEnvironment:getFusionEnvironment', __args__, opts=opts, typ=GetFusionEnvironmentResult).value

    return AwaitableGetFusionEnvironmentResult(
        additional_language_packs=pulumi.get(__ret__, 'additional_language_packs'),
        applied_patch_bundles=pulumi.get(__ret__, 'applied_patch_bundles'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        create_fusion_environment_admin_user_details=pulumi.get(__ret__, 'create_fusion_environment_admin_user_details'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        dns_prefix=pulumi.get(__ret__, 'dns_prefix'),
        domain_id=pulumi.get(__ret__, 'domain_id'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        fusion_environment_family_id=pulumi.get(__ret__, 'fusion_environment_family_id'),
        fusion_environment_id=pulumi.get(__ret__, 'fusion_environment_id'),
        fusion_environment_type=pulumi.get(__ret__, 'fusion_environment_type'),
        id=pulumi.get(__ret__, 'id'),
        idcs_domain_url=pulumi.get(__ret__, 'idcs_domain_url'),
        is_break_glass_enabled=pulumi.get(__ret__, 'is_break_glass_enabled'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        kms_key_infos=pulumi.get(__ret__, 'kms_key_infos'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        lockbox_id=pulumi.get(__ret__, 'lockbox_id'),
        maintenance_policies=pulumi.get(__ret__, 'maintenance_policies'),
        public_url=pulumi.get(__ret__, 'public_url'),
        refreshes=pulumi.get(__ret__, 'refreshes'),
        rules=pulumi.get(__ret__, 'rules'),
        state=pulumi.get(__ret__, 'state'),
        subscription_ids=pulumi.get(__ret__, 'subscription_ids'),
        system_name=pulumi.get(__ret__, 'system_name'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_upcoming_maintenance=pulumi.get(__ret__, 'time_upcoming_maintenance'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_fusion_environment)
def get_fusion_environment_output(fusion_environment_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFusionEnvironmentResult]:
    """
    This data source provides details about a specific Fusion Environment resource in Oracle Cloud Infrastructure Fusion Apps service.

    Gets a FusionEnvironment by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment = oci.Functions.get_fusion_environment(fusion_environment_id=test_fusion_environment_oci_fusion_apps_fusion_environment["id"])
    ```


    :param str fusion_environment_id: unique FusionEnvironment identifier
    """
    ...
