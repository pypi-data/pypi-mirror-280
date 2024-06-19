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
    'GetDomainsCloudGateMappingsResult',
    'AwaitableGetDomainsCloudGateMappingsResult',
    'get_domains_cloud_gate_mappings',
    'get_domains_cloud_gate_mappings_output',
]

@pulumi.output_type
class GetDomainsCloudGateMappingsResult:
    """
    A collection of values returned by getDomainsCloudGateMappings.
    """
    def __init__(__self__, attribute_sets=None, attributes=None, authorization=None, cloud_gate_mapping_count=None, cloud_gate_mapping_filter=None, cloud_gate_mappings=None, compartment_id=None, id=None, idcs_endpoint=None, items_per_page=None, resource_type_schema_version=None, schemas=None, sort_by=None, sort_order=None, start_index=None, total_results=None):
        if attribute_sets and not isinstance(attribute_sets, list):
            raise TypeError("Expected argument 'attribute_sets' to be a list")
        pulumi.set(__self__, "attribute_sets", attribute_sets)
        if attributes and not isinstance(attributes, str):
            raise TypeError("Expected argument 'attributes' to be a str")
        pulumi.set(__self__, "attributes", attributes)
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if cloud_gate_mapping_count and not isinstance(cloud_gate_mapping_count, int):
            raise TypeError("Expected argument 'cloud_gate_mapping_count' to be a int")
        pulumi.set(__self__, "cloud_gate_mapping_count", cloud_gate_mapping_count)
        if cloud_gate_mapping_filter and not isinstance(cloud_gate_mapping_filter, str):
            raise TypeError("Expected argument 'cloud_gate_mapping_filter' to be a str")
        pulumi.set(__self__, "cloud_gate_mapping_filter", cloud_gate_mapping_filter)
        if cloud_gate_mappings and not isinstance(cloud_gate_mappings, list):
            raise TypeError("Expected argument 'cloud_gate_mappings' to be a list")
        pulumi.set(__self__, "cloud_gate_mappings", cloud_gate_mappings)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_endpoint and not isinstance(idcs_endpoint, str):
            raise TypeError("Expected argument 'idcs_endpoint' to be a str")
        pulumi.set(__self__, "idcs_endpoint", idcs_endpoint)
        if items_per_page and not isinstance(items_per_page, int):
            raise TypeError("Expected argument 'items_per_page' to be a int")
        pulumi.set(__self__, "items_per_page", items_per_page)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if sort_by and not isinstance(sort_by, str):
            raise TypeError("Expected argument 'sort_by' to be a str")
        pulumi.set(__self__, "sort_by", sort_by)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)
        if start_index and not isinstance(start_index, int):
            raise TypeError("Expected argument 'start_index' to be a int")
        pulumi.set(__self__, "start_index", start_index)
        if total_results and not isinstance(total_results, int):
            raise TypeError("Expected argument 'total_results' to be a int")
        pulumi.set(__self__, "total_results", total_results)

    @property
    @pulumi.getter(name="attributeSets")
    def attribute_sets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "attribute_sets")

    @property
    @pulumi.getter
    def attributes(self) -> Optional[str]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def authorization(self) -> Optional[str]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="cloudGateMappingCount")
    def cloud_gate_mapping_count(self) -> Optional[int]:
        return pulumi.get(self, "cloud_gate_mapping_count")

    @property
    @pulumi.getter(name="cloudGateMappingFilter")
    def cloud_gate_mapping_filter(self) -> Optional[str]:
        return pulumi.get(self, "cloud_gate_mapping_filter")

    @property
    @pulumi.getter(name="cloudGateMappings")
    def cloud_gate_mappings(self) -> Sequence['outputs.GetDomainsCloudGateMappingsCloudGateMappingResult']:
        """
        The list of cloud_gate_mappings.
        """
        return pulumi.get(self, "cloud_gate_mappings")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsEndpoint")
    def idcs_endpoint(self) -> str:
        return pulumi.get(self, "idcs_endpoint")

    @property
    @pulumi.getter(name="itemsPerPage")
    def items_per_page(self) -> int:
        return pulumi.get(self, "items_per_page")

    @property
    @pulumi.getter(name="resourceTypeSchemaVersion")
    def resource_type_schema_version(self) -> Optional[str]:
        return pulumi.get(self, "resource_type_schema_version")

    @property
    @pulumi.getter
    def schemas(self) -> Sequence[str]:
        """
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\"enterprise\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter(name="sortBy")
    def sort_by(self) -> Optional[str]:
        return pulumi.get(self, "sort_by")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        return pulumi.get(self, "sort_order")

    @property
    @pulumi.getter(name="startIndex")
    def start_index(self) -> Optional[int]:
        return pulumi.get(self, "start_index")

    @property
    @pulumi.getter(name="totalResults")
    def total_results(self) -> int:
        return pulumi.get(self, "total_results")


class AwaitableGetDomainsCloudGateMappingsResult(GetDomainsCloudGateMappingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsCloudGateMappingsResult(
            attribute_sets=self.attribute_sets,
            attributes=self.attributes,
            authorization=self.authorization,
            cloud_gate_mapping_count=self.cloud_gate_mapping_count,
            cloud_gate_mapping_filter=self.cloud_gate_mapping_filter,
            cloud_gate_mappings=self.cloud_gate_mappings,
            compartment_id=self.compartment_id,
            id=self.id,
            idcs_endpoint=self.idcs_endpoint,
            items_per_page=self.items_per_page,
            resource_type_schema_version=self.resource_type_schema_version,
            schemas=self.schemas,
            sort_by=self.sort_by,
            sort_order=self.sort_order,
            start_index=self.start_index,
            total_results=self.total_results)


def get_domains_cloud_gate_mappings(attribute_sets: Optional[Sequence[str]] = None,
                                    attributes: Optional[str] = None,
                                    authorization: Optional[str] = None,
                                    cloud_gate_mapping_count: Optional[int] = None,
                                    cloud_gate_mapping_filter: Optional[str] = None,
                                    compartment_id: Optional[str] = None,
                                    idcs_endpoint: Optional[str] = None,
                                    resource_type_schema_version: Optional[str] = None,
                                    sort_by: Optional[str] = None,
                                    sort_order: Optional[str] = None,
                                    start_index: Optional[int] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsCloudGateMappingsResult:
    """
    This data source provides the list of Cloud Gate Mappings in Oracle Cloud Infrastructure Identity Domains service.

    Search Cloud Gate mappings

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cloud_gate_mappings = oci.Identity.get_domains_cloud_gate_mappings(idcs_endpoint=test_domain["url"],
        cloud_gate_mapping_count=cloud_gate_mapping_cloud_gate_mapping_count,
        cloud_gate_mapping_filter=cloud_gate_mapping_cloud_gate_mapping_filter,
        attribute_sets=["all"],
        attributes="",
        authorization=cloud_gate_mapping_authorization,
        resource_type_schema_version=cloud_gate_mapping_resource_type_schema_version,
        start_index=cloud_gate_mapping_start_index)
    ```


    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param int cloud_gate_mapping_count: OPTIONAL. An integer that indicates the desired maximum number of query results per page. 1000 is the largest value that you can use. See the Pagination section of the System for Cross-Domain Identity Management Protocol specification for more information. (Section 3.4.2.4).
    :param str cloud_gate_mapping_filter: OPTIONAL. The filter string that is used to request a subset of resources. The filter string MUST be a valid filter expression. See the Filtering section of the SCIM specification for more information (Section 3.4.2.2). The string should contain at least one condition that each item must match in order to be returned in the search results. Each condition specifies an attribute, an operator, and a value. Conditions within a filter can be connected by logical operators (such as AND and OR). Sets of conditions can be grouped together using parentheses.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    :param int start_index: OPTIONAL. An integer that indicates the 1-based index of the first query result. See the Pagination section of the SCIM specification for more information. (Section 3.4.2.4). The number of results pages to return. The first page is 1. Specify 2 to access the second page of results, and so on.
    """
    __args__ = dict()
    __args__['attributeSets'] = attribute_sets
    __args__['attributes'] = attributes
    __args__['authorization'] = authorization
    __args__['cloudGateMappingCount'] = cloud_gate_mapping_count
    __args__['cloudGateMappingFilter'] = cloud_gate_mapping_filter
    __args__['compartmentId'] = compartment_id
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    __args__['sortBy'] = sort_by
    __args__['sortOrder'] = sort_order
    __args__['startIndex'] = start_index
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsCloudGateMappings:getDomainsCloudGateMappings', __args__, opts=opts, typ=GetDomainsCloudGateMappingsResult).value

    return AwaitableGetDomainsCloudGateMappingsResult(
        attribute_sets=pulumi.get(__ret__, 'attribute_sets'),
        attributes=pulumi.get(__ret__, 'attributes'),
        authorization=pulumi.get(__ret__, 'authorization'),
        cloud_gate_mapping_count=pulumi.get(__ret__, 'cloud_gate_mapping_count'),
        cloud_gate_mapping_filter=pulumi.get(__ret__, 'cloud_gate_mapping_filter'),
        cloud_gate_mappings=pulumi.get(__ret__, 'cloud_gate_mappings'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        items_per_page=pulumi.get(__ret__, 'items_per_page'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        schemas=pulumi.get(__ret__, 'schemas'),
        sort_by=pulumi.get(__ret__, 'sort_by'),
        sort_order=pulumi.get(__ret__, 'sort_order'),
        start_index=pulumi.get(__ret__, 'start_index'),
        total_results=pulumi.get(__ret__, 'total_results'))


@_utilities.lift_output_func(get_domains_cloud_gate_mappings)
def get_domains_cloud_gate_mappings_output(attribute_sets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                           attributes: Optional[pulumi.Input[Optional[str]]] = None,
                                           authorization: Optional[pulumi.Input[Optional[str]]] = None,
                                           cloud_gate_mapping_count: Optional[pulumi.Input[Optional[int]]] = None,
                                           cloud_gate_mapping_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                           compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                           idcs_endpoint: Optional[pulumi.Input[str]] = None,
                                           resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                                           sort_by: Optional[pulumi.Input[Optional[str]]] = None,
                                           sort_order: Optional[pulumi.Input[Optional[str]]] = None,
                                           start_index: Optional[pulumi.Input[Optional[int]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsCloudGateMappingsResult]:
    """
    This data source provides the list of Cloud Gate Mappings in Oracle Cloud Infrastructure Identity Domains service.

    Search Cloud Gate mappings

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cloud_gate_mappings = oci.Identity.get_domains_cloud_gate_mappings(idcs_endpoint=test_domain["url"],
        cloud_gate_mapping_count=cloud_gate_mapping_cloud_gate_mapping_count,
        cloud_gate_mapping_filter=cloud_gate_mapping_cloud_gate_mapping_filter,
        attribute_sets=["all"],
        attributes="",
        authorization=cloud_gate_mapping_authorization,
        resource_type_schema_version=cloud_gate_mapping_resource_type_schema_version,
        start_index=cloud_gate_mapping_start_index)
    ```


    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param int cloud_gate_mapping_count: OPTIONAL. An integer that indicates the desired maximum number of query results per page. 1000 is the largest value that you can use. See the Pagination section of the System for Cross-Domain Identity Management Protocol specification for more information. (Section 3.4.2.4).
    :param str cloud_gate_mapping_filter: OPTIONAL. The filter string that is used to request a subset of resources. The filter string MUST be a valid filter expression. See the Filtering section of the SCIM specification for more information (Section 3.4.2.2). The string should contain at least one condition that each item must match in order to be returned in the search results. Each condition specifies an attribute, an operator, and a value. Conditions within a filter can be connected by logical operators (such as AND and OR). Sets of conditions can be grouped together using parentheses.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    :param int start_index: OPTIONAL. An integer that indicates the 1-based index of the first query result. See the Pagination section of the SCIM specification for more information. (Section 3.4.2.4). The number of results pages to return. The first page is 1. Specify 2 to access the second page of results, and so on.
    """
    ...
