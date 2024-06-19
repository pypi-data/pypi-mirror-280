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
    'GetWorkspaceFoldersResult',
    'AwaitableGetWorkspaceFoldersResult',
    'get_workspace_folders',
    'get_workspace_folders_output',
]

@pulumi.output_type
class GetWorkspaceFoldersResult:
    """
    A collection of values returned by getWorkspaceFolders.
    """
    def __init__(__self__, aggregator_key=None, fields=None, filters=None, folder_summary_collections=None, id=None, identifiers=None, name=None, name_contains=None, workspace_id=None):
        if aggregator_key and not isinstance(aggregator_key, str):
            raise TypeError("Expected argument 'aggregator_key' to be a str")
        pulumi.set(__self__, "aggregator_key", aggregator_key)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if folder_summary_collections and not isinstance(folder_summary_collections, list):
            raise TypeError("Expected argument 'folder_summary_collections' to be a list")
        pulumi.set(__self__, "folder_summary_collections", folder_summary_collections)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identifiers and not isinstance(identifiers, list):
            raise TypeError("Expected argument 'identifiers' to be a list")
        pulumi.set(__self__, "identifiers", identifiers)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_contains and not isinstance(name_contains, str):
            raise TypeError("Expected argument 'name_contains' to be a str")
        pulumi.set(__self__, "name_contains", name_contains)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="aggregatorKey")
    def aggregator_key(self) -> Optional[str]:
        """
        The owning object key for this object.
        """
        return pulumi.get(self, "aggregator_key")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetWorkspaceFoldersFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="folderSummaryCollections")
    def folder_summary_collections(self) -> Sequence['outputs.GetWorkspaceFoldersFolderSummaryCollectionResult']:
        """
        The list of folder_summary_collection.
        """
        return pulumi.get(self, "folder_summary_collections")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identifiers(self) -> Optional[Sequence[str]]:
        """
        The identifier of the aggregator.
        """
        return pulumi.get(self, "identifiers")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameContains")
    def name_contains(self) -> Optional[str]:
        return pulumi.get(self, "name_contains")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> str:
        return pulumi.get(self, "workspace_id")


class AwaitableGetWorkspaceFoldersResult(GetWorkspaceFoldersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceFoldersResult(
            aggregator_key=self.aggregator_key,
            fields=self.fields,
            filters=self.filters,
            folder_summary_collections=self.folder_summary_collections,
            id=self.id,
            identifiers=self.identifiers,
            name=self.name,
            name_contains=self.name_contains,
            workspace_id=self.workspace_id)


def get_workspace_folders(aggregator_key: Optional[str] = None,
                          fields: Optional[Sequence[str]] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetWorkspaceFoldersFilterArgs']]] = None,
                          identifiers: Optional[Sequence[str]] = None,
                          name: Optional[str] = None,
                          name_contains: Optional[str] = None,
                          workspace_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceFoldersResult:
    """
    This data source provides the list of Workspace Folders in Oracle Cloud Infrastructure Data Integration service.

    Retrieves a list of folders in a project and provides options to filter the list.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_workspace_folders = oci.DataIntegration.get_workspace_folders(workspace_id=test_workspace["id"],
        aggregator_key=workspace_folder_aggregator_key,
        fields=workspace_folder_fields,
        identifiers=workspace_folder_identifier,
        name=workspace_folder_name,
        name_contains=workspace_folder_name_contains)
    ```


    :param str aggregator_key: Used to filter by the project or the folder object.
    :param Sequence[str] fields: Specifies the fields to get for an object.
    :param Sequence[str] identifiers: Used to filter by the identifier of the object.
    :param str name: Used to filter by the name of the object.
    :param str name_contains: This parameter can be used to filter objects by the names that match partially or fully with the given value.
    :param str workspace_id: The workspace ID.
    """
    __args__ = dict()
    __args__['aggregatorKey'] = aggregator_key
    __args__['fields'] = fields
    __args__['filters'] = filters
    __args__['identifiers'] = identifiers
    __args__['name'] = name
    __args__['nameContains'] = name_contains
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataIntegration/getWorkspaceFolders:getWorkspaceFolders', __args__, opts=opts, typ=GetWorkspaceFoldersResult).value

    return AwaitableGetWorkspaceFoldersResult(
        aggregator_key=pulumi.get(__ret__, 'aggregator_key'),
        fields=pulumi.get(__ret__, 'fields'),
        filters=pulumi.get(__ret__, 'filters'),
        folder_summary_collections=pulumi.get(__ret__, 'folder_summary_collections'),
        id=pulumi.get(__ret__, 'id'),
        identifiers=pulumi.get(__ret__, 'identifiers'),
        name=pulumi.get(__ret__, 'name'),
        name_contains=pulumi.get(__ret__, 'name_contains'),
        workspace_id=pulumi.get(__ret__, 'workspace_id'))


@_utilities.lift_output_func(get_workspace_folders)
def get_workspace_folders_output(aggregator_key: Optional[pulumi.Input[Optional[str]]] = None,
                                 fields: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetWorkspaceFoldersFilterArgs']]]]] = None,
                                 identifiers: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 name: Optional[pulumi.Input[Optional[str]]] = None,
                                 name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                 workspace_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceFoldersResult]:
    """
    This data source provides the list of Workspace Folders in Oracle Cloud Infrastructure Data Integration service.

    Retrieves a list of folders in a project and provides options to filter the list.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_workspace_folders = oci.DataIntegration.get_workspace_folders(workspace_id=test_workspace["id"],
        aggregator_key=workspace_folder_aggregator_key,
        fields=workspace_folder_fields,
        identifiers=workspace_folder_identifier,
        name=workspace_folder_name,
        name_contains=workspace_folder_name_contains)
    ```


    :param str aggregator_key: Used to filter by the project or the folder object.
    :param Sequence[str] fields: Specifies the fields to get for an object.
    :param Sequence[str] identifiers: Used to filter by the identifier of the object.
    :param str name: Used to filter by the name of the object.
    :param str name_contains: This parameter can be used to filter objects by the names that match partially or fully with the given value.
    :param str workspace_id: The workspace ID.
    """
    ...
