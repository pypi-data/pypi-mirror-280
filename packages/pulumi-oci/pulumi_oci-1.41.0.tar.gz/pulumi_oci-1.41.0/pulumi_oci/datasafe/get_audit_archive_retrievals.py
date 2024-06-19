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
    'GetAuditArchiveRetrievalsResult',
    'AwaitableGetAuditArchiveRetrievalsResult',
    'get_audit_archive_retrievals',
    'get_audit_archive_retrievals_output',
]

@pulumi.output_type
class GetAuditArchiveRetrievalsResult:
    """
    A collection of values returned by getAuditArchiveRetrievals.
    """
    def __init__(__self__, access_level=None, audit_archive_retrieval_collections=None, audit_archive_retrieval_id=None, compartment_id=None, compartment_id_in_subtree=None, display_name=None, filters=None, id=None, state=None, target_id=None, time_of_expiry=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        pulumi.set(__self__, "access_level", access_level)
        if audit_archive_retrieval_collections and not isinstance(audit_archive_retrieval_collections, list):
            raise TypeError("Expected argument 'audit_archive_retrieval_collections' to be a list")
        pulumi.set(__self__, "audit_archive_retrieval_collections", audit_archive_retrieval_collections)
        if audit_archive_retrieval_id and not isinstance(audit_archive_retrieval_id, str):
            raise TypeError("Expected argument 'audit_archive_retrieval_id' to be a str")
        pulumi.set(__self__, "audit_archive_retrieval_id", audit_archive_retrieval_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if time_of_expiry and not isinstance(time_of_expiry, str):
            raise TypeError("Expected argument 'time_of_expiry' to be a str")
        pulumi.set(__self__, "time_of_expiry", time_of_expiry)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[str]:
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="auditArchiveRetrievalCollections")
    def audit_archive_retrieval_collections(self) -> Sequence['outputs.GetAuditArchiveRetrievalsAuditArchiveRetrievalCollectionResult']:
        """
        The list of audit_archive_retrieval_collection.
        """
        return pulumi.get(self, "audit_archive_retrieval_collections")

    @property
    @pulumi.getter(name="auditArchiveRetrievalId")
    def audit_archive_retrieval_id(self) -> Optional[str]:
        return pulumi.get(self, "audit_archive_retrieval_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains archive retrieval.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the archive retrieval. The name does not have to be unique, and is changeable.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAuditArchiveRetrievalsFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current state of the archive retrieval.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        """
        The OCID of the target associated with the archive retrieval.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="timeOfExpiry")
    def time_of_expiry(self) -> Optional[str]:
        """
        The date time when retrieved archive data will be deleted from Data Safe and unloaded back into archival.
        """
        return pulumi.get(self, "time_of_expiry")


class AwaitableGetAuditArchiveRetrievalsResult(GetAuditArchiveRetrievalsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuditArchiveRetrievalsResult(
            access_level=self.access_level,
            audit_archive_retrieval_collections=self.audit_archive_retrieval_collections,
            audit_archive_retrieval_id=self.audit_archive_retrieval_id,
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state,
            target_id=self.target_id,
            time_of_expiry=self.time_of_expiry)


def get_audit_archive_retrievals(access_level: Optional[str] = None,
                                 audit_archive_retrieval_id: Optional[str] = None,
                                 compartment_id: Optional[str] = None,
                                 compartment_id_in_subtree: Optional[bool] = None,
                                 display_name: Optional[str] = None,
                                 filters: Optional[Sequence[pulumi.InputType['GetAuditArchiveRetrievalsFilterArgs']]] = None,
                                 state: Optional[str] = None,
                                 target_id: Optional[str] = None,
                                 time_of_expiry: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuditArchiveRetrievalsResult:
    """
    This data source provides the list of Audit Archive Retrievals in Oracle Cloud Infrastructure Data Safe service.

    Returns the list of audit archive retrieval.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_audit_archive_retrievals = oci.DataSafe.get_audit_archive_retrievals(compartment_id=compartment_id,
        access_level=audit_archive_retrieval_access_level,
        audit_archive_retrieval_id=test_audit_archive_retrieval["id"],
        compartment_id_in_subtree=audit_archive_retrieval_compartment_id_in_subtree,
        display_name=audit_archive_retrieval_display_name,
        state=audit_archive_retrieval_state,
        target_id=test_target["id"],
        time_of_expiry=audit_archive_retrieval_time_of_expiry)
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str audit_archive_retrieval_id: OCID of the archive retrieval.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str display_name: A filter to return only resources that match the specified display name.
    :param str state: A filter to return only resources that matches the specified lifecycle state.
    :param str target_id: The OCID of the target associated with the archive retrieval.
    :param str time_of_expiry: The date time when retrieved archive data will be deleted from Data Safe and unloaded back into archival.
    """
    __args__ = dict()
    __args__['accessLevel'] = access_level
    __args__['auditArchiveRetrievalId'] = audit_archive_retrieval_id
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['targetId'] = target_id
    __args__['timeOfExpiry'] = time_of_expiry
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getAuditArchiveRetrievals:getAuditArchiveRetrievals', __args__, opts=opts, typ=GetAuditArchiveRetrievalsResult).value

    return AwaitableGetAuditArchiveRetrievalsResult(
        access_level=pulumi.get(__ret__, 'access_level'),
        audit_archive_retrieval_collections=pulumi.get(__ret__, 'audit_archive_retrieval_collections'),
        audit_archive_retrieval_id=pulumi.get(__ret__, 'audit_archive_retrieval_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'),
        target_id=pulumi.get(__ret__, 'target_id'),
        time_of_expiry=pulumi.get(__ret__, 'time_of_expiry'))


@_utilities.lift_output_func(get_audit_archive_retrievals)
def get_audit_archive_retrievals_output(access_level: Optional[pulumi.Input[Optional[str]]] = None,
                                        audit_archive_retrieval_id: Optional[pulumi.Input[Optional[str]]] = None,
                                        compartment_id: Optional[pulumi.Input[str]] = None,
                                        compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                                        display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAuditArchiveRetrievalsFilterArgs']]]]] = None,
                                        state: Optional[pulumi.Input[Optional[str]]] = None,
                                        target_id: Optional[pulumi.Input[Optional[str]]] = None,
                                        time_of_expiry: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuditArchiveRetrievalsResult]:
    """
    This data source provides the list of Audit Archive Retrievals in Oracle Cloud Infrastructure Data Safe service.

    Returns the list of audit archive retrieval.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_audit_archive_retrievals = oci.DataSafe.get_audit_archive_retrievals(compartment_id=compartment_id,
        access_level=audit_archive_retrieval_access_level,
        audit_archive_retrieval_id=test_audit_archive_retrieval["id"],
        compartment_id_in_subtree=audit_archive_retrieval_compartment_id_in_subtree,
        display_name=audit_archive_retrieval_display_name,
        state=audit_archive_retrieval_state,
        target_id=test_target["id"],
        time_of_expiry=audit_archive_retrieval_time_of_expiry)
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str audit_archive_retrieval_id: OCID of the archive retrieval.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str display_name: A filter to return only resources that match the specified display name.
    :param str state: A filter to return only resources that matches the specified lifecycle state.
    :param str target_id: The OCID of the target associated with the archive retrieval.
    :param str time_of_expiry: The date time when retrieved archive data will be deleted from Data Safe and unloaded back into archival.
    """
    ...
