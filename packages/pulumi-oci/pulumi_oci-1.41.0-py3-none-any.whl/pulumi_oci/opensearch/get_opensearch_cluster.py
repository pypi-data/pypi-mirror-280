# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetOpensearchClusterResult',
    'AwaitableGetOpensearchClusterResult',
    'get_opensearch_cluster',
    'get_opensearch_cluster_output',
]

@pulumi.output_type
class GetOpensearchClusterResult:
    """
    A collection of values returned by getOpensearchCluster.
    """
    def __init__(__self__, availability_domains=None, compartment_id=None, data_node_count=None, data_node_host_bare_metal_shape=None, data_node_host_memory_gb=None, data_node_host_ocpu_count=None, data_node_host_type=None, data_node_storage_gb=None, defined_tags=None, display_name=None, fqdn=None, freeform_tags=None, id=None, lifecycle_details=None, master_node_count=None, master_node_host_bare_metal_shape=None, master_node_host_memory_gb=None, master_node_host_ocpu_count=None, master_node_host_type=None, opendashboard_fqdn=None, opendashboard_node_count=None, opendashboard_node_host_memory_gb=None, opendashboard_node_host_ocpu_count=None, opendashboard_private_ip=None, opensearch_cluster_id=None, opensearch_fqdn=None, opensearch_private_ip=None, security_master_user_name=None, security_master_user_password_hash=None, security_mode=None, software_version=None, state=None, subnet_compartment_id=None, subnet_id=None, system_tags=None, time_created=None, time_deleted=None, time_updated=None, total_storage_gb=None, vcn_compartment_id=None, vcn_id=None):
        if availability_domains and not isinstance(availability_domains, list):
            raise TypeError("Expected argument 'availability_domains' to be a list")
        pulumi.set(__self__, "availability_domains", availability_domains)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if data_node_count and not isinstance(data_node_count, int):
            raise TypeError("Expected argument 'data_node_count' to be a int")
        pulumi.set(__self__, "data_node_count", data_node_count)
        if data_node_host_bare_metal_shape and not isinstance(data_node_host_bare_metal_shape, str):
            raise TypeError("Expected argument 'data_node_host_bare_metal_shape' to be a str")
        pulumi.set(__self__, "data_node_host_bare_metal_shape", data_node_host_bare_metal_shape)
        if data_node_host_memory_gb and not isinstance(data_node_host_memory_gb, int):
            raise TypeError("Expected argument 'data_node_host_memory_gb' to be a int")
        pulumi.set(__self__, "data_node_host_memory_gb", data_node_host_memory_gb)
        if data_node_host_ocpu_count and not isinstance(data_node_host_ocpu_count, int):
            raise TypeError("Expected argument 'data_node_host_ocpu_count' to be a int")
        pulumi.set(__self__, "data_node_host_ocpu_count", data_node_host_ocpu_count)
        if data_node_host_type and not isinstance(data_node_host_type, str):
            raise TypeError("Expected argument 'data_node_host_type' to be a str")
        pulumi.set(__self__, "data_node_host_type", data_node_host_type)
        if data_node_storage_gb and not isinstance(data_node_storage_gb, int):
            raise TypeError("Expected argument 'data_node_storage_gb' to be a int")
        pulumi.set(__self__, "data_node_storage_gb", data_node_storage_gb)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if master_node_count and not isinstance(master_node_count, int):
            raise TypeError("Expected argument 'master_node_count' to be a int")
        pulumi.set(__self__, "master_node_count", master_node_count)
        if master_node_host_bare_metal_shape and not isinstance(master_node_host_bare_metal_shape, str):
            raise TypeError("Expected argument 'master_node_host_bare_metal_shape' to be a str")
        pulumi.set(__self__, "master_node_host_bare_metal_shape", master_node_host_bare_metal_shape)
        if master_node_host_memory_gb and not isinstance(master_node_host_memory_gb, int):
            raise TypeError("Expected argument 'master_node_host_memory_gb' to be a int")
        pulumi.set(__self__, "master_node_host_memory_gb", master_node_host_memory_gb)
        if master_node_host_ocpu_count and not isinstance(master_node_host_ocpu_count, int):
            raise TypeError("Expected argument 'master_node_host_ocpu_count' to be a int")
        pulumi.set(__self__, "master_node_host_ocpu_count", master_node_host_ocpu_count)
        if master_node_host_type and not isinstance(master_node_host_type, str):
            raise TypeError("Expected argument 'master_node_host_type' to be a str")
        pulumi.set(__self__, "master_node_host_type", master_node_host_type)
        if opendashboard_fqdn and not isinstance(opendashboard_fqdn, str):
            raise TypeError("Expected argument 'opendashboard_fqdn' to be a str")
        pulumi.set(__self__, "opendashboard_fqdn", opendashboard_fqdn)
        if opendashboard_node_count and not isinstance(opendashboard_node_count, int):
            raise TypeError("Expected argument 'opendashboard_node_count' to be a int")
        pulumi.set(__self__, "opendashboard_node_count", opendashboard_node_count)
        if opendashboard_node_host_memory_gb and not isinstance(opendashboard_node_host_memory_gb, int):
            raise TypeError("Expected argument 'opendashboard_node_host_memory_gb' to be a int")
        pulumi.set(__self__, "opendashboard_node_host_memory_gb", opendashboard_node_host_memory_gb)
        if opendashboard_node_host_ocpu_count and not isinstance(opendashboard_node_host_ocpu_count, int):
            raise TypeError("Expected argument 'opendashboard_node_host_ocpu_count' to be a int")
        pulumi.set(__self__, "opendashboard_node_host_ocpu_count", opendashboard_node_host_ocpu_count)
        if opendashboard_private_ip and not isinstance(opendashboard_private_ip, str):
            raise TypeError("Expected argument 'opendashboard_private_ip' to be a str")
        pulumi.set(__self__, "opendashboard_private_ip", opendashboard_private_ip)
        if opensearch_cluster_id and not isinstance(opensearch_cluster_id, str):
            raise TypeError("Expected argument 'opensearch_cluster_id' to be a str")
        pulumi.set(__self__, "opensearch_cluster_id", opensearch_cluster_id)
        if opensearch_fqdn and not isinstance(opensearch_fqdn, str):
            raise TypeError("Expected argument 'opensearch_fqdn' to be a str")
        pulumi.set(__self__, "opensearch_fqdn", opensearch_fqdn)
        if opensearch_private_ip and not isinstance(opensearch_private_ip, str):
            raise TypeError("Expected argument 'opensearch_private_ip' to be a str")
        pulumi.set(__self__, "opensearch_private_ip", opensearch_private_ip)
        if security_master_user_name and not isinstance(security_master_user_name, str):
            raise TypeError("Expected argument 'security_master_user_name' to be a str")
        pulumi.set(__self__, "security_master_user_name", security_master_user_name)
        if security_master_user_password_hash and not isinstance(security_master_user_password_hash, str):
            raise TypeError("Expected argument 'security_master_user_password_hash' to be a str")
        pulumi.set(__self__, "security_master_user_password_hash", security_master_user_password_hash)
        if security_mode and not isinstance(security_mode, str):
            raise TypeError("Expected argument 'security_mode' to be a str")
        pulumi.set(__self__, "security_mode", security_mode)
        if software_version and not isinstance(software_version, str):
            raise TypeError("Expected argument 'software_version' to be a str")
        pulumi.set(__self__, "software_version", software_version)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_compartment_id and not isinstance(subnet_compartment_id, str):
            raise TypeError("Expected argument 'subnet_compartment_id' to be a str")
        pulumi.set(__self__, "subnet_compartment_id", subnet_compartment_id)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_deleted and not isinstance(time_deleted, str):
            raise TypeError("Expected argument 'time_deleted' to be a str")
        pulumi.set(__self__, "time_deleted", time_deleted)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if total_storage_gb and not isinstance(total_storage_gb, int):
            raise TypeError("Expected argument 'total_storage_gb' to be a int")
        pulumi.set(__self__, "total_storage_gb", total_storage_gb)
        if vcn_compartment_id and not isinstance(vcn_compartment_id, str):
            raise TypeError("Expected argument 'vcn_compartment_id' to be a str")
        pulumi.set(__self__, "vcn_compartment_id", vcn_compartment_id)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)

    @property
    @pulumi.getter(name="availabilityDomains")
    def availability_domains(self) -> Sequence[str]:
        """
        The availability domains to distribute the cluser nodes across.
        """
        return pulumi.get(self, "availability_domains")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment where the cluster is located.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dataNodeCount")
    def data_node_count(self) -> int:
        """
        The number of data nodes configured for the cluster.
        """
        return pulumi.get(self, "data_node_count")

    @property
    @pulumi.getter(name="dataNodeHostBareMetalShape")
    def data_node_host_bare_metal_shape(self) -> str:
        """
        The bare metal shape for the cluster's data nodes.
        """
        return pulumi.get(self, "data_node_host_bare_metal_shape")

    @property
    @pulumi.getter(name="dataNodeHostMemoryGb")
    def data_node_host_memory_gb(self) -> int:
        """
        The amount of memory in GB, for the cluster's data nodes.
        """
        return pulumi.get(self, "data_node_host_memory_gb")

    @property
    @pulumi.getter(name="dataNodeHostOcpuCount")
    def data_node_host_ocpu_count(self) -> int:
        """
        The number of OCPUs configured for the cluster's data nodes.
        """
        return pulumi.get(self, "data_node_host_ocpu_count")

    @property
    @pulumi.getter(name="dataNodeHostType")
    def data_node_host_type(self) -> str:
        """
        The instance type for the cluster's data nodes.
        """
        return pulumi.get(self, "data_node_host_type")

    @property
    @pulumi.getter(name="dataNodeStorageGb")
    def data_node_storage_gb(self) -> int:
        """
        The amount of storage in GB, to configure per node for the cluster's data nodes.
        """
        return pulumi.get(self, "data_node_storage_gb")

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
        The name of the cluster. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The fully qualified domain name (FQDN) for the cluster's API endpoint.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state of the cluster.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="masterNodeCount")
    def master_node_count(self) -> int:
        """
        The number of master nodes configured for the cluster.
        """
        return pulumi.get(self, "master_node_count")

    @property
    @pulumi.getter(name="masterNodeHostBareMetalShape")
    def master_node_host_bare_metal_shape(self) -> str:
        """
        The bare metal shape for the cluster's master nodes.
        """
        return pulumi.get(self, "master_node_host_bare_metal_shape")

    @property
    @pulumi.getter(name="masterNodeHostMemoryGb")
    def master_node_host_memory_gb(self) -> int:
        """
        The amount of memory in GB, for the cluster's master nodes.
        """
        return pulumi.get(self, "master_node_host_memory_gb")

    @property
    @pulumi.getter(name="masterNodeHostOcpuCount")
    def master_node_host_ocpu_count(self) -> int:
        """
        The number of OCPUs configured for cluster's master nodes.
        """
        return pulumi.get(self, "master_node_host_ocpu_count")

    @property
    @pulumi.getter(name="masterNodeHostType")
    def master_node_host_type(self) -> str:
        """
        The instance type for the cluster's master nodes.
        """
        return pulumi.get(self, "master_node_host_type")

    @property
    @pulumi.getter(name="opendashboardFqdn")
    def opendashboard_fqdn(self) -> str:
        """
        The fully qualified domain name (FQDN) for the cluster's OpenSearch Dashboard API endpoint.
        """
        return pulumi.get(self, "opendashboard_fqdn")

    @property
    @pulumi.getter(name="opendashboardNodeCount")
    def opendashboard_node_count(self) -> int:
        """
        The number of OpenSearch Dashboard nodes configured for the cluster.
        """
        return pulumi.get(self, "opendashboard_node_count")

    @property
    @pulumi.getter(name="opendashboardNodeHostMemoryGb")
    def opendashboard_node_host_memory_gb(self) -> int:
        """
        The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.
        """
        return pulumi.get(self, "opendashboard_node_host_memory_gb")

    @property
    @pulumi.getter(name="opendashboardNodeHostOcpuCount")
    def opendashboard_node_host_ocpu_count(self) -> int:
        """
        The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.
        """
        return pulumi.get(self, "opendashboard_node_host_ocpu_count")

    @property
    @pulumi.getter(name="opendashboardPrivateIp")
    def opendashboard_private_ip(self) -> str:
        """
        The private IP address for the cluster's OpenSearch Dashboard.
        """
        return pulumi.get(self, "opendashboard_private_ip")

    @property
    @pulumi.getter(name="opensearchClusterId")
    def opensearch_cluster_id(self) -> str:
        return pulumi.get(self, "opensearch_cluster_id")

    @property
    @pulumi.getter(name="opensearchFqdn")
    def opensearch_fqdn(self) -> str:
        """
        The fully qualified domain name (FQDN) for the cluster's API endpoint.
        """
        return pulumi.get(self, "opensearch_fqdn")

    @property
    @pulumi.getter(name="opensearchPrivateIp")
    def opensearch_private_ip(self) -> str:
        """
        The cluster's private IP address.
        """
        return pulumi.get(self, "opensearch_private_ip")

    @property
    @pulumi.getter(name="securityMasterUserName")
    def security_master_user_name(self) -> str:
        """
        The name of the master user that are used to manage security config
        """
        return pulumi.get(self, "security_master_user_name")

    @property
    @pulumi.getter(name="securityMasterUserPasswordHash")
    def security_master_user_password_hash(self) -> str:
        """
        The password hash of the master user that are used to manage security config
        """
        return pulumi.get(self, "security_master_user_password_hash")

    @property
    @pulumi.getter(name="securityMode")
    def security_mode(self) -> str:
        """
        The security mode of the cluster.
        """
        return pulumi.get(self, "security_mode")

    @property
    @pulumi.getter(name="softwareVersion")
    def software_version(self) -> str:
        """
        The software version the cluster is running.
        """
        return pulumi.get(self, "software_version")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetCompartmentId")
    def subnet_compartment_id(self) -> str:
        """
        The OCID for the compartment where the cluster's subnet is located.
        """
        return pulumi.get(self, "subnet_compartment_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The OCID of the cluster's subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The amount of time in milliseconds since the cluster was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeDeleted")
    def time_deleted(self) -> str:
        """
        The amount of time in milliseconds since the cluster was updated.
        """
        return pulumi.get(self, "time_deleted")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The amount of time in milliseconds since the cluster was updated.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="totalStorageGb")
    def total_storage_gb(self) -> int:
        """
        The size in GB of the cluster's total storage.
        """
        return pulumi.get(self, "total_storage_gb")

    @property
    @pulumi.getter(name="vcnCompartmentId")
    def vcn_compartment_id(self) -> str:
        """
        The OCID for the compartment where the cluster's VCN is located.
        """
        return pulumi.get(self, "vcn_compartment_id")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> str:
        """
        The OCID of the cluster's VCN.
        """
        return pulumi.get(self, "vcn_id")


