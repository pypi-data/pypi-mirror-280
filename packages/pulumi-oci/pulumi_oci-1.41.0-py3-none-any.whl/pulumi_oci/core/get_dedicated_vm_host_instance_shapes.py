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
    'GetDedicatedVmHostInstanceShapesResult',
    'AwaitableGetDedicatedVmHostInstanceShapesResult',
    'get_dedicated_vm_host_instance_shapes',
    'get_dedicated_vm_host_instance_shapes_output',
]

@pulumi.output_type
class GetDedicatedVmHostInstanceShapesResult:
    """
    A collection of values returned by getDedicatedVmHostInstanceShapes.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, dedicated_vm_host_instance_shapes=None, dedicated_vm_host_shape=None, filters=None, id=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if dedicated_vm_host_instance_shapes and not isinstance(dedicated_vm_host_instance_shapes, list):
            raise TypeError("Expected argument 'dedicated_vm_host_instance_shapes' to be a list")
        pulumi.set(__self__, "dedicated_vm_host_instance_shapes", dedicated_vm_host_instance_shapes)
        if dedicated_vm_host_shape and not isinstance(dedicated_vm_host_shape, str):
            raise TypeError("Expected argument 'dedicated_vm_host_shape' to be a str")
        pulumi.set(__self__, "dedicated_vm_host_shape", dedicated_vm_host_shape)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> Optional[str]:
        """
        The shape's availability domain.
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dedicatedVmHostInstanceShapes")
    def dedicated_vm_host_instance_shapes(self) -> Sequence['outputs.GetDedicatedVmHostInstanceShapesDedicatedVmHostInstanceShapeResult']:
        """
        The list of dedicated_vm_host_instance_shapes.
        """
        return pulumi.get(self, "dedicated_vm_host_instance_shapes")

    @property
    @pulumi.getter(name="dedicatedVmHostShape")
    def dedicated_vm_host_shape(self) -> Optional[str]:
        return pulumi.get(self, "dedicated_vm_host_shape")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDedicatedVmHostInstanceShapesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetDedicatedVmHostInstanceShapesResult(GetDedicatedVmHostInstanceShapesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedVmHostInstanceShapesResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            dedicated_vm_host_instance_shapes=self.dedicated_vm_host_instance_shapes,
            dedicated_vm_host_shape=self.dedicated_vm_host_shape,
            filters=self.filters,
            id=self.id)


def get_dedicated_vm_host_instance_shapes(availability_domain: Optional[str] = None,
                                          compartment_id: Optional[str] = None,
                                          dedicated_vm_host_shape: Optional[str] = None,
                                          filters: Optional[Sequence[pulumi.InputType['GetDedicatedVmHostInstanceShapesFilterArgs']]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedVmHostInstanceShapesResult:
    """
    This data source provides the list of Dedicated Vm Host Instance Shapes in Oracle Cloud Infrastructure Core service.

    Lists the shapes that can be used to launch a virtual machine instance on a dedicated virtual machine host within the specified compartment.
    You can filter the list by compatibility with a specific dedicated virtual machine host shape.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_dedicated_vm_host_instance_shapes = oci.Core.get_dedicated_vm_host_instance_shapes(compartment_id=compartment_id,
        availability_domain=dedicated_vm_host_instance_shape_availability_domain,
        dedicated_vm_host_shape=dedicated_vm_host_instance_shape_dedicated_vm_host_shape)
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str dedicated_vm_host_shape: Dedicated VM host shape name
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['dedicatedVmHostShape'] = dedicated_vm_host_shape
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getDedicatedVmHostInstanceShapes:getDedicatedVmHostInstanceShapes', __args__, opts=opts, typ=GetDedicatedVmHostInstanceShapesResult).value

    return AwaitableGetDedicatedVmHostInstanceShapesResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        dedicated_vm_host_instance_shapes=pulumi.get(__ret__, 'dedicated_vm_host_instance_shapes'),
        dedicated_vm_host_shape=pulumi.get(__ret__, 'dedicated_vm_host_shape'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_dedicated_vm_host_instance_shapes)
def get_dedicated_vm_host_instance_shapes_output(availability_domain: Optional[pulumi.Input[Optional[str]]] = None,
                                                 compartment_id: Optional[pulumi.Input[str]] = None,
                                                 dedicated_vm_host_shape: Optional[pulumi.Input[Optional[str]]] = None,
                                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDedicatedVmHostInstanceShapesFilterArgs']]]]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDedicatedVmHostInstanceShapesResult]:
    """
    This data source provides the list of Dedicated Vm Host Instance Shapes in Oracle Cloud Infrastructure Core service.

    Lists the shapes that can be used to launch a virtual machine instance on a dedicated virtual machine host within the specified compartment.
    You can filter the list by compatibility with a specific dedicated virtual machine host shape.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_dedicated_vm_host_instance_shapes = oci.Core.get_dedicated_vm_host_instance_shapes(compartment_id=compartment_id,
        availability_domain=dedicated_vm_host_instance_shape_availability_domain,
        dedicated_vm_host_shape=dedicated_vm_host_instance_shape_dedicated_vm_host_shape)
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str dedicated_vm_host_shape: Dedicated VM host shape name
    """
    ...
