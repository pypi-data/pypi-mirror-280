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
    'GetSecurityPolicyReportRoleGrantPathsResult',
    'AwaitableGetSecurityPolicyReportRoleGrantPathsResult',
    'get_security_policy_report_role_grant_paths',
    'get_security_policy_report_role_grant_paths_output',
]

@pulumi.output_type
class GetSecurityPolicyReportRoleGrantPathsResult:
    """
    A collection of values returned by getSecurityPolicyReportRoleGrantPaths.
    """
    def __init__(__self__, filters=None, granted_role=None, grantee=None, id=None, role_grant_path_collections=None, security_policy_report_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if granted_role and not isinstance(granted_role, str):
            raise TypeError("Expected argument 'granted_role' to be a str")
        pulumi.set(__self__, "granted_role", granted_role)
        if grantee and not isinstance(grantee, str):
            raise TypeError("Expected argument 'grantee' to be a str")
        pulumi.set(__self__, "grantee", grantee)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if role_grant_path_collections and not isinstance(role_grant_path_collections, list):
            raise TypeError("Expected argument 'role_grant_path_collections' to be a list")
        pulumi.set(__self__, "role_grant_path_collections", role_grant_path_collections)
        if security_policy_report_id and not isinstance(security_policy_report_id, str):
            raise TypeError("Expected argument 'security_policy_report_id' to be a str")
        pulumi.set(__self__, "security_policy_report_id", security_policy_report_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSecurityPolicyReportRoleGrantPathsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="grantedRole")
    def granted_role(self) -> str:
        """
        The name of the role.
        """
        return pulumi.get(self, "granted_role")

    @property
    @pulumi.getter
    def grantee(self) -> str:
        """
        Grantee is the user who can access the table.
        """
        return pulumi.get(self, "grantee")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="roleGrantPathCollections")
    def role_grant_path_collections(self) -> Sequence['outputs.GetSecurityPolicyReportRoleGrantPathsRoleGrantPathCollectionResult']:
        """
        The list of role_grant_path_collection.
        """
        return pulumi.get(self, "role_grant_path_collections")

    @property
    @pulumi.getter(name="securityPolicyReportId")
    def security_policy_report_id(self) -> str:
        return pulumi.get(self, "security_policy_report_id")


class AwaitableGetSecurityPolicyReportRoleGrantPathsResult(GetSecurityPolicyReportRoleGrantPathsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityPolicyReportRoleGrantPathsResult(
            filters=self.filters,
            granted_role=self.granted_role,
            grantee=self.grantee,
            id=self.id,
            role_grant_path_collections=self.role_grant_path_collections,
            security_policy_report_id=self.security_policy_report_id)


def get_security_policy_report_role_grant_paths(filters: Optional[Sequence[pulumi.InputType['GetSecurityPolicyReportRoleGrantPathsFilterArgs']]] = None,
                                                granted_role: Optional[str] = None,
                                                grantee: Optional[str] = None,
                                                security_policy_report_id: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityPolicyReportRoleGrantPathsResult:
    """
    This data source provides the list of Security Policy Report Role Grant Paths in Oracle Cloud Infrastructure Data Safe service.

    Retrieves a list of all role grant paths for a particular user.

    The ListRoleGrantPaths operation returns only the role grant paths for the specified security policy report.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_security_policy_report_role_grant_paths = oci.DataSafe.get_security_policy_report_role_grant_paths(granted_role=security_policy_report_role_grant_path_granted_role,
        grantee=security_policy_report_role_grant_path_grantee,
        security_policy_report_id=test_security_policy_report["id"])
    ```


    :param str granted_role: A filter to return only items that match the specified role.
    :param str grantee: A filter to return only items that match the specified grantee.
    :param str security_policy_report_id: The OCID of the security policy report resource.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['grantedRole'] = granted_role
    __args__['grantee'] = grantee
    __args__['securityPolicyReportId'] = security_policy_report_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSecurityPolicyReportRoleGrantPaths:getSecurityPolicyReportRoleGrantPaths', __args__, opts=opts, typ=GetSecurityPolicyReportRoleGrantPathsResult).value

    return AwaitableGetSecurityPolicyReportRoleGrantPathsResult(
        filters=pulumi.get(__ret__, 'filters'),
        granted_role=pulumi.get(__ret__, 'granted_role'),
        grantee=pulumi.get(__ret__, 'grantee'),
        id=pulumi.get(__ret__, 'id'),
        role_grant_path_collections=pulumi.get(__ret__, 'role_grant_path_collections'),
        security_policy_report_id=pulumi.get(__ret__, 'security_policy_report_id'))


@_utilities.lift_output_func(get_security_policy_report_role_grant_paths)
def get_security_policy_report_role_grant_paths_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSecurityPolicyReportRoleGrantPathsFilterArgs']]]]] = None,
                                                       granted_role: Optional[pulumi.Input[str]] = None,
                                                       grantee: Optional[pulumi.Input[str]] = None,
                                                       security_policy_report_id: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityPolicyReportRoleGrantPathsResult]:
    """
    This data source provides the list of Security Policy Report Role Grant Paths in Oracle Cloud Infrastructure Data Safe service.

    Retrieves a list of all role grant paths for a particular user.

    The ListRoleGrantPaths operation returns only the role grant paths for the specified security policy report.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_security_policy_report_role_grant_paths = oci.DataSafe.get_security_policy_report_role_grant_paths(granted_role=security_policy_report_role_grant_path_granted_role,
        grantee=security_policy_report_role_grant_path_grantee,
        security_policy_report_id=test_security_policy_report["id"])
    ```


    :param str granted_role: A filter to return only items that match the specified role.
    :param str grantee: A filter to return only items that match the specified grantee.
    :param str security_policy_report_id: The OCID of the security policy report resource.
    """
    ...
