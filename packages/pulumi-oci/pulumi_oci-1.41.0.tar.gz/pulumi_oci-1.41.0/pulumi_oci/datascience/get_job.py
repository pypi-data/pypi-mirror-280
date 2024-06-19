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
    'GetJobResult',
    'AwaitableGetJobResult',
    'get_job',
    'get_job_output',
]

@pulumi.output_type
class GetJobResult:
    """
    A collection of values returned by getJob.
    """
    def __init__(__self__, artifact_content_disposition=None, artifact_content_length=None, artifact_content_md5=None, artifact_last_modified=None, compartment_id=None, created_by=None, defined_tags=None, delete_related_job_runs=None, description=None, display_name=None, empty_artifact=None, freeform_tags=None, id=None, job_artifact=None, job_configuration_details=None, job_environment_configuration_details=None, job_id=None, job_infrastructure_configuration_details=None, job_log_configuration_details=None, job_storage_mount_configuration_details_lists=None, lifecycle_details=None, project_id=None, state=None, time_created=None):
        if artifact_content_disposition and not isinstance(artifact_content_disposition, str):
            raise TypeError("Expected argument 'artifact_content_disposition' to be a str")
        pulumi.set(__self__, "artifact_content_disposition", artifact_content_disposition)
        if artifact_content_length and not isinstance(artifact_content_length, str):
            raise TypeError("Expected argument 'artifact_content_length' to be a str")
        pulumi.set(__self__, "artifact_content_length", artifact_content_length)
        if artifact_content_md5 and not isinstance(artifact_content_md5, str):
            raise TypeError("Expected argument 'artifact_content_md5' to be a str")
        pulumi.set(__self__, "artifact_content_md5", artifact_content_md5)
        if artifact_last_modified and not isinstance(artifact_last_modified, str):
            raise TypeError("Expected argument 'artifact_last_modified' to be a str")
        pulumi.set(__self__, "artifact_last_modified", artifact_last_modified)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if delete_related_job_runs and not isinstance(delete_related_job_runs, bool):
            raise TypeError("Expected argument 'delete_related_job_runs' to be a bool")
        pulumi.set(__self__, "delete_related_job_runs", delete_related_job_runs)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if empty_artifact and not isinstance(empty_artifact, bool):
            raise TypeError("Expected argument 'empty_artifact' to be a bool")
        pulumi.set(__self__, "empty_artifact", empty_artifact)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if job_artifact and not isinstance(job_artifact, str):
            raise TypeError("Expected argument 'job_artifact' to be a str")
        pulumi.set(__self__, "job_artifact", job_artifact)
        if job_configuration_details and not isinstance(job_configuration_details, list):
            raise TypeError("Expected argument 'job_configuration_details' to be a list")
        pulumi.set(__self__, "job_configuration_details", job_configuration_details)
        if job_environment_configuration_details and not isinstance(job_environment_configuration_details, list):
            raise TypeError("Expected argument 'job_environment_configuration_details' to be a list")
        pulumi.set(__self__, "job_environment_configuration_details", job_environment_configuration_details)
        if job_id and not isinstance(job_id, str):
            raise TypeError("Expected argument 'job_id' to be a str")
        pulumi.set(__self__, "job_id", job_id)
        if job_infrastructure_configuration_details and not isinstance(job_infrastructure_configuration_details, list):
            raise TypeError("Expected argument 'job_infrastructure_configuration_details' to be a list")
        pulumi.set(__self__, "job_infrastructure_configuration_details", job_infrastructure_configuration_details)
        if job_log_configuration_details and not isinstance(job_log_configuration_details, list):
            raise TypeError("Expected argument 'job_log_configuration_details' to be a list")
        pulumi.set(__self__, "job_log_configuration_details", job_log_configuration_details)
        if job_storage_mount_configuration_details_lists and not isinstance(job_storage_mount_configuration_details_lists, list):
            raise TypeError("Expected argument 'job_storage_mount_configuration_details_lists' to be a list")
        pulumi.set(__self__, "job_storage_mount_configuration_details_lists", job_storage_mount_configuration_details_lists)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)

    @property
    @pulumi.getter(name="artifactContentDisposition")
    def artifact_content_disposition(self) -> str:
        return pulumi.get(self, "artifact_content_disposition")

    @property
    @pulumi.getter(name="artifactContentLength")
    def artifact_content_length(self) -> str:
        return pulumi.get(self, "artifact_content_length")

    @property
    @pulumi.getter(name="artifactContentMd5")
    def artifact_content_md5(self) -> str:
        return pulumi.get(self, "artifact_content_md5")

    @property
    @pulumi.getter(name="artifactLastModified")
    def artifact_last_modified(self) -> str:
        return pulumi.get(self, "artifact_last_modified")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the job.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the project.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="deleteRelatedJobRuns")
    def delete_related_job_runs(self) -> bool:
        return pulumi.get(self, "delete_related_job_runs")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A short description of the job.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly display name for the resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="emptyArtifact")
    def empty_artifact(self) -> bool:
        return pulumi.get(self, "empty_artifact")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="jobArtifact")
    def job_artifact(self) -> str:
        return pulumi.get(self, "job_artifact")

    @property
    @pulumi.getter(name="jobConfigurationDetails")
    def job_configuration_details(self) -> Sequence['outputs.GetJobJobConfigurationDetailResult']:
        """
        The job configuration details
        """
        return pulumi.get(self, "job_configuration_details")

    @property
    @pulumi.getter(name="jobEnvironmentConfigurationDetails")
    def job_environment_configuration_details(self) -> Sequence['outputs.GetJobJobEnvironmentConfigurationDetailResult']:
        """
        Environment configuration to capture job runtime dependencies.
        """
        return pulumi.get(self, "job_environment_configuration_details")

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> str:
        return pulumi.get(self, "job_id")

    @property
    @pulumi.getter(name="jobInfrastructureConfigurationDetails")
    def job_infrastructure_configuration_details(self) -> Sequence['outputs.GetJobJobInfrastructureConfigurationDetailResult']:
        """
        The job infrastructure configuration details (shape, block storage, etc.)
        """
        return pulumi.get(self, "job_infrastructure_configuration_details")

    @property
    @pulumi.getter(name="jobLogConfigurationDetails")
    def job_log_configuration_details(self) -> Sequence['outputs.GetJobJobLogConfigurationDetailResult']:
        """
        Logging configuration for resource.
        """
        return pulumi.get(self, "job_log_configuration_details")

    @property
    @pulumi.getter(name="jobStorageMountConfigurationDetailsLists")
    def job_storage_mount_configuration_details_lists(self) -> Sequence['outputs.GetJobJobStorageMountConfigurationDetailsListResult']:
        """
        Collection of JobStorageMountConfigurationDetails.
        """
        return pulumi.get(self, "job_storage_mount_configuration_details_lists")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        The state of the job.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the job with.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the resource was created in the timestamp format defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z
        """
        return pulumi.get(self, "time_created")


class AwaitableGetJobResult(GetJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobResult(
            artifact_content_disposition=self.artifact_content_disposition,
            artifact_content_length=self.artifact_content_length,
            artifact_content_md5=self.artifact_content_md5,
            artifact_last_modified=self.artifact_last_modified,
            compartment_id=self.compartment_id,
            created_by=self.created_by,
            defined_tags=self.defined_tags,
            delete_related_job_runs=self.delete_related_job_runs,
            description=self.description,
            display_name=self.display_name,
            empty_artifact=self.empty_artifact,
            freeform_tags=self.freeform_tags,
            id=self.id,
            job_artifact=self.job_artifact,
            job_configuration_details=self.job_configuration_details,
            job_environment_configuration_details=self.job_environment_configuration_details,
            job_id=self.job_id,
            job_infrastructure_configuration_details=self.job_infrastructure_configuration_details,
            job_log_configuration_details=self.job_log_configuration_details,
            job_storage_mount_configuration_details_lists=self.job_storage_mount_configuration_details_lists,
            lifecycle_details=self.lifecycle_details,
            project_id=self.project_id,
            state=self.state,
            time_created=self.time_created)


def get_job(job_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobResult:
    """
    This data source provides details about a specific Job resource in Oracle Cloud Infrastructure Data Science service.

    Gets a job.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_job = oci.DataScience.get_job(job_id=test_job_oci_datascience_job["id"])
    ```


    :param str job_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
    """
    __args__ = dict()
    __args__['jobId'] = job_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataScience/getJob:getJob', __args__, opts=opts, typ=GetJobResult).value

    return AwaitableGetJobResult(
        artifact_content_disposition=pulumi.get(__ret__, 'artifact_content_disposition'),
        artifact_content_length=pulumi.get(__ret__, 'artifact_content_length'),
        artifact_content_md5=pulumi.get(__ret__, 'artifact_content_md5'),
        artifact_last_modified=pulumi.get(__ret__, 'artifact_last_modified'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_by=pulumi.get(__ret__, 'created_by'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        delete_related_job_runs=pulumi.get(__ret__, 'delete_related_job_runs'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        empty_artifact=pulumi.get(__ret__, 'empty_artifact'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        job_artifact=pulumi.get(__ret__, 'job_artifact'),
        job_configuration_details=pulumi.get(__ret__, 'job_configuration_details'),
        job_environment_configuration_details=pulumi.get(__ret__, 'job_environment_configuration_details'),
        job_id=pulumi.get(__ret__, 'job_id'),
        job_infrastructure_configuration_details=pulumi.get(__ret__, 'job_infrastructure_configuration_details'),
        job_log_configuration_details=pulumi.get(__ret__, 'job_log_configuration_details'),
        job_storage_mount_configuration_details_lists=pulumi.get(__ret__, 'job_storage_mount_configuration_details_lists'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'))


@_utilities.lift_output_func(get_job)
def get_job_output(job_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobResult]:
    """
    This data source provides details about a specific Job resource in Oracle Cloud Infrastructure Data Science service.

    Gets a job.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_job = oci.DataScience.get_job(job_id=test_job_oci_datascience_job["id"])
    ```


    :param str job_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
    """
    ...
