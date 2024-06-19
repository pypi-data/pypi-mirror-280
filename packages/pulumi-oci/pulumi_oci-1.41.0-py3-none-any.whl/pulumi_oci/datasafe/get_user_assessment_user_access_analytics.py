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
    'GetUserAssessmentUserAccessAnalyticsResult',
    'AwaitableGetUserAssessmentUserAccessAnalyticsResult',
    'get_user_assessment_user_access_analytics',
    'get_user_assessment_user_access_analytics_output',
]

@pulumi.output_type
class GetUserAssessmentUserAccessAnalyticsResult:
    """
    A collection of values returned by getUserAssessmentUserAccessAnalytics.
    """
    def __init__(__self__, filters=None, id=None, user_access_analytics_collections=None, user_assessment_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if user_access_analytics_collections and not isinstance(user_access_analytics_collections, list):
            raise TypeError("Expected argument 'user_access_analytics_collections' to be a list")
        pulumi.set(__self__, "user_access_analytics_collections", user_access_analytics_collections)
        if user_assessment_id and not isinstance(user_assessment_id, str):
            raise TypeError("Expected argument 'user_assessment_id' to be a str")
        pulumi.set(__self__, "user_assessment_id", user_assessment_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetUserAssessmentUserAccessAnalyticsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="userAccessAnalyticsCollections")
    def user_access_analytics_collections(self) -> Sequence['outputs.GetUserAssessmentUserAccessAnalyticsUserAccessAnalyticsCollectionResult']:
        """
        The list of user_access_analytics_collection.
        """
        return pulumi.get(self, "user_access_analytics_collections")

    @property
    @pulumi.getter(name="userAssessmentId")
    def user_assessment_id(self) -> str:
        return pulumi.get(self, "user_assessment_id")


class AwaitableGetUserAssessmentUserAccessAnalyticsResult(GetUserAssessmentUserAccessAnalyticsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserAssessmentUserAccessAnalyticsResult(
            filters=self.filters,
            id=self.id,
            user_access_analytics_collections=self.user_access_analytics_collections,
            user_assessment_id=self.user_assessment_id)


def get_user_assessment_user_access_analytics(filters: Optional[Sequence[pulumi.InputType['GetUserAssessmentUserAccessAnalyticsFilterArgs']]] = None,
                                              user_assessment_id: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserAssessmentUserAccessAnalyticsResult:
    """
    This data source provides the list of User Assessment User Access Analytics in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of aggregated user access analytics in the specified target in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_user_assessment_user_access_analytics = oci.DataSafe.get_user_assessment_user_access_analytics(user_assessment_id=test_user_assessment["id"])
    ```


    :param str user_assessment_id: The OCID of the user assessment.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['userAssessmentId'] = user_assessment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getUserAssessmentUserAccessAnalytics:getUserAssessmentUserAccessAnalytics', __args__, opts=opts, typ=GetUserAssessmentUserAccessAnalyticsResult).value

    return AwaitableGetUserAssessmentUserAccessAnalyticsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        user_access_analytics_collections=pulumi.get(__ret__, 'user_access_analytics_collections'),
        user_assessment_id=pulumi.get(__ret__, 'user_assessment_id'))


@_utilities.lift_output_func(get_user_assessment_user_access_analytics)
def get_user_assessment_user_access_analytics_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetUserAssessmentUserAccessAnalyticsFilterArgs']]]]] = None,
                                                     user_assessment_id: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserAssessmentUserAccessAnalyticsResult]:
    """
    This data source provides the list of User Assessment User Access Analytics in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of aggregated user access analytics in the specified target in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_user_assessment_user_access_analytics = oci.DataSafe.get_user_assessment_user_access_analytics(user_assessment_id=test_user_assessment["id"])
    ```


    :param str user_assessment_id: The OCID of the user assessment.
    """
    ...
