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
    'GetEkmsPrivateEndpointsResult',
    'AwaitableGetEkmsPrivateEndpointsResult',
    'get_ekms_private_endpoints',
    'get_ekms_private_endpoints_output',
]

@pulumi.output_type
class GetEkmsPrivateEndpointsResult:
    """
    A collection of values returned by getEkmsPrivateEndpoints.
    """
    def __init__(__self__, compartment_id=None, ekms_private_endpoints=None, filters=None, id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if ekms_private_endpoints and not isinstance(ekms_private_endpoints, list):
            raise TypeError("Expected argument 'ekms_private_endpoints' to be a list")
        pulumi.set(__self__, "ekms_private_endpoints", ekms_private_endpoints)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Identifier of the compartment this EKMS private endpoint belongs to
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="ekmsPrivateEndpoints")
    def ekms_private_endpoints(self) -> Sequence['outputs.GetEkmsPrivateEndpointsEkmsPrivateEndpointResult']:
        """
        The list of ekms_private_endpoints.
        """
        return pulumi.get(self, "ekms_private_endpoints")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetEkmsPrivateEndpointsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetEkmsPrivateEndpointsResult(GetEkmsPrivateEndpointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEkmsPrivateEndpointsResult(
            compartment_id=self.compartment_id,
            ekms_private_endpoints=self.ekms_private_endpoints,
            filters=self.filters,
            id=self.id)


def get_ekms_private_endpoints(compartment_id: Optional[str] = None,
                               filters: Optional[Sequence[pulumi.InputType['GetEkmsPrivateEndpointsFilterArgs']]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEkmsPrivateEndpointsResult:
    """
    This data source provides the list of Ekms Private Endpoints in Oracle Cloud Infrastructure Kms service.

    Returns a list of all the EKMS private endpoints in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ekms_private_endpoints = oci.Kms.get_ekms_private_endpoints(compartment_id=compartment_id)
    ```


    :param str compartment_id: The OCID of the compartment.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Kms/getEkmsPrivateEndpoints:getEkmsPrivateEndpoints', __args__, opts=opts, typ=GetEkmsPrivateEndpointsResult).value

    return AwaitableGetEkmsPrivateEndpointsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        ekms_private_endpoints=pulumi.get(__ret__, 'ekms_private_endpoints'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_ekms_private_endpoints)
def get_ekms_private_endpoints_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetEkmsPrivateEndpointsFilterArgs']]]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEkmsPrivateEndpointsResult]:
    """
    This data source provides the list of Ekms Private Endpoints in Oracle Cloud Infrastructure Kms service.

    Returns a list of all the EKMS private endpoints in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ekms_private_endpoints = oci.Kms.get_ekms_private_endpoints(compartment_id=compartment_id)
    ```


    :param str compartment_id: The OCID of the compartment.
    """
    ...
