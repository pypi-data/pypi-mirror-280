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
    'GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult',
    'AwaitableGetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult',
    'get_managed_database_sql_tuning_advisor_tasks_recommendations',
    'get_managed_database_sql_tuning_advisor_tasks_recommendations_output',
]

@pulumi.output_type
class GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult:
    """
    A collection of values returned by getManagedDatabaseSqlTuningAdvisorTasksRecommendations.
    """
    def __init__(__self__, execution_id=None, filters=None, id=None, managed_database_id=None, opc_named_credential_id=None, sql_object_id=None, sql_tuning_advisor_task_id=None, sql_tuning_advisor_task_recommendation_collections=None):
        if execution_id and not isinstance(execution_id, str):
            raise TypeError("Expected argument 'execution_id' to be a str")
        pulumi.set(__self__, "execution_id", execution_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if opc_named_credential_id and not isinstance(opc_named_credential_id, str):
            raise TypeError("Expected argument 'opc_named_credential_id' to be a str")
        pulumi.set(__self__, "opc_named_credential_id", opc_named_credential_id)
        if sql_object_id and not isinstance(sql_object_id, str):
            raise TypeError("Expected argument 'sql_object_id' to be a str")
        pulumi.set(__self__, "sql_object_id", sql_object_id)
        if sql_tuning_advisor_task_id and not isinstance(sql_tuning_advisor_task_id, str):
            raise TypeError("Expected argument 'sql_tuning_advisor_task_id' to be a str")
        pulumi.set(__self__, "sql_tuning_advisor_task_id", sql_tuning_advisor_task_id)
        if sql_tuning_advisor_task_recommendation_collections and not isinstance(sql_tuning_advisor_task_recommendation_collections, list):
            raise TypeError("Expected argument 'sql_tuning_advisor_task_recommendation_collections' to be a list")
        pulumi.set(__self__, "sql_tuning_advisor_task_recommendation_collections", sql_tuning_advisor_task_recommendation_collections)

    @property
    @pulumi.getter(name="executionId")
    def execution_id(self) -> str:
        return pulumi.get(self, "execution_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsFilterResult']]:
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
    @pulumi.getter(name="opcNamedCredentialId")
    def opc_named_credential_id(self) -> Optional[str]:
        return pulumi.get(self, "opc_named_credential_id")

    @property
    @pulumi.getter(name="sqlObjectId")
    def sql_object_id(self) -> str:
        return pulumi.get(self, "sql_object_id")

    @property
    @pulumi.getter(name="sqlTuningAdvisorTaskId")
    def sql_tuning_advisor_task_id(self) -> str:
        """
        The unique identifier of the task. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "sql_tuning_advisor_task_id")

    @property
    @pulumi.getter(name="sqlTuningAdvisorTaskRecommendationCollections")
    def sql_tuning_advisor_task_recommendation_collections(self) -> Sequence['outputs.GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsSqlTuningAdvisorTaskRecommendationCollectionResult']:
        """
        The list of sql_tuning_advisor_task_recommendation_collection.
        """
        return pulumi.get(self, "sql_tuning_advisor_task_recommendation_collections")


class AwaitableGetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult(GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult(
            execution_id=self.execution_id,
            filters=self.filters,
            id=self.id,
            managed_database_id=self.managed_database_id,
            opc_named_credential_id=self.opc_named_credential_id,
            sql_object_id=self.sql_object_id,
            sql_tuning_advisor_task_id=self.sql_tuning_advisor_task_id,
            sql_tuning_advisor_task_recommendation_collections=self.sql_tuning_advisor_task_recommendation_collections)


def get_managed_database_sql_tuning_advisor_tasks_recommendations(execution_id: Optional[str] = None,
                                                                  filters: Optional[Sequence[pulumi.InputType['GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsFilterArgs']]] = None,
                                                                  managed_database_id: Optional[str] = None,
                                                                  opc_named_credential_id: Optional[str] = None,
                                                                  sql_object_id: Optional[str] = None,
                                                                  sql_tuning_advisor_task_id: Optional[str] = None,
                                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult:
    """
    This data source provides the list of Managed Database Sql Tuning Advisor Tasks Recommendations in Oracle Cloud Infrastructure Database Management service.

    Gets the findings and possible actions for a given object in a SQL tuning task.
    The task ID and object ID are used to retrieve the findings and recommendations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_sql_tuning_advisor_tasks_recommendations = oci.DatabaseManagement.get_managed_database_sql_tuning_advisor_tasks_recommendations(execution_id=test_execution["id"],
        managed_database_id=test_managed_database["id"],
        sql_object_id=test_object["id"],
        sql_tuning_advisor_task_id=test_sql_tuning_advisor_task["id"],
        opc_named_credential_id=managed_database_sql_tuning_advisor_tasks_recommendation_opc_named_credential_id)
    ```


    :param str execution_id: The execution ID for an execution of a SQL tuning task. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str opc_named_credential_id: The OCID of the Named Credential.
    :param str sql_object_id: The SQL object ID for the SQL tuning task. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str sql_tuning_advisor_task_id: The SQL tuning task identifier. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['executionId'] = execution_id
    __args__['filters'] = filters
    __args__['managedDatabaseId'] = managed_database_id
    __args__['opcNamedCredentialId'] = opc_named_credential_id
    __args__['sqlObjectId'] = sql_object_id
    __args__['sqlTuningAdvisorTaskId'] = sql_tuning_advisor_task_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseSqlTuningAdvisorTasksRecommendations:getManagedDatabaseSqlTuningAdvisorTasksRecommendations', __args__, opts=opts, typ=GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult).value

    return AwaitableGetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult(
        execution_id=pulumi.get(__ret__, 'execution_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        opc_named_credential_id=pulumi.get(__ret__, 'opc_named_credential_id'),
        sql_object_id=pulumi.get(__ret__, 'sql_object_id'),
        sql_tuning_advisor_task_id=pulumi.get(__ret__, 'sql_tuning_advisor_task_id'),
        sql_tuning_advisor_task_recommendation_collections=pulumi.get(__ret__, 'sql_tuning_advisor_task_recommendation_collections'))


@_utilities.lift_output_func(get_managed_database_sql_tuning_advisor_tasks_recommendations)
def get_managed_database_sql_tuning_advisor_tasks_recommendations_output(execution_id: Optional[pulumi.Input[str]] = None,
                                                                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsFilterArgs']]]]] = None,
                                                                         managed_database_id: Optional[pulumi.Input[str]] = None,
                                                                         opc_named_credential_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                                         sql_object_id: Optional[pulumi.Input[str]] = None,
                                                                         sql_tuning_advisor_task_id: Optional[pulumi.Input[str]] = None,
                                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseSqlTuningAdvisorTasksRecommendationsResult]:
    """
    This data source provides the list of Managed Database Sql Tuning Advisor Tasks Recommendations in Oracle Cloud Infrastructure Database Management service.

    Gets the findings and possible actions for a given object in a SQL tuning task.
    The task ID and object ID are used to retrieve the findings and recommendations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_sql_tuning_advisor_tasks_recommendations = oci.DatabaseManagement.get_managed_database_sql_tuning_advisor_tasks_recommendations(execution_id=test_execution["id"],
        managed_database_id=test_managed_database["id"],
        sql_object_id=test_object["id"],
        sql_tuning_advisor_task_id=test_sql_tuning_advisor_task["id"],
        opc_named_credential_id=managed_database_sql_tuning_advisor_tasks_recommendation_opc_named_credential_id)
    ```


    :param str execution_id: The execution ID for an execution of a SQL tuning task. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str opc_named_credential_id: The OCID of the Named Credential.
    :param str sql_object_id: The SQL object ID for the SQL tuning task. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str sql_tuning_advisor_task_id: The SQL tuning task identifier. This is not the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
