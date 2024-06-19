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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, agent_configs=None, async_=None, availability_configs=None, availability_domain=None, boot_volume_id=None, capacity_reservation_id=None, cluster_placement_group_id=None, compartment_id=None, compute_cluster_id=None, create_vnic_details=None, dedicated_vm_host_id=None, defined_tags=None, display_name=None, extended_metadata=None, fault_domain=None, freeform_tags=None, hostname_label=None, id=None, image=None, instance_configuration_id=None, instance_id=None, instance_options=None, ipxe_script=None, is_cross_numa_node=None, is_pv_encryption_in_transit_enabled=None, launch_mode=None, launch_options=None, launch_volume_attachments=None, metadata=None, platform_configs=None, preemptible_instance_configs=None, preserve_boot_volume=None, preserve_data_volumes_created_at_launch=None, private_ip=None, public_ip=None, region=None, shape=None, shape_configs=None, source_details=None, state=None, subnet_id=None, system_tags=None, time_created=None, time_maintenance_reboot_due=None, update_operation_constraint=None):
        if agent_configs and not isinstance(agent_configs, list):
            raise TypeError("Expected argument 'agent_configs' to be a list")
        pulumi.set(__self__, "agent_configs", agent_configs)
        if async_ and not isinstance(async_, bool):
            raise TypeError("Expected argument 'async_' to be a bool")
        pulumi.set(__self__, "async_", async_)
        if availability_configs and not isinstance(availability_configs, list):
            raise TypeError("Expected argument 'availability_configs' to be a list")
        pulumi.set(__self__, "availability_configs", availability_configs)
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if boot_volume_id and not isinstance(boot_volume_id, str):
            raise TypeError("Expected argument 'boot_volume_id' to be a str")
        pulumi.set(__self__, "boot_volume_id", boot_volume_id)
        if capacity_reservation_id and not isinstance(capacity_reservation_id, str):
            raise TypeError("Expected argument 'capacity_reservation_id' to be a str")
        pulumi.set(__self__, "capacity_reservation_id", capacity_reservation_id)
        if cluster_placement_group_id and not isinstance(cluster_placement_group_id, str):
            raise TypeError("Expected argument 'cluster_placement_group_id' to be a str")
        pulumi.set(__self__, "cluster_placement_group_id", cluster_placement_group_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compute_cluster_id and not isinstance(compute_cluster_id, str):
            raise TypeError("Expected argument 'compute_cluster_id' to be a str")
        pulumi.set(__self__, "compute_cluster_id", compute_cluster_id)
        if create_vnic_details and not isinstance(create_vnic_details, list):
            raise TypeError("Expected argument 'create_vnic_details' to be a list")
        pulumi.set(__self__, "create_vnic_details", create_vnic_details)
        if dedicated_vm_host_id and not isinstance(dedicated_vm_host_id, str):
            raise TypeError("Expected argument 'dedicated_vm_host_id' to be a str")
        pulumi.set(__self__, "dedicated_vm_host_id", dedicated_vm_host_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if extended_metadata and not isinstance(extended_metadata, dict):
            raise TypeError("Expected argument 'extended_metadata' to be a dict")
        pulumi.set(__self__, "extended_metadata", extended_metadata)
        if fault_domain and not isinstance(fault_domain, str):
            raise TypeError("Expected argument 'fault_domain' to be a str")
        pulumi.set(__self__, "fault_domain", fault_domain)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if hostname_label and not isinstance(hostname_label, str):
            raise TypeError("Expected argument 'hostname_label' to be a str")
        pulumi.set(__self__, "hostname_label", hostname_label)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image and not isinstance(image, str):
            raise TypeError("Expected argument 'image' to be a str")
        pulumi.set(__self__, "image", image)
        if instance_configuration_id and not isinstance(instance_configuration_id, str):
            raise TypeError("Expected argument 'instance_configuration_id' to be a str")
        pulumi.set(__self__, "instance_configuration_id", instance_configuration_id)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if instance_options and not isinstance(instance_options, list):
            raise TypeError("Expected argument 'instance_options' to be a list")
        pulumi.set(__self__, "instance_options", instance_options)
        if ipxe_script and not isinstance(ipxe_script, str):
            raise TypeError("Expected argument 'ipxe_script' to be a str")
        pulumi.set(__self__, "ipxe_script", ipxe_script)
        if is_cross_numa_node and not isinstance(is_cross_numa_node, bool):
            raise TypeError("Expected argument 'is_cross_numa_node' to be a bool")
        pulumi.set(__self__, "is_cross_numa_node", is_cross_numa_node)
        if is_pv_encryption_in_transit_enabled and not isinstance(is_pv_encryption_in_transit_enabled, bool):
            raise TypeError("Expected argument 'is_pv_encryption_in_transit_enabled' to be a bool")
        pulumi.set(__self__, "is_pv_encryption_in_transit_enabled", is_pv_encryption_in_transit_enabled)
        if launch_mode and not isinstance(launch_mode, str):
            raise TypeError("Expected argument 'launch_mode' to be a str")
        pulumi.set(__self__, "launch_mode", launch_mode)
        if launch_options and not isinstance(launch_options, list):
            raise TypeError("Expected argument 'launch_options' to be a list")
        pulumi.set(__self__, "launch_options", launch_options)
        if launch_volume_attachments and not isinstance(launch_volume_attachments, list):
            raise TypeError("Expected argument 'launch_volume_attachments' to be a list")
        pulumi.set(__self__, "launch_volume_attachments", launch_volume_attachments)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if platform_configs and not isinstance(platform_configs, list):
            raise TypeError("Expected argument 'platform_configs' to be a list")
        pulumi.set(__self__, "platform_configs", platform_configs)
        if preemptible_instance_configs and not isinstance(preemptible_instance_configs, list):
            raise TypeError("Expected argument 'preemptible_instance_configs' to be a list")
        pulumi.set(__self__, "preemptible_instance_configs", preemptible_instance_configs)
        if preserve_boot_volume and not isinstance(preserve_boot_volume, bool):
            raise TypeError("Expected argument 'preserve_boot_volume' to be a bool")
        pulumi.set(__self__, "preserve_boot_volume", preserve_boot_volume)
        if preserve_data_volumes_created_at_launch and not isinstance(preserve_data_volumes_created_at_launch, bool):
            raise TypeError("Expected argument 'preserve_data_volumes_created_at_launch' to be a bool")
        pulumi.set(__self__, "preserve_data_volumes_created_at_launch", preserve_data_volumes_created_at_launch)
        if private_ip and not isinstance(private_ip, str):
            raise TypeError("Expected argument 'private_ip' to be a str")
        pulumi.set(__self__, "private_ip", private_ip)
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        pulumi.set(__self__, "public_ip", public_ip)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if shape and not isinstance(shape, str):
            raise TypeError("Expected argument 'shape' to be a str")
        pulumi.set(__self__, "shape", shape)
        if shape_configs and not isinstance(shape_configs, list):
            raise TypeError("Expected argument 'shape_configs' to be a list")
        pulumi.set(__self__, "shape_configs", shape_configs)
        if source_details and not isinstance(source_details, list):
            raise TypeError("Expected argument 'source_details' to be a list")
        pulumi.set(__self__, "source_details", source_details)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_maintenance_reboot_due and not isinstance(time_maintenance_reboot_due, str):
            raise TypeError("Expected argument 'time_maintenance_reboot_due' to be a str")
        pulumi.set(__self__, "time_maintenance_reboot_due", time_maintenance_reboot_due)
        if update_operation_constraint and not isinstance(update_operation_constraint, str):
            raise TypeError("Expected argument 'update_operation_constraint' to be a str")
        pulumi.set(__self__, "update_operation_constraint", update_operation_constraint)

    @property
    @pulumi.getter(name="agentConfigs")
    def agent_configs(self) -> Sequence['outputs.GetInstanceAgentConfigResult']:
        """
        Configuration options for the Oracle Cloud Agent software running on the instance.
        """
        return pulumi.get(self, "agent_configs")

    @property
    @pulumi.getter(name="async")
    def async_(self) -> bool:
        return pulumi.get(self, "async_")

    @property
    @pulumi.getter(name="availabilityConfigs")
    def availability_configs(self) -> Sequence['outputs.GetInstanceAvailabilityConfigResult']:
        """
        Options for defining the availabiity of a VM instance after a maintenance event that impacts the underlying hardware.
        """
        return pulumi.get(self, "availability_configs")

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain the instance is running in.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="bootVolumeId")
    def boot_volume_id(self) -> str:
        """
        The OCID of the attached boot volume. If the `source_type` is `bootVolume`, this will be the same OCID as the `source_id`.
        """
        return pulumi.get(self, "boot_volume_id")

    @property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> str:
        """
        The OCID of the compute capacity reservation this instance is launched under. When this field contains an empty string or is null, the instance is not currently in a capacity reservation. For more information, see [Capacity Reservations](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
        """
        return pulumi.get(self, "capacity_reservation_id")

    @property
    @pulumi.getter(name="clusterPlacementGroupId")
    def cluster_placement_group_id(self) -> str:
        """
        The OCID of the cluster placement group of the instance.
        """
        return pulumi.get(self, "cluster_placement_group_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing images to search
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> str:
        return pulumi.get(self, "compute_cluster_id")

    @property
    @pulumi.getter(name="createVnicDetails")
    def create_vnic_details(self) -> Sequence['outputs.GetInstanceCreateVnicDetailResult']:
        return pulumi.get(self, "create_vnic_details")

    @property
    @pulumi.getter(name="dedicatedVmHostId")
    def dedicated_vm_host_id(self) -> str:
        """
        The OCID of the dedicated virtual machine host that the instance is placed on.
        """
        return pulumi.get(self, "dedicated_vm_host_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
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
    @pulumi.getter(name="extendedMetadata")
    def extended_metadata(self) -> Mapping[str, Any]:
        """
        Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.
        """
        return pulumi.get(self, "extended_metadata")

    @property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> str:
        """
        The name of the fault domain the instance is running in.
        """
        return pulumi.get(self, "fault_domain")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="hostnameLabel")
    def hostname_label(self) -> str:
        """
        The hostname for the instance VNIC's primary private IP.
        """
        warnings.warn("""The 'hostname_label' field has been deprecated. Please use 'hostname_label under create_vnic_details' instead.""", DeprecationWarning)
        pulumi.log.warn("""hostname_label is deprecated: The 'hostname_label' field has been deprecated. Please use 'hostname_label under create_vnic_details' instead.""")

        return pulumi.get(self, "hostname_label")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def image(self) -> str:
        """
        Deprecated. Use `sourceDetails` instead.
        """
        warnings.warn("""The 'image' field has been deprecated. Please use 'source_details' instead. If both fields are specified, then 'source_details' will be used.""", DeprecationWarning)
        pulumi.log.warn("""image is deprecated: The 'image' field has been deprecated. Please use 'source_details' instead. If both fields are specified, then 'source_details' will be used.""")

        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="instanceConfigurationId")
    def instance_configuration_id(self) -> str:
        """
        The OCID of the Instance Configuration used to source launch details for this instance. Any other fields supplied in the instance launch request override the details stored in the Instance Configuration for this instance launch.
        """
        return pulumi.get(self, "instance_configuration_id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="instanceOptions")
    def instance_options(self) -> Sequence['outputs.GetInstanceInstanceOptionResult']:
        """
        Optional mutable instance options
        """
        return pulumi.get(self, "instance_options")

    @property
    @pulumi.getter(name="ipxeScript")
    def ipxe_script(self) -> str:
        """
        When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.
        """
        return pulumi.get(self, "ipxe_script")

    @property
    @pulumi.getter(name="isCrossNumaNode")
    def is_cross_numa_node(self) -> bool:
        """
        Whether the instance’s OCPUs and memory are distributed across multiple NUMA nodes.
        """
        return pulumi.get(self, "is_cross_numa_node")

    @property
    @pulumi.getter(name="isPvEncryptionInTransitEnabled")
    def is_pv_encryption_in_transit_enabled(self) -> bool:
        """
        Deprecated. Instead use `isPvEncryptionInTransitEnabled` in [LaunchInstanceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/datatypes/LaunchInstanceDetails).
        """
        return pulumi.get(self, "is_pv_encryption_in_transit_enabled")

    @property
    @pulumi.getter(name="launchMode")
    def launch_mode(self) -> str:
        """
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.
        """
        return pulumi.get(self, "launch_mode")

    @property
    @pulumi.getter(name="launchOptions")
    def launch_options(self) -> Sequence['outputs.GetInstanceLaunchOptionResult']:
        """
        Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.
        """
        return pulumi.get(self, "launch_options")

    @property
    @pulumi.getter(name="launchVolumeAttachments")
    def launch_volume_attachments(self) -> Sequence['outputs.GetInstanceLaunchVolumeAttachmentResult']:
        return pulumi.get(self, "launch_volume_attachments")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, Any]:
        """
        Custom metadata that you provide.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="platformConfigs")
    def platform_configs(self) -> Sequence['outputs.GetInstancePlatformConfigResult']:
        """
        The platform configuration for the instance.
        """
        return pulumi.get(self, "platform_configs")

    @property
    @pulumi.getter(name="preemptibleInstanceConfigs")
    def preemptible_instance_configs(self) -> Sequence['outputs.GetInstancePreemptibleInstanceConfigResult']:
        """
        (Optional) Configuration options for preemptible instances.
        """
        return pulumi.get(self, "preemptible_instance_configs")

    @property
    @pulumi.getter(name="preserveBootVolume")
    def preserve_boot_volume(self) -> bool:
        """
        (Optional) Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.
        """
        return pulumi.get(self, "preserve_boot_volume")

    @property
    @pulumi.getter(name="preserveDataVolumesCreatedAtLaunch")
    def preserve_data_volumes_created_at_launch(self) -> bool:
        return pulumi.get(self, "preserve_data_volumes_created_at_launch")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        """
        The private IP address of instance VNIC. To set the private IP address, use the `private_ip` argument in create_vnic_details.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        """
        The public IP address of instance VNIC (if enabled).
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region that contains the availability domain the instance is running in.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def shape(self) -> str:
        """
        The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. You can enumerate all available shapes by calling [ListShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/Shape/ListShapes).
        """
        return pulumi.get(self, "shape")

    @property
    @pulumi.getter(name="shapeConfigs")
    def shape_configs(self) -> Sequence['outputs.GetInstanceShapeConfigResult']:
        """
        The shape configuration for an instance. The shape configuration determines the resources allocated to an instance.
        """
        return pulumi.get(self, "shape_configs")

    @property
    @pulumi.getter(name="sourceDetails")
    def source_details(self) -> Sequence['outputs.GetInstanceSourceDetailResult']:
        return pulumi.get(self, "source_details")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        warnings.warn("""The 'subnet_id' field has been deprecated. Please use 'subnet_id under create_vnic_details' instead.""", DeprecationWarning)
        pulumi.log.warn("""subnet_id is deprecated: The 'subnet_id' field has been deprecated. Please use 'subnet_id under create_vnic_details' instead.""")

        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the instance was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeMaintenanceRebootDue")
    def time_maintenance_reboot_due(self) -> str:
        """
        The date and time the instance is expected to be stopped / started,  in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339). After that time if instance hasn't been rebooted, Oracle will reboot the instance within 24 hours of the due time. Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state. Example: `2018-05-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_maintenance_reboot_due")

    @property
    @pulumi.getter(name="updateOperationConstraint")
    def update_operation_constraint(self) -> str:
        return pulumi.get(self, "update_operation_constraint")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            agent_configs=self.agent_configs,
            async_=self.async_,
            availability_configs=self.availability_configs,
            availability_domain=self.availability_domain,
            boot_volume_id=self.boot_volume_id,
            capacity_reservation_id=self.capacity_reservation_id,
            cluster_placement_group_id=self.cluster_placement_group_id,
            compartment_id=self.compartment_id,
            compute_cluster_id=self.compute_cluster_id,
            create_vnic_details=self.create_vnic_details,
            dedicated_vm_host_id=self.dedicated_vm_host_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            extended_metadata=self.extended_metadata,
            fault_domain=self.fault_domain,
            freeform_tags=self.freeform_tags,
            hostname_label=self.hostname_label,
            id=self.id,
            image=self.image,
            instance_configuration_id=self.instance_configuration_id,
            instance_id=self.instance_id,
            instance_options=self.instance_options,
            ipxe_script=self.ipxe_script,
            is_cross_numa_node=self.is_cross_numa_node,
            is_pv_encryption_in_transit_enabled=self.is_pv_encryption_in_transit_enabled,
            launch_mode=self.launch_mode,
            launch_options=self.launch_options,
            launch_volume_attachments=self.launch_volume_attachments,
            metadata=self.metadata,
            platform_configs=self.platform_configs,
            preemptible_instance_configs=self.preemptible_instance_configs,
            preserve_boot_volume=self.preserve_boot_volume,
            preserve_data_volumes_created_at_launch=self.preserve_data_volumes_created_at_launch,
            private_ip=self.private_ip,
            public_ip=self.public_ip,
            region=self.region,
            shape=self.shape,
            shape_configs=self.shape_configs,
            source_details=self.source_details,
            state=self.state,
            subnet_id=self.subnet_id,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_maintenance_reboot_due=self.time_maintenance_reboot_due,
            update_operation_constraint=self.update_operation_constraint)


