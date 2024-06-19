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
    'GetLoadBalancerRoutingPoliciesResult',
    'AwaitableGetLoadBalancerRoutingPoliciesResult',
    'get_load_balancer_routing_policies',
    'get_load_balancer_routing_policies_output',
]

@pulumi.output_type
class GetLoadBalancerRoutingPoliciesResult:
    """
    A collection of values returned by getLoadBalancerRoutingPolicies.
    """
    def __init__(__self__, filters=None, id=None, load_balancer_id=None, routing_policies=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancer_id and not isinstance(load_balancer_id, str):
            raise TypeError("Expected argument 'load_balancer_id' to be a str")
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        if routing_policies and not isinstance(routing_policies, list):
            raise TypeError("Expected argument 'routing_policies' to be a list")
        pulumi.set(__self__, "routing_policies", routing_policies)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetLoadBalancerRoutingPoliciesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> str:
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter(name="routingPolicies")
    def routing_policies(self) -> Sequence['outputs.GetLoadBalancerRoutingPoliciesRoutingPolicyResult']:
        """
        The list of routing_policies.
        """
        return pulumi.get(self, "routing_policies")


class AwaitableGetLoadBalancerRoutingPoliciesResult(GetLoadBalancerRoutingPoliciesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerRoutingPoliciesResult(
            filters=self.filters,
            id=self.id,
            load_balancer_id=self.load_balancer_id,
            routing_policies=self.routing_policies)


def get_load_balancer_routing_policies(filters: Optional[Sequence[pulumi.InputType['GetLoadBalancerRoutingPoliciesFilterArgs']]] = None,
                                       load_balancer_id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerRoutingPoliciesResult:
    """
    This data source provides the list of Load Balancer Routing Policies in Oracle Cloud Infrastructure Load Balancer service.

    Lists all routing policies associated with the specified load balancer.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_load_balancer_routing_policies = oci.LoadBalancer.get_load_balancer_routing_policies(load_balancer_id=test_load_balancer["id"])
    ```


    :param str load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer associated with the routing policies.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['loadBalancerId'] = load_balancer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LoadBalancer/getLoadBalancerRoutingPolicies:getLoadBalancerRoutingPolicies', __args__, opts=opts, typ=GetLoadBalancerRoutingPoliciesResult).value

    return AwaitableGetLoadBalancerRoutingPoliciesResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        load_balancer_id=pulumi.get(__ret__, 'load_balancer_id'),
        routing_policies=pulumi.get(__ret__, 'routing_policies'))


@_utilities.lift_output_func(get_load_balancer_routing_policies)
def get_load_balancer_routing_policies_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetLoadBalancerRoutingPoliciesFilterArgs']]]]] = None,
                                              load_balancer_id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoadBalancerRoutingPoliciesResult]:
    """
    This data source provides the list of Load Balancer Routing Policies in Oracle Cloud Infrastructure Load Balancer service.

    Lists all routing policies associated with the specified load balancer.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_load_balancer_routing_policies = oci.LoadBalancer.get_load_balancer_routing_policies(load_balancer_id=test_load_balancer["id"])
    ```


    :param str load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer associated with the routing policies.
    """
    ...
