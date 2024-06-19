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
    'GetResourceActionsResult',
    'AwaitableGetResourceActionsResult',
    'get_resource_actions',
    'get_resource_actions_output',
]

@pulumi.output_type
class GetResourceActionsResult:
    """
    A collection of values returned by getResourceActions.
    """
    def __init__(__self__, child_tenancy_ids=None, compartment_id=None, compartment_id_in_subtree=None, filters=None, id=None, include_organization=None, include_resource_metadata=None, name=None, recommendation_id=None, recommendation_name=None, resource_action_collections=None, resource_type=None, state=None, status=None):
        if child_tenancy_ids and not isinstance(child_tenancy_ids, list):
            raise TypeError("Expected argument 'child_tenancy_ids' to be a list")
        pulumi.set(__self__, "child_tenancy_ids", child_tenancy_ids)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_organization and not isinstance(include_organization, bool):
            raise TypeError("Expected argument 'include_organization' to be a bool")
        pulumi.set(__self__, "include_organization", include_organization)
        if include_resource_metadata and not isinstance(include_resource_metadata, bool):
            raise TypeError("Expected argument 'include_resource_metadata' to be a bool")
        pulumi.set(__self__, "include_resource_metadata", include_resource_metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recommendation_id and not isinstance(recommendation_id, str):
            raise TypeError("Expected argument 'recommendation_id' to be a str")
        pulumi.set(__self__, "recommendation_id", recommendation_id)
        if recommendation_name and not isinstance(recommendation_name, str):
            raise TypeError("Expected argument 'recommendation_name' to be a str")
        pulumi.set(__self__, "recommendation_name", recommendation_name)
        if resource_action_collections and not isinstance(resource_action_collections, list):
            raise TypeError("Expected argument 'resource_action_collections' to be a list")
        pulumi.set(__self__, "resource_action_collections", resource_action_collections)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="childTenancyIds")
    def child_tenancy_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "child_tenancy_ids")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> bool:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetResourceActionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeOrganization")
    def include_organization(self) -> Optional[bool]:
        return pulumi.get(self, "include_organization")

    @property
    @pulumi.getter(name="includeResourceMetadata")
    def include_resource_metadata(self) -> Optional[bool]:
        return pulumi.get(self, "include_resource_metadata")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name assigned to the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recommendationId")
    def recommendation_id(self) -> Optional[str]:
        """
        The unique OCID associated with the recommendation.
        """
        return pulumi.get(self, "recommendation_id")

    @property
    @pulumi.getter(name="recommendationName")
    def recommendation_name(self) -> Optional[str]:
        return pulumi.get(self, "recommendation_name")

    @property
    @pulumi.getter(name="resourceActionCollections")
    def resource_action_collections(self) -> Sequence['outputs.GetResourceActionsResourceActionCollectionResult']:
        """
        The list of resource_action_collection.
        """
        return pulumi.get(self, "resource_action_collections")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        The kind of resource.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The resource action's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The current status of the resource action.
        """
        return pulumi.get(self, "status")


class AwaitableGetResourceActionsResult(GetResourceActionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceActionsResult(
            child_tenancy_ids=self.child_tenancy_ids,
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            filters=self.filters,
            id=self.id,
            include_organization=self.include_organization,
            include_resource_metadata=self.include_resource_metadata,
            name=self.name,
            recommendation_id=self.recommendation_id,
            recommendation_name=self.recommendation_name,
            resource_action_collections=self.resource_action_collections,
            resource_type=self.resource_type,
            state=self.state,
            status=self.status)


def get_resource_actions(child_tenancy_ids: Optional[Sequence[str]] = None,
                         compartment_id: Optional[str] = None,
                         compartment_id_in_subtree: Optional[bool] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetResourceActionsFilterArgs']]] = None,
                         include_organization: Optional[bool] = None,
                         include_resource_metadata: Optional[bool] = None,
                         name: Optional[str] = None,
                         recommendation_id: Optional[str] = None,
                         recommendation_name: Optional[str] = None,
                         resource_type: Optional[str] = None,
                         state: Optional[str] = None,
                         status: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceActionsResult:
    """
    This data source provides the list of Resource Actions in Oracle Cloud Infrastructure Optimizer service.

    Lists the Cloud Advisor resource actions that are supported.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_resource_actions = oci.Optimizer.get_resource_actions(compartment_id=compartment_id,
        compartment_id_in_subtree=resource_action_compartment_id_in_subtree,
        child_tenancy_ids=resource_action_child_tenancy_ids,
        include_organization=resource_action_include_organization,
        include_resource_metadata=resource_action_include_resource_metadata,
        name=resource_action_name,
        recommendation_id=test_recommendation["id"],
        recommendation_name=test_recommendation["name"],
        resource_type=resource_action_resource_type,
        state=resource_action_state,
        status=resource_action_status)
    ```


    :param Sequence[str] child_tenancy_ids: A list of child tenancies for which the respective data will be returned. Please note that  the parent tenancy id can also be included in this list. For example, if there is a parent P with two children A and B, to return results of only parent P and child A, this list should be populated with  tenancy id of parent P and child A. 
           
           If this list contains a tenancy id that isn't part of the organization of parent P, the request will  fail. That is, let's say there is an organization with parent P with children A and B, and also one  other tenant T that isn't part of the organization. If T is included in the list of  childTenancyIds, the request will fail.
           
           It is important to note that if you are setting the includeOrganization parameter value as true and  also populating the childTenancyIds parameter with a list of child tenancies, the request will fail. The childTenancyIds and includeOrganization should be used exclusively.
           
           When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.
    :param str compartment_id: The OCID of the compartment.
    :param bool compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.
           
           Can only be set to true when performing ListCompartments on the tenancy (root compartment).
    :param bool include_organization: When set to true, the data for all child tenancies including the parent is returned. That is, if  there is an organization with parent P and children A and B, to return the data for the parent P, child  A and child B, this parameter value should be set to true.
           
           Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like  to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate the list with tenancy id of P and A.
           
           When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.
    :param bool include_resource_metadata: Supplement additional resource information in extended metadata response.
    :param str name: Optional. A filter that returns results that match the name specified.
    :param str recommendation_id: The unique OCID associated with the recommendation.
    :param str recommendation_name: Optional. A filter that returns results that match the recommendation name specified.
    :param str resource_type: Optional. A filter that returns results that match the resource type specified.
    :param str state: A filter that returns results that match the lifecycle state specified.
    :param str status: A filter that returns recommendations that match the status specified.
    """
    __args__ = dict()
    __args__['childTenancyIds'] = child_tenancy_ids
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['filters'] = filters
    __args__['includeOrganization'] = include_organization
    __args__['includeResourceMetadata'] = include_resource_metadata
    __args__['name'] = name
    __args__['recommendationId'] = recommendation_id
    __args__['recommendationName'] = recommendation_name
    __args__['resourceType'] = resource_type
    __args__['state'] = state
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Optimizer/getResourceActions:getResourceActions', __args__, opts=opts, typ=GetResourceActionsResult).value

    return AwaitableGetResourceActionsResult(
        child_tenancy_ids=pulumi.get(__ret__, 'child_tenancy_ids'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        include_organization=pulumi.get(__ret__, 'include_organization'),
        include_resource_metadata=pulumi.get(__ret__, 'include_resource_metadata'),
        name=pulumi.get(__ret__, 'name'),
        recommendation_id=pulumi.get(__ret__, 'recommendation_id'),
        recommendation_name=pulumi.get(__ret__, 'recommendation_name'),
        resource_action_collections=pulumi.get(__ret__, 'resource_action_collections'),
        resource_type=pulumi.get(__ret__, 'resource_type'),
        state=pulumi.get(__ret__, 'state'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_resource_actions)
def get_resource_actions_output(child_tenancy_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                compartment_id: Optional[pulumi.Input[str]] = None,
                                compartment_id_in_subtree: Optional[pulumi.Input[bool]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetResourceActionsFilterArgs']]]]] = None,
                                include_organization: Optional[pulumi.Input[Optional[bool]]] = None,
                                include_resource_metadata: Optional[pulumi.Input[Optional[bool]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                recommendation_id: Optional[pulumi.Input[Optional[str]]] = None,
                                recommendation_name: Optional[pulumi.Input[Optional[str]]] = None,
                                resource_type: Optional[pulumi.Input[Optional[str]]] = None,
                                state: Optional[pulumi.Input[Optional[str]]] = None,
                                status: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceActionsResult]:
    """
    This data source provides the list of Resource Actions in Oracle Cloud Infrastructure Optimizer service.

    Lists the Cloud Advisor resource actions that are supported.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_resource_actions = oci.Optimizer.get_resource_actions(compartment_id=compartment_id,
        compartment_id_in_subtree=resource_action_compartment_id_in_subtree,
        child_tenancy_ids=resource_action_child_tenancy_ids,
        include_organization=resource_action_include_organization,
        include_resource_metadata=resource_action_include_resource_metadata,
        name=resource_action_name,
        recommendation_id=test_recommendation["id"],
        recommendation_name=test_recommendation["name"],
        resource_type=resource_action_resource_type,
        state=resource_action_state,
        status=resource_action_status)
    ```


    :param Sequence[str] child_tenancy_ids: A list of child tenancies for which the respective data will be returned. Please note that  the parent tenancy id can also be included in this list. For example, if there is a parent P with two children A and B, to return results of only parent P and child A, this list should be populated with  tenancy id of parent P and child A. 
           
           If this list contains a tenancy id that isn't part of the organization of parent P, the request will  fail. That is, let's say there is an organization with parent P with children A and B, and also one  other tenant T that isn't part of the organization. If T is included in the list of  childTenancyIds, the request will fail.
           
           It is important to note that if you are setting the includeOrganization parameter value as true and  also populating the childTenancyIds parameter with a list of child tenancies, the request will fail. The childTenancyIds and includeOrganization should be used exclusively.
           
           When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.
    :param str compartment_id: The OCID of the compartment.
    :param bool compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.
           
           Can only be set to true when performing ListCompartments on the tenancy (root compartment).
    :param bool include_organization: When set to true, the data for all child tenancies including the parent is returned. That is, if  there is an organization with parent P and children A and B, to return the data for the parent P, child  A and child B, this parameter value should be set to true.
           
           Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like  to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate the list with tenancy id of P and A.
           
           When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.
    :param bool include_resource_metadata: Supplement additional resource information in extended metadata response.
    :param str name: Optional. A filter that returns results that match the name specified.
    :param str recommendation_id: The unique OCID associated with the recommendation.
    :param str recommendation_name: Optional. A filter that returns results that match the recommendation name specified.
    :param str resource_type: Optional. A filter that returns results that match the resource type specified.
    :param str state: A filter that returns results that match the lifecycle state specified.
    :param str status: A filter that returns recommendations that match the status specified.
    """
    ...
