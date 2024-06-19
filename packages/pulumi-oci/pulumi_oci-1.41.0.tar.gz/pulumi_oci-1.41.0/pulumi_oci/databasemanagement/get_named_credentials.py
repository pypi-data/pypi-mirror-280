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
    'GetNamedCredentialsResult',
    'AwaitableGetNamedCredentialsResult',
    'get_named_credentials',
    'get_named_credentials_output',
]

@pulumi.output_type
class GetNamedCredentialsResult:
    """
    A collection of values returned by getNamedCredentials.
    """
    def __init__(__self__, associated_resource=None, compartment_id=None, filters=None, id=None, name=None, named_credential_collections=None, scope=None, type=None):
        if associated_resource and not isinstance(associated_resource, str):
            raise TypeError("Expected argument 'associated_resource' to be a str")
        pulumi.set(__self__, "associated_resource", associated_resource)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if named_credential_collections and not isinstance(named_credential_collections, list):
            raise TypeError("Expected argument 'named_credential_collections' to be a list")
        pulumi.set(__self__, "named_credential_collections", named_credential_collections)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="associatedResource")
    def associated_resource(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that  is associated to the named credential.
        """
        return pulumi.get(self, "associated_resource")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNamedCredentialsFilterResult']]:
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
    def name(self) -> Optional[str]:
        """
        The name of the named credential.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namedCredentialCollections")
    def named_credential_collections(self) -> Sequence['outputs.GetNamedCredentialsNamedCredentialCollectionResult']:
        """
        The list of named_credential_collection.
        """
        return pulumi.get(self, "named_credential_collections")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        The scope of the named credential.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of resource associated with the named credential.
        """
        return pulumi.get(self, "type")


class AwaitableGetNamedCredentialsResult(GetNamedCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamedCredentialsResult(
            associated_resource=self.associated_resource,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            named_credential_collections=self.named_credential_collections,
            scope=self.scope,
            type=self.type)


def get_named_credentials(associated_resource: Optional[str] = None,
                          compartment_id: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetNamedCredentialsFilterArgs']]] = None,
                          name: Optional[str] = None,
                          scope: Optional[str] = None,
                          type: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamedCredentialsResult:
    """
    This data source provides the list of Named Credentials in Oracle Cloud Infrastructure Database Management service.

    Gets a single named credential specified by the name or all the named credentials in a specific compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_named_credentials = oci.DatabaseManagement.get_named_credentials(compartment_id=compartment_id,
        associated_resource=named_credential_associated_resource,
        name=named_credential_name,
        scope=named_credential_scope,
        type=named_credential_type)
    ```


    :param str associated_resource: The resource associated to the named credential.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str name: The name of the named credential.
    :param str scope: The scope of named credential.
    :param str type: The type of database that is associated to the named credential.
    """
    __args__ = dict()
    __args__['associatedResource'] = associated_resource
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['scope'] = scope
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getNamedCredentials:getNamedCredentials', __args__, opts=opts, typ=GetNamedCredentialsResult).value

    return AwaitableGetNamedCredentialsResult(
        associated_resource=pulumi.get(__ret__, 'associated_resource'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        named_credential_collections=pulumi.get(__ret__, 'named_credential_collections'),
        scope=pulumi.get(__ret__, 'scope'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_named_credentials)
def get_named_credentials_output(associated_resource: Optional[pulumi.Input[Optional[str]]] = None,
                                 compartment_id: Optional[pulumi.Input[str]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNamedCredentialsFilterArgs']]]]] = None,
                                 name: Optional[pulumi.Input[Optional[str]]] = None,
                                 scope: Optional[pulumi.Input[Optional[str]]] = None,
                                 type: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamedCredentialsResult]:
    """
    This data source provides the list of Named Credentials in Oracle Cloud Infrastructure Database Management service.

    Gets a single named credential specified by the name or all the named credentials in a specific compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_named_credentials = oci.DatabaseManagement.get_named_credentials(compartment_id=compartment_id,
        associated_resource=named_credential_associated_resource,
        name=named_credential_name,
        scope=named_credential_scope,
        type=named_credential_type)
    ```


    :param str associated_resource: The resource associated to the named credential.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str name: The name of the named credential.
    :param str scope: The scope of named credential.
    :param str type: The type of database that is associated to the named credential.
    """
    ...
