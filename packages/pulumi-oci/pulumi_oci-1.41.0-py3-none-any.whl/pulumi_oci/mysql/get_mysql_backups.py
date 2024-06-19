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
    'GetMysqlBackupsResult',
    'AwaitableGetMysqlBackupsResult',
    'get_mysql_backups',
    'get_mysql_backups_output',
]

@pulumi.output_type
class GetMysqlBackupsResult:
    """
    A collection of values returned by getMysqlBackups.
    """
    def __init__(__self__, backup_id=None, backups=None, compartment_id=None, creation_type=None, db_system_id=None, display_name=None, filters=None, id=None, state=None):
        if backup_id and not isinstance(backup_id, str):
            raise TypeError("Expected argument 'backup_id' to be a str")
        pulumi.set(__self__, "backup_id", backup_id)
        if backups and not isinstance(backups, list):
            raise TypeError("Expected argument 'backups' to be a list")
        pulumi.set(__self__, "backups", backups)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if creation_type and not isinstance(creation_type, str):
            raise TypeError("Expected argument 'creation_type' to be a str")
        pulumi.set(__self__, "creation_type", creation_type)
        if db_system_id and not isinstance(db_system_id, str):
            raise TypeError("Expected argument 'db_system_id' to be a str")
        pulumi.set(__self__, "db_system_id", db_system_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[str]:
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter
    def backups(self) -> Sequence['outputs.GetMysqlBackupsBackupResult']:
        """
        The list of backups.
        """
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment the DB System belongs in.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="creationType")
    def creation_type(self) -> Optional[str]:
        """
        Indicates how the backup was created: manually, automatic, or by an Operator.
        """
        return pulumi.get(self, "creation_type")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[str]:
        """
        The OCID of the DB System the backup is associated with.
        """
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-supplied display name for the backup.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMysqlBackupsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the backup.
        """
        return pulumi.get(self, "state")


class AwaitableGetMysqlBackupsResult(GetMysqlBackupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMysqlBackupsResult(
            backup_id=self.backup_id,
            backups=self.backups,
            compartment_id=self.compartment_id,
            creation_type=self.creation_type,
            db_system_id=self.db_system_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_mysql_backups(backup_id: Optional[str] = None,
                      compartment_id: Optional[str] = None,
                      creation_type: Optional[str] = None,
                      db_system_id: Optional[str] = None,
                      display_name: Optional[str] = None,
                      filters: Optional[Sequence[pulumi.InputType['GetMysqlBackupsFilterArgs']]] = None,
                      state: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMysqlBackupsResult:
    """
    This data source provides the list of Mysql Backups in Oracle Cloud Infrastructure MySQL Database service.

    Get a list of DB System backups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_mysql_backups = oci.Mysql.get_mysql_backups(compartment_id=compartment_id,
        backup_id=test_backup["id"],
        creation_type=mysql_backup_creation_type,
        db_system_id=test_db_system["id"],
        display_name=mysql_backup_display_name,
        state=mysql_backup_state)
    ```


    :param str backup_id: Backup OCID
    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str creation_type: Backup creationType
    :param str db_system_id: The DB System [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only the resource matching the given display name exactly.
    :param str state: Backup Lifecycle State
    """
    __args__ = dict()
    __args__['backupId'] = backup_id
    __args__['compartmentId'] = compartment_id
    __args__['creationType'] = creation_type
    __args__['dbSystemId'] = db_system_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Mysql/getMysqlBackups:getMysqlBackups', __args__, opts=opts, typ=GetMysqlBackupsResult).value

    return AwaitableGetMysqlBackupsResult(
        backup_id=pulumi.get(__ret__, 'backup_id'),
        backups=pulumi.get(__ret__, 'backups'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        creation_type=pulumi.get(__ret__, 'creation_type'),
        db_system_id=pulumi.get(__ret__, 'db_system_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_mysql_backups)
def get_mysql_backups_output(backup_id: Optional[pulumi.Input[Optional[str]]] = None,
                             compartment_id: Optional[pulumi.Input[str]] = None,
                             creation_type: Optional[pulumi.Input[Optional[str]]] = None,
                             db_system_id: Optional[pulumi.Input[Optional[str]]] = None,
                             display_name: Optional[pulumi.Input[Optional[str]]] = None,
                             filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMysqlBackupsFilterArgs']]]]] = None,
                             state: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMysqlBackupsResult]:
    """
    This data source provides the list of Mysql Backups in Oracle Cloud Infrastructure MySQL Database service.

    Get a list of DB System backups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_mysql_backups = oci.Mysql.get_mysql_backups(compartment_id=compartment_id,
        backup_id=test_backup["id"],
        creation_type=mysql_backup_creation_type,
        db_system_id=test_db_system["id"],
        display_name=mysql_backup_display_name,
        state=mysql_backup_state)
    ```


    :param str backup_id: Backup OCID
    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str creation_type: Backup creationType
    :param str db_system_id: The DB System [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only the resource matching the given display name exactly.
    :param str state: Backup Lifecycle State
    """
    ...
