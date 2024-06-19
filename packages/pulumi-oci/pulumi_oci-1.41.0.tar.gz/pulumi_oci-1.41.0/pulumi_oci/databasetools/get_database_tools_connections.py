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
    'GetDatabaseToolsConnectionsResult',
    'AwaitableGetDatabaseToolsConnectionsResult',
    'get_database_tools_connections',
    'get_database_tools_connections_output',
]

@pulumi.output_type
class GetDatabaseToolsConnectionsResult:
    """
    A collection of values returned by getDatabaseToolsConnections.
    """
    def __init__(__self__, compartment_id=None, database_tools_connection_collections=None, display_name=None, filters=None, id=None, related_resource_identifier=None, runtime_supports=None, state=None, types=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if database_tools_connection_collections and not isinstance(database_tools_connection_collections, list):
            raise TypeError("Expected argument 'database_tools_connection_collections' to be a list")
        pulumi.set(__self__, "database_tools_connection_collections", database_tools_connection_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if related_resource_identifier and not isinstance(related_resource_identifier, str):
            raise TypeError("Expected argument 'related_resource_identifier' to be a str")
        pulumi.set(__self__, "related_resource_identifier", related_resource_identifier)
        if runtime_supports and not isinstance(runtime_supports, list):
            raise TypeError("Expected argument 'runtime_supports' to be a list")
        pulumi.set(__self__, "runtime_supports", runtime_supports)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if types and not isinstance(types, list):
            raise TypeError("Expected argument 'types' to be a list")
        pulumi.set(__self__, "types", types)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Database Tools connection.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="databaseToolsConnectionCollections")
    def database_tools_connection_collections(self) -> Sequence['outputs.GetDatabaseToolsConnectionsDatabaseToolsConnectionCollectionResult']:
        """
        The list of database_tools_connection_collection.
        """
        return pulumi.get(self, "database_tools_connection_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDatabaseToolsConnectionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="relatedResourceIdentifier")
    def related_resource_identifier(self) -> Optional[str]:
        return pulumi.get(self, "related_resource_identifier")

    @property
    @pulumi.getter(name="runtimeSupports")
    def runtime_supports(self) -> Optional[Sequence[str]]:
        """
        Specifies whether this connection is supported by the Database Tools Runtime.
        """
        return pulumi.get(self, "runtime_supports")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Database Tools connection.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def types(self) -> Optional[Sequence[str]]:
        """
        The Database Tools connection type.
        """
        return pulumi.get(self, "types")


class AwaitableGetDatabaseToolsConnectionsResult(GetDatabaseToolsConnectionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseToolsConnectionsResult(
            compartment_id=self.compartment_id,
            database_tools_connection_collections=self.database_tools_connection_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            related_resource_identifier=self.related_resource_identifier,
            runtime_supports=self.runtime_supports,
            state=self.state,
            types=self.types)


def get_database_tools_connections(compartment_id: Optional[str] = None,
                                   display_name: Optional[str] = None,
                                   filters: Optional[Sequence[pulumi.InputType['GetDatabaseToolsConnectionsFilterArgs']]] = None,
                                   related_resource_identifier: Optional[str] = None,
                                   runtime_supports: Optional[Sequence[str]] = None,
                                   state: Optional[str] = None,
                                   types: Optional[Sequence[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseToolsConnectionsResult:
    """
    This data source provides the list of Database Tools Connections in Oracle Cloud Infrastructure Database Tools service.

    Returns a list of Database Tools connections.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_tools_connections = oci.DatabaseTools.get_database_tools_connections(compartment_id=compartment_id,
        display_name=database_tools_connection_display_name,
        related_resource_identifier=database_tools_connection_related_resource_identifier,
        runtime_supports=database_tools_connection_runtime_support,
        state=database_tools_connection_state,
        types=database_tools_connection_type)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire specified display name.
    :param str related_resource_identifier: A filter to return only resources associated to the related resource identifier OCID passed in the query string.
    :param Sequence[str] runtime_supports: A filter to return only resources with one of the specified runtimeSupport values.
    :param str state: A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.
    :param Sequence[str] types: A filter to return only resources their type matches the specified type.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['relatedResourceIdentifier'] = related_resource_identifier
    __args__['runtimeSupports'] = runtime_supports
    __args__['state'] = state
    __args__['types'] = types
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseTools/getDatabaseToolsConnections:getDatabaseToolsConnections', __args__, opts=opts, typ=GetDatabaseToolsConnectionsResult).value

    return AwaitableGetDatabaseToolsConnectionsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        database_tools_connection_collections=pulumi.get(__ret__, 'database_tools_connection_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        related_resource_identifier=pulumi.get(__ret__, 'related_resource_identifier'),
        runtime_supports=pulumi.get(__ret__, 'runtime_supports'),
        state=pulumi.get(__ret__, 'state'),
        types=pulumi.get(__ret__, 'types'))


@_utilities.lift_output_func(get_database_tools_connections)
def get_database_tools_connections_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                          display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseToolsConnectionsFilterArgs']]]]] = None,
                                          related_resource_identifier: Optional[pulumi.Input[Optional[str]]] = None,
                                          runtime_supports: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                          state: Optional[pulumi.Input[Optional[str]]] = None,
                                          types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseToolsConnectionsResult]:
    """
    This data source provides the list of Database Tools Connections in Oracle Cloud Infrastructure Database Tools service.

    Returns a list of Database Tools connections.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_tools_connections = oci.DatabaseTools.get_database_tools_connections(compartment_id=compartment_id,
        display_name=database_tools_connection_display_name,
        related_resource_identifier=database_tools_connection_related_resource_identifier,
        runtime_supports=database_tools_connection_runtime_support,
        state=database_tools_connection_state,
        types=database_tools_connection_type)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire specified display name.
    :param str related_resource_identifier: A filter to return only resources associated to the related resource identifier OCID passed in the query string.
    :param Sequence[str] runtime_supports: A filter to return only resources with one of the specified runtimeSupport values.
    :param str state: A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.
    :param Sequence[str] types: A filter to return only resources their type matches the specified type.
    """
    ...
