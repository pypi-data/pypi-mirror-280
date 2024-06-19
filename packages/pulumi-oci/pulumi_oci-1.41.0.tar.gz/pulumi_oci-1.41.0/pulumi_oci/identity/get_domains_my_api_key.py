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
    'GetDomainsMyApiKeyResult',
    'AwaitableGetDomainsMyApiKeyResult',
    'get_domains_my_api_key',
    'get_domains_my_api_key_output',
]

@pulumi.output_type
class GetDomainsMyApiKeyResult:
    """
    A collection of values returned by getDomainsMyApiKey.
    """
    def __init__(__self__, authorization=None, compartment_ocid=None, delete_in_progress=None, description=None, domain_ocid=None, fingerprint=None, id=None, idcs_created_bies=None, idcs_endpoint=None, idcs_last_modified_bies=None, idcs_last_upgraded_in_release=None, idcs_prevented_operations=None, key=None, metas=None, my_api_key_id=None, ocid=None, resource_type_schema_version=None, schemas=None, tags=None, tenancy_ocid=None, users=None):
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if compartment_ocid and not isinstance(compartment_ocid, str):
            raise TypeError("Expected argument 'compartment_ocid' to be a str")
        pulumi.set(__self__, "compartment_ocid", compartment_ocid)
        if delete_in_progress and not isinstance(delete_in_progress, bool):
            raise TypeError("Expected argument 'delete_in_progress' to be a bool")
        pulumi.set(__self__, "delete_in_progress", delete_in_progress)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain_ocid and not isinstance(domain_ocid, str):
            raise TypeError("Expected argument 'domain_ocid' to be a str")
        pulumi.set(__self__, "domain_ocid", domain_ocid)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
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
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if metas and not isinstance(metas, list):
            raise TypeError("Expected argument 'metas' to be a list")
        pulumi.set(__self__, "metas", metas)
        if my_api_key_id and not isinstance(my_api_key_id, str):
            raise TypeError("Expected argument 'my_api_key_id' to be a str")
        pulumi.set(__self__, "my_api_key_id", my_api_key_id)
        if ocid and not isinstance(ocid, str):
            raise TypeError("Expected argument 'ocid' to be a str")
        pulumi.set(__self__, "ocid", ocid)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tenancy_ocid and not isinstance(tenancy_ocid, str):
            raise TypeError("Expected argument 'tenancy_ocid' to be a str")
        pulumi.set(__self__, "tenancy_ocid", tenancy_ocid)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

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
        Description
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
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        Fingerprint
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsCreatedBies")
    def idcs_created_bies(self) -> Sequence['outputs.GetDomainsMyApiKeyIdcsCreatedByResult']:
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
    def idcs_last_modified_bies(self) -> Sequence['outputs.GetDomainsMyApiKeyIdcsLastModifiedByResult']:
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
    def key(self) -> str:
        """
        Key or name of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def metas(self) -> Sequence['outputs.GetDomainsMyApiKeyMetaResult']:
        """
        A complex attribute that contains resource metadata. All sub-attributes are OPTIONAL.
        """
        return pulumi.get(self, "metas")

    @property
    @pulumi.getter(name="myApiKeyId")
    def my_api_key_id(self) -> str:
        return pulumi.get(self, "my_api_key_id")

    @property
    @pulumi.getter
    def ocid(self) -> str:
        """
        The user's OCID.
        """
        return pulumi.get(self, "ocid")

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
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetDomainsMyApiKeyTagResult']:
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

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetDomainsMyApiKeyUserResult']:
        """
        The user linked to the API key.
        """
        return pulumi.get(self, "users")


class AwaitableGetDomainsMyApiKeyResult(GetDomainsMyApiKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsMyApiKeyResult(
            authorization=self.authorization,
            compartment_ocid=self.compartment_ocid,
            delete_in_progress=self.delete_in_progress,
            description=self.description,
            domain_ocid=self.domain_ocid,
            fingerprint=self.fingerprint,
            id=self.id,
            idcs_created_bies=self.idcs_created_bies,
            idcs_endpoint=self.idcs_endpoint,
            idcs_last_modified_bies=self.idcs_last_modified_bies,
            idcs_last_upgraded_in_release=self.idcs_last_upgraded_in_release,
            idcs_prevented_operations=self.idcs_prevented_operations,
            key=self.key,
            metas=self.metas,
            my_api_key_id=self.my_api_key_id,
            ocid=self.ocid,
            resource_type_schema_version=self.resource_type_schema_version,
            schemas=self.schemas,
            tags=self.tags,
            tenancy_ocid=self.tenancy_ocid,
            users=self.users)


def get_domains_my_api_key(authorization: Optional[str] = None,
                           idcs_endpoint: Optional[str] = None,
                           my_api_key_id: Optional[str] = None,
                           resource_type_schema_version: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsMyApiKeyResult:
    """
    This data source provides details about a specific My Api Key resource in Oracle Cloud Infrastructure Identity Domains service.

    Get a user's own API key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_my_api_key = oci.Identity.get_domains_my_api_key(idcs_endpoint=test_domain["url"],
        my_api_key_id=test_api_key["id"],
        authorization=my_api_key_authorization,
        resource_type_schema_version=my_api_key_resource_type_schema_version)
    ```


    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str my_api_key_id: ID of the resource
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    __args__ = dict()
    __args__['authorization'] = authorization
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['myApiKeyId'] = my_api_key_id
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsMyApiKey:getDomainsMyApiKey', __args__, opts=opts, typ=GetDomainsMyApiKeyResult).value

    return AwaitableGetDomainsMyApiKeyResult(
        authorization=pulumi.get(__ret__, 'authorization'),
        compartment_ocid=pulumi.get(__ret__, 'compartment_ocid'),
        delete_in_progress=pulumi.get(__ret__, 'delete_in_progress'),
        description=pulumi.get(__ret__, 'description'),
        domain_ocid=pulumi.get(__ret__, 'domain_ocid'),
        fingerprint=pulumi.get(__ret__, 'fingerprint'),
        id=pulumi.get(__ret__, 'id'),
        idcs_created_bies=pulumi.get(__ret__, 'idcs_created_bies'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        idcs_last_modified_bies=pulumi.get(__ret__, 'idcs_last_modified_bies'),
        idcs_last_upgraded_in_release=pulumi.get(__ret__, 'idcs_last_upgraded_in_release'),
        idcs_prevented_operations=pulumi.get(__ret__, 'idcs_prevented_operations'),
        key=pulumi.get(__ret__, 'key'),
        metas=pulumi.get(__ret__, 'metas'),
        my_api_key_id=pulumi.get(__ret__, 'my_api_key_id'),
        ocid=pulumi.get(__ret__, 'ocid'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        schemas=pulumi.get(__ret__, 'schemas'),
        tags=pulumi.get(__ret__, 'tags'),
        tenancy_ocid=pulumi.get(__ret__, 'tenancy_ocid'),
        users=pulumi.get(__ret__, 'users'))


@_utilities.lift_output_func(get_domains_my_api_key)
def get_domains_my_api_key_output(authorization: Optional[pulumi.Input[Optional[str]]] = None,
                                  idcs_endpoint: Optional[pulumi.Input[str]] = None,
                                  my_api_key_id: Optional[pulumi.Input[str]] = None,
                                  resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsMyApiKeyResult]:
    """
    This data source provides details about a specific My Api Key resource in Oracle Cloud Infrastructure Identity Domains service.

    Get a user's own API key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_my_api_key = oci.Identity.get_domains_my_api_key(idcs_endpoint=test_domain["url"],
        my_api_key_id=test_api_key["id"],
        authorization=my_api_key_authorization,
        resource_type_schema_version=my_api_key_resource_type_schema_version)
    ```


    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str my_api_key_id: ID of the resource
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    ...
