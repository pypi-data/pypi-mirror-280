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
    'GetDiscoveryJobsResultsResult',
    'AwaitableGetDiscoveryJobsResultsResult',
    'get_discovery_jobs_results',
    'get_discovery_jobs_results_output',
]

@pulumi.output_type
class GetDiscoveryJobsResultsResult:
    """
    A collection of values returned by getDiscoveryJobsResults.
    """
    def __init__(__self__, column_names=None, discovery_job_id=None, discovery_job_result_collections=None, discovery_type=None, filters=None, id=None, is_result_applied=None, objects=None, planned_action=None, schema_names=None):
        if column_names and not isinstance(column_names, list):
            raise TypeError("Expected argument 'column_names' to be a list")
        pulumi.set(__self__, "column_names", column_names)
        if discovery_job_id and not isinstance(discovery_job_id, str):
            raise TypeError("Expected argument 'discovery_job_id' to be a str")
        pulumi.set(__self__, "discovery_job_id", discovery_job_id)
        if discovery_job_result_collections and not isinstance(discovery_job_result_collections, list):
            raise TypeError("Expected argument 'discovery_job_result_collections' to be a list")
        pulumi.set(__self__, "discovery_job_result_collections", discovery_job_result_collections)
        if discovery_type and not isinstance(discovery_type, str):
            raise TypeError("Expected argument 'discovery_type' to be a str")
        pulumi.set(__self__, "discovery_type", discovery_type)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_result_applied and not isinstance(is_result_applied, bool):
            raise TypeError("Expected argument 'is_result_applied' to be a bool")
        pulumi.set(__self__, "is_result_applied", is_result_applied)
        if objects and not isinstance(objects, list):
            raise TypeError("Expected argument 'objects' to be a list")
        pulumi.set(__self__, "objects", objects)
        if planned_action and not isinstance(planned_action, str):
            raise TypeError("Expected argument 'planned_action' to be a str")
        pulumi.set(__self__, "planned_action", planned_action)
        if schema_names and not isinstance(schema_names, list):
            raise TypeError("Expected argument 'schema_names' to be a list")
        pulumi.set(__self__, "schema_names", schema_names)

    @property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[str]]:
        """
        The name of the sensitive column.
        """
        return pulumi.get(self, "column_names")

    @property
    @pulumi.getter(name="discoveryJobId")
    def discovery_job_id(self) -> str:
        """
        The OCID of the discovery job.
        """
        return pulumi.get(self, "discovery_job_id")

    @property
    @pulumi.getter(name="discoveryJobResultCollections")
    def discovery_job_result_collections(self) -> Sequence['outputs.GetDiscoveryJobsResultsDiscoveryJobResultCollectionResult']:
        """
        The list of discovery_job_result_collection.
        """
        return pulumi.get(self, "discovery_job_result_collections")

    @property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[str]:
        """
        The type of the discovery result. It can be one of the following three types: NEW: A new sensitive column in the target database that is not in the sensitive data model. DELETED: A column that is present in the sensitive data model but has been deleted from the target database. MODIFIED: A column that is present in the target database as well as the sensitive data model but some of its attributes have been modified.
        """
        return pulumi.get(self, "discovery_type")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDiscoveryJobsResultsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isResultApplied")
    def is_result_applied(self) -> Optional[bool]:
        """
        Indicates whether the discovery result has been processed. You can update this attribute using the PatchDiscoveryJobResults operation to track whether the discovery result has already been processed and applied to the sensitive data model.
        """
        return pulumi.get(self, "is_result_applied")

    @property
    @pulumi.getter
    def objects(self) -> Optional[Sequence[str]]:
        """
        The database object that contains the sensitive column.
        """
        return pulumi.get(self, "objects")

    @property
    @pulumi.getter(name="plannedAction")
    def planned_action(self) -> Optional[str]:
        """
        Specifies how to process the discovery result. It's set to NONE by default. Use the PatchDiscoveryJobResults operation to update this attribute. You can choose one of the following options: ACCEPT: To accept the discovery result and update the sensitive data model to reflect the changes. REJECT: To reject the discovery result so that it doesn't change the sensitive data model. INVALIDATE: To invalidate a newly discovered column. It adds the column to the sensitive data model but marks it as invalid. It helps track false positives and ensure that they aren't reported by future discovery jobs. After specifying the planned action, you can use the ApplyDiscoveryJobResults operation to automatically process the discovery results.
        """
        return pulumi.get(self, "planned_action")

    @property
    @pulumi.getter(name="schemaNames")
    def schema_names(self) -> Optional[Sequence[str]]:
        """
        The database schema that contains the sensitive column.
        """
        return pulumi.get(self, "schema_names")


