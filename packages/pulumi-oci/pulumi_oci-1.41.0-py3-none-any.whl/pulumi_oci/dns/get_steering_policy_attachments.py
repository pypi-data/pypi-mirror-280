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
    'GetSteeringPolicyAttachmentsResult',
    'AwaitableGetSteeringPolicyAttachmentsResult',
    'get_steering_policy_attachments',
    'get_steering_policy_attachments_output',
]

@pulumi.output_type
class GetSteeringPolicyAttachmentsResult:
    """
    A collection of values returned by getSteeringPolicyAttachments.
    """
    def __init__(__self__, compartment_id=None, display_name=None, domain=None, domain_contains=None, filters=None, id=None, state=None, steering_policy_attachments=None, steering_policy_id=None, time_created_greater_than_or_equal_to=None, time_created_less_than=None, zone_id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if domain_contains and not isinstance(domain_contains, str):
            raise TypeError("Expected argument 'domain_contains' to be a str")
        pulumi.set(__self__, "domain_contains", domain_contains)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if steering_policy_attachments and not isinstance(steering_policy_attachments, list):
            raise TypeError("Expected argument 'steering_policy_attachments' to be a list")
        pulumi.set(__self__, "steering_policy_attachments", steering_policy_attachments)
        if steering_policy_id and not isinstance(steering_policy_id, str):
            raise TypeError("Expected argument 'steering_policy_id' to be a str")
        pulumi.set(__self__, "steering_policy_id", steering_policy_id)
        if time_created_greater_than_or_equal_to and not isinstance(time_created_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_created_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_created_greater_than_or_equal_to", time_created_greater_than_or_equal_to)
        if time_created_less_than and not isinstance(time_created_less_than, str):
            raise TypeError("Expected argument 'time_created_less_than' to be a str")
        pulumi.set(__self__, "time_created_less_than", time_created_less_than)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the steering policy attachment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="domainContains")
    def domain_contains(self) -> Optional[str]:
        return pulumi.get(self, "domain_contains")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSteeringPolicyAttachmentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The OCID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="steeringPolicyAttachments")
    def steering_policy_attachments(self) -> Sequence['outputs.GetSteeringPolicyAttachmentsSteeringPolicyAttachmentResult']:
        """
        The list of steering_policy_attachments.
        """
        return pulumi.get(self, "steering_policy_attachments")

    @property
    @pulumi.getter(name="steeringPolicyId")
    def steering_policy_id(self) -> Optional[str]:
        """
        The OCID of the attached steering policy.
        """
        return pulumi.get(self, "steering_policy_id")

    @property
    @pulumi.getter(name="timeCreatedGreaterThanOrEqualTo")
    def time_created_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeCreatedLessThan")
    def time_created_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_less_than")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        """
        The OCID of the attached zone.
        """
        return pulumi.get(self, "zone_id")


class AwaitableGetSteeringPolicyAttachmentsResult(GetSteeringPolicyAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSteeringPolicyAttachmentsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            domain=self.domain,
            domain_contains=self.domain_contains,
            filters=self.filters,
            id=self.id,
            state=self.state,
            steering_policy_attachments=self.steering_policy_attachments,
            steering_policy_id=self.steering_policy_id,
            time_created_greater_than_or_equal_to=self.time_created_greater_than_or_equal_to,
            time_created_less_than=self.time_created_less_than,
            zone_id=self.zone_id)


def get_steering_policy_attachments(compartment_id: Optional[str] = None,
                                    display_name: Optional[str] = None,
                                    domain: Optional[str] = None,
                                    domain_contains: Optional[str] = None,
                                    filters: Optional[Sequence[pulumi.InputType['GetSteeringPolicyAttachmentsFilterArgs']]] = None,
                                    id: Optional[str] = None,
                                    state: Optional[str] = None,
                                    steering_policy_id: Optional[str] = None,
                                    time_created_greater_than_or_equal_to: Optional[str] = None,
                                    time_created_less_than: Optional[str] = None,
                                    zone_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSteeringPolicyAttachmentsResult:
    """
    This data source provides the list of Steering Policy Attachments in Oracle Cloud Infrastructure DNS service.

    Lists the steering policy attachments in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_steering_policy_attachments = oci.Dns.get_steering_policy_attachments(compartment_id=compartment_id,
        display_name=steering_policy_attachment_display_name,
        domain=steering_policy_attachment_domain,
        domain_contains=steering_policy_attachment_domain_contains,
        id=steering_policy_attachment_id,
        state=steering_policy_attachment_state,
        steering_policy_id=test_steering_policy["id"],
        time_created_greater_than_or_equal_to=steering_policy_attachment_time_created_greater_than_or_equal_to,
        time_created_less_than=steering_policy_attachment_time_created_less_than,
        zone_id=test_zone["id"])
    ```


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str display_name: The displayName of a resource.
    :param str domain: Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.
    :param str domain_contains: Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.
    :param str id: The OCID of a resource.
    :param str state: The state of a resource.
    :param str steering_policy_id: Search by steering policy OCID. Will match any resource whose steering policy ID matches the provided value.
    :param str time_created_greater_than_or_equal_to: An [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp that states all returned resources were created on or after the indicated time.
    :param str time_created_less_than: An [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp that states all returned resources were created before the indicated time.
    :param str zone_id: Search by zone OCID. Will match any resource whose zone ID matches the provided value.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['domain'] = domain
    __args__['domainContains'] = domain_contains
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    __args__['steeringPolicyId'] = steering_policy_id
    __args__['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to
    __args__['timeCreatedLessThan'] = time_created_less_than
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getSteeringPolicyAttachments:getSteeringPolicyAttachments', __args__, opts=opts, typ=GetSteeringPolicyAttachmentsResult).value

    return AwaitableGetSteeringPolicyAttachmentsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        domain=pulumi.get(__ret__, 'domain'),
        domain_contains=pulumi.get(__ret__, 'domain_contains'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'),
        steering_policy_attachments=pulumi.get(__ret__, 'steering_policy_attachments'),
        steering_policy_id=pulumi.get(__ret__, 'steering_policy_id'),
        time_created_greater_than_or_equal_to=pulumi.get(__ret__, 'time_created_greater_than_or_equal_to'),
        time_created_less_than=pulumi.get(__ret__, 'time_created_less_than'),
        zone_id=pulumi.get(__ret__, 'zone_id'))


@_utilities.lift_output_func(get_steering_policy_attachments)
def get_steering_policy_attachments_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                           display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                           domain: Optional[pulumi.Input[Optional[str]]] = None,
                                           domain_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSteeringPolicyAttachmentsFilterArgs']]]]] = None,
                                           id: Optional[pulumi.Input[Optional[str]]] = None,
                                           state: Optional[pulumi.Input[Optional[str]]] = None,
                                           steering_policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                                           time_created_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                           time_created_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                                           zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSteeringPolicyAttachmentsResult]:
    """
    This data source provides the list of Steering Policy Attachments in Oracle Cloud Infrastructure DNS service.

    Lists the steering policy attachments in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_steering_policy_attachments = oci.Dns.get_steering_policy_attachments(compartment_id=compartment_id,
        display_name=steering_policy_attachment_display_name,
        domain=steering_policy_attachment_domain,
        domain_contains=steering_policy_attachment_domain_contains,
        id=steering_policy_attachment_id,
        state=steering_policy_attachment_state,
        steering_policy_id=test_steering_policy["id"],
        time_created_greater_than_or_equal_to=steering_policy_attachment_time_created_greater_than_or_equal_to,
        time_created_less_than=steering_policy_attachment_time_created_less_than,
        zone_id=test_zone["id"])
    ```


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str display_name: The displayName of a resource.
    :param str domain: Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.
    :param str domain_contains: Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.
    :param str id: The OCID of a resource.
    :param str state: The state of a resource.
    :param str steering_policy_id: Search by steering policy OCID. Will match any resource whose steering policy ID matches the provided value.
    :param str time_created_greater_than_or_equal_to: An [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp that states all returned resources were created on or after the indicated time.
    :param str time_created_less_than: An [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp that states all returned resources were created before the indicated time.
    :param str zone_id: Search by zone OCID. Will match any resource whose zone ID matches the provided value.
    """
    ...
