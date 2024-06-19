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
    'GetDomainsOauthPartnerCertificateResult',
    'AwaitableGetDomainsOauthPartnerCertificateResult',
    'get_domains_oauth_partner_certificate',
    'get_domains_oauth_partner_certificate_output',
]

@pulumi.output_type
class GetDomainsOauthPartnerCertificateResult:
    """
    A collection of values returned by getDomainsOauthPartnerCertificate.
    """
    def __init__(__self__, authorization=None, cert_end_date=None, cert_start_date=None, certificate_alias=None, compartment_ocid=None, delete_in_progress=None, domain_ocid=None, external_id=None, id=None, idcs_created_bies=None, idcs_endpoint=None, idcs_last_modified_bies=None, idcs_last_upgraded_in_release=None, idcs_prevented_operations=None, key_store_id=None, key_store_name=None, key_store_password=None, map=None, metas=None, o_auth_partner_certificate_id=None, ocid=None, resource_type_schema_version=None, schemas=None, sha1thumbprint=None, sha256thumbprint=None, tags=None, tenancy_ocid=None, x509base64certificate=None):
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if cert_end_date and not isinstance(cert_end_date, str):
            raise TypeError("Expected argument 'cert_end_date' to be a str")
        pulumi.set(__self__, "cert_end_date", cert_end_date)
        if cert_start_date and not isinstance(cert_start_date, str):
            raise TypeError("Expected argument 'cert_start_date' to be a str")
        pulumi.set(__self__, "cert_start_date", cert_start_date)
        if certificate_alias and not isinstance(certificate_alias, str):
            raise TypeError("Expected argument 'certificate_alias' to be a str")
        pulumi.set(__self__, "certificate_alias", certificate_alias)
        if compartment_ocid and not isinstance(compartment_ocid, str):
            raise TypeError("Expected argument 'compartment_ocid' to be a str")
        pulumi.set(__self__, "compartment_ocid", compartment_ocid)
        if delete_in_progress and not isinstance(delete_in_progress, bool):
            raise TypeError("Expected argument 'delete_in_progress' to be a bool")
        pulumi.set(__self__, "delete_in_progress", delete_in_progress)
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
        if key_store_id and not isinstance(key_store_id, str):
            raise TypeError("Expected argument 'key_store_id' to be a str")
        pulumi.set(__self__, "key_store_id", key_store_id)
        if key_store_name and not isinstance(key_store_name, str):
            raise TypeError("Expected argument 'key_store_name' to be a str")
        pulumi.set(__self__, "key_store_name", key_store_name)
        if key_store_password and not isinstance(key_store_password, str):
            raise TypeError("Expected argument 'key_store_password' to be a str")
        pulumi.set(__self__, "key_store_password", key_store_password)
        if map and not isinstance(map, str):
            raise TypeError("Expected argument 'map' to be a str")
        pulumi.set(__self__, "map", map)
        if metas and not isinstance(metas, list):
            raise TypeError("Expected argument 'metas' to be a list")
        pulumi.set(__self__, "metas", metas)
        if o_auth_partner_certificate_id and not isinstance(o_auth_partner_certificate_id, str):
            raise TypeError("Expected argument 'o_auth_partner_certificate_id' to be a str")
        pulumi.set(__self__, "o_auth_partner_certificate_id", o_auth_partner_certificate_id)
        if ocid and not isinstance(ocid, str):
            raise TypeError("Expected argument 'ocid' to be a str")
        pulumi.set(__self__, "ocid", ocid)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if sha1thumbprint and not isinstance(sha1thumbprint, str):
            raise TypeError("Expected argument 'sha1thumbprint' to be a str")
        pulumi.set(__self__, "sha1thumbprint", sha1thumbprint)
        if sha256thumbprint and not isinstance(sha256thumbprint, str):
            raise TypeError("Expected argument 'sha256thumbprint' to be a str")
        pulumi.set(__self__, "sha256thumbprint", sha256thumbprint)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tenancy_ocid and not isinstance(tenancy_ocid, str):
            raise TypeError("Expected argument 'tenancy_ocid' to be a str")
        pulumi.set(__self__, "tenancy_ocid", tenancy_ocid)
        if x509base64certificate and not isinstance(x509base64certificate, str):
            raise TypeError("Expected argument 'x509base64certificate' to be a str")
        pulumi.set(__self__, "x509base64certificate", x509base64certificate)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[str]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="certEndDate")
    def cert_end_date(self) -> str:
        """
        Certificate end date
        """
        return pulumi.get(self, "cert_end_date")

    @property
    @pulumi.getter(name="certStartDate")
    def cert_start_date(self) -> str:
        """
        Certificate start date
        """
        return pulumi.get(self, "cert_start_date")

    @property
    @pulumi.getter(name="certificateAlias")
    def certificate_alias(self) -> str:
        """
        Certificate alias
        """
        return pulumi.get(self, "certificate_alias")

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
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.
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
    def idcs_created_bies(self) -> Sequence['outputs.GetDomainsOauthPartnerCertificateIdcsCreatedByResult']:
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
    def idcs_last_modified_bies(self) -> Sequence['outputs.GetDomainsOauthPartnerCertificateIdcsLastModifiedByResult']:
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
    @pulumi.getter(name="keyStoreId")
    def key_store_id(self) -> str:
        """
        Key store ID
        """
        return pulumi.get(self, "key_store_id")

    @property
    @pulumi.getter(name="keyStoreName")
    def key_store_name(self) -> str:
        """
        Key store name
        """
        return pulumi.get(self, "key_store_name")

    @property
    @pulumi.getter(name="keyStorePassword")
    def key_store_password(self) -> str:
        """
        Key store password
        """
        return pulumi.get(self, "key_store_password")

    @property
    @pulumi.getter
    def map(self) -> str:
        """
        Map
        """
        return pulumi.get(self, "map")

    @property
    @pulumi.getter
    def metas(self) -> Sequence['outputs.GetDomainsOauthPartnerCertificateMetaResult']:
        """
        A complex attribute that contains resource metadata. All sub-attributes are OPTIONAL.
        """
        return pulumi.get(self, "metas")

    @property
    @pulumi.getter(name="oAuthPartnerCertificateId")
    def o_auth_partner_certificate_id(self) -> str:
        return pulumi.get(self, "o_auth_partner_certificate_id")

    @property
    @pulumi.getter
    def ocid(self) -> str:
        """
        Unique Oracle Cloud Infrastructure identifier for the SCIM Resource.
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
    def sha1thumbprint(self) -> str:
        """
        SHA-1 Thumbprint
        """
        return pulumi.get(self, "sha1thumbprint")

    @property
    @pulumi.getter
    def sha256thumbprint(self) -> str:
        """
        SHA-256 Thumbprint
        """
        return pulumi.get(self, "sha256thumbprint")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetDomainsOauthPartnerCertificateTagResult']:
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
    def x509base64certificate(self) -> str:
        """
        Base 64Key data attribute
        """
        return pulumi.get(self, "x509base64certificate")


class AwaitableGetDomainsOauthPartnerCertificateResult(GetDomainsOauthPartnerCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsOauthPartnerCertificateResult(
            authorization=self.authorization,
            cert_end_date=self.cert_end_date,
            cert_start_date=self.cert_start_date,
            certificate_alias=self.certificate_alias,
            compartment_ocid=self.compartment_ocid,
            delete_in_progress=self.delete_in_progress,
            domain_ocid=self.domain_ocid,
            external_id=self.external_id,
            id=self.id,
            idcs_created_bies=self.idcs_created_bies,
            idcs_endpoint=self.idcs_endpoint,
            idcs_last_modified_bies=self.idcs_last_modified_bies,
            idcs_last_upgraded_in_release=self.idcs_last_upgraded_in_release,
            idcs_prevented_operations=self.idcs_prevented_operations,
            key_store_id=self.key_store_id,
            key_store_name=self.key_store_name,
            key_store_password=self.key_store_password,
            map=self.map,
            metas=self.metas,
            o_auth_partner_certificate_id=self.o_auth_partner_certificate_id,
            ocid=self.ocid,
            resource_type_schema_version=self.resource_type_schema_version,
            schemas=self.schemas,
            sha1thumbprint=self.sha1thumbprint,
            sha256thumbprint=self.sha256thumbprint,
            tags=self.tags,
            tenancy_ocid=self.tenancy_ocid,
            x509base64certificate=self.x509base64certificate)


def get_domains_oauth_partner_certificate(authorization: Optional[str] = None,
                                          idcs_endpoint: Optional[str] = None,
                                          o_auth_partner_certificate_id: Optional[str] = None,
                                          resource_type_schema_version: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsOauthPartnerCertificateResult:
    """
    This data source provides details about a specific O Auth Partner Certificate resource in Oracle Cloud Infrastructure Identity Domains service.

    Get an OAuth Partner Certificate

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oauth_partner_certificate = oci.Identity.get_domains_oauth_partner_certificate(idcs_endpoint=test_domain["url"],
        o_auth_partner_certificate_id=test_oauth_partner_certificate_oci_identity_domains_oauth_partner_certificate["id"],
        authorization=oauth_partner_certificate_authorization,
        resource_type_schema_version=oauth_partner_certificate_resource_type_schema_version)
    ```


    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str o_auth_partner_certificate_id: ID of the resource
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    __args__ = dict()
    __args__['authorization'] = authorization
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['oAuthPartnerCertificateId'] = o_auth_partner_certificate_id
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsOauthPartnerCertificate:getDomainsOauthPartnerCertificate', __args__, opts=opts, typ=GetDomainsOauthPartnerCertificateResult).value

    return AwaitableGetDomainsOauthPartnerCertificateResult(
        authorization=pulumi.get(__ret__, 'authorization'),
        cert_end_date=pulumi.get(__ret__, 'cert_end_date'),
        cert_start_date=pulumi.get(__ret__, 'cert_start_date'),
        certificate_alias=pulumi.get(__ret__, 'certificate_alias'),
        compartment_ocid=pulumi.get(__ret__, 'compartment_ocid'),
        delete_in_progress=pulumi.get(__ret__, 'delete_in_progress'),
        domain_ocid=pulumi.get(__ret__, 'domain_ocid'),
        external_id=pulumi.get(__ret__, 'external_id'),
        id=pulumi.get(__ret__, 'id'),
        idcs_created_bies=pulumi.get(__ret__, 'idcs_created_bies'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        idcs_last_modified_bies=pulumi.get(__ret__, 'idcs_last_modified_bies'),
        idcs_last_upgraded_in_release=pulumi.get(__ret__, 'idcs_last_upgraded_in_release'),
        idcs_prevented_operations=pulumi.get(__ret__, 'idcs_prevented_operations'),
        key_store_id=pulumi.get(__ret__, 'key_store_id'),
        key_store_name=pulumi.get(__ret__, 'key_store_name'),
        key_store_password=pulumi.get(__ret__, 'key_store_password'),
        map=pulumi.get(__ret__, 'map'),
        metas=pulumi.get(__ret__, 'metas'),
        o_auth_partner_certificate_id=pulumi.get(__ret__, 'o_auth_partner_certificate_id'),
        ocid=pulumi.get(__ret__, 'ocid'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        schemas=pulumi.get(__ret__, 'schemas'),
        sha1thumbprint=pulumi.get(__ret__, 'sha1thumbprint'),
        sha256thumbprint=pulumi.get(__ret__, 'sha256thumbprint'),
        tags=pulumi.get(__ret__, 'tags'),
        tenancy_ocid=pulumi.get(__ret__, 'tenancy_ocid'),
        x509base64certificate=pulumi.get(__ret__, 'x509base64certificate'))


@_utilities.lift_output_func(get_domains_oauth_partner_certificate)
def get_domains_oauth_partner_certificate_output(authorization: Optional[pulumi.Input[Optional[str]]] = None,
                                                 idcs_endpoint: Optional[pulumi.Input[str]] = None,
                                                 o_auth_partner_certificate_id: Optional[pulumi.Input[str]] = None,
                                                 resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsOauthPartnerCertificateResult]:
    """
    This data source provides details about a specific O Auth Partner Certificate resource in Oracle Cloud Infrastructure Identity Domains service.

    Get an OAuth Partner Certificate

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oauth_partner_certificate = oci.Identity.get_domains_oauth_partner_certificate(idcs_endpoint=test_domain["url"],
        o_auth_partner_certificate_id=test_oauth_partner_certificate_oci_identity_domains_oauth_partner_certificate["id"],
        authorization=oauth_partner_certificate_authorization,
        resource_type_schema_version=oauth_partner_certificate_resource_type_schema_version)
    ```


    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str o_auth_partner_certificate_id: ID of the resource
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    ...
