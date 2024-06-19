# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTsigKeyResult',
    'AwaitableGetTsigKeyResult',
    'get_tsig_key',
    'get_tsig_key_output',
]

@pulumi.output_type
class GetTsigKeyResult:
    """
    A collection of values returned by getTsigKey.
    """
    def __init__(__self__, algorithm=None, compartment_id=None, defined_tags=None, freeform_tags=None, id=None, name=None, secret=None, self=None, state=None, time_created=None, time_updated=None, tsig_key_id=None):
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if secret and not isinstance(secret, str):
            raise TypeError("Expected argument 'secret' to be a str")
        pulumi.set(__self__, "secret", secret)
        if self and not isinstance(self, str):
            raise TypeError("Expected argument 'self' to be a str")
        pulumi.set(__self__, "self", self)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if tsig_key_id and not isinstance(tsig_key_id, str):
            raise TypeError("Expected argument 'tsig_key_id' to be a str")
        pulumi.set(__self__, "tsig_key_id", tsig_key_id)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        """
        TSIG key algorithms are encoded as domain names, but most consist of only one non-empty label, which is not required to be explicitly absolute. Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more information on these algorithms, see [RFC 4635](https://tools.ietf.org/html/rfc4635#section-2).
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the TSIG key.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A globally unique domain name identifying the key for a given pair of hosts.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> str:
        """
        A base64 string encoding the binary shared secret.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def self(self) -> str:
        """
        The canonical absolute URL of the resource.
        """
        return pulumi.get(self, "self")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the resource was created, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the resource was last updated, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="tsigKeyId")
    def tsig_key_id(self) -> str:
        return pulumi.get(self, "tsig_key_id")


class AwaitableGetTsigKeyResult(GetTsigKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTsigKeyResult(
            algorithm=self.algorithm,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            freeform_tags=self.freeform_tags,
            id=self.id,
            name=self.name,
            secret=self.secret,
            self=self.self,
            state=self.state,
            time_created=self.time_created,
            time_updated=self.time_updated,
            tsig_key_id=self.tsig_key_id)


def get_tsig_key(tsig_key_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTsigKeyResult:
    """
    This data source provides details about a specific Tsig Key resource in Oracle Cloud Infrastructure DNS service.

    Gets information about the specified TSIG key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tsig_key = oci.Dns.get_tsig_key(tsig_key_id=test_tsig_key_oci_dns_tsig_key["id"])
    ```


    :param str tsig_key_id: The OCID of the target TSIG key.
    """
    __args__ = dict()
    __args__['tsigKeyId'] = tsig_key_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getTsigKey:getTsigKey', __args__, opts=opts, typ=GetTsigKeyResult).value

    return AwaitableGetTsigKeyResult(
        algorithm=pulumi.get(__ret__, 'algorithm'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        secret=pulumi.get(__ret__, 'secret'),
        self=pulumi.get(__ret__, 'self'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        tsig_key_id=pulumi.get(__ret__, 'tsig_key_id'))


@_utilities.lift_output_func(get_tsig_key)
def get_tsig_key_output(tsig_key_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTsigKeyResult]:
    """
    This data source provides details about a specific Tsig Key resource in Oracle Cloud Infrastructure DNS service.

    Gets information about the specified TSIG key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tsig_key = oci.Dns.get_tsig_key(tsig_key_id=test_tsig_key_oci_dns_tsig_key["id"])
    ```


    :param str tsig_key_id: The OCID of the target TSIG key.
    """
    ...
