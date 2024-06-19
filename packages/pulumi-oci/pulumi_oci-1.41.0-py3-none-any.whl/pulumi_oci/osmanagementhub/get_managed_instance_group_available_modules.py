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
from ._inputs import *

__all__ = [
    'GetManagedInstanceGroupAvailableModulesResult',
    'AwaitableGetManagedInstanceGroupAvailableModulesResult',
    'get_managed_instance_group_available_modules',
    'get_managed_instance_group_available_modules_output',
]

@pulumi.output_type
class GetManagedInstanceGroupAvailableModulesResult:
    """
    A collection of values returned by getManagedInstanceGroupAvailableModules.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, managed_instance_group_available_module_collections=None, managed_instance_group_id=None, name=None, name_contains=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_instance_group_available_module_collections and not isinstance(managed_instance_group_available_module_collections, list):
            raise TypeError("Expected argument 'managed_instance_group_available_module_collections' to be a list")
        pulumi.set(__self__, "managed_instance_group_available_module_collections", managed_instance_group_available_module_collections)
        if managed_instance_group_id and not isinstance(managed_instance_group_id, str):
            raise TypeError("Expected argument 'managed_instance_group_id' to be a str")
        pulumi.set(__self__, "managed_instance_group_id", managed_instance_group_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_contains and not isinstance(name_contains, str):
            raise TypeError("Expected argument 'name_contains' to be a str")
        pulumi.set(__self__, "name_contains", name_contains)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedInstanceGroupAvailableModulesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstanceGroupAvailableModuleCollections")
    def managed_instance_group_available_module_collections(self) -> Sequence['outputs.GetManagedInstanceGroupAvailableModulesManagedInstanceGroupAvailableModuleCollectionResult']:
        """
        The list of managed_instance_group_available_module_collection.
        """
        return pulumi.get(self, "managed_instance_group_available_module_collections")

    @property
    @pulumi.getter(name="managedInstanceGroupId")
    def managed_instance_group_id(self) -> str:
        return pulumi.get(self, "managed_instance_group_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the module that is available to the managed instance group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameContains")
    def name_contains(self) -> Optional[str]:
        return pulumi.get(self, "name_contains")


class AwaitableGetManagedInstanceGroupAvailableModulesResult(GetManagedInstanceGroupAvailableModulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceGroupAvailableModulesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            managed_instance_group_available_module_collections=self.managed_instance_group_available_module_collections,
            managed_instance_group_id=self.managed_instance_group_id,
            name=self.name,
            name_contains=self.name_contains)


def get_managed_instance_group_available_modules(compartment_id: Optional[str] = None,
                                                 filters: Optional[Sequence[pulumi.InputType['GetManagedInstanceGroupAvailableModulesFilterArgs']]] = None,
                                                 managed_instance_group_id: Optional[str] = None,
                                                 name: Optional[str] = None,
                                                 name_contains: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceGroupAvailableModulesResult:
    """
    This data source provides the list of Managed Instance Group Available Modules in Oracle Cloud Infrastructure Os Management Hub service.

    List modules that are available for installation on the specified managed instance group. Filter the list against a variety of criteria including but not limited to module name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_group_available_modules = oci.OsManagementHub.get_managed_instance_group_available_modules(managed_instance_group_id=test_managed_instance_group["id"],
        compartment_id=compartment_id,
        name=managed_instance_group_available_module_name,
        name_contains=managed_instance_group_available_module_name_contains)
    ```


    :param str compartment_id: The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
    :param str managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
    :param str name: The resource name.
    :param str name_contains: A filter to return resources that may partially match the name given.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['managedInstanceGroupId'] = managed_instance_group_id
    __args__['name'] = name
    __args__['nameContains'] = name_contains
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagementHub/getManagedInstanceGroupAvailableModules:getManagedInstanceGroupAvailableModules', __args__, opts=opts, typ=GetManagedInstanceGroupAvailableModulesResult).value

    return AwaitableGetManagedInstanceGroupAvailableModulesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_instance_group_available_module_collections=pulumi.get(__ret__, 'managed_instance_group_available_module_collections'),
        managed_instance_group_id=pulumi.get(__ret__, 'managed_instance_group_id'),
        name=pulumi.get(__ret__, 'name'),
        name_contains=pulumi.get(__ret__, 'name_contains'))


@_utilities.lift_output_func(get_managed_instance_group_available_modules)
def get_managed_instance_group_available_modules_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedInstanceGroupAvailableModulesFilterArgs']]]]] = None,
                                                        managed_instance_group_id: Optional[pulumi.Input[str]] = None,
                                                        name: Optional[pulumi.Input[Optional[str]]] = None,
                                                        name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceGroupAvailableModulesResult]:
    """
    This data source provides the list of Managed Instance Group Available Modules in Oracle Cloud Infrastructure Os Management Hub service.

    List modules that are available for installation on the specified managed instance group. Filter the list against a variety of criteria including but not limited to module name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_group_available_modules = oci.OsManagementHub.get_managed_instance_group_available_modules(managed_instance_group_id=test_managed_instance_group["id"],
        compartment_id=compartment_id,
        name=managed_instance_group_available_module_name,
        name_contains=managed_instance_group_available_module_name_contains)
    ```


    :param str compartment_id: The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
    :param str managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
    :param str name: The resource name.
    :param str name_contains: A filter to return resources that may partially match the name given.
    """
    ...
