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
    'GetManagementAgentImagesResult',
    'AwaitableGetManagementAgentImagesResult',
    'get_management_agent_images',
    'get_management_agent_images_output',
]

@pulumi.output_type
class GetManagementAgentImagesResult:
    """
    A collection of values returned by getManagementAgentImages.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, install_type=None, management_agent_images=None, name=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if install_type and not isinstance(install_type, str):
            raise TypeError("Expected argument 'install_type' to be a str")
        pulumi.set(__self__, "install_type", install_type)
        if management_agent_images and not isinstance(management_agent_images, list):
            raise TypeError("Expected argument 'management_agent_images' to be a list")
        pulumi.set(__self__, "management_agent_images", management_agent_images)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagementAgentImagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installType")
    def install_type(self) -> Optional[str]:
        return pulumi.get(self, "install_type")

    @property
    @pulumi.getter(name="managementAgentImages")
    def management_agent_images(self) -> Sequence['outputs.GetManagementAgentImagesManagementAgentImageResult']:
        """
        The list of management_agent_images.
        """
        return pulumi.get(self, "management_agent_images")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of Management Agent Image
        """
        return pulumi.get(self, "state")


class AwaitableGetManagementAgentImagesResult(GetManagementAgentImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementAgentImagesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            install_type=self.install_type,
            management_agent_images=self.management_agent_images,
            name=self.name,
            state=self.state)


def get_management_agent_images(compartment_id: Optional[str] = None,
                                filters: Optional[Sequence[pulumi.InputType['GetManagementAgentImagesFilterArgs']]] = None,
                                install_type: Optional[str] = None,
                                name: Optional[str] = None,
                                state: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementAgentImagesResult:
    """
    This data source provides the list of Management Agent Images in Oracle Cloud Infrastructure Management Agent service.

    Get supported agent image information

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_management_agent_images = oci.ManagementAgent.get_management_agent_images(compartment_id=compartment_id,
        install_type=management_agent_image_install_type,
        name=management_agent_image_name,
        state=management_agent_image_state)
    ```


    :param str compartment_id: The OCID of the compartment to which a request will be scoped.
    :param str install_type: A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.
    :param str name: A filter to return only resources that match the entire platform name given.
    :param str state: Filter to return only Management Agents in the particular lifecycle state.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['installType'] = install_type
    __args__['name'] = name
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ManagementAgent/getManagementAgentImages:getManagementAgentImages', __args__, opts=opts, typ=GetManagementAgentImagesResult).value

    return AwaitableGetManagementAgentImagesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        install_type=pulumi.get(__ret__, 'install_type'),
        management_agent_images=pulumi.get(__ret__, 'management_agent_images'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_management_agent_images)
def get_management_agent_images_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagementAgentImagesFilterArgs']]]]] = None,
                                       install_type: Optional[pulumi.Input[Optional[str]]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       state: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagementAgentImagesResult]:
    """
    This data source provides the list of Management Agent Images in Oracle Cloud Infrastructure Management Agent service.

    Get supported agent image information

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_management_agent_images = oci.ManagementAgent.get_management_agent_images(compartment_id=compartment_id,
        install_type=management_agent_image_install_type,
        name=management_agent_image_name,
        state=management_agent_image_state)
    ```


    :param str compartment_id: The OCID of the compartment to which a request will be scoped.
    :param str install_type: A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.
    :param str name: A filter to return only resources that match the entire platform name given.
    :param str state: Filter to return only Management Agents in the particular lifecycle state.
    """
    ...
