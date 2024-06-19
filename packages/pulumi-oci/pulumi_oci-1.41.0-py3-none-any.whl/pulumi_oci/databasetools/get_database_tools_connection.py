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
    'GetDatabaseToolsConnectionResult',
    'AwaitableGetDatabaseToolsConnectionResult',
    'get_database_tools_connection',
    'get_database_tools_connection_output',
]

@pulumi.output_type
class GetDatabaseToolsConnectionResult:
    """
    A collection of values returned by getDatabaseToolsConnection.
    """
    def __init__(__self__, advanced_properties=None, compartment_id=None, connection_string=None, database_tools_connection_id=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, key_stores=None, lifecycle_details=None, locks=None, private_endpoint_id=None, proxy_clients=None, related_resources=None, runtime_support=None, state=None, system_tags=None, time_created=None, time_updated=None, type=None, url=None, user_name=None, user_passwords=None):
        if advanced_properties and not isinstance(advanced_properties, dict):
            raise TypeError("Expected argument 'advanced_properties' to be a dict")
        pulumi.set(__self__, "advanced_properties", advanced_properties)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if database_tools_connection_id and not isinstance(database_tools_connection_id, str):
            raise TypeError("Expected argument 'database_tools_connection_id' to be a str")
        pulumi.set(__self__, "database_tools_connection_id", database_tools_connection_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_stores and not isinstance(key_stores, list):
            raise TypeError("Expected argument 'key_stores' to be a list")
        pulumi.set(__self__, "key_stores", key_stores)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if locks and not isinstance(locks, list):
            raise TypeError("Expected argument 'locks' to be a list")
        pulumi.set(__self__, "locks", locks)
        if private_endpoint_id and not isinstance(private_endpoint_id, str):
            raise TypeError("Expected argument 'private_endpoint_id' to be a str")
        pulumi.set(__self__, "private_endpoint_id", private_endpoint_id)
        if proxy_clients and not isinstance(proxy_clients, list):
            raise TypeError("Expected argument 'proxy_clients' to be a list")
        pulumi.set(__self__, "proxy_clients", proxy_clients)
        if related_resources and not isinstance(related_resources, list):
            raise TypeError("Expected argument 'related_resources' to be a list")
        pulumi.set(__self__, "related_resources", related_resources)
        if runtime_support and not isinstance(runtime_support, str):
            raise TypeError("Expected argument 'runtime_support' to be a str")
        pulumi.set(__self__, "runtime_support", runtime_support)
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
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)
        if user_passwords and not isinstance(user_passwords, list):
            raise TypeError("Expected argument 'user_passwords' to be a list")
        pulumi.set(__self__, "user_passwords", user_passwords)

    @property
    @pulumi.getter(name="advancedProperties")
    def advanced_properties(self) -> Mapping[str, Any]:
        """
        The advanced connection properties key-value pair (for example, `oracle.net.ssl_server_dn_match`).
        """
        return pulumi.get(self, "advanced_properties")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Database Tools connection.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        The connect descriptor or Easy Connect Naming method used to connect to the database.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="databaseToolsConnectionId")
    def database_tools_connection_id(self) -> str:
        return pulumi.get(self, "database_tools_connection_id")

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
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
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
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Tools connection.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyStores")
    def key_stores(self) -> Sequence['outputs.GetDatabaseToolsConnectionKeyStoreResult']:
        """
        The Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.
        """
        return pulumi.get(self, "key_stores")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, this message can be used to provide actionable information for a resource in the Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def locks(self) -> Sequence['outputs.GetDatabaseToolsConnectionLockResult']:
        """
        Locks associated with this resource.
        """
        return pulumi.get(self, "locks")

    @property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Tools private endpoint used to access the database in the customer VCN.
        """
        return pulumi.get(self, "private_endpoint_id")

    @property
    @pulumi.getter(name="proxyClients")
    def proxy_clients(self) -> Sequence['outputs.GetDatabaseToolsConnectionProxyClientResult']:
        """
        The proxy client information.
        """
        return pulumi.get(self, "proxy_clients")

    @property
    @pulumi.getter(name="relatedResources")
    def related_resources(self) -> Sequence['outputs.GetDatabaseToolsConnectionRelatedResourceResult']:
        """
        A related resource
        """
        return pulumi.get(self, "related_resources")

    @property
    @pulumi.getter(name="runtimeSupport")
    def runtime_support(self) -> str:
        """
        Specifies whether this connection is supported by the Database Tools Runtime.
        """
        return pulumi.get(self, "runtime_support")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Database Tools connection.
        """
        return pulumi.get(self, "state")

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
        The time the Database Tools connection was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the DatabaseToolsConnection was updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Database Tools connection type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        The JDBC URL used to connect to the Generic JDBC database system.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        The database user name.
        """
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="userPasswords")
    def user_passwords(self) -> Sequence['outputs.GetDatabaseToolsConnectionUserPasswordResult']:
        """
        The user password.
        """
        return pulumi.get(self, "user_passwords")


class AwaitableGetDatabaseToolsConnectionResult(GetDatabaseToolsConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseToolsConnectionResult(
            advanced_properties=self.advanced_properties,
            compartment_id=self.compartment_id,
            connection_string=self.connection_string,
            database_tools_connection_id=self.database_tools_connection_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            key_stores=self.key_stores,
            lifecycle_details=self.lifecycle_details,
            locks=self.locks,
            private_endpoint_id=self.private_endpoint_id,
            proxy_clients=self.proxy_clients,
            related_resources=self.related_resources,
            runtime_support=self.runtime_support,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            type=self.type,
            url=self.url,
            user_name=self.user_name,
            user_passwords=self.user_passwords)


def get_database_tools_connection(database_tools_connection_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseToolsConnectionResult:
    """
    This data source provides details about a specific Database Tools Connection resource in Oracle Cloud Infrastructure Database Tools service.

    Gets details of the specified Database Tools connection.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_tools_connection = oci.DatabaseTools.get_database_tools_connection(database_tools_connection_id=test_database_tools_connection_oci_database_tools_database_tools_connection["id"])
    ```


    :param str database_tools_connection_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a Database Tools connection.
    """
    __args__ = dict()
    __args__['databaseToolsConnectionId'] = database_tools_connection_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseTools/getDatabaseToolsConnection:getDatabaseToolsConnection', __args__, opts=opts, typ=GetDatabaseToolsConnectionResult).value

    return AwaitableGetDatabaseToolsConnectionResult(
        advanced_properties=pulumi.get(__ret__, 'advanced_properties'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        connection_string=pulumi.get(__ret__, 'connection_string'),
        database_tools_connection_id=pulumi.get(__ret__, 'database_tools_connection_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        key_stores=pulumi.get(__ret__, 'key_stores'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        locks=pulumi.get(__ret__, 'locks'),
        private_endpoint_id=pulumi.get(__ret__, 'private_endpoint_id'),
        proxy_clients=pulumi.get(__ret__, 'proxy_clients'),
        related_resources=pulumi.get(__ret__, 'related_resources'),
        runtime_support=pulumi.get(__ret__, 'runtime_support'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        type=pulumi.get(__ret__, 'type'),
        url=pulumi.get(__ret__, 'url'),
        user_name=pulumi.get(__ret__, 'user_name'),
        user_passwords=pulumi.get(__ret__, 'user_passwords'))


@_utilities.lift_output_func(get_database_tools_connection)
def get_database_tools_connection_output(database_tools_connection_id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseToolsConnectionResult]:
    """
    This data source provides details about a specific Database Tools Connection resource in Oracle Cloud Infrastructure Database Tools service.

    Gets details of the specified Database Tools connection.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_tools_connection = oci.DatabaseTools.get_database_tools_connection(database_tools_connection_id=test_database_tools_connection_oci_database_tools_database_tools_connection["id"])
    ```


    :param str database_tools_connection_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a Database Tools connection.
    """
    ...
