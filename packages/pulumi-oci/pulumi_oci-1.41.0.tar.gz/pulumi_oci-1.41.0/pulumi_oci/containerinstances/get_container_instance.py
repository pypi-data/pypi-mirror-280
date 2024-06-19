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
    'GetContainerInstanceResult',
    'AwaitableGetContainerInstanceResult',
    'get_container_instance',
    'get_container_instance_output',
]

@pulumi.output_type
class GetContainerInstanceResult:
    """
    A collection of values returned by getContainerInstance.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, container_count=None, container_instance_id=None, container_restart_policy=None, containers=None, defined_tags=None, display_name=None, dns_configs=None, fault_domain=None, freeform_tags=None, graceful_shutdown_timeout_in_seconds=None, id=None, image_pull_secrets=None, lifecycle_details=None, shape=None, shape_configs=None, state=None, system_tags=None, time_created=None, time_updated=None, vnics=None, volume_count=None, volumes=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if container_count and not isinstance(container_count, int):
            raise TypeError("Expected argument 'container_count' to be a int")
        pulumi.set(__self__, "container_count", container_count)
        if container_instance_id and not isinstance(container_instance_id, str):
            raise TypeError("Expected argument 'container_instance_id' to be a str")
        pulumi.set(__self__, "container_instance_id", container_instance_id)
        if container_restart_policy and not isinstance(container_restart_policy, str):
            raise TypeError("Expected argument 'container_restart_policy' to be a str")
        pulumi.set(__self__, "container_restart_policy", container_restart_policy)
        if containers and not isinstance(containers, list):
            raise TypeError("Expected argument 'containers' to be a list")
        pulumi.set(__self__, "containers", containers)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if dns_configs and not isinstance(dns_configs, list):
            raise TypeError("Expected argument 'dns_configs' to be a list")
        pulumi.set(__self__, "dns_configs", dns_configs)
        if fault_domain and not isinstance(fault_domain, str):
            raise TypeError("Expected argument 'fault_domain' to be a str")
        pulumi.set(__self__, "fault_domain", fault_domain)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if graceful_shutdown_timeout_in_seconds and not isinstance(graceful_shutdown_timeout_in_seconds, str):
            raise TypeError("Expected argument 'graceful_shutdown_timeout_in_seconds' to be a str")
        pulumi.set(__self__, "graceful_shutdown_timeout_in_seconds", graceful_shutdown_timeout_in_seconds)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_pull_secrets and not isinstance(image_pull_secrets, list):
            raise TypeError("Expected argument 'image_pull_secrets' to be a list")
        pulumi.set(__self__, "image_pull_secrets", image_pull_secrets)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if shape and not isinstance(shape, str):
            raise TypeError("Expected argument 'shape' to be a str")
        pulumi.set(__self__, "shape", shape)
        if shape_configs and not isinstance(shape_configs, list):
            raise TypeError("Expected argument 'shape_configs' to be a list")
        pulumi.set(__self__, "shape_configs", shape_configs)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if vnics and not isinstance(vnics, list):
            raise TypeError("Expected argument 'vnics' to be a list")
        pulumi.set(__self__, "vnics", vnics)
        if volume_count and not isinstance(volume_count, int):
            raise TypeError("Expected argument 'volume_count' to be a int")
        pulumi.set(__self__, "volume_count", volume_count)
        if volumes and not isinstance(volumes, list):
            raise TypeError("Expected argument 'volumes' to be a list")
        pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain to place the container instance.
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="containerCount")
    def container_count(self) -> int:
        """
        The number of containers on the container instance.
        """
        return pulumi.get(self, "container_count")

    @property
    @pulumi.getter(name="containerInstanceId")
    def container_instance_id(self) -> str:
        return pulumi.get(self, "container_instance_id")

    @property
    @pulumi.getter(name="containerRestartPolicy")
    def container_restart_policy(self) -> str:
        """
        The container restart policy is applied for all containers in container instance.
        """
        return pulumi.get(self, "container_restart_policy")

    @property
    @pulumi.getter
    def containers(self) -> Sequence['outputs.GetContainerInstanceContainerResult']:
        """
        The containers on the container instance.
        """
        return pulumi.get(self, "containers")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsConfigs")
    def dns_configs(self) -> Sequence['outputs.GetContainerInstanceDnsConfigResult']:
        """
        DNS settings for containers.
        """
        return pulumi.get(self, "dns_configs")

    @property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> str:
        """
        The fault domain to place the container instance.
        """
        return pulumi.get(self, "fault_domain")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="gracefulShutdownTimeoutInSeconds")
    def graceful_shutdown_timeout_in_seconds(self) -> str:
        """
        The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a container instance. After the timeout is reached, the processes are sent a signal to be deleted.
        """
        return pulumi.get(self, "graceful_shutdown_timeout_in_seconds")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An OCID that cannot be changed.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imagePullSecrets")
    def image_pull_secrets(self) -> Sequence['outputs.GetContainerInstanceImagePullSecretResult']:
        """
        The image pulls secrets so you can access private registry to pull container images.
        """
        return pulumi.get(self, "image_pull_secrets")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message that describes the current state of the container in more detail. Can be used to provide actionable information.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def shape(self) -> str:
        """
        The shape of the container instance. The shape determines the number of OCPUs, amount of memory, and other resources that are allocated to a container instance.
        """
        return pulumi.get(self, "shape")

    @property
    @pulumi.getter(name="shapeConfigs")
    def shape_configs(self) -> Sequence['outputs.GetContainerInstanceShapeConfigResult']:
        """
        The shape configuration for a container instance. The shape configuration determines the resources thats are available to the container instance and its containers.
        """
        return pulumi.get(self, "shape_configs")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the container instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`.
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the container instance was created, in the format defined by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the container instance was updated, in the format defined by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def vnics(self) -> Sequence['outputs.GetContainerInstanceVnicResult']:
        """
        The virtual networks available to the containers in the container instance.
        """
        return pulumi.get(self, "vnics")

    @property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> int:
        """
        The number of volumes that are attached to the container instance.
        """
        return pulumi.get(self, "volume_count")

    @property
    @pulumi.getter
    def volumes(self) -> Sequence['outputs.GetContainerInstanceVolumeResult']:
        """
        A volume is a directory with data that is accessible across multiple containers in a container instance.
        """
        return pulumi.get(self, "volumes")


class AwaitableGetContainerInstanceResult(GetContainerInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerInstanceResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            container_count=self.container_count,
            container_instance_id=self.container_instance_id,
            container_restart_policy=self.container_restart_policy,
            containers=self.containers,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            dns_configs=self.dns_configs,
            fault_domain=self.fault_domain,
            freeform_tags=self.freeform_tags,
            graceful_shutdown_timeout_in_seconds=self.graceful_shutdown_timeout_in_seconds,
            id=self.id,
            image_pull_secrets=self.image_pull_secrets,
            lifecycle_details=self.lifecycle_details,
            shape=self.shape,
            shape_configs=self.shape_configs,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            vnics=self.vnics,
            volume_count=self.volume_count,
            volumes=self.volumes)


def get_container_instance(container_instance_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerInstanceResult:
    """
    This data source provides details about a specific Container Instance resource in Oracle Cloud Infrastructure Container Instances service.

    Gets information about the specified container instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_instance = oci.ContainerInstances.get_container_instance(container_instance_id=test_container_instance_oci_container_instances_container_instance["id"])
    ```


    :param str container_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance.
    """
    __args__ = dict()
    __args__['containerInstanceId'] = container_instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ContainerInstances/getContainerInstance:getContainerInstance', __args__, opts=opts, typ=GetContainerInstanceResult).value

    return AwaitableGetContainerInstanceResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        container_count=pulumi.get(__ret__, 'container_count'),
        container_instance_id=pulumi.get(__ret__, 'container_instance_id'),
        container_restart_policy=pulumi.get(__ret__, 'container_restart_policy'),
        containers=pulumi.get(__ret__, 'containers'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        dns_configs=pulumi.get(__ret__, 'dns_configs'),
        fault_domain=pulumi.get(__ret__, 'fault_domain'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        graceful_shutdown_timeout_in_seconds=pulumi.get(__ret__, 'graceful_shutdown_timeout_in_seconds'),
        id=pulumi.get(__ret__, 'id'),
        image_pull_secrets=pulumi.get(__ret__, 'image_pull_secrets'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        shape=pulumi.get(__ret__, 'shape'),
        shape_configs=pulumi.get(__ret__, 'shape_configs'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        vnics=pulumi.get(__ret__, 'vnics'),
        volume_count=pulumi.get(__ret__, 'volume_count'),
        volumes=pulumi.get(__ret__, 'volumes'))


@_utilities.lift_output_func(get_container_instance)
def get_container_instance_output(container_instance_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerInstanceResult]:
    """
    This data source provides details about a specific Container Instance resource in Oracle Cloud Infrastructure Container Instances service.

    Gets information about the specified container instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_instance = oci.ContainerInstances.get_container_instance(container_instance_id=test_container_instance_oci_container_instances_container_instance["id"])
    ```


    :param str container_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance.
    """
    ...