class AwaitableGetDiscoveryJobsResultsResult(GetDiscoveryJobsResultsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiscoveryJobsResultsResult(
            column_names=self.column_names,
            discovery_job_id=self.discovery_job_id,
            discovery_job_result_collections=self.discovery_job_result_collections,
            discovery_type=self.discovery_type,
            filters=self.filters,
            id=self.id,
            is_result_applied=self.is_result_applied,
            objects=self.objects,
            planned_action=self.planned_action,
            schema_names=self.schema_names)


def get_discovery_jobs_results(column_names: Optional[Sequence[str]] = None,
                               discovery_job_id: Optional[str] = None,
                               discovery_type: Optional[str] = None,
                               filters: Optional[Sequence[pulumi.InputType['GetDiscoveryJobsResultsFilterArgs']]] = None,
                               is_result_applied: Optional[bool] = None,
                               objects: Optional[Sequence[str]] = None,
                               planned_action: Optional[str] = None,
                               schema_names: Optional[Sequence[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiscoveryJobsResultsResult:
    """
    This data source provides the list of Discovery Jobs Results in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of discovery results based on the specified query parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_discovery_jobs_results = oci.DataSafe.get_discovery_jobs_results(discovery_job_id=test_discovery_job["id"],
        column_names=discovery_jobs_result_column_name,
        discovery_type=discovery_jobs_result_discovery_type,
        is_result_applied=discovery_jobs_result_is_result_applied,
        objects=discovery_jobs_result_object,
        planned_action=discovery_jobs_result_planned_action,
        schema_names=discovery_jobs_result_schema_name)
    ```


    :param Sequence[str] column_names: A filter to return only a specific column based on column name.
    :param str discovery_job_id: The OCID of the discovery job.
    :param str discovery_type: A filter to return only the resources that match the specified discovery type.
    :param bool is_result_applied: A filter to return the discovery result resources based on the value of their isResultApplied attribute.
    :param Sequence[str] objects: A filter to return only items related to a specific object name.
    :param str planned_action: A filter to return only the resources that match the specified planned action.
    :param Sequence[str] schema_names: A filter to return only items related to specific schema name.
    """
    __args__ = dict()
    __args__['columnNames'] = column_names
    __args__['discoveryJobId'] = discovery_job_id
    __args__['discoveryType'] = discovery_type
    __args__['filters'] = filters
    __args__['isResultApplied'] = is_result_applied
    __args__['objects'] = objects
    __args__['plannedAction'] = planned_action
    __args__['schemaNames'] = schema_names
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getDiscoveryJobsResults:getDiscoveryJobsResults', __args__, opts=opts, typ=GetDiscoveryJobsResultsResult).value

    return AwaitableGetDiscoveryJobsResultsResult(
        column_names=pulumi.get(__ret__, 'column_names'),
        discovery_job_id=pulumi.get(__ret__, 'discovery_job_id'),
        discovery_job_result_collections=pulumi.get(__ret__, 'discovery_job_result_collections'),
        discovery_type=pulumi.get(__ret__, 'discovery_type'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_result_applied=pulumi.get(__ret__, 'is_result_applied'),
        objects=pulumi.get(__ret__, 'objects'),
        planned_action=pulumi.get(__ret__, 'planned_action'),
        schema_names=pulumi.get(__ret__, 'schema_names'))


@_utilities.lift_output_func(get_discovery_jobs_results)
def get_discovery_jobs_results_output(column_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      discovery_job_id: Optional[pulumi.Input[str]] = None,
                                      discovery_type: Optional[pulumi.Input[Optional[str]]] = None,
                                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDiscoveryJobsResultsFilterArgs']]]]] = None,
                                      is_result_applied: Optional[pulumi.Input[Optional[bool]]] = None,
                                      objects: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      planned_action: Optional[pulumi.Input[Optional[str]]] = None,
                                      schema_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiscoveryJobsResultsResult]:
    """
    This data source provides the list of Discovery Jobs Results in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of discovery results based on the specified query parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_discovery_jobs_results = oci.DataSafe.get_discovery_jobs_results(discovery_job_id=test_discovery_job["id"],
        column_names=discovery_jobs_result_column_name,
        discovery_type=discovery_jobs_result_discovery_type,
        is_result_applied=discovery_jobs_result_is_result_applied,
        objects=discovery_jobs_result_object,
        planned_action=discovery_jobs_result_planned_action,
        schema_names=discovery_jobs_result_schema_name)
    ```


    :param Sequence[str] column_names: A filter to return only a specific column based on column name.
    :param str discovery_job_id: The OCID of the discovery job.
    :param str discovery_type: A filter to return only the resources that match the specified discovery type.
    :param bool is_result_applied: A filter to return the discovery result resources based on the value of their isResultApplied attribute.
    :param Sequence[str] objects: A filter to return only items related to a specific object name.
    :param str planned_action: A filter to return only the resources that match the specified planned action.
    :param Sequence[str] schema_names: A filter to return only items related to specific schema name.
    """
    ...
