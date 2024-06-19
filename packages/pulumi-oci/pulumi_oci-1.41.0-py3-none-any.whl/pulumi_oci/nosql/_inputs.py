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
    'IndexKeyArgs',
    'TableReplicaArgs',
    'TableSchemaArgs',
    'TableSchemaColumnArgs',
    'TableSchemaIdentityArgs',
    'TableTableLimitsArgs',
    'GetIndexesFilterArgs',
    'GetTablesFilterArgs',
]

@pulumi.input_type
class IndexKeyArgs:
    def __init__(__self__, *,
                 column_name: pulumi.Input[str],
                 json_field_type: Optional[pulumi.Input[str]] = None,
                 json_path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] column_name: The name of a column to be included as an index key.
        :param pulumi.Input[str] json_field_type: If the specified column is of type JSON, jsonFieldType contains the type of the field indicated by jsonPath.
        :param pulumi.Input[str] json_path: If the specified column is of type JSON, jsonPath contains a dotted path indicating the field within the JSON object that will be the index key.
        """
        pulumi.set(__self__, "column_name", column_name)
        if json_field_type is not None:
            pulumi.set(__self__, "json_field_type", json_field_type)
        if json_path is not None:
            pulumi.set(__self__, "json_path", json_path)

    @property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[str]:
        """
        The name of a column to be included as an index key.
        """
        return pulumi.get(self, "column_name")

    @column_name.setter
    def column_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "column_name", value)

    @property
    @pulumi.getter(name="jsonFieldType")
    def json_field_type(self) -> Optional[pulumi.Input[str]]:
        """
        If the specified column is of type JSON, jsonFieldType contains the type of the field indicated by jsonPath.
        """
        return pulumi.get(self, "json_field_type")

    @json_field_type.setter
    def json_field_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "json_field_type", value)

    @property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> Optional[pulumi.Input[str]]:
        """
        If the specified column is of type JSON, jsonPath contains a dotted path indicating the field within the JSON object that will be the index key.
        """
        return pulumi.get(self, "json_path")

    @json_path.setter
    def json_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "json_path", value)


@pulumi.input_type
class TableReplicaArgs:
    def __init__(__self__, *,
                 capacity_mode: Optional[pulumi.Input[str]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 max_write_units: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 table_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] capacity_mode: The capacity mode of the table.  If capacityMode = ON_DEMAND, maxReadUnits and maxWriteUnits are not used, and both will have the value of zero.
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail.
        :param pulumi.Input[int] max_write_units: Maximum sustained write throughput limit for the table.
        :param pulumi.Input[str] region: A customer-facing region identifier
        :param pulumi.Input[str] state: The state of a table.
        :param pulumi.Input[str] table_id: The OCID of the replica table
        """
        if capacity_mode is not None:
            pulumi.set(__self__, "capacity_mode", capacity_mode)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if max_write_units is not None:
            pulumi.set(__self__, "max_write_units", max_write_units)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if table_id is not None:
            pulumi.set(__self__, "table_id", table_id)

    @property
    @pulumi.getter(name="capacityMode")
    def capacity_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The capacity mode of the table.  If capacityMode = ON_DEMAND, maxReadUnits and maxWriteUnits are not used, and both will have the value of zero.
        """
        return pulumi.get(self, "capacity_mode")

    @capacity_mode.setter
    def capacity_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_mode", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="maxWriteUnits")
    def max_write_units(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum sustained write throughput limit for the table.
        """
        return pulumi.get(self, "max_write_units")

    @max_write_units.setter
    def max_write_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_write_units", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        A customer-facing region identifier
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of a table.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the replica table
        """
        return pulumi.get(self, "table_id")

    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_id", value)


@pulumi.input_type
class TableSchemaArgs:
    def __init__(__self__, *,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaColumnArgs']]]] = None,
                 identities: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaIdentityArgs']]]] = None,
                 primary_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 shard_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['TableSchemaColumnArgs']]] columns: The columns of a table.
        :param pulumi.Input[Sequence[pulumi.Input['TableSchemaIdentityArgs']]] identities: The identity properties of a table, if any.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] primary_keys: A list of column names that make up a key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] shard_keys: A list of column names that make up a key.
        :param pulumi.Input[int] ttl: The default Time-to-Live for the table, in days.
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if identities is not None:
            pulumi.set(__self__, "identities", identities)
        if primary_keys is not None:
            pulumi.set(__self__, "primary_keys", primary_keys)
        if shard_keys is not None:
            pulumi.set(__self__, "shard_keys", shard_keys)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaColumnArgs']]]]:
        """
        The columns of a table.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaIdentityArgs']]]]:
        """
        The identity properties of a table, if any.
        """
        return pulumi.get(self, "identities")

    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaIdentityArgs']]]]):
        pulumi.set(self, "identities", value)

    @property
    @pulumi.getter(name="primaryKeys")
    def primary_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of column names that make up a key.
        """
        return pulumi.get(self, "primary_keys")

    @primary_keys.setter
    def primary_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "primary_keys", value)

    @property
    @pulumi.getter(name="shardKeys")
    def shard_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of column names that make up a key.
        """
        return pulumi.get(self, "shard_keys")

    @shard_keys.setter
    def shard_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "shard_keys", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The default Time-to-Live for the table, in days.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class TableSchemaColumnArgs:
    def __init__(__self__, *,
                 default_value: Optional[pulumi.Input[str]] = None,
                 is_as_uuid: Optional[pulumi.Input[bool]] = None,
                 is_generated: Optional[pulumi.Input[bool]] = None,
                 is_nullable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] default_value: The column default value.
        :param pulumi.Input[bool] is_as_uuid: True if the STRING column was declared AS UUID.
        :param pulumi.Input[bool] is_generated: True if the STRING AS UUID column is also GENERATED BY DEFAULT.
        :param pulumi.Input[bool] is_nullable: The column nullable flag.
        :param pulumi.Input[str] name: Table name.
        :param pulumi.Input[str] type: The column type.
        """
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if is_as_uuid is not None:
            pulumi.set(__self__, "is_as_uuid", is_as_uuid)
        if is_generated is not None:
            pulumi.set(__self__, "is_generated", is_generated)
        if is_nullable is not None:
            pulumi.set(__self__, "is_nullable", is_nullable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[str]]:
        """
        The column default value.
        """
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter(name="isAsUuid")
    def is_as_uuid(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the STRING column was declared AS UUID.
        """
        return pulumi.get(self, "is_as_uuid")

    @is_as_uuid.setter
    def is_as_uuid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_as_uuid", value)

    @property
    @pulumi.getter(name="isGenerated")
    def is_generated(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the STRING AS UUID column is also GENERATED BY DEFAULT.
        """
        return pulumi.get(self, "is_generated")

    @is_generated.setter
    def is_generated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_generated", value)

    @property
    @pulumi.getter(name="isNullable")
    def is_nullable(self) -> Optional[pulumi.Input[bool]]:
        """
        The column nullable flag.
        """
        return pulumi.get(self, "is_nullable")

    @is_nullable.setter
    def is_nullable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_nullable", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Table name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The column type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class TableSchemaIdentityArgs:
    def __init__(__self__, *,
                 column_name: Optional[pulumi.Input[str]] = None,
                 is_always: Optional[pulumi.Input[bool]] = None,
                 is_null: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] column_name: The name of the identity column.
        :param pulumi.Input[bool] is_always: True if the identity value is GENERATED ALWAYS.
        :param pulumi.Input[bool] is_null: True if the identity value is GENERATED BY DEFAULT ON NULL.
        """
        if column_name is not None:
            pulumi.set(__self__, "column_name", column_name)
        if is_always is not None:
            pulumi.set(__self__, "is_always", is_always)
        if is_null is not None:
            pulumi.set(__self__, "is_null", is_null)

    @property
    @pulumi.getter(name="columnName")
    def column_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the identity column.
        """
        return pulumi.get(self, "column_name")

    @column_name.setter
    def column_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "column_name", value)

    @property
    @pulumi.getter(name="isAlways")
    def is_always(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the identity value is GENERATED ALWAYS.
        """
        return pulumi.get(self, "is_always")

    @is_always.setter
    def is_always(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_always", value)

    @property
    @pulumi.getter(name="isNull")
    def is_null(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the identity value is GENERATED BY DEFAULT ON NULL.
        """
        return pulumi.get(self, "is_null")

    @is_null.setter
    def is_null(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_null", value)


@pulumi.input_type
class TableTableLimitsArgs:
    def __init__(__self__, *,
                 max_read_units: pulumi.Input[int],
                 max_storage_in_gbs: pulumi.Input[int],
                 max_write_units: pulumi.Input[int],
                 capacity_mode: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] max_read_units: (Updatable) Maximum sustained read throughput limit for the table.
        :param pulumi.Input[int] max_storage_in_gbs: (Updatable) Maximum size of storage used by the table.
        :param pulumi.Input[int] max_write_units: (Updatable) Maximum sustained write throughput limit for the table.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] capacity_mode: (Updatable) The capacity mode of the table.  If capacityMode = ON_DEMAND, maxReadUnits and maxWriteUnits are not used, and both will have the value of zero.
        """
        pulumi.set(__self__, "max_read_units", max_read_units)
        pulumi.set(__self__, "max_storage_in_gbs", max_storage_in_gbs)
        pulumi.set(__self__, "max_write_units", max_write_units)
        if capacity_mode is not None:
            pulumi.set(__self__, "capacity_mode", capacity_mode)

    @property
    @pulumi.getter(name="maxReadUnits")
    def max_read_units(self) -> pulumi.Input[int]:
        """
        (Updatable) Maximum sustained read throughput limit for the table.
        """
        return pulumi.get(self, "max_read_units")

    @max_read_units.setter
    def max_read_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_read_units", value)

    @property
    @pulumi.getter(name="maxStorageInGbs")
    def max_storage_in_gbs(self) -> pulumi.Input[int]:
        """
        (Updatable) Maximum size of storage used by the table.
        """
        return pulumi.get(self, "max_storage_in_gbs")

    @max_storage_in_gbs.setter
    def max_storage_in_gbs(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_storage_in_gbs", value)

    @property
    @pulumi.getter(name="maxWriteUnits")
    def max_write_units(self) -> pulumi.Input[int]:
        """
        (Updatable) Maximum sustained write throughput limit for the table.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "max_write_units")

    @max_write_units.setter
    def max_write_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_write_units", value)

    @property
    @pulumi.getter(name="capacityMode")
    def capacity_mode(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The capacity mode of the table.  If capacityMode = ON_DEMAND, maxReadUnits and maxWriteUnits are not used, and both will have the value of zero.
        """
        return pulumi.get(self, "capacity_mode")

    @capacity_mode.setter
    def capacity_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_mode", value)


@pulumi.input_type
class GetIndexesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: A shell-globbing-style (*?[]) filter for names.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A shell-globbing-style (*?[]) filter for names.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetTablesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: A shell-globbing-style (*?[]) filter for names.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A shell-globbing-style (*?[]) filter for names.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


