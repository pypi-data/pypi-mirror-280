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
    'GetWorkspaceExportRequestsResult',
    'AwaitableGetWorkspaceExportRequestsResult',
    'get_workspace_export_requests',
    'get_workspace_export_requests_output',
]

@pulumi.output_type
class GetWorkspaceExportRequestsResult:
    """
    A collection of values returned by getWorkspaceExportRequests.
    """
    def __init__(__self__, export_request_summary_collections=None, export_status=None, filters=None, id=None, name=None, projection=None, time_ended_in_millis=None, time_started_in_millis=None, workspace_id=None):
        if export_request_summary_collections and not isinstance(export_request_summary_collections, list):
            raise TypeError("Expected argument 'export_request_summary_collections' to be a list")
        pulumi.set(__self__, "export_request_summary_collections", export_request_summary_collections)
        if export_status and not isinstance(export_status, str):
            raise TypeError("Expected argument 'export_status' to be a str")
        pulumi.set(__self__, "export_status", export_status)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if projection and not isinstance(projection, str):
            raise TypeError("Expected argument 'projection' to be a str")
        pulumi.set(__self__, "projection", projection)
        if time_ended_in_millis and not isinstance(time_ended_in_millis, str):
            raise TypeError("Expected argument 'time_ended_in_millis' to be a str")
        pulumi.set(__self__, "time_ended_in_millis", time_ended_in_millis)
        if time_started_in_millis and not isinstance(time_started_in_millis, str):
            raise TypeError("Expected argument 'time_started_in_millis' to be a str")
        pulumi.set(__self__, "time_started_in_millis", time_started_in_millis)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="exportRequestSummaryCollections")
    def export_request_summary_collections(self) -> Sequence['outputs.GetWorkspaceExportRequestsExportRequestSummaryCollectionResult']:
        """
        The list of export_request_summary_collection.
        """
        return pulumi.get(self, "export_request_summary_collections")

    @property
    @pulumi.getter(name="exportStatus")
    def export_status(self) -> Optional[str]:
        return pulumi.get(self, "export_status")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetWorkspaceExportRequestsFilterResult']]:
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
    def name(self) -> Optional[str]:
        """
        Name of the export request.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def projection(self) -> Optional[str]:
        return pulumi.get(self, "projection")

    @property
    @pulumi.getter(name="timeEndedInMillis")
    def time_ended_in_millis(self) -> Optional[str]:
        """
        Time at which the request was completely processed.
        """
        return pulumi.get(self, "time_ended_in_millis")

    @property
    @pulumi.getter(name="timeStartedInMillis")
    def time_started_in_millis(self) -> Optional[str]:
        """
        Time at which the request started getting processed.
        """
        return pulumi.get(self, "time_started_in_millis")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> str:
        return pulumi.get(self, "workspace_id")


class AwaitableGetWorkspaceExportRequestsResult(GetWorkspaceExportRequestsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceExportRequestsResult(
            export_request_summary_collections=self.export_request_summary_collections,
            export_status=self.export_status,
            filters=self.filters,
            id=self.id,
            name=self.name,
            projection=self.projection,
            time_ended_in_millis=self.time_ended_in_millis,
            time_started_in_millis=self.time_started_in_millis,
            workspace_id=self.workspace_id)


def get_workspace_export_requests(export_status: Optional[str] = None,
                                  filters: Optional[Sequence[pulumi.InputType['GetWorkspaceExportRequestsFilterArgs']]] = None,
                                  name: Optional[str] = None,
                                  projection: Optional[str] = None,
                                  time_ended_in_millis: Optional[str] = None,
                                  time_started_in_millis: Optional[str] = None,
                                  workspace_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceExportRequestsResult:
    """
    This data source provides the list of Workspace Export Requests in Oracle Cloud Infrastructure Data Integration service.

    This endpoint can be used to get the list of export object requests.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_workspace_export_requests = oci.DataIntegration.get_workspace_export_requests(workspace_id=test_workspace["id"],
        export_status=workspace_export_request_export_status,
        name=workspace_export_request_name,
        projection=workspace_export_request_projection,
        time_ended_in_millis=workspace_export_request_time_ended_in_millis,
        time_started_in_millis=workspace_export_request_time_started_in_millis)
    ```


    :param str export_status: Specifies export status to use, either -  ALL, SUCCESSFUL, IN_PROGRESS, QUEUED, FAILED .
    :param str name: Used to filter by the name of the object.
    :param str projection: This parameter allows users to specify which view of the export object response to return. SUMMARY - Summary of the export object request will be returned. This is the default option when no value is specified. DETAILS - Details of export object request will be returned. This will include details of all the objects to be exported.
    :param str time_ended_in_millis: Specifies end time of a copy object request.
    :param str time_started_in_millis: Specifies start time of a copy object request.
    :param str workspace_id: The workspace ID.
    """
    __args__ = dict()
    __args__['exportStatus'] = export_status
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['projection'] = projection
    __args__['timeEndedInMillis'] = time_ended_in_millis
    __args__['timeStartedInMillis'] = time_started_in_millis
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataIntegration/getWorkspaceExportRequests:getWorkspaceExportRequests', __args__, opts=opts, typ=GetWorkspaceExportRequestsResult).value

    return AwaitableGetWorkspaceExportRequestsResult(
        export_request_summary_collections=pulumi.get(__ret__, 'export_request_summary_collections'),
        export_status=pulumi.get(__ret__, 'export_status'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        projection=pulumi.get(__ret__, 'projection'),
        time_ended_in_millis=pulumi.get(__ret__, 'time_ended_in_millis'),
        time_started_in_millis=pulumi.get(__ret__, 'time_started_in_millis'),
        workspace_id=pulumi.get(__ret__, 'workspace_id'))


@_utilities.lift_output_func(get_workspace_export_requests)
def get_workspace_export_requests_output(export_status: Optional[pulumi.Input[Optional[str]]] = None,
                                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetWorkspaceExportRequestsFilterArgs']]]]] = None,
                                         name: Optional[pulumi.Input[Optional[str]]] = None,
                                         projection: Optional[pulumi.Input[Optional[str]]] = None,
                                         time_ended_in_millis: Optional[pulumi.Input[Optional[str]]] = None,
                                         time_started_in_millis: Optional[pulumi.Input[Optional[str]]] = None,
                                         workspace_id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceExportRequestsResult]:
    """
    This data source provides the list of Workspace Export Requests in Oracle Cloud Infrastructure Data Integration service.

    This endpoint can be used to get the list of export object requests.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_workspace_export_requests = oci.DataIntegration.get_workspace_export_requests(workspace_id=test_workspace["id"],
        export_status=workspace_export_request_export_status,
        name=workspace_export_request_name,
        projection=workspace_export_request_projection,
        time_ended_in_millis=workspace_export_request_time_ended_in_millis,
        time_started_in_millis=workspace_export_request_time_started_in_millis)
    ```


    :param str export_status: Specifies export status to use, either -  ALL, SUCCESSFUL, IN_PROGRESS, QUEUED, FAILED .
    :param str name: Used to filter by the name of the object.
    :param str projection: This parameter allows users to specify which view of the export object response to return. SUMMARY - Summary of the export object request will be returned. This is the default option when no value is specified. DETAILS - Details of export object request will be returned. This will include details of all the objects to be exported.
    :param str time_ended_in_millis: Specifies end time of a copy object request.
    :param str time_started_in_millis: Specifies start time of a copy object request.
    :param str workspace_id: The workspace ID.
    """
    ...
