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

__all__ = [
    'GetImageShapeResult',
    'AwaitableGetImageShapeResult',
    'get_image_shape',
    'get_image_shape_output',
]

@pulumi.output_type
class GetImageShapeResult:
    """
    A collection of values returned by getImageShape.
    """
    def __init__(__self__, id=None, image_id=None, memory_constraints=None, ocpu_constraints=None, shape=None, shape_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if memory_constraints and not isinstance(memory_constraints, list):
            raise TypeError("Expected argument 'memory_constraints' to be a list")
        pulumi.set(__self__, "memory_constraints", memory_constraints)
        if ocpu_constraints and not isinstance(ocpu_constraints, list):
            raise TypeError("Expected argument 'ocpu_constraints' to be a list")
        pulumi.set(__self__, "ocpu_constraints", ocpu_constraints)
        if shape and not isinstance(shape, str):
            raise TypeError("Expected argument 'shape' to be a str")
        pulumi.set(__self__, "shape", shape)
        if shape_name and not isinstance(shape_name, str):
            raise TypeError("Expected argument 'shape_name' to be a str")
        pulumi.set(__self__, "shape_name", shape_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        The image [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="memoryConstraints")
    def memory_constraints(self) -> Sequence['outputs.GetImageShapeMemoryConstraintResult']:
        """
        For a flexible image and shape, the amount of memory supported for instances that use this image.
        """
        return pulumi.get(self, "memory_constraints")

    @property
    @pulumi.getter(name="ocpuConstraints")
    def ocpu_constraints(self) -> Sequence['outputs.GetImageShapeOcpuConstraintResult']:
        """
        OCPU options for an image and shape.
        """
        return pulumi.get(self, "ocpu_constraints")

    @property
    @pulumi.getter
    def shape(self) -> str:
        """
        The shape name.
        """
        return pulumi.get(self, "shape")

    @property
    @pulumi.getter(name="shapeName")
    def shape_name(self) -> str:
        return pulumi.get(self, "shape_name")


class AwaitableGetImageShapeResult(GetImageShapeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageShapeResult(
            id=self.id,
            image_id=self.image_id,
            memory_constraints=self.memory_constraints,
            ocpu_constraints=self.ocpu_constraints,
            shape=self.shape,
            shape_name=self.shape_name)


def get_image_shape(image_id: Optional[str] = None,
                    shape_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageShapeResult:
    """
    This data source provides details about a specific Image Shape resource in Oracle Cloud Infrastructure Core service.

    Retrieves an image shape compatibility entry.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_image_shape = oci.Core.get_image_shape(image_id=test_image["id"],
        shape_name=test_shape["name"])
    ```


    :param str image_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
    :param str shape_name: Shape name.
    """
    __args__ = dict()
    __args__['imageId'] = image_id
    __args__['shapeName'] = shape_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getImageShape:getImageShape', __args__, opts=opts, typ=GetImageShapeResult).value

    return AwaitableGetImageShapeResult(
        id=pulumi.get(__ret__, 'id'),
        image_id=pulumi.get(__ret__, 'image_id'),
        memory_constraints=pulumi.get(__ret__, 'memory_constraints'),
        ocpu_constraints=pulumi.get(__ret__, 'ocpu_constraints'),
        shape=pulumi.get(__ret__, 'shape'),
        shape_name=pulumi.get(__ret__, 'shape_name'))


@_utilities.lift_output_func(get_image_shape)
def get_image_shape_output(image_id: Optional[pulumi.Input[str]] = None,
                           shape_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImageShapeResult]:
    """
    This data source provides details about a specific Image Shape resource in Oracle Cloud Infrastructure Core service.

    Retrieves an image shape compatibility entry.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_image_shape = oci.Core.get_image_shape(image_id=test_image["id"],
        shape_name=test_shape["name"])
    ```


    :param str image_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
    :param str shape_name: Shape name.
    """
    ...
