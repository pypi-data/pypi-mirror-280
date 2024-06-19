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
    'GetContainerImagesResult',
    'AwaitableGetContainerImagesResult',
    'get_container_images',
    'get_container_images_output',
]

@pulumi.output_type
class GetContainerImagesResult:
    """
    A collection of values returned by getContainerImages.
    """
    def __init__(__self__, compartment_id=None, compartment_id_in_subtree=None, container_image_collections=None, display_name=None, filters=None, id=None, image_id=None, is_versioned=None, repository_id=None, repository_name=None, state=None, version=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if container_image_collections and not isinstance(container_image_collections, list):
            raise TypeError("Expected argument 'container_image_collections' to be a list")
        pulumi.set(__self__, "container_image_collections", container_image_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if is_versioned and not isinstance(is_versioned, bool):
            raise TypeError("Expected argument 'is_versioned' to be a bool")
        pulumi.set(__self__, "is_versioned", is_versioned)
        if repository_id and not isinstance(repository_id, str):
            raise TypeError("Expected argument 'repository_id' to be a str")
        pulumi.set(__self__, "repository_id", repository_id)
        if repository_name and not isinstance(repository_name, str):
            raise TypeError("Expected argument 'repository_name' to be a str")
        pulumi.set(__self__, "repository_name", repository_name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The compartment OCID to which the container image belongs. Inferred from the container repository.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="containerImageCollections")
    def container_image_collections(self) -> Sequence['outputs.GetContainerImagesContainerImageCollectionResult']:
        """
        The list of container_image_collection.
        """
        return pulumi.get(self, "container_image_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The repository name and the most recent version associated with the image. If there are no versions associated with the image, then last known version and digest are used instead. If the last known version is unavailable, then 'unknown' is used instead of the version.  Example: `ubuntu:latest` or `ubuntu:latest@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetContainerImagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[str]:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="isVersioned")
    def is_versioned(self) -> Optional[bool]:
        return pulumi.get(self, "is_versioned")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container repository.
        """
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[str]:
        """
        The container repository name.
        """
        return pulumi.get(self, "repository_name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the container image.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version name.
        """
        return pulumi.get(self, "version")


class AwaitableGetContainerImagesResult(GetContainerImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerImagesResult(
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            container_image_collections=self.container_image_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            image_id=self.image_id,
            is_versioned=self.is_versioned,
            repository_id=self.repository_id,
            repository_name=self.repository_name,
            state=self.state,
            version=self.version)


def get_container_images(compartment_id: Optional[str] = None,
                         compartment_id_in_subtree: Optional[bool] = None,
                         display_name: Optional[str] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetContainerImagesFilterArgs']]] = None,
                         image_id: Optional[str] = None,
                         is_versioned: Optional[bool] = None,
                         repository_id: Optional[str] = None,
                         repository_name: Optional[str] = None,
                         state: Optional[str] = None,
                         version: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerImagesResult:
    """
    This data source provides the list of Container Images in Oracle Cloud Infrastructure Artifacts service.

    List container images in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_images = oci.Artifacts.get_container_images(compartment_id=compartment_id,
        compartment_id_in_subtree=container_image_compartment_id_in_subtree,
        display_name=container_image_display_name,
        image_id=test_image["id"],
        is_versioned=container_image_is_versioned,
        repository_id=test_repository["id"],
        repository_name=test_repository["name"],
        state=container_image_state,
        version=container_image_version)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param bool compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are inspected depending on the the setting of `accessLevel`. Default is false. Can only be set to true when calling the API on the tenancy (root compartment).
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str image_id: A filter to return a container image summary only for the specified container image OCID.
    :param bool is_versioned: A filter to return container images based on whether there are any associated versions.
    :param str repository_id: A filter to return container images only for the specified container repository OCID.
    :param str repository_name: A filter to return container images or container image signatures that match the repository name.  Example: `foo` or `foo*`
    :param str state: A filter to return only resources that match the given lifecycle state name exactly.
    :param str version: A filter to return container images that match the version.  Example: `foo` or `foo*`
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['imageId'] = image_id
    __args__['isVersioned'] = is_versioned
    __args__['repositoryId'] = repository_id
    __args__['repositoryName'] = repository_name
    __args__['state'] = state
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Artifacts/getContainerImages:getContainerImages', __args__, opts=opts, typ=GetContainerImagesResult).value

    return AwaitableGetContainerImagesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        container_image_collections=pulumi.get(__ret__, 'container_image_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        image_id=pulumi.get(__ret__, 'image_id'),
        is_versioned=pulumi.get(__ret__, 'is_versioned'),
        repository_id=pulumi.get(__ret__, 'repository_id'),
        repository_name=pulumi.get(__ret__, 'repository_name'),
        state=pulumi.get(__ret__, 'state'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_container_images)
def get_container_images_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                                display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetContainerImagesFilterArgs']]]]] = None,
                                image_id: Optional[pulumi.Input[Optional[str]]] = None,
                                is_versioned: Optional[pulumi.Input[Optional[bool]]] = None,
                                repository_id: Optional[pulumi.Input[Optional[str]]] = None,
                                repository_name: Optional[pulumi.Input[Optional[str]]] = None,
                                state: Optional[pulumi.Input[Optional[str]]] = None,
                                version: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerImagesResult]:
    """
    This data source provides the list of Container Images in Oracle Cloud Infrastructure Artifacts service.

    List container images in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_images = oci.Artifacts.get_container_images(compartment_id=compartment_id,
        compartment_id_in_subtree=container_image_compartment_id_in_subtree,
        display_name=container_image_display_name,
        image_id=test_image["id"],
        is_versioned=container_image_is_versioned,
        repository_id=test_repository["id"],
        repository_name=test_repository["name"],
        state=container_image_state,
        version=container_image_version)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param bool compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are inspected depending on the the setting of `accessLevel`. Default is false. Can only be set to true when calling the API on the tenancy (root compartment).
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str image_id: A filter to return a container image summary only for the specified container image OCID.
    :param bool is_versioned: A filter to return container images based on whether there are any associated versions.
    :param str repository_id: A filter to return container images only for the specified container repository OCID.
    :param str repository_name: A filter to return container images or container image signatures that match the repository name.  Example: `foo` or `foo*`
    :param str state: A filter to return only resources that match the given lifecycle state name exactly.
    :param str version: A filter to return container images that match the version.  Example: `foo` or `foo*`
    """
    ...
