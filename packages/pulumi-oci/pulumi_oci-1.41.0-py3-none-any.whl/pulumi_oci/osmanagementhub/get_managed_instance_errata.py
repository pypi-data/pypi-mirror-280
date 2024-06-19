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
    'GetManagedInstanceErrataResult',
    'AwaitableGetManagedInstanceErrataResult',
    'get_managed_instance_errata',
    'get_managed_instance_errata_output',
]

@pulumi.output_type
class GetManagedInstanceErrataResult:
    """
    A collection of values returned by getManagedInstanceErrata.
    """
    def __init__(__self__, classification_types=None, compartment_id=None, filters=None, id=None, managed_instance_erratum_summary_collections=None, managed_instance_id=None, name_contains=None, names=None):
        if classification_types and not isinstance(classification_types, list):
            raise TypeError("Expected argument 'classification_types' to be a list")
        pulumi.set(__self__, "classification_types", classification_types)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_instance_erratum_summary_collections and not isinstance(managed_instance_erratum_summary_collections, list):
            raise TypeError("Expected argument 'managed_instance_erratum_summary_collections' to be a list")
        pulumi.set(__self__, "managed_instance_erratum_summary_collections", managed_instance_erratum_summary_collections)
        if managed_instance_id and not isinstance(managed_instance_id, str):
            raise TypeError("Expected argument 'managed_instance_id' to be a str")
        pulumi.set(__self__, "managed_instance_id", managed_instance_id)
        if name_contains and not isinstance(name_contains, str):
            raise TypeError("Expected argument 'name_contains' to be a str")
        pulumi.set(__self__, "name_contains", name_contains)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)

    @property
    @pulumi.getter(name="classificationTypes")
    def classification_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "classification_types")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedInstanceErrataFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstanceErratumSummaryCollections")
    def managed_instance_erratum_summary_collections(self) -> Sequence['outputs.GetManagedInstanceErrataManagedInstanceErratumSummaryCollectionResult']:
        """
        The list of managed_instance_erratum_summary_collection.
        """
        return pulumi.get(self, "managed_instance_erratum_summary_collections")

    @property
    @pulumi.getter(name="managedInstanceId")
    def managed_instance_id(self) -> str:
        return pulumi.get(self, "managed_instance_id")

    @property
    @pulumi.getter(name="nameContains")
    def name_contains(self) -> Optional[str]:
        return pulumi.get(self, "name_contains")

    @property
    @pulumi.getter
    def names(self) -> Optional[Sequence[str]]:
        """
        The name of the software package.
        """
        return pulumi.get(self, "names")


class AwaitableGetManagedInstanceErrataResult(GetManagedInstanceErrataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceErrataResult(
            classification_types=self.classification_types,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            managed_instance_erratum_summary_collections=self.managed_instance_erratum_summary_collections,
            managed_instance_id=self.managed_instance_id,
            name_contains=self.name_contains,
            names=self.names)


def get_managed_instance_errata(classification_types: Optional[Sequence[str]] = None,
                                compartment_id: Optional[str] = None,
                                filters: Optional[Sequence[pulumi.InputType['GetManagedInstanceErrataFilterArgs']]] = None,
                                managed_instance_id: Optional[str] = None,
                                name_contains: Optional[str] = None,
                                names: Optional[Sequence[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceErrataResult:
    """
    This data source provides the list of Managed Instance Errata in Oracle Cloud Infrastructure Os Management Hub service.

    Returns a list of applicable errata on the managed instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_errata = oci.OsManagementHub.get_managed_instance_errata(managed_instance_id=test_managed_instance["id"],
        classification_types=managed_instance_errata_classification_type,
        compartment_id=compartment_id,
        names=managed_instance_errata_name,
        name_contains=managed_instance_errata_name_contains)
    ```


    :param Sequence[str] classification_types: A filter to return only packages that match the given update classification type.
    :param str compartment_id: The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
    :param str managed_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
    :param str name_contains: A filter to return resources that may partially match the erratum name given.
    :param Sequence[str] names: The assigned erratum name. It's unique and not changeable.  Example: `ELSA-2020-5804`
    """
    __args__ = dict()
    __args__['classificationTypes'] = classification_types
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['managedInstanceId'] = managed_instance_id
    __args__['nameContains'] = name_contains
    __args__['names'] = names
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagementHub/getManagedInstanceErrata:getManagedInstanceErrata', __args__, opts=opts, typ=GetManagedInstanceErrataResult).value

    return AwaitableGetManagedInstanceErrataResult(
        classification_types=pulumi.get(__ret__, 'classification_types'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_instance_erratum_summary_collections=pulumi.get(__ret__, 'managed_instance_erratum_summary_collections'),
        managed_instance_id=pulumi.get(__ret__, 'managed_instance_id'),
        name_contains=pulumi.get(__ret__, 'name_contains'),
        names=pulumi.get(__ret__, 'names'))


@_utilities.lift_output_func(get_managed_instance_errata)
def get_managed_instance_errata_output(classification_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                       compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedInstanceErrataFilterArgs']]]]] = None,
                                       managed_instance_id: Optional[pulumi.Input[str]] = None,
                                       name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                       names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceErrataResult]:
    """
    This data source provides the list of Managed Instance Errata in Oracle Cloud Infrastructure Os Management Hub service.

    Returns a list of applicable errata on the managed instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_errata = oci.OsManagementHub.get_managed_instance_errata(managed_instance_id=test_managed_instance["id"],
        classification_types=managed_instance_errata_classification_type,
        compartment_id=compartment_id,
        names=managed_instance_errata_name,
        name_contains=managed_instance_errata_name_contains)
    ```


    :param Sequence[str] classification_types: A filter to return only packages that match the given update classification type.
    :param str compartment_id: The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
    :param str managed_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
    :param str name_contains: A filter to return resources that may partially match the erratum name given.
    :param Sequence[str] names: The assigned erratum name. It's unique and not changeable.  Example: `ELSA-2020-5804`
    """
    ...
