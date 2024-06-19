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
    'GetMigrationObjectTypesResult',
    'AwaitableGetMigrationObjectTypesResult',
    'get_migration_object_types',
    'get_migration_object_types_output',
]

@pulumi.output_type
class GetMigrationObjectTypesResult:
    """
    A collection of values returned by getMigrationObjectTypes.
    """
    def __init__(__self__, filters=None, id=None, migration_object_type_summary_collections=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if migration_object_type_summary_collections and not isinstance(migration_object_type_summary_collections, list):
            raise TypeError("Expected argument 'migration_object_type_summary_collections' to be a list")
        pulumi.set(__self__, "migration_object_type_summary_collections", migration_object_type_summary_collections)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMigrationObjectTypesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="migrationObjectTypeSummaryCollections")
    def migration_object_type_summary_collections(self) -> Sequence['outputs.GetMigrationObjectTypesMigrationObjectTypeSummaryCollectionResult']:
        """
        The list of migration_object_type_summary_collection.
        """
        return pulumi.get(self, "migration_object_type_summary_collections")


class AwaitableGetMigrationObjectTypesResult(GetMigrationObjectTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMigrationObjectTypesResult(
            filters=self.filters,
            id=self.id,
            migration_object_type_summary_collections=self.migration_object_type_summary_collections)


def get_migration_object_types(filters: Optional[Sequence[pulumi.InputType['GetMigrationObjectTypesFilterArgs']]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMigrationObjectTypesResult:
    """
    This data source provides the list of Migration Object Types in Oracle Cloud Infrastructure Database Migration service.

    Display sample object types to exclude or include for a Migration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_migration_object_types = oci.DatabaseMigration.get_migration_object_types()
    ```
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseMigration/getMigrationObjectTypes:getMigrationObjectTypes', __args__, opts=opts, typ=GetMigrationObjectTypesResult).value

    return AwaitableGetMigrationObjectTypesResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        migration_object_type_summary_collections=pulumi.get(__ret__, 'migration_object_type_summary_collections'))


@_utilities.lift_output_func(get_migration_object_types)
def get_migration_object_types_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMigrationObjectTypesFilterArgs']]]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMigrationObjectTypesResult]:
    """
    This data source provides the list of Migration Object Types in Oracle Cloud Infrastructure Database Migration service.

    Display sample object types to exclude or include for a Migration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_migration_object_types = oci.DatabaseMigration.get_migration_object_types()
    ```
    """
    ...
