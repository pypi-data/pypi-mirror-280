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
    'GetBackendSetHealthResult',
    'AwaitableGetBackendSetHealthResult',
    'get_backend_set_health',
    'get_backend_set_health_output',
]

@pulumi.output_type
class GetBackendSetHealthResult:
    """
    A collection of values returned by getBackendSetHealth.
    """
    def __init__(__self__, backend_set_name=None, critical_state_backend_names=None, id=None, load_balancer_id=None, status=None, total_backend_count=None, unknown_state_backend_names=None, warning_state_backend_names=None):
        if backend_set_name and not isinstance(backend_set_name, str):
            raise TypeError("Expected argument 'backend_set_name' to be a str")
        pulumi.set(__self__, "backend_set_name", backend_set_name)
        if critical_state_backend_names and not isinstance(critical_state_backend_names, list):
            raise TypeError("Expected argument 'critical_state_backend_names' to be a list")
        pulumi.set(__self__, "critical_state_backend_names", critical_state_backend_names)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancer_id and not isinstance(load_balancer_id, str):
            raise TypeError("Expected argument 'load_balancer_id' to be a str")
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if total_backend_count and not isinstance(total_backend_count, int):
            raise TypeError("Expected argument 'total_backend_count' to be a int")
        pulumi.set(__self__, "total_backend_count", total_backend_count)
        if unknown_state_backend_names and not isinstance(unknown_state_backend_names, list):
            raise TypeError("Expected argument 'unknown_state_backend_names' to be a list")
        pulumi.set(__self__, "unknown_state_backend_names", unknown_state_backend_names)
        if warning_state_backend_names and not isinstance(warning_state_backend_names, list):
            raise TypeError("Expected argument 'warning_state_backend_names' to be a list")
        pulumi.set(__self__, "warning_state_backend_names", warning_state_backend_names)

    @property
    @pulumi.getter(name="backendSetName")
    def backend_set_name(self) -> str:
        return pulumi.get(self, "backend_set_name")

    @property
    @pulumi.getter(name="criticalStateBackendNames")
    def critical_state_backend_names(self) -> Sequence[str]:
        """
        A list of backend servers that are currently in the `CRITICAL` health state. The list identifies each backend server by IP address and port.  Example: `10.0.0.4:8080`
        """
        return pulumi.get(self, "critical_state_backend_names")

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
    @pulumi.getter
    def status(self) -> str:
        """
        Overall health status of the backend set.
        *  **OK:** All backend servers in the backend set return a status of `OK`.
        *  **WARNING:** Half or more of the backend set's backend servers return a status of `OK` and at least one backend server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`.
        *  **CRITICAL:** Fewer than half of the backend set's backend servers return a status of `OK`.
        *  **UNKNOWN:** More than half of the backend set's backend servers return a status of `UNKNOWN`, the system was unable to retrieve metrics, or the backend set does not have a listener attached.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="totalBackendCount")
    def total_backend_count(self) -> int:
        """
        The total number of backend servers in this backend set.  Example: `7`
        """
        return pulumi.get(self, "total_backend_count")

    @property
    @pulumi.getter(name="unknownStateBackendNames")
    def unknown_state_backend_names(self) -> Sequence[str]:
        """
        A list of backend servers that are currently in the `UNKNOWN` health state. The list identifies each backend server by IP address and port.  Example: `10.0.0.5:8080`
        """
        return pulumi.get(self, "unknown_state_backend_names")

    @property
    @pulumi.getter(name="warningStateBackendNames")
    def warning_state_backend_names(self) -> Sequence[str]:
        """
        A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by IP address and port.  Example: `10.0.0.3:8080`
        """
        return pulumi.get(self, "warning_state_backend_names")


class AwaitableGetBackendSetHealthResult(GetBackendSetHealthResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackendSetHealthResult(
            backend_set_name=self.backend_set_name,
            critical_state_backend_names=self.critical_state_backend_names,
            id=self.id,
            load_balancer_id=self.load_balancer_id,
            status=self.status,
            total_backend_count=self.total_backend_count,
            unknown_state_backend_names=self.unknown_state_backend_names,
            warning_state_backend_names=self.warning_state_backend_names)


def get_backend_set_health(backend_set_name: Optional[str] = None,
                           load_balancer_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackendSetHealthResult:
    """
    This data source provides details about a specific Backend Set Health resource in Oracle Cloud Infrastructure Load Balancer service.

    Gets the health status for the specified backend set.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_backend_set_health = oci.LoadBalancer.get_backend_set_health(backend_set_name=test_backend_set["name"],
        load_balancer_id=test_load_balancer["id"])
    ```


    :param str backend_set_name: The name of the backend set to retrieve the health status for.  Example: `example_backend_set`
    :param str load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend set health status to be retrieved.
    """
    __args__ = dict()
    __args__['backendSetName'] = backend_set_name
    __args__['loadBalancerId'] = load_balancer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LoadBalancer/getBackendSetHealth:getBackendSetHealth', __args__, opts=opts, typ=GetBackendSetHealthResult).value

    return AwaitableGetBackendSetHealthResult(
        backend_set_name=pulumi.get(__ret__, 'backend_set_name'),
        critical_state_backend_names=pulumi.get(__ret__, 'critical_state_backend_names'),
        id=pulumi.get(__ret__, 'id'),
        load_balancer_id=pulumi.get(__ret__, 'load_balancer_id'),
        status=pulumi.get(__ret__, 'status'),
        total_backend_count=pulumi.get(__ret__, 'total_backend_count'),
        unknown_state_backend_names=pulumi.get(__ret__, 'unknown_state_backend_names'),
        warning_state_backend_names=pulumi.get(__ret__, 'warning_state_backend_names'))


@_utilities.lift_output_func(get_backend_set_health)
def get_backend_set_health_output(backend_set_name: Optional[pulumi.Input[str]] = None,
                                  load_balancer_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackendSetHealthResult]:
    """
    This data source provides details about a specific Backend Set Health resource in Oracle Cloud Infrastructure Load Balancer service.

    Gets the health status for the specified backend set.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_backend_set_health = oci.LoadBalancer.get_backend_set_health(backend_set_name=test_backend_set["name"],
        load_balancer_id=test_load_balancer["id"])
    ```


    :param str backend_set_name: The name of the backend set to retrieve the health status for.  Example: `example_backend_set`
    :param str load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend set health status to be retrieved.
    """
    ...
