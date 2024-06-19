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
    'GetJavaDownloadsJavaDownloadTokensResult',
    'AwaitableGetJavaDownloadsJavaDownloadTokensResult',
    'get_java_downloads_java_download_tokens',
    'get_java_downloads_java_download_tokens_output',
]

@pulumi.output_type
class GetJavaDownloadsJavaDownloadTokensResult:
    """
    A collection of values returned by getJavaDownloadsJavaDownloadTokens.
    """
    def __init__(__self__, compartment_id=None, display_name=None, family_version=None, filters=None, id=None, java_download_token_collections=None, search_by_user=None, state=None, value=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if family_version and not isinstance(family_version, str):
            raise TypeError("Expected argument 'family_version' to be a str")
        pulumi.set(__self__, "family_version", family_version)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if java_download_token_collections and not isinstance(java_download_token_collections, list):
            raise TypeError("Expected argument 'java_download_token_collections' to be a list")
        pulumi.set(__self__, "java_download_token_collections", java_download_token_collections)
        if search_by_user and not isinstance(search_by_user, str):
            raise TypeError("Expected argument 'search_by_user' to be a str")
        pulumi.set(__self__, "search_by_user", search_by_user)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy scoped to the JavaDownloadToken.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The name of the principal.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="familyVersion")
    def family_version(self) -> Optional[str]:
        return pulumi.get(self, "family_version")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetJavaDownloadsJavaDownloadTokensFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the principal.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="javaDownloadTokenCollections")
    def java_download_token_collections(self) -> Sequence['outputs.GetJavaDownloadsJavaDownloadTokensJavaDownloadTokenCollectionResult']:
        """
        The list of java_download_token_collection.
        """
        return pulumi.get(self, "java_download_token_collections")

    @property
    @pulumi.getter(name="searchByUser")
    def search_by_user(self) -> Optional[str]:
        return pulumi.get(self, "search_by_user")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the JavaDownloadToken.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Uniquely generated value for the JavaDownloadToken.
        """
        return pulumi.get(self, "value")


class AwaitableGetJavaDownloadsJavaDownloadTokensResult(GetJavaDownloadsJavaDownloadTokensResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJavaDownloadsJavaDownloadTokensResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            family_version=self.family_version,
            filters=self.filters,
            id=self.id,
            java_download_token_collections=self.java_download_token_collections,
            search_by_user=self.search_by_user,
            state=self.state,
            value=self.value)


def get_java_downloads_java_download_tokens(compartment_id: Optional[str] = None,
                                            display_name: Optional[str] = None,
                                            family_version: Optional[str] = None,
                                            filters: Optional[Sequence[pulumi.InputType['GetJavaDownloadsJavaDownloadTokensFilterArgs']]] = None,
                                            id: Optional[str] = None,
                                            search_by_user: Optional[str] = None,
                                            state: Optional[str] = None,
                                            value: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJavaDownloadsJavaDownloadTokensResult:
    """
    This data source provides the list of Java Download Tokens in Oracle Cloud Infrastructure Jms Java Downloads service.

    Returns a list of JavaDownloadTokens.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_java_download_tokens = oci.Jms.get_java_downloads_java_download_tokens(compartment_id=tenancy_ocid,
        display_name=java_download_token_display_name,
        family_version=java_download_token_family_version,
        id=java_download_token_id,
        search_by_user=java_download_token_search_by_user,
        state=java_download_token_state,
        value=java_download_token_value)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str family_version: Unique Java family version identifier.
    :param str id: Unique JavaDownloadToken identifier.
    :param str search_by_user: A filter to return only resources that match the user principal detail.  The search string can be any of the property values from the [Principal](https://docs.cloud.oracle.com/iaas/api/#/en/jms/latest/datatypes/Principal) object. This object is used as response datatype for the `createdBy` and `lastUpdatedBy` fields in applicable resource.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    :param str value: Unique JavaDownloadToken value.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['familyVersion'] = family_version
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['searchByUser'] = search_by_user
    __args__['state'] = state
    __args__['value'] = value
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Jms/getJavaDownloadsJavaDownloadTokens:getJavaDownloadsJavaDownloadTokens', __args__, opts=opts, typ=GetJavaDownloadsJavaDownloadTokensResult).value

    return AwaitableGetJavaDownloadsJavaDownloadTokensResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        family_version=pulumi.get(__ret__, 'family_version'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        java_download_token_collections=pulumi.get(__ret__, 'java_download_token_collections'),
        search_by_user=pulumi.get(__ret__, 'search_by_user'),
        state=pulumi.get(__ret__, 'state'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_java_downloads_java_download_tokens)
def get_java_downloads_java_download_tokens_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                   display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                   family_version: Optional[pulumi.Input[Optional[str]]] = None,
                                                   filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetJavaDownloadsJavaDownloadTokensFilterArgs']]]]] = None,
                                                   id: Optional[pulumi.Input[Optional[str]]] = None,
                                                   search_by_user: Optional[pulumi.Input[Optional[str]]] = None,
                                                   state: Optional[pulumi.Input[Optional[str]]] = None,
                                                   value: Optional[pulumi.Input[Optional[str]]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJavaDownloadsJavaDownloadTokensResult]:
    """
    This data source provides the list of Java Download Tokens in Oracle Cloud Infrastructure Jms Java Downloads service.

    Returns a list of JavaDownloadTokens.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_java_download_tokens = oci.Jms.get_java_downloads_java_download_tokens(compartment_id=tenancy_ocid,
        display_name=java_download_token_display_name,
        family_version=java_download_token_family_version,
        id=java_download_token_id,
        search_by_user=java_download_token_search_by_user,
        state=java_download_token_state,
        value=java_download_token_value)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str family_version: Unique Java family version identifier.
    :param str id: Unique JavaDownloadToken identifier.
    :param str search_by_user: A filter to return only resources that match the user principal detail.  The search string can be any of the property values from the [Principal](https://docs.cloud.oracle.com/iaas/api/#/en/jms/latest/datatypes/Principal) object. This object is used as response datatype for the `createdBy` and `lastUpdatedBy` fields in applicable resource.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    :param str value: Unique JavaDownloadToken value.
    """
    ...
