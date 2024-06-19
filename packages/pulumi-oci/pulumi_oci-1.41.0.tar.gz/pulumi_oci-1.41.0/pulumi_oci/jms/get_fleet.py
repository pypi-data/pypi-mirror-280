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
    'GetFleetResult',
    'AwaitableGetFleetResult',
    'get_fleet',
    'get_fleet_output',
]

@pulumi.output_type
class GetFleetResult:
    """
    A collection of values returned by getFleet.
    """
    def __init__(__self__, approximate_application_count=None, approximate_installation_count=None, approximate_java_server_count=None, approximate_jre_count=None, approximate_managed_instance_count=None, compartment_id=None, defined_tags=None, description=None, display_name=None, fleet_id=None, freeform_tags=None, id=None, inventory_logs=None, is_advanced_features_enabled=None, is_export_setting_enabled=None, operation_logs=None, state=None, system_tags=None, time_created=None):
        if approximate_application_count and not isinstance(approximate_application_count, int):
            raise TypeError("Expected argument 'approximate_application_count' to be a int")
        pulumi.set(__self__, "approximate_application_count", approximate_application_count)
        if approximate_installation_count and not isinstance(approximate_installation_count, int):
            raise TypeError("Expected argument 'approximate_installation_count' to be a int")
        pulumi.set(__self__, "approximate_installation_count", approximate_installation_count)
        if approximate_java_server_count and not isinstance(approximate_java_server_count, int):
            raise TypeError("Expected argument 'approximate_java_server_count' to be a int")
        pulumi.set(__self__, "approximate_java_server_count", approximate_java_server_count)
        if approximate_jre_count and not isinstance(approximate_jre_count, int):
            raise TypeError("Expected argument 'approximate_jre_count' to be a int")
        pulumi.set(__self__, "approximate_jre_count", approximate_jre_count)
        if approximate_managed_instance_count and not isinstance(approximate_managed_instance_count, int):
            raise TypeError("Expected argument 'approximate_managed_instance_count' to be a int")
        pulumi.set(__self__, "approximate_managed_instance_count", approximate_managed_instance_count)
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
        if fleet_id and not isinstance(fleet_id, str):
            raise TypeError("Expected argument 'fleet_id' to be a str")
        pulumi.set(__self__, "fleet_id", fleet_id)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inventory_logs and not isinstance(inventory_logs, list):
            raise TypeError("Expected argument 'inventory_logs' to be a list")
        pulumi.set(__self__, "inventory_logs", inventory_logs)
        if is_advanced_features_enabled and not isinstance(is_advanced_features_enabled, bool):
            raise TypeError("Expected argument 'is_advanced_features_enabled' to be a bool")
        pulumi.set(__self__, "is_advanced_features_enabled", is_advanced_features_enabled)
        if is_export_setting_enabled and not isinstance(is_export_setting_enabled, bool):
            raise TypeError("Expected argument 'is_export_setting_enabled' to be a bool")
        pulumi.set(__self__, "is_export_setting_enabled", is_export_setting_enabled)
        if operation_logs and not isinstance(operation_logs, list):
            raise TypeError("Expected argument 'operation_logs' to be a list")
        pulumi.set(__self__, "operation_logs", operation_logs)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)

    @property
    @pulumi.getter(name="approximateApplicationCount")
    def approximate_application_count(self) -> int:
        """
        The approximate count of all unique applications in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
        """
        return pulumi.get(self, "approximate_application_count")

    @property
    @pulumi.getter(name="approximateInstallationCount")
    def approximate_installation_count(self) -> int:
        """
        The approximate count of all unique Java installations in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
        """
        return pulumi.get(self, "approximate_installation_count")

    @property
    @pulumi.getter(name="approximateJavaServerCount")
    def approximate_java_server_count(self) -> int:
        """
        The approximate count of all unique Java servers in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
        """
        return pulumi.get(self, "approximate_java_server_count")

    @property
    @pulumi.getter(name="approximateJreCount")
    def approximate_jre_count(self) -> int:
        """
        The approximate count of all unique Java Runtimes in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
        """
        return pulumi.get(self, "approximate_jre_count")

    @property
    @pulumi.getter(name="approximateManagedInstanceCount")
    def approximate_managed_instance_count(self) -> int:
        """
        The approximate count of all unique managed instances in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
        """
        return pulumi.get(self, "approximate_managed_instance_count")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment of the Fleet.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. (See [Understanding Free-form Tags](https://docs.cloud.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The Fleet's description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The name of the Fleet.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> str:
        return pulumi.get(self, "fleet_id")

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
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Fleet.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inventoryLogs")
    def inventory_logs(self) -> Sequence['outputs.GetFleetInventoryLogResult']:
        """
        Custom Log for inventory or operation log.
        """
        return pulumi.get(self, "inventory_logs")

    @property
    @pulumi.getter(name="isAdvancedFeaturesEnabled")
    def is_advanced_features_enabled(self) -> bool:
        """
        Whether or not advanced features are enabled in this Fleet. Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.
        """
        return pulumi.get(self, "is_advanced_features_enabled")

    @property
    @pulumi.getter(name="isExportSettingEnabled")
    def is_export_setting_enabled(self) -> bool:
        """
        Whether or not export setting is enabled in this Fleet.
        """
        return pulumi.get(self, "is_export_setting_enabled")

    @property
    @pulumi.getter(name="operationLogs")
    def operation_logs(self) -> Sequence['outputs.GetFleetOperationLogResult']:
        """
        Custom Log for inventory or operation log.
        """
        return pulumi.get(self, "operation_logs")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The lifecycle state of the Fleet.
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
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The creation date and time of the Fleet (formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).
        """
        return pulumi.get(self, "time_created")


class AwaitableGetFleetResult(GetFleetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetResult(
            approximate_application_count=self.approximate_application_count,
            approximate_installation_count=self.approximate_installation_count,
            approximate_java_server_count=self.approximate_java_server_count,
            approximate_jre_count=self.approximate_jre_count,
            approximate_managed_instance_count=self.approximate_managed_instance_count,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            fleet_id=self.fleet_id,
            freeform_tags=self.freeform_tags,
            id=self.id,
            inventory_logs=self.inventory_logs,
            is_advanced_features_enabled=self.is_advanced_features_enabled,
            is_export_setting_enabled=self.is_export_setting_enabled,
            operation_logs=self.operation_logs,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created)


def get_fleet(fleet_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetResult:
    """
    This data source provides details about a specific Fleet resource in Oracle Cloud Infrastructure Jms service.

    Retrieve a Fleet with the specified identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fleet = oci.Jms.get_fleet(fleet_id=test_fleet_oci_jms_fleet["id"])
    ```


    :param str fleet_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Fleet.
    """
    __args__ = dict()
    __args__['fleetId'] = fleet_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Jms/getFleet:getFleet', __args__, opts=opts, typ=GetFleetResult).value

    return AwaitableGetFleetResult(
        approximate_application_count=pulumi.get(__ret__, 'approximate_application_count'),
        approximate_installation_count=pulumi.get(__ret__, 'approximate_installation_count'),
        approximate_java_server_count=pulumi.get(__ret__, 'approximate_java_server_count'),
        approximate_jre_count=pulumi.get(__ret__, 'approximate_jre_count'),
        approximate_managed_instance_count=pulumi.get(__ret__, 'approximate_managed_instance_count'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        fleet_id=pulumi.get(__ret__, 'fleet_id'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        inventory_logs=pulumi.get(__ret__, 'inventory_logs'),
        is_advanced_features_enabled=pulumi.get(__ret__, 'is_advanced_features_enabled'),
        is_export_setting_enabled=pulumi.get(__ret__, 'is_export_setting_enabled'),
        operation_logs=pulumi.get(__ret__, 'operation_logs'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'))


@_utilities.lift_output_func(get_fleet)
def get_fleet_output(fleet_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFleetResult]:
    """
    This data source provides details about a specific Fleet resource in Oracle Cloud Infrastructure Jms service.

    Retrieve a Fleet with the specified identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fleet = oci.Jms.get_fleet(fleet_id=test_fleet_oci_jms_fleet["id"])
    ```


    :param str fleet_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Fleet.
    """
    ...