class AwaitableGetOpensearchClusterResult(GetOpensearchClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOpensearchClusterResult(
            availability_domains=self.availability_domains,
            compartment_id=self.compartment_id,
            data_node_count=self.data_node_count,
            data_node_host_bare_metal_shape=self.data_node_host_bare_metal_shape,
            data_node_host_memory_gb=self.data_node_host_memory_gb,
            data_node_host_ocpu_count=self.data_node_host_ocpu_count,
            data_node_host_type=self.data_node_host_type,
            data_node_storage_gb=self.data_node_storage_gb,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            fqdn=self.fqdn,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            master_node_count=self.master_node_count,
            master_node_host_bare_metal_shape=self.master_node_host_bare_metal_shape,
            master_node_host_memory_gb=self.master_node_host_memory_gb,
            master_node_host_ocpu_count=self.master_node_host_ocpu_count,
            master_node_host_type=self.master_node_host_type,
            opendashboard_fqdn=self.opendashboard_fqdn,
            opendashboard_node_count=self.opendashboard_node_count,
            opendashboard_node_host_memory_gb=self.opendashboard_node_host_memory_gb,
            opendashboard_node_host_ocpu_count=self.opendashboard_node_host_ocpu_count,
            opendashboard_private_ip=self.opendashboard_private_ip,
            opensearch_cluster_id=self.opensearch_cluster_id,
            opensearch_fqdn=self.opensearch_fqdn,
            opensearch_private_ip=self.opensearch_private_ip,
            security_master_user_name=self.security_master_user_name,
            security_master_user_password_hash=self.security_master_user_password_hash,
            security_mode=self.security_mode,
            software_version=self.software_version,
            state=self.state,
            subnet_compartment_id=self.subnet_compartment_id,
            subnet_id=self.subnet_id,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_deleted=self.time_deleted,
            time_updated=self.time_updated,
            total_storage_gb=self.total_storage_gb,
            vcn_compartment_id=self.vcn_compartment_id,
            vcn_id=self.vcn_id)


def get_opensearch_cluster(opensearch_cluster_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOpensearchClusterResult:
    """
    This data source provides details about a specific Opensearch Cluster resource in Oracle Cloud Infrastructure Opensearch service.

    Gets a OpensearchCluster by identifier

    ## Prerequisites

    The below policies must be created in compartment before creating OpensearchCluster

    ##### {Compartment-Name} - Name of  your compartment

    For latest documentation on OpenSearch use please refer to https://docs.oracle.com/en-us/iaas/Content/search-opensearch/home.htm\\
    Required permissions: https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Concepts/ocisearchpermissions.htm

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_opensearch_cluster = oci.Opensearch.get_opensearch_cluster(opensearch_cluster_id=test_opensearch_cluster_oci_opensearch_opensearch_cluster["id"])
    ```


    :param str opensearch_cluster_id: unique OpensearchCluster identifier
    """
    __args__ = dict()
    __args__['opensearchClusterId'] = opensearch_cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Opensearch/getOpensearchCluster:getOpensearchCluster', __args__, opts=opts, typ=GetOpensearchClusterResult).value

    return AwaitableGetOpensearchClusterResult(
        availability_domains=pulumi.get(__ret__, 'availability_domains'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        data_node_count=pulumi.get(__ret__, 'data_node_count'),
        data_node_host_bare_metal_shape=pulumi.get(__ret__, 'data_node_host_bare_metal_shape'),
        data_node_host_memory_gb=pulumi.get(__ret__, 'data_node_host_memory_gb'),
        data_node_host_ocpu_count=pulumi.get(__ret__, 'data_node_host_ocpu_count'),
        data_node_host_type=pulumi.get(__ret__, 'data_node_host_type'),
        data_node_storage_gb=pulumi.get(__ret__, 'data_node_storage_gb'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        master_node_count=pulumi.get(__ret__, 'master_node_count'),
        master_node_host_bare_metal_shape=pulumi.get(__ret__, 'master_node_host_bare_metal_shape'),
        master_node_host_memory_gb=pulumi.get(__ret__, 'master_node_host_memory_gb'),
        master_node_host_ocpu_count=pulumi.get(__ret__, 'master_node_host_ocpu_count'),
        master_node_host_type=pulumi.get(__ret__, 'master_node_host_type'),
        opendashboard_fqdn=pulumi.get(__ret__, 'opendashboard_fqdn'),
        opendashboard_node_count=pulumi.get(__ret__, 'opendashboard_node_count'),
        opendashboard_node_host_memory_gb=pulumi.get(__ret__, 'opendashboard_node_host_memory_gb'),
        opendashboard_node_host_ocpu_count=pulumi.get(__ret__, 'opendashboard_node_host_ocpu_count'),
        opendashboard_private_ip=pulumi.get(__ret__, 'opendashboard_private_ip'),
        opensearch_cluster_id=pulumi.get(__ret__, 'opensearch_cluster_id'),
        opensearch_fqdn=pulumi.get(__ret__, 'opensearch_fqdn'),
        opensearch_private_ip=pulumi.get(__ret__, 'opensearch_private_ip'),
        security_master_user_name=pulumi.get(__ret__, 'security_master_user_name'),
        security_master_user_password_hash=pulumi.get(__ret__, 'security_master_user_password_hash'),
        security_mode=pulumi.get(__ret__, 'security_mode'),
        software_version=pulumi.get(__ret__, 'software_version'),
        state=pulumi.get(__ret__, 'state'),
        subnet_compartment_id=pulumi.get(__ret__, 'subnet_compartment_id'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_deleted=pulumi.get(__ret__, 'time_deleted'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        total_storage_gb=pulumi.get(__ret__, 'total_storage_gb'),
        vcn_compartment_id=pulumi.get(__ret__, 'vcn_compartment_id'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'))


@_utilities.lift_output_func(get_opensearch_cluster)
def get_opensearch_cluster_output(opensearch_cluster_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOpensearchClusterResult]:
    """
    This data source provides details about a specific Opensearch Cluster resource in Oracle Cloud Infrastructure Opensearch service.

    Gets a OpensearchCluster by identifier

    ## Prerequisites

    The below policies must be created in compartment before creating OpensearchCluster

    ##### {Compartment-Name} - Name of  your compartment

    For latest documentation on OpenSearch use please refer to https://docs.oracle.com/en-us/iaas/Content/search-opensearch/home.htm\\
    Required permissions: https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Concepts/ocisearchpermissions.htm

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_opensearch_cluster = oci.Opensearch.get_opensearch_cluster(opensearch_cluster_id=test_opensearch_cluster_oci_opensearch_opensearch_cluster["id"])
    ```


    :param str opensearch_cluster_id: unique OpensearchCluster identifier
    """
    ...
