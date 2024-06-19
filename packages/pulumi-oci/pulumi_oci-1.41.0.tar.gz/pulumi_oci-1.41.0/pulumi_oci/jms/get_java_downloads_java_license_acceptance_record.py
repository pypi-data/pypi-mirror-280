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
    'GetJavaDownloadsJavaLicenseAcceptanceRecordResult',
    'AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordResult',
    'get_java_downloads_java_license_acceptance_record',
    'get_java_downloads_java_license_acceptance_record_output',
]

@pulumi.output_type
class GetJavaDownloadsJavaLicenseAcceptanceRecordResult:
    """
    A collection of values returned by getJavaDownloadsJavaLicenseAcceptanceRecord.
    """
    def __init__(__self__, compartment_id=None, created_bies=None, defined_tags=None, freeform_tags=None, id=None, java_license_acceptance_record_id=None, last_updated_bies=None, license_acceptance_status=None, license_type=None, state=None, system_tags=None, time_accepted=None, time_last_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_bies and not isinstance(created_bies, list):
            raise TypeError("Expected argument 'created_bies' to be a list")
        pulumi.set(__self__, "created_bies", created_bies)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if java_license_acceptance_record_id and not isinstance(java_license_acceptance_record_id, str):
            raise TypeError("Expected argument 'java_license_acceptance_record_id' to be a str")
        pulumi.set(__self__, "java_license_acceptance_record_id", java_license_acceptance_record_id)
        if last_updated_bies and not isinstance(last_updated_bies, list):
            raise TypeError("Expected argument 'last_updated_bies' to be a list")
        pulumi.set(__self__, "last_updated_bies", last_updated_bies)
        if license_acceptance_status and not isinstance(license_acceptance_status, str):
            raise TypeError("Expected argument 'license_acceptance_status' to be a str")
        pulumi.set(__self__, "license_acceptance_status", license_acceptance_status)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_accepted and not isinstance(time_accepted, str):
            raise TypeError("Expected argument 'time_accepted' to be a str")
        pulumi.set(__self__, "time_accepted", time_accepted)
        if time_last_updated and not isinstance(time_last_updated, str):
            raise TypeError("Expected argument 'time_last_updated' to be a str")
        pulumi.set(__self__, "time_last_updated", time_last_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The tenancy [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user accepting the license.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdBies")
    def created_bies(self) -> Sequence['outputs.GetJavaDownloadsJavaLicenseAcceptanceRecordCreatedByResult']:
        """
        An authorized principal.
        """
        return pulumi.get(self, "created_bies")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. (See [Understanding Free-form Tags](https://docs.cloud.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`. (See [Managing Tags and Tag Namespaces](https://docs.cloud.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the principal.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="javaLicenseAcceptanceRecordId")
    def java_license_acceptance_record_id(self) -> str:
        return pulumi.get(self, "java_license_acceptance_record_id")

    @property
    @pulumi.getter(name="lastUpdatedBies")
    def last_updated_bies(self) -> Sequence['outputs.GetJavaDownloadsJavaLicenseAcceptanceRecordLastUpdatedByResult']:
        """
        An authorized principal.
        """
        return pulumi.get(self, "last_updated_bies")

    @property
    @pulumi.getter(name="licenseAcceptanceStatus")
    def license_acceptance_status(self) -> str:
        """
        Status of license acceptance.
        """
        return pulumi.get(self, "license_acceptance_status")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> str:
        """
        License type associated with the acceptance.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the JavaLicenseAcceptanceRecord.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeAccepted")
    def time_accepted(self) -> str:
        """
        The date and time of license acceptance (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
        """
        return pulumi.get(self, "time_accepted")

    @property
    @pulumi.getter(name="timeLastUpdated")
    def time_last_updated(self) -> str:
        """
        The date and time of last update (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
        """
        return pulumi.get(self, "time_last_updated")


class AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordResult(GetJavaDownloadsJavaLicenseAcceptanceRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJavaDownloadsJavaLicenseAcceptanceRecordResult(
            compartment_id=self.compartment_id,
            created_bies=self.created_bies,
            defined_tags=self.defined_tags,
            freeform_tags=self.freeform_tags,
            id=self.id,
            java_license_acceptance_record_id=self.java_license_acceptance_record_id,
            last_updated_bies=self.last_updated_bies,
            license_acceptance_status=self.license_acceptance_status,
            license_type=self.license_type,
            state=self.state,
            system_tags=self.system_tags,
            time_accepted=self.time_accepted,
            time_last_updated=self.time_last_updated)


def get_java_downloads_java_license_acceptance_record(java_license_acceptance_record_id: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordResult:
    """
    This data source provides details about a specific Java License Acceptance Record resource in Oracle Cloud Infrastructure Jms Java Downloads service.

    Returns a specific Java license acceptance record in a tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_java_license_acceptance_record = oci.Jms.get_java_downloads_java_license_acceptance_record(java_license_acceptance_record_id=test_java_license_acceptance_record_oci_jms_java_downloads_java_license_acceptance_record["id"])
    ```


    :param str java_license_acceptance_record_id: Unique Java license acceptance record identifier.
    """
    __args__ = dict()
    __args__['javaLicenseAcceptanceRecordId'] = java_license_acceptance_record_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Jms/getJavaDownloadsJavaLicenseAcceptanceRecord:getJavaDownloadsJavaLicenseAcceptanceRecord', __args__, opts=opts, typ=GetJavaDownloadsJavaLicenseAcceptanceRecordResult).value

    return AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_bies=pulumi.get(__ret__, 'created_bies'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        java_license_acceptance_record_id=pulumi.get(__ret__, 'java_license_acceptance_record_id'),
        last_updated_bies=pulumi.get(__ret__, 'last_updated_bies'),
        license_acceptance_status=pulumi.get(__ret__, 'license_acceptance_status'),
        license_type=pulumi.get(__ret__, 'license_type'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_accepted=pulumi.get(__ret__, 'time_accepted'),
        time_last_updated=pulumi.get(__ret__, 'time_last_updated'))


@_utilities.lift_output_func(get_java_downloads_java_license_acceptance_record)
def get_java_downloads_java_license_acceptance_record_output(java_license_acceptance_record_id: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJavaDownloadsJavaLicenseAcceptanceRecordResult]:
    """
    This data source provides details about a specific Java License Acceptance Record resource in Oracle Cloud Infrastructure Jms Java Downloads service.

    Returns a specific Java license acceptance record in a tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_java_license_acceptance_record = oci.Jms.get_java_downloads_java_license_acceptance_record(java_license_acceptance_record_id=test_java_license_acceptance_record_oci_jms_java_downloads_java_license_acceptance_record["id"])
    ```


    :param str java_license_acceptance_record_id: Unique Java license acceptance record identifier.
    """
    ...
