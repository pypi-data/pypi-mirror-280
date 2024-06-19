# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetLicenseMetricResult',
    'AwaitableGetLicenseMetricResult',
    'get_license_metric',
    'get_license_metric_output',
]

@pulumi.output_type
class GetLicenseMetricResult:
    """
    A collection of values returned by getLicenseMetric.
    """
    def __init__(__self__, compartment_id=None, id=None, is_compartment_id_in_subtree=None, license_record_expiring_soon_count=None, total_byol_instance_count=None, total_license_included_instance_count=None, total_product_license_count=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_compartment_id_in_subtree and not isinstance(is_compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'is_compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "is_compartment_id_in_subtree", is_compartment_id_in_subtree)
        if license_record_expiring_soon_count and not isinstance(license_record_expiring_soon_count, int):
            raise TypeError("Expected argument 'license_record_expiring_soon_count' to be a int")
        pulumi.set(__self__, "license_record_expiring_soon_count", license_record_expiring_soon_count)
        if total_byol_instance_count and not isinstance(total_byol_instance_count, int):
            raise TypeError("Expected argument 'total_byol_instance_count' to be a int")
        pulumi.set(__self__, "total_byol_instance_count", total_byol_instance_count)
        if total_license_included_instance_count and not isinstance(total_license_included_instance_count, int):
            raise TypeError("Expected argument 'total_license_included_instance_count' to be a int")
        pulumi.set(__self__, "total_license_included_instance_count", total_license_included_instance_count)
        if total_product_license_count and not isinstance(total_product_license_count, int):
            raise TypeError("Expected argument 'total_product_license_count' to be a int")
        pulumi.set(__self__, "total_product_license_count", total_product_license_count)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCompartmentIdInSubtree")
    def is_compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "is_compartment_id_in_subtree")

    @property
    @pulumi.getter(name="licenseRecordExpiringSoonCount")
    def license_record_expiring_soon_count(self) -> int:
        """
        Total number of license records that will expire within 90 days in a particular compartment.
        """
        return pulumi.get(self, "license_record_expiring_soon_count")

    @property
    @pulumi.getter(name="totalByolInstanceCount")
    def total_byol_instance_count(self) -> int:
        """
        Total number of BYOL instances in a particular compartment.
        """
        return pulumi.get(self, "total_byol_instance_count")

    @property
    @pulumi.getter(name="totalLicenseIncludedInstanceCount")
    def total_license_included_instance_count(self) -> int:
        """
        Total number of License Included (LI) instances in a particular compartment.
        """
        return pulumi.get(self, "total_license_included_instance_count")

    @property
    @pulumi.getter(name="totalProductLicenseCount")
    def total_product_license_count(self) -> int:
        """
        Total number of product licenses in a particular compartment.
        """
        return pulumi.get(self, "total_product_license_count")


class AwaitableGetLicenseMetricResult(GetLicenseMetricResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicenseMetricResult(
            compartment_id=self.compartment_id,
            id=self.id,
            is_compartment_id_in_subtree=self.is_compartment_id_in_subtree,
            license_record_expiring_soon_count=self.license_record_expiring_soon_count,
            total_byol_instance_count=self.total_byol_instance_count,
            total_license_included_instance_count=self.total_license_included_instance_count,
            total_product_license_count=self.total_product_license_count)


def get_license_metric(compartment_id: Optional[str] = None,
                       is_compartment_id_in_subtree: Optional[bool] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicenseMetricResult:
    """
    This data source provides details about a specific License Metric resource in Oracle Cloud Infrastructure License Manager service.

    Retrieves the license metrics for a given compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_license_metric = oci.LicenseManager.get_license_metric(compartment_id=compartment_id,
        is_compartment_id_in_subtree=license_metric_is_compartment_id_in_subtree)
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
    :param bool is_compartment_id_in_subtree: Indicates if the given compartment is the root compartment.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['isCompartmentIdInSubtree'] = is_compartment_id_in_subtree
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LicenseManager/getLicenseMetric:getLicenseMetric', __args__, opts=opts, typ=GetLicenseMetricResult).value

    return AwaitableGetLicenseMetricResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        is_compartment_id_in_subtree=pulumi.get(__ret__, 'is_compartment_id_in_subtree'),
        license_record_expiring_soon_count=pulumi.get(__ret__, 'license_record_expiring_soon_count'),
        total_byol_instance_count=pulumi.get(__ret__, 'total_byol_instance_count'),
        total_license_included_instance_count=pulumi.get(__ret__, 'total_license_included_instance_count'),
        total_product_license_count=pulumi.get(__ret__, 'total_product_license_count'))


@_utilities.lift_output_func(get_license_metric)
def get_license_metric_output(compartment_id: Optional[pulumi.Input[str]] = None,
                              is_compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLicenseMetricResult]:
    """
    This data source provides details about a specific License Metric resource in Oracle Cloud Infrastructure License Manager service.

    Retrieves the license metrics for a given compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_license_metric = oci.LicenseManager.get_license_metric(compartment_id=compartment_id,
        is_compartment_id_in_subtree=license_metric_is_compartment_id_in_subtree)
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
    :param bool is_compartment_id_in_subtree: Indicates if the given compartment is the root compartment.
    """
    ...
