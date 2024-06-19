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
    'GetAtCustomerCccInfrastructureResult',
    'AwaitableGetAtCustomerCccInfrastructureResult',
    'get_at_customer_ccc_infrastructure',
    'get_at_customer_ccc_infrastructure_output',
]

@pulumi.output_type
class GetAtCustomerCccInfrastructureResult:
    """
    A collection of values returned by getAtCustomerCccInfrastructure.
    """
    def __init__(__self__, ccc_infrastructure_id=None, ccc_upgrade_schedule_id=None, compartment_id=None, connection_details=None, connection_state=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, infrastructure_inventories=None, infrastructure_network_configurations=None, lifecycle_details=None, provisioning_fingerprint=None, provisioning_pin=None, short_name=None, state=None, subnet_id=None, system_tags=None, time_created=None, time_updated=None, upgrade_informations=None):
        if ccc_infrastructure_id and not isinstance(ccc_infrastructure_id, str):
            raise TypeError("Expected argument 'ccc_infrastructure_id' to be a str")
        pulumi.set(__self__, "ccc_infrastructure_id", ccc_infrastructure_id)
        if ccc_upgrade_schedule_id and not isinstance(ccc_upgrade_schedule_id, str):
            raise TypeError("Expected argument 'ccc_upgrade_schedule_id' to be a str")
        pulumi.set(__self__, "ccc_upgrade_schedule_id", ccc_upgrade_schedule_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if connection_details and not isinstance(connection_details, str):
            raise TypeError("Expected argument 'connection_details' to be a str")
        pulumi.set(__self__, "connection_details", connection_details)
        if connection_state and not isinstance(connection_state, str):
            raise TypeError("Expected argument 'connection_state' to be a str")
        pulumi.set(__self__, "connection_state", connection_state)
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
        if infrastructure_inventories and not isinstance(infrastructure_inventories, list):
            raise TypeError("Expected argument 'infrastructure_inventories' to be a list")
        pulumi.set(__self__, "infrastructure_inventories", infrastructure_inventories)
        if infrastructure_network_configurations and not isinstance(infrastructure_network_configurations, list):
            raise TypeError("Expected argument 'infrastructure_network_configurations' to be a list")
        pulumi.set(__self__, "infrastructure_network_configurations", infrastructure_network_configurations)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if provisioning_fingerprint and not isinstance(provisioning_fingerprint, str):
            raise TypeError("Expected argument 'provisioning_fingerprint' to be a str")
        pulumi.set(__self__, "provisioning_fingerprint", provisioning_fingerprint)
        if provisioning_pin and not isinstance(provisioning_pin, str):
            raise TypeError("Expected argument 'provisioning_pin' to be a str")
        pulumi.set(__self__, "provisioning_pin", provisioning_pin)
        if short_name and not isinstance(short_name, str):
            raise TypeError("Expected argument 'short_name' to be a str")
        pulumi.set(__self__, "short_name", short_name)
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
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if upgrade_informations and not isinstance(upgrade_informations, list):
            raise TypeError("Expected argument 'upgrade_informations' to be a list")
        pulumi.set(__self__, "upgrade_informations", upgrade_informations)

    @property
    @pulumi.getter(name="cccInfrastructureId")
    def ccc_infrastructure_id(self) -> str:
        return pulumi.get(self, "ccc_infrastructure_id")

    @property
    @pulumi.getter(name="cccUpgradeScheduleId")
    def ccc_upgrade_schedule_id(self) -> str:
        """
        Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.
        """
        return pulumi.get(self, "ccc_upgrade_schedule_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The infrastructure compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="connectionDetails")
    def connection_details(self) -> str:
        """
        A message describing the current connection state in more detail.
        """
        return pulumi.get(self, "connection_details")

    @property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> str:
        """
        The current connection state of the infrastructure. A user can only update it from REQUEST to READY or from any state back to REJECT. The system automatically handles the REJECT to REQUEST, READY to CONNECTED, or CONNECTED to DISCONNECTED transitions.
        """
        return pulumi.get(self, "connection_state")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure. Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The name that will be used to display the Compute Cloud@Customer infrastructure in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

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
        The Compute Cloud@Customer infrastructure [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This cannot be changed once created.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="infrastructureInventories")
    def infrastructure_inventories(self) -> Sequence['outputs.GetAtCustomerCccInfrastructureInfrastructureInventoryResult']:
        """
        Inventory for a Compute Cloud@Customer infrastructure. This information cannot be updated and is from the infrastructure. The information will only be available after the connectionState is transitioned to CONNECTED.
        """
        return pulumi.get(self, "infrastructure_inventories")

    @property
    @pulumi.getter(name="infrastructureNetworkConfigurations")
    def infrastructure_network_configurations(self) -> Sequence['outputs.GetAtCustomerCccInfrastructureInfrastructureNetworkConfigurationResult']:
        """
        Configuration information for the Compute Cloud@Customer infrastructure. This  network configuration information cannot be updated and is retrieved from the data center. The information will only be available after the connectionState is transitioned to CONNECTED.
        """
        return pulumi.get(self, "infrastructure_network_configurations")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current lifecycle state in more detail. For example, this can be used to provide actionable information for a resource that is in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="provisioningFingerprint")
    def provisioning_fingerprint(self) -> str:
        """
        Fingerprint of a Compute Cloud@Customer infrastructure in a data center generated during the initial connection to this resource. The fingerprint should be verified by the administrator when changing the connectionState from REQUEST to READY.
        """
        return pulumi.get(self, "provisioning_fingerprint")

    @property
    @pulumi.getter(name="provisioningPin")
    def provisioning_pin(self) -> str:
        """
        Code that is required for service personnel to connect a Compute Cloud@Customer infrastructure in a data center to this resource. This code will only be available when the connectionState is REJECT (usually at create time of the Compute Cloud@Customer infrastructure).
        """
        return pulumi.get(self, "provisioning_pin")

    @property
    @pulumi.getter(name="shortName")
    def short_name(self) -> str:
        """
        The Compute Cloud@Customer infrastructure short name. This cannot be changed once created. The short name is used to refer to the infrastructure in several contexts and is unique.
        """
        return pulumi.get(self, "short_name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Compute Cloud@Customer infrastructure.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the network subnet that is used to communicate with Compute Cloud@Customer infrastructure.
        """
        return pulumi.get(self, "subnet_id")

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
        Compute Cloud@Customer infrastructure creation date and time, using an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        Compute Cloud@Customer infrastructure updated date and time, using an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="upgradeInformations")
    def upgrade_informations(self) -> Sequence['outputs.GetAtCustomerCccInfrastructureUpgradeInformationResult']:
        """
        Upgrade information that relates to a Compute Cloud@Customer infrastructure. This information cannot be updated.
        """
        return pulumi.get(self, "upgrade_informations")


class AwaitableGetAtCustomerCccInfrastructureResult(GetAtCustomerCccInfrastructureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAtCustomerCccInfrastructureResult(
            ccc_infrastructure_id=self.ccc_infrastructure_id,
            ccc_upgrade_schedule_id=self.ccc_upgrade_schedule_id,
            compartment_id=self.compartment_id,
            connection_details=self.connection_details,
            connection_state=self.connection_state,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            infrastructure_inventories=self.infrastructure_inventories,
            infrastructure_network_configurations=self.infrastructure_network_configurations,
            lifecycle_details=self.lifecycle_details,
            provisioning_fingerprint=self.provisioning_fingerprint,
            provisioning_pin=self.provisioning_pin,
            short_name=self.short_name,
            state=self.state,
            subnet_id=self.subnet_id,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            upgrade_informations=self.upgrade_informations)


def get_at_customer_ccc_infrastructure(ccc_infrastructure_id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAtCustomerCccInfrastructureResult:
    """
    This data source provides details about a specific Ccc Infrastructure resource in Oracle Cloud Infrastructure Compute Cloud At Customer service.

    Gets a Compute Cloud@Customer infrastructure using the infrastructure
    [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ccc_infrastructure = oci.ComputeCloud.get_at_customer_ccc_infrastructure(ccc_infrastructure_id=test_ccc_infrastructure_oci_compute_cloud_at_customer_ccc_infrastructure["id"])
    ```


    :param str ccc_infrastructure_id: An [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for a  Compute Cloud@Customer Infrastructure.
    """
    __args__ = dict()
    __args__['cccInfrastructureId'] = ccc_infrastructure_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ComputeCloud/getAtCustomerCccInfrastructure:getAtCustomerCccInfrastructure', __args__, opts=opts, typ=GetAtCustomerCccInfrastructureResult).value

    return AwaitableGetAtCustomerCccInfrastructureResult(
        ccc_infrastructure_id=pulumi.get(__ret__, 'ccc_infrastructure_id'),
        ccc_upgrade_schedule_id=pulumi.get(__ret__, 'ccc_upgrade_schedule_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        connection_details=pulumi.get(__ret__, 'connection_details'),
        connection_state=pulumi.get(__ret__, 'connection_state'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        infrastructure_inventories=pulumi.get(__ret__, 'infrastructure_inventories'),
        infrastructure_network_configurations=pulumi.get(__ret__, 'infrastructure_network_configurations'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        provisioning_fingerprint=pulumi.get(__ret__, 'provisioning_fingerprint'),
        provisioning_pin=pulumi.get(__ret__, 'provisioning_pin'),
        short_name=pulumi.get(__ret__, 'short_name'),
        state=pulumi.get(__ret__, 'state'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        upgrade_informations=pulumi.get(__ret__, 'upgrade_informations'))


@_utilities.lift_output_func(get_at_customer_ccc_infrastructure)
def get_at_customer_ccc_infrastructure_output(ccc_infrastructure_id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAtCustomerCccInfrastructureResult]:
    """
    This data source provides details about a specific Ccc Infrastructure resource in Oracle Cloud Infrastructure Compute Cloud At Customer service.

    Gets a Compute Cloud@Customer infrastructure using the infrastructure
    [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ccc_infrastructure = oci.ComputeCloud.get_at_customer_ccc_infrastructure(ccc_infrastructure_id=test_ccc_infrastructure_oci_compute_cloud_at_customer_ccc_infrastructure["id"])
    ```


    :param str ccc_infrastructure_id: An [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for a  Compute Cloud@Customer Infrastructure.
    """
    ...
