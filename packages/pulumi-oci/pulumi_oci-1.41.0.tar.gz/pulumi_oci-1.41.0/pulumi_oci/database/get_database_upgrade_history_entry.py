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
    'GetDatabaseUpgradeHistoryEntryResult',
    'AwaitableGetDatabaseUpgradeHistoryEntryResult',
    'get_database_upgrade_history_entry',
    'get_database_upgrade_history_entry_output',
]

@pulumi.output_type
class GetDatabaseUpgradeHistoryEntryResult:
    """
    A collection of values returned by getDatabaseUpgradeHistoryEntry.
    """
    def __init__(__self__, action=None, database_id=None, id=None, lifecycle_details=None, options=None, source=None, source_db_home_id=None, state=None, target_database_software_image_id=None, target_db_home_id=None, target_db_version=None, time_ended=None, time_started=None, upgrade_history_entry_id=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if database_id and not isinstance(database_id, str):
            raise TypeError("Expected argument 'database_id' to be a str")
        pulumi.set(__self__, "database_id", database_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if options and not isinstance(options, str):
            raise TypeError("Expected argument 'options' to be a str")
        pulumi.set(__self__, "options", options)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if source_db_home_id and not isinstance(source_db_home_id, str):
            raise TypeError("Expected argument 'source_db_home_id' to be a str")
        pulumi.set(__self__, "source_db_home_id", source_db_home_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_database_software_image_id and not isinstance(target_database_software_image_id, str):
            raise TypeError("Expected argument 'target_database_software_image_id' to be a str")
        pulumi.set(__self__, "target_database_software_image_id", target_database_software_image_id)
        if target_db_home_id and not isinstance(target_db_home_id, str):
            raise TypeError("Expected argument 'target_db_home_id' to be a str")
        pulumi.set(__self__, "target_db_home_id", target_db_home_id)
        if target_db_version and not isinstance(target_db_version, str):
            raise TypeError("Expected argument 'target_db_version' to be a str")
        pulumi.set(__self__, "target_db_version", target_db_version)
        if time_ended and not isinstance(time_ended, str):
            raise TypeError("Expected argument 'time_ended' to be a str")
        pulumi.set(__self__, "time_ended", time_ended)
        if time_started and not isinstance(time_started, str):
            raise TypeError("Expected argument 'time_started' to be a str")
        pulumi.set(__self__, "time_started", time_started)
        if upgrade_history_entry_id and not isinstance(upgrade_history_entry_id, str):
            raise TypeError("Expected argument 'upgrade_history_entry_id' to be a str")
        pulumi.set(__self__, "upgrade_history_entry_id", upgrade_history_entry_id)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The database upgrade action.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> str:
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def options(self) -> str:
        """
        Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: "-upgradeTimezone false -keepEvents"
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source of the Oracle Database software to be used for the upgrade.
        * Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
        * Use `DB_SOFTWARE_IMAGE` to specify a [database software image](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm) to upgrade the database.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="sourceDbHomeId")
    def source_db_home_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Home.
        """
        return pulumi.get(self, "source_db_home_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Status of database upgrade history SUCCEEDED|IN_PROGRESS|FAILED.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetDatabaseSoftwareImageId")
    def target_database_software_image_id(self) -> str:
        """
        the database software image used for upgrading database.
        """
        return pulumi.get(self, "target_database_software_image_id")

    @property
    @pulumi.getter(name="targetDbHomeId")
    def target_db_home_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Home.
        """
        return pulumi.get(self, "target_db_home_id")

    @property
    @pulumi.getter(name="targetDbVersion")
    def target_db_version(self) -> str:
        """
        A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.
        """
        return pulumi.get(self, "target_db_version")

    @property
    @pulumi.getter(name="timeEnded")
    def time_ended(self) -> str:
        """
        The date and time when the database upgrade ended.
        """
        return pulumi.get(self, "time_ended")

    @property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> str:
        """
        The date and time when the database upgrade started.
        """
        return pulumi.get(self, "time_started")

    @property
    @pulumi.getter(name="upgradeHistoryEntryId")
    def upgrade_history_entry_id(self) -> str:
        return pulumi.get(self, "upgrade_history_entry_id")


class AwaitableGetDatabaseUpgradeHistoryEntryResult(GetDatabaseUpgradeHistoryEntryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseUpgradeHistoryEntryResult(
            action=self.action,
            database_id=self.database_id,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            options=self.options,
            source=self.source,
            source_db_home_id=self.source_db_home_id,
            state=self.state,
            target_database_software_image_id=self.target_database_software_image_id,
            target_db_home_id=self.target_db_home_id,
            target_db_version=self.target_db_version,
            time_ended=self.time_ended,
            time_started=self.time_started,
            upgrade_history_entry_id=self.upgrade_history_entry_id)


def get_database_upgrade_history_entry(database_id: Optional[str] = None,
                                       upgrade_history_entry_id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseUpgradeHistoryEntryResult:
    """
    This data source provides details about a specific Database Upgrade History Entry resource in Oracle Cloud Infrastructure Database service.

    gets the upgrade history for a specified database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_upgrade_history_entry = oci.Database.get_database_upgrade_history_entry(database_id=test_database["id"],
        upgrade_history_entry_id=test_upgrade_history_entry["id"])
    ```


    :param str database_id: The database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str upgrade_history_entry_id: The database/db system upgrade History [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['databaseId'] = database_id
    __args__['upgradeHistoryEntryId'] = upgrade_history_entry_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getDatabaseUpgradeHistoryEntry:getDatabaseUpgradeHistoryEntry', __args__, opts=opts, typ=GetDatabaseUpgradeHistoryEntryResult).value

    return AwaitableGetDatabaseUpgradeHistoryEntryResult(
        action=pulumi.get(__ret__, 'action'),
        database_id=pulumi.get(__ret__, 'database_id'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        options=pulumi.get(__ret__, 'options'),
        source=pulumi.get(__ret__, 'source'),
        source_db_home_id=pulumi.get(__ret__, 'source_db_home_id'),
        state=pulumi.get(__ret__, 'state'),
        target_database_software_image_id=pulumi.get(__ret__, 'target_database_software_image_id'),
        target_db_home_id=pulumi.get(__ret__, 'target_db_home_id'),
        target_db_version=pulumi.get(__ret__, 'target_db_version'),
        time_ended=pulumi.get(__ret__, 'time_ended'),
        time_started=pulumi.get(__ret__, 'time_started'),
        upgrade_history_entry_id=pulumi.get(__ret__, 'upgrade_history_entry_id'))


@_utilities.lift_output_func(get_database_upgrade_history_entry)
def get_database_upgrade_history_entry_output(database_id: Optional[pulumi.Input[str]] = None,
                                              upgrade_history_entry_id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseUpgradeHistoryEntryResult]:
    """
    This data source provides details about a specific Database Upgrade History Entry resource in Oracle Cloud Infrastructure Database service.

    gets the upgrade history for a specified database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_upgrade_history_entry = oci.Database.get_database_upgrade_history_entry(database_id=test_database["id"],
        upgrade_history_entry_id=test_upgrade_history_entry["id"])
    ```


    :param str database_id: The database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str upgrade_history_entry_id: The database/db system upgrade History [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
