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
    'GetRepositoriesResult',
    'AwaitableGetRepositoriesResult',
    'get_repositories',
    'get_repositories_output',
]

@pulumi.output_type
class GetRepositoriesResult:
    """
    A collection of values returned by getRepositories.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, project_id=None, repository_collections=None, repository_id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if repository_collections and not isinstance(repository_collections, list):
            raise TypeError("Expected argument 'repository_collections' to be a list")
        pulumi.set(__self__, "repository_collections", repository_collections)
        if repository_id and not isinstance(repository_id, str):
            raise TypeError("Expected argument 'repository_id' to be a str")
        pulumi.set(__self__, "repository_id", repository_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The OCID of the repository's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRepositoriesFilterResult']]:
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
        Unique name of a repository. This value is mutable.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The OCID of the DevOps project containing the repository.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="repositoryCollections")
    def repository_collections(self) -> Sequence['outputs.GetRepositoriesRepositoryCollectionResult']:
        """
        The list of repository_collection.
        """
        return pulumi.get(self, "repository_collections")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[str]:
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the repository.
        """
        return pulumi.get(self, "state")


class AwaitableGetRepositoriesResult(GetRepositoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoriesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            project_id=self.project_id,
            repository_collections=self.repository_collections,
            repository_id=self.repository_id,
            state=self.state)


def get_repositories(compartment_id: Optional[str] = None,
                     filters: Optional[Sequence[pulumi.InputType['GetRepositoriesFilterArgs']]] = None,
                     name: Optional[str] = None,
                     project_id: Optional[str] = None,
                     repository_id: Optional[str] = None,
                     state: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoriesResult:
    """
    This data source provides the list of Repositories in Oracle Cloud Infrastructure Devops service.

    Returns a list of repositories given a compartment ID or a project ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_repositories = oci.DevOps.get_repositories(compartment_id=compartment_id,
        name=repository_name,
        project_id=test_project["id"],
        repository_id=test_repository["id"],
        state=repository_state)
    ```


    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str name: A filter to return only resources that match the entire name given.
    :param str project_id: unique project identifier
    :param str repository_id: Unique repository identifier.
    :param str state: A filter to return only resources whose lifecycle state matches the given lifecycle state.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['projectId'] = project_id
    __args__['repositoryId'] = repository_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DevOps/getRepositories:getRepositories', __args__, opts=opts, typ=GetRepositoriesResult).value

    return AwaitableGetRepositoriesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        project_id=pulumi.get(__ret__, 'project_id'),
        repository_collections=pulumi.get(__ret__, 'repository_collections'),
        repository_id=pulumi.get(__ret__, 'repository_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_repositories)
def get_repositories_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetRepositoriesFilterArgs']]]]] = None,
                            name: Optional[pulumi.Input[Optional[str]]] = None,
                            project_id: Optional[pulumi.Input[Optional[str]]] = None,
                            repository_id: Optional[pulumi.Input[Optional[str]]] = None,
                            state: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoriesResult]:
    """
    This data source provides the list of Repositories in Oracle Cloud Infrastructure Devops service.

    Returns a list of repositories given a compartment ID or a project ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_repositories = oci.DevOps.get_repositories(compartment_id=compartment_id,
        name=repository_name,
        project_id=test_project["id"],
        repository_id=test_repository["id"],
        state=repository_state)
    ```


    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str name: A filter to return only resources that match the entire name given.
    :param str project_id: unique project identifier
    :param str repository_id: Unique repository identifier.
    :param str state: A filter to return only resources whose lifecycle state matches the given lifecycle state.
    """
    ...