def get_instance(instance_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    This data source provides details about a specific Instance resource in Oracle Cloud Infrastructure Core service.

    Gets information about the specified instance.

    **Note:** To retrieve public and private IP addresses for an instance, use the [ListVnicAttachments](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
    operation to get the VNIC ID for the instance, and then call [GetVnic](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/Vnic/GetVnic) with the VNIC ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_instance = oci.Core.get_instance(instance_id=test_instance_oci_core_instance["id"])
    ```


    :param str instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        agent_configs=pulumi.get(__ret__, 'agent_configs'),
        async_=pulumi.get(__ret__, 'async_'),
        availability_configs=pulumi.get(__ret__, 'availability_configs'),
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        boot_volume_id=pulumi.get(__ret__, 'boot_volume_id'),
        capacity_reservation_id=pulumi.get(__ret__, 'capacity_reservation_id'),
        cluster_placement_group_id=pulumi.get(__ret__, 'cluster_placement_group_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compute_cluster_id=pulumi.get(__ret__, 'compute_cluster_id'),
        create_vnic_details=pulumi.get(__ret__, 'create_vnic_details'),
        dedicated_vm_host_id=pulumi.get(__ret__, 'dedicated_vm_host_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        extended_metadata=pulumi.get(__ret__, 'extended_metadata'),
        fault_domain=pulumi.get(__ret__, 'fault_domain'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        hostname_label=pulumi.get(__ret__, 'hostname_label'),
        id=pulumi.get(__ret__, 'id'),
        image=pulumi.get(__ret__, 'image'),
        instance_configuration_id=pulumi.get(__ret__, 'instance_configuration_id'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        instance_options=pulumi.get(__ret__, 'instance_options'),
        ipxe_script=pulumi.get(__ret__, 'ipxe_script'),
        is_cross_numa_node=pulumi.get(__ret__, 'is_cross_numa_node'),
        is_pv_encryption_in_transit_enabled=pulumi.get(__ret__, 'is_pv_encryption_in_transit_enabled'),
        launch_mode=pulumi.get(__ret__, 'launch_mode'),
        launch_options=pulumi.get(__ret__, 'launch_options'),
        launch_volume_attachments=pulumi.get(__ret__, 'launch_volume_attachments'),
        metadata=pulumi.get(__ret__, 'metadata'),
        platform_configs=pulumi.get(__ret__, 'platform_configs'),
        preemptible_instance_configs=pulumi.get(__ret__, 'preemptible_instance_configs'),
        preserve_boot_volume=pulumi.get(__ret__, 'preserve_boot_volume'),
        preserve_data_volumes_created_at_launch=pulumi.get(__ret__, 'preserve_data_volumes_created_at_launch'),
        private_ip=pulumi.get(__ret__, 'private_ip'),
        public_ip=pulumi.get(__ret__, 'public_ip'),
        region=pulumi.get(__ret__, 'region'),
        shape=pulumi.get(__ret__, 'shape'),
        shape_configs=pulumi.get(__ret__, 'shape_configs'),
        source_details=pulumi.get(__ret__, 'source_details'),
        state=pulumi.get(__ret__, 'state'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_maintenance_reboot_due=pulumi.get(__ret__, 'time_maintenance_reboot_due'),
        update_operation_constraint=pulumi.get(__ret__, 'update_operation_constraint'))


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    This data source provides details about a specific Instance resource in Oracle Cloud Infrastructure Core service.

    Gets information about the specified instance.

    **Note:** To retrieve public and private IP addresses for an instance, use the [ListVnicAttachments](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
    operation to get the VNIC ID for the instance, and then call [GetVnic](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/Vnic/GetVnic) with the VNIC ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_instance = oci.Core.get_instance(instance_id=test_instance_oci_core_instance["id"])
    ```


    :param str instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
    """
    ...
