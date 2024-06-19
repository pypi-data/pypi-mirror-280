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
    'GetExternalAsmResult',
    'AwaitableGetExternalAsmResult',
    'get_external_asm',
    'get_external_asm_output',
]

@pulumi.output_type
class GetExternalAsmResult:
    """
    A collection of values returned by getExternalAsm.
    """
    def __init__(__self__, additional_details=None, compartment_id=None, component_name=None, defined_tags=None, display_name=None, external_asm_id=None, external_connector_id=None, external_db_system_id=None, freeform_tags=None, grid_home=None, id=None, is_cluster=None, is_flex_enabled=None, lifecycle_details=None, serviced_databases=None, state=None, system_tags=None, time_created=None, time_updated=None, version=None):
        if additional_details and not isinstance(additional_details, dict):
            raise TypeError("Expected argument 'additional_details' to be a dict")
        pulumi.set(__self__, "additional_details", additional_details)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if component_name and not isinstance(component_name, str):
            raise TypeError("Expected argument 'component_name' to be a str")
        pulumi.set(__self__, "component_name", component_name)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_asm_id and not isinstance(external_asm_id, str):
            raise TypeError("Expected argument 'external_asm_id' to be a str")
        pulumi.set(__self__, "external_asm_id", external_asm_id)
        if external_connector_id and not isinstance(external_connector_id, str):
            raise TypeError("Expected argument 'external_connector_id' to be a str")
        pulumi.set(__self__, "external_connector_id", external_connector_id)
        if external_db_system_id and not isinstance(external_db_system_id, str):
            raise TypeError("Expected argument 'external_db_system_id' to be a str")
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if grid_home and not isinstance(grid_home, str):
            raise TypeError("Expected argument 'grid_home' to be a str")
        pulumi.set(__self__, "grid_home", grid_home)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_cluster and not isinstance(is_cluster, bool):
            raise TypeError("Expected argument 'is_cluster' to be a bool")
        pulumi.set(__self__, "is_cluster", is_cluster)
        if is_flex_enabled and not isinstance(is_flex_enabled, bool):
            raise TypeError("Expected argument 'is_flex_enabled' to be a bool")
        pulumi.set(__self__, "is_flex_enabled", is_flex_enabled)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if serviced_databases and not isinstance(serviced_databases, list):
            raise TypeError("Expected argument 'serviced_databases' to be a list")
        pulumi.set(__self__, "serviced_databases", serviced_databases)
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
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Mapping[str, Any]:
        """
        The additional details of the external ASM defined in `{"key": "value"}` format. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "additional_details")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the external database resides.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> str:
        """
        The name of the external ASM.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-friendly name for the database. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalAsmId")
    def external_asm_id(self) -> str:
        return pulumi.get(self, "external_asm_id")

    @property
    @pulumi.getter(name="externalConnectorId")
    def external_connector_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
        """
        return pulumi.get(self, "external_connector_id")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="gridHome")
    def grid_home(self) -> str:
        """
        The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.
        """
        return pulumi.get(self, "grid_home")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external database.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCluster")
    def is_cluster(self) -> bool:
        """
        Indicates whether the ASM is a cluster ASM or not.
        """
        return pulumi.get(self, "is_cluster")

    @property
    @pulumi.getter(name="isFlexEnabled")
    def is_flex_enabled(self) -> bool:
        """
        Indicates whether Oracle Flex ASM is enabled or not.
        """
        return pulumi.get(self, "is_flex_enabled")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="servicedDatabases")
    def serviced_databases(self) -> Sequence['outputs.GetExternalAsmServicedDatabaseResult']:
        """
        The list of databases that are serviced by the ASM.
        """
        return pulumi.get(self, "serviced_databases")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of the external ASM.
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
        The date and time the external ASM was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the external ASM was last updated.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The ASM version.
        """
        return pulumi.get(self, "version")


class AwaitableGetExternalAsmResult(GetExternalAsmResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalAsmResult(
            additional_details=self.additional_details,
            compartment_id=self.compartment_id,
            component_name=self.component_name,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            external_asm_id=self.external_asm_id,
            external_connector_id=self.external_connector_id,
            external_db_system_id=self.external_db_system_id,
            freeform_tags=self.freeform_tags,
            grid_home=self.grid_home,
            id=self.id,
            is_cluster=self.is_cluster,
            is_flex_enabled=self.is_flex_enabled,
            lifecycle_details=self.lifecycle_details,
            serviced_databases=self.serviced_databases,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            version=self.version)


def get_external_asm(external_asm_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalAsmResult:
    """
    This data source provides details about a specific External Asm resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external ASM specified by `externalAsmId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_asm = oci.DatabaseManagement.get_external_asm(external_asm_id=test_external_asm_oci_database_management_external_asm["id"])
    ```


    :param str external_asm_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM.
    """
    __args__ = dict()
    __args__['externalAsmId'] = external_asm_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalAsm:getExternalAsm', __args__, opts=opts, typ=GetExternalAsmResult).value

    return AwaitableGetExternalAsmResult(
        additional_details=pulumi.get(__ret__, 'additional_details'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        component_name=pulumi.get(__ret__, 'component_name'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_asm_id=pulumi.get(__ret__, 'external_asm_id'),
        external_connector_id=pulumi.get(__ret__, 'external_connector_id'),
        external_db_system_id=pulumi.get(__ret__, 'external_db_system_id'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        grid_home=pulumi.get(__ret__, 'grid_home'),
        id=pulumi.get(__ret__, 'id'),
        is_cluster=pulumi.get(__ret__, 'is_cluster'),
        is_flex_enabled=pulumi.get(__ret__, 'is_flex_enabled'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        serviced_databases=pulumi.get(__ret__, 'serviced_databases'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_external_asm)
def get_external_asm_output(external_asm_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalAsmResult]:
    """
    This data source provides details about a specific External Asm resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external ASM specified by `externalAsmId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_asm = oci.DatabaseManagement.get_external_asm(external_asm_id=test_external_asm_oci_database_management_external_asm["id"])
    ```


    :param str external_asm_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external ASM.
    """
    ...
