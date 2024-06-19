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
    'GetDomainsRuleResult',
    'AwaitableGetDomainsRuleResult',
    'get_domains_rule',
    'get_domains_rule_output',
]

@pulumi.output_type
class GetDomainsRuleResult:
    """
    A collection of values returned by getDomainsRule.
    """
    def __init__(__self__, active=None, attribute_sets=None, attributes=None, authorization=None, compartment_ocid=None, condition=None, condition_groups=None, delete_in_progress=None, description=None, domain_ocid=None, external_id=None, id=None, idcs_created_bies=None, idcs_endpoint=None, idcs_last_modified_bies=None, idcs_last_upgraded_in_release=None, idcs_prevented_operations=None, locked=None, metas=None, name=None, ocid=None, policy_types=None, resource_type_schema_version=None, returns=None, rule_groovy=None, rule_id=None, schemas=None, tags=None, tenancy_ocid=None):
        if active and not isinstance(active, bool):
            raise TypeError("Expected argument 'active' to be a bool")
        pulumi.set(__self__, "active", active)
        if attribute_sets and not isinstance(attribute_sets, list):
            raise TypeError("Expected argument 'attribute_sets' to be a list")
        pulumi.set(__self__, "attribute_sets", attribute_sets)
        if attributes and not isinstance(attributes, str):
            raise TypeError("Expected argument 'attributes' to be a str")
        pulumi.set(__self__, "attributes", attributes)
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if compartment_ocid and not isinstance(compartment_ocid, str):
            raise TypeError("Expected argument 'compartment_ocid' to be a str")
        pulumi.set(__self__, "compartment_ocid", compartment_ocid)
        if condition and not isinstance(condition, str):
            raise TypeError("Expected argument 'condition' to be a str")
        pulumi.set(__self__, "condition", condition)
        if condition_groups and not isinstance(condition_groups, list):
            raise TypeError("Expected argument 'condition_groups' to be a list")
        pulumi.set(__self__, "condition_groups", condition_groups)
        if delete_in_progress and not isinstance(delete_in_progress, bool):
            raise TypeError("Expected argument 'delete_in_progress' to be a bool")
        pulumi.set(__self__, "delete_in_progress", delete_in_progress)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain_ocid and not isinstance(domain_ocid, str):
            raise TypeError("Expected argument 'domain_ocid' to be a str")
        pulumi.set(__self__, "domain_ocid", domain_ocid)
        if external_id and not isinstance(external_id, str):
            raise TypeError("Expected argument 'external_id' to be a str")
        pulumi.set(__self__, "external_id", external_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_created_bies and not isinstance(idcs_created_bies, list):
            raise TypeError("Expected argument 'idcs_created_bies' to be a list")
        pulumi.set(__self__, "idcs_created_bies", idcs_created_bies)
        if idcs_endpoint and not isinstance(idcs_endpoint, str):
            raise TypeError("Expected argument 'idcs_endpoint' to be a str")
        pulumi.set(__self__, "idcs_endpoint", idcs_endpoint)
        if idcs_last_modified_bies and not isinstance(idcs_last_modified_bies, list):
            raise TypeError("Expected argument 'idcs_last_modified_bies' to be a list")
        pulumi.set(__self__, "idcs_last_modified_bies", idcs_last_modified_bies)
        if idcs_last_upgraded_in_release and not isinstance(idcs_last_upgraded_in_release, str):
            raise TypeError("Expected argument 'idcs_last_upgraded_in_release' to be a str")
        pulumi.set(__self__, "idcs_last_upgraded_in_release", idcs_last_upgraded_in_release)
        if idcs_prevented_operations and not isinstance(idcs_prevented_operations, list):
            raise TypeError("Expected argument 'idcs_prevented_operations' to be a list")
        pulumi.set(__self__, "idcs_prevented_operations", idcs_prevented_operations)
        if locked and not isinstance(locked, bool):
            raise TypeError("Expected argument 'locked' to be a bool")
        pulumi.set(__self__, "locked", locked)
        if metas and not isinstance(metas, list):
            raise TypeError("Expected argument 'metas' to be a list")
        pulumi.set(__self__, "metas", metas)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if ocid and not isinstance(ocid, str):
            raise TypeError("Expected argument 'ocid' to be a str")
        pulumi.set(__self__, "ocid", ocid)
        if policy_types and not isinstance(policy_types, list):
            raise TypeError("Expected argument 'policy_types' to be a list")
        pulumi.set(__self__, "policy_types", policy_types)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if returns and not isinstance(returns, list):
            raise TypeError("Expected argument 'returns' to be a list")
        pulumi.set(__self__, "returns", returns)
        if rule_groovy and not isinstance(rule_groovy, str):
            raise TypeError("Expected argument 'rule_groovy' to be a str")
        pulumi.set(__self__, "rule_groovy", rule_groovy)
        if rule_id and not isinstance(rule_id, str):
            raise TypeError("Expected argument 'rule_id' to be a str")
        pulumi.set(__self__, "rule_id", rule_id)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tenancy_ocid and not isinstance(tenancy_ocid, str):
            raise TypeError("Expected argument 'tenancy_ocid' to be a str")
        pulumi.set(__self__, "tenancy_ocid", tenancy_ocid)

    @property
    @pulumi.getter
    def active(self) -> bool:
        """
        If true, rule is active
        """
        return pulumi.get(self, "active")

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
    @pulumi.getter(name="compartmentOcid")
    def compartment_ocid(self) -> str:
        """
        Oracle Cloud Infrastructure Compartment Id (ocid) in which the resource lives.
        """
        return pulumi.get(self, "compartment_ocid")

    @property
    @pulumi.getter
    def condition(self) -> str:
        """
        SCIM filters
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter(name="conditionGroups")
    def condition_groups(self) -> Sequence['outputs.GetDomainsRuleConditionGroupResult']:
        """
        Condition or ConditionGroup assigned to the rule
        """
        return pulumi.get(self, "condition_groups")

    @property
    @pulumi.getter(name="deleteInProgress")
    def delete_in_progress(self) -> bool:
        """
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.
        """
        return pulumi.get(self, "delete_in_progress")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Rule Description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainOcid")
    def domain_ocid(self) -> str:
        """
        Oracle Cloud Infrastructure Domain Id (ocid) in which the resource lives.
        """
        return pulumi.get(self, "domain_ocid")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> str:
        """
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value.  The value of the externalId attribute is always issued be the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsCreatedBies")
    def idcs_created_bies(self) -> Sequence['outputs.GetDomainsRuleIdcsCreatedByResult']:
        """
        The User or App who created the Resource
        """
        return pulumi.get(self, "idcs_created_bies")

    @property
    @pulumi.getter(name="idcsEndpoint")
    def idcs_endpoint(self) -> str:
        return pulumi.get(self, "idcs_endpoint")

    @property
    @pulumi.getter(name="idcsLastModifiedBies")
    def idcs_last_modified_bies(self) -> Sequence['outputs.GetDomainsRuleIdcsLastModifiedByResult']:
        """
        The User or App who modified the Resource
        """
        return pulumi.get(self, "idcs_last_modified_bies")

    @property
    @pulumi.getter(name="idcsLastUpgradedInRelease")
    def idcs_last_upgraded_in_release(self) -> str:
        """
        The release number when the resource was upgraded.
        """
        return pulumi.get(self, "idcs_last_upgraded_in_release")

    @property
    @pulumi.getter(name="idcsPreventedOperations")
    def idcs_prevented_operations(self) -> Sequence[str]:
        """
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.
        """
        return pulumi.get(self, "idcs_prevented_operations")

    @property
    @pulumi.getter
    def locked(self) -> bool:
        """
        Shows if the rule is locked
        """
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter
    def metas(self) -> Sequence['outputs.GetDomainsRuleMetaResult']:
        """
        A complex attribute that contains resource metadata. All sub-attributes are OPTIONAL.
        """
        return pulumi.get(self, "metas")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Attribute name of an individual value to be returned.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ocid(self) -> str:
        """
        Unique Oracle Cloud Infrastructure identifier for the SCIM Resource.
        """
        return pulumi.get(self, "ocid")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Sequence['outputs.GetDomainsRulePolicyTypeResult']:
        """
        PolicyType on which the policy is based
        """
        return pulumi.get(self, "policy_types")

    @property
    @pulumi.getter(name="resourceTypeSchemaVersion")
    def resource_type_schema_version(self) -> Optional[str]:
        return pulumi.get(self, "resource_type_schema_version")

    @property
    @pulumi.getter
    def returns(self) -> Sequence['outputs.GetDomainsRuleReturnResult']:
        """
        The return values are the then portion of a Rule
        """
        return pulumi.get(self, "returns")

    @property
    @pulumi.getter(name="ruleGroovy")
    def rule_groovy(self) -> str:
        """
        The Groovy script that is run instead of the rule, if policy type allows the rule to be a Groovy script.
        """
        return pulumi.get(self, "rule_groovy")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> str:
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter
    def schemas(self) -> Sequence[str]:
        """
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\"enterprise\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetDomainsRuleTagResult']:
        """
        A list of tags on this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenancyOcid")
    def tenancy_ocid(self) -> str:
        """
        Oracle Cloud Infrastructure Tenant Id (ocid) in which the resource lives.
        """
        return pulumi.get(self, "tenancy_ocid")


class AwaitableGetDomainsRuleResult(GetDomainsRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsRuleResult(
            active=self.active,
            attribute_sets=self.attribute_sets,
            attributes=self.attributes,
            authorization=self.authorization,
            compartment_ocid=self.compartment_ocid,
            condition=self.condition,
            condition_groups=self.condition_groups,
            delete_in_progress=self.delete_in_progress,
            description=self.description,
            domain_ocid=self.domain_ocid,
            external_id=self.external_id,
            id=self.id,
            idcs_created_bies=self.idcs_created_bies,
            idcs_endpoint=self.idcs_endpoint,
            idcs_last_modified_bies=self.idcs_last_modified_bies,
            idcs_last_upgraded_in_release=self.idcs_last_upgraded_in_release,
            idcs_prevented_operations=self.idcs_prevented_operations,
            locked=self.locked,
            metas=self.metas,
            name=self.name,
            ocid=self.ocid,
            policy_types=self.policy_types,
            resource_type_schema_version=self.resource_type_schema_version,
            returns=self.returns,
            rule_groovy=self.rule_groovy,
            rule_id=self.rule_id,
            schemas=self.schemas,
            tags=self.tags,
            tenancy_ocid=self.tenancy_ocid)


def get_domains_rule(attribute_sets: Optional[Sequence[str]] = None,
                     attributes: Optional[str] = None,
                     authorization: Optional[str] = None,
                     idcs_endpoint: Optional[str] = None,
                     resource_type_schema_version: Optional[str] = None,
                     rule_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsRuleResult:
    """
    This data source provides details about a specific Rule resource in Oracle Cloud Infrastructure Identity Domains service.

    Get a Rule

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_rule = oci.Identity.get_domains_rule(idcs_endpoint=test_domain["url"],
        rule_id=test_rule_oci_events_rule["id"],
        attribute_sets=["all"],
        attributes="",
        authorization=rule_authorization,
        resource_type_schema_version=rule_resource_type_schema_version)
    ```


    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    :param str rule_id: ID of the resource
    """
    __args__ = dict()
    __args__['attributeSets'] = attribute_sets
    __args__['attributes'] = attributes
    __args__['authorization'] = authorization
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    __args__['ruleId'] = rule_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsRule:getDomainsRule', __args__, opts=opts, typ=GetDomainsRuleResult).value

    return AwaitableGetDomainsRuleResult(
        active=pulumi.get(__ret__, 'active'),
        attribute_sets=pulumi.get(__ret__, 'attribute_sets'),
        attributes=pulumi.get(__ret__, 'attributes'),
        authorization=pulumi.get(__ret__, 'authorization'),
        compartment_ocid=pulumi.get(__ret__, 'compartment_ocid'),
        condition=pulumi.get(__ret__, 'condition'),
        condition_groups=pulumi.get(__ret__, 'condition_groups'),
        delete_in_progress=pulumi.get(__ret__, 'delete_in_progress'),
        description=pulumi.get(__ret__, 'description'),
        domain_ocid=pulumi.get(__ret__, 'domain_ocid'),
        external_id=pulumi.get(__ret__, 'external_id'),
        id=pulumi.get(__ret__, 'id'),
        idcs_created_bies=pulumi.get(__ret__, 'idcs_created_bies'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        idcs_last_modified_bies=pulumi.get(__ret__, 'idcs_last_modified_bies'),
        idcs_last_upgraded_in_release=pulumi.get(__ret__, 'idcs_last_upgraded_in_release'),
        idcs_prevented_operations=pulumi.get(__ret__, 'idcs_prevented_operations'),
        locked=pulumi.get(__ret__, 'locked'),
        metas=pulumi.get(__ret__, 'metas'),
        name=pulumi.get(__ret__, 'name'),
        ocid=pulumi.get(__ret__, 'ocid'),
        policy_types=pulumi.get(__ret__, 'policy_types'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        returns=pulumi.get(__ret__, 'returns'),
        rule_groovy=pulumi.get(__ret__, 'rule_groovy'),
        rule_id=pulumi.get(__ret__, 'rule_id'),
        schemas=pulumi.get(__ret__, 'schemas'),
        tags=pulumi.get(__ret__, 'tags'),
        tenancy_ocid=pulumi.get(__ret__, 'tenancy_ocid'))


@_utilities.lift_output_func(get_domains_rule)
def get_domains_rule_output(attribute_sets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            attributes: Optional[pulumi.Input[Optional[str]]] = None,
                            authorization: Optional[pulumi.Input[Optional[str]]] = None,
                            idcs_endpoint: Optional[pulumi.Input[str]] = None,
                            resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                            rule_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsRuleResult]:
    """
    This data source provides details about a specific Rule resource in Oracle Cloud Infrastructure Identity Domains service.

    Get a Rule

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_rule = oci.Identity.get_domains_rule(idcs_endpoint=test_domain["url"],
        rule_id=test_rule_oci_events_rule["id"],
        attribute_sets=["all"],
        attributes="",
        authorization=rule_authorization,
        resource_type_schema_version=rule_resource_type_schema_version)
    ```


    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    :param str rule_id: ID of the resource
    """
    ...
