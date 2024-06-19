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
    'GetManagedDatabaseUserConsumerGroupPrivilegesResult',
    'AwaitableGetManagedDatabaseUserConsumerGroupPrivilegesResult',
    'get_managed_database_user_consumer_group_privileges',
    'get_managed_database_user_consumer_group_privileges_output',
]

@pulumi.output_type
class GetManagedDatabaseUserConsumerGroupPrivilegesResult:
    """
    A collection of values returned by getManagedDatabaseUserConsumerGroupPrivileges.
    """
    def __init__(__self__, consumer_group_privilege_collections=None, filters=None, id=None, managed_database_id=None, name=None, opc_named_credential_id=None, user_name=None):
        if consumer_group_privilege_collections and not isinstance(consumer_group_privilege_collections, list):
            raise TypeError("Expected argument 'consumer_group_privilege_collections' to be a list")
        pulumi.set(__self__, "consumer_group_privilege_collections", consumer_group_privilege_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if opc_named_credential_id and not isinstance(opc_named_credential_id, str):
            raise TypeError("Expected argument 'opc_named_credential_id' to be a str")
        pulumi.set(__self__, "opc_named_credential_id", opc_named_credential_id)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="consumerGroupPrivilegeCollections")
    def consumer_group_privilege_collections(self) -> Sequence['outputs.GetManagedDatabaseUserConsumerGroupPrivilegesConsumerGroupPrivilegeCollectionResult']:
        """
        The list of consumer_group_privilege_collection.
        """
        return pulumi.get(self, "consumer_group_privilege_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedDatabaseUserConsumerGroupPrivilegesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> str:
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the granted consumer group privilege.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="opcNamedCredentialId")
    def opc_named_credential_id(self) -> Optional[str]:
        return pulumi.get(self, "opc_named_credential_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        return pulumi.get(self, "user_name")


class AwaitableGetManagedDatabaseUserConsumerGroupPrivilegesResult(GetManagedDatabaseUserConsumerGroupPrivilegesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseUserConsumerGroupPrivilegesResult(
            consumer_group_privilege_collections=self.consumer_group_privilege_collections,
            filters=self.filters,
            id=self.id,
            managed_database_id=self.managed_database_id,
            name=self.name,
            opc_named_credential_id=self.opc_named_credential_id,
            user_name=self.user_name)


def get_managed_database_user_consumer_group_privileges(filters: Optional[Sequence[pulumi.InputType['GetManagedDatabaseUserConsumerGroupPrivilegesFilterArgs']]] = None,
                                                        managed_database_id: Optional[str] = None,
                                                        name: Optional[str] = None,
                                                        opc_named_credential_id: Optional[str] = None,
                                                        user_name: Optional[str] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseUserConsumerGroupPrivilegesResult:
    """
    This data source provides the list of Managed Database User Consumer Group Privileges in Oracle Cloud Infrastructure Database Management service.

    Gets the list of consumer group privileges granted to a specific user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_user_consumer_group_privileges = oci.DatabaseManagement.get_managed_database_user_consumer_group_privileges(managed_database_id=test_managed_database["id"],
        user_name=test_user["name"],
        name=managed_database_user_consumer_group_privilege_name,
        opc_named_credential_id=managed_database_user_consumer_group_privilege_opc_named_credential_id)
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str name: A filter to return only resources that match the entire name.
    :param str opc_named_credential_id: The OCID of the Named Credential.
    :param str user_name: The name of the user whose details are to be viewed.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['managedDatabaseId'] = managed_database_id
    __args__['name'] = name
    __args__['opcNamedCredentialId'] = opc_named_credential_id
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseUserConsumerGroupPrivileges:getManagedDatabaseUserConsumerGroupPrivileges', __args__, opts=opts, typ=GetManagedDatabaseUserConsumerGroupPrivilegesResult).value

    return AwaitableGetManagedDatabaseUserConsumerGroupPrivilegesResult(
        consumer_group_privilege_collections=pulumi.get(__ret__, 'consumer_group_privilege_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        name=pulumi.get(__ret__, 'name'),
        opc_named_credential_id=pulumi.get(__ret__, 'opc_named_credential_id'),
        user_name=pulumi.get(__ret__, 'user_name'))


@_utilities.lift_output_func(get_managed_database_user_consumer_group_privileges)
def get_managed_database_user_consumer_group_privileges_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedDatabaseUserConsumerGroupPrivilegesFilterArgs']]]]] = None,
                                                               managed_database_id: Optional[pulumi.Input[str]] = None,
                                                               name: Optional[pulumi.Input[Optional[str]]] = None,
                                                               opc_named_credential_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                               user_name: Optional[pulumi.Input[str]] = None,
                                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseUserConsumerGroupPrivilegesResult]:
    """
    This data source provides the list of Managed Database User Consumer Group Privileges in Oracle Cloud Infrastructure Database Management service.

    Gets the list of consumer group privileges granted to a specific user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_user_consumer_group_privileges = oci.DatabaseManagement.get_managed_database_user_consumer_group_privileges(managed_database_id=test_managed_database["id"],
        user_name=test_user["name"],
        name=managed_database_user_consumer_group_privilege_name,
        opc_named_credential_id=managed_database_user_consumer_group_privilege_opc_named_credential_id)
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str name: A filter to return only resources that match the entire name.
    :param str opc_named_credential_id: The OCID of the Named Credential.
    :param str user_name: The name of the user whose details are to be viewed.
    """
    ...
