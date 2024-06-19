# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BackendArgs', 'Backend']

@pulumi.input_type
class BackendArgs:
    def __init__(__self__, *,
                 backend_set_name: pulumi.Input[str],
                 network_load_balancer_id: pulumi.Input[str],
                 port: pulumi.Input[int],
                 ip_address: Optional[pulumi.Input[str]] = None,
                 is_backup: Optional[pulumi.Input[bool]] = None,
                 is_drain: Optional[pulumi.Input[bool]] = None,
                 is_offline: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Backend resource.
        :param pulumi.Input[str] backend_set_name: The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[int] port: The communication port for the backend server.  Example: `8080`
        :param pulumi.Input[str] ip_address: The IP address of the backend server. Example: `10.0.0.3`
        :param pulumi.Input[bool] is_backup: (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        :param pulumi.Input[bool] is_drain: (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        :param pulumi.Input[bool] is_offline: (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        :param pulumi.Input[str] name: Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        :param pulumi.Input[str] target_id: The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        :param pulumi.Input[int] weight: (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "backend_set_name", backend_set_name)
        pulumi.set(__self__, "network_load_balancer_id", network_load_balancer_id)
        pulumi.set(__self__, "port", port)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if is_backup is not None:
            pulumi.set(__self__, "is_backup", is_backup)
        if is_drain is not None:
            pulumi.set(__self__, "is_drain", is_drain)
        if is_offline is not None:
            pulumi.set(__self__, "is_offline", is_offline)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if target_id is not None:
            pulumi.set(__self__, "target_id", target_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="backendSetName")
    def backend_set_name(self) -> pulumi.Input[str]:
        """
        The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        """
        return pulumi.get(self, "backend_set_name")

    @backend_set_name.setter
    def backend_set_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "backend_set_name", value)

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        """
        return pulumi.get(self, "network_load_balancer_id")

    @network_load_balancer_id.setter
    def network_load_balancer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_load_balancer_id", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        The communication port for the backend server.  Example: `8080`
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the backend server. Example: `10.0.0.3`
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="isBackup")
    def is_backup(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        """
        return pulumi.get(self, "is_backup")

    @is_backup.setter
    def is_backup(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_backup", value)

    @property
    @pulumi.getter(name="isDrain")
    def is_drain(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        """
        return pulumi.get(self, "is_drain")

    @is_drain.setter
    def is_drain(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_drain", value)

    @property
    @pulumi.getter(name="isOffline")
    def is_offline(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        """
        return pulumi.get(self, "is_offline")

    @is_offline.setter
    def is_offline(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_offline", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class _BackendState:
    def __init__(__self__, *,
                 backend_set_name: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 is_backup: Optional[pulumi.Input[bool]] = None,
                 is_drain: Optional[pulumi.Input[bool]] = None,
                 is_offline: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Backend resources.
        :param pulumi.Input[str] backend_set_name: The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        :param pulumi.Input[str] ip_address: The IP address of the backend server. Example: `10.0.0.3`
        :param pulumi.Input[bool] is_backup: (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        :param pulumi.Input[bool] is_drain: (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        :param pulumi.Input[bool] is_offline: (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        :param pulumi.Input[str] name: Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[int] port: The communication port for the backend server.  Example: `8080`
        :param pulumi.Input[str] target_id: The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        :param pulumi.Input[int] weight: (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if backend_set_name is not None:
            pulumi.set(__self__, "backend_set_name", backend_set_name)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if is_backup is not None:
            pulumi.set(__self__, "is_backup", is_backup)
        if is_drain is not None:
            pulumi.set(__self__, "is_drain", is_drain)
        if is_offline is not None:
            pulumi.set(__self__, "is_offline", is_offline)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_load_balancer_id is not None:
            pulumi.set(__self__, "network_load_balancer_id", network_load_balancer_id)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if target_id is not None:
            pulumi.set(__self__, "target_id", target_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="backendSetName")
    def backend_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        """
        return pulumi.get(self, "backend_set_name")

    @backend_set_name.setter
    def backend_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend_set_name", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the backend server. Example: `10.0.0.3`
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="isBackup")
    def is_backup(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        """
        return pulumi.get(self, "is_backup")

    @is_backup.setter
    def is_backup(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_backup", value)

    @property
    @pulumi.getter(name="isDrain")
    def is_drain(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        """
        return pulumi.get(self, "is_drain")

    @is_drain.setter
    def is_drain(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_drain", value)

    @property
    @pulumi.getter(name="isOffline")
    def is_offline(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        """
        return pulumi.get(self, "is_offline")

    @is_offline.setter
    def is_offline(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_offline", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        """
        return pulumi.get(self, "network_load_balancer_id")

    @network_load_balancer_id.setter
    def network_load_balancer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_load_balancer_id", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The communication port for the backend server.  Example: `8080`
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class Backend(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_set_name: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 is_backup: Optional[pulumi.Input[bool]] = None,
                 is_drain: Optional[pulumi.Input[bool]] = None,
                 is_offline: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        This resource provides the Backend resource in Oracle Cloud Infrastructure Network Load Balancer service.

        Adds a backend server to a backend set.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_backend = oci.network_load_balancer.Backend("test_backend",
            backend_set_name=test_backend_set["name"],
            network_load_balancer_id=test_network_load_balancer["id"],
            port=backend_port,
            ip_address=backend_ip_address,
            is_backup=backend_is_backup,
            is_drain=backend_is_drain,
            is_offline=backend_is_offline,
            name=backend_name,
            target_id=test_target["id"],
            weight=backend_weight)
        ```

        ## Import

        Backends can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:NetworkLoadBalancer/backend:Backend test_backend "networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_set_name: The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        :param pulumi.Input[str] ip_address: The IP address of the backend server. Example: `10.0.0.3`
        :param pulumi.Input[bool] is_backup: (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        :param pulumi.Input[bool] is_drain: (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        :param pulumi.Input[bool] is_offline: (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        :param pulumi.Input[str] name: Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[int] port: The communication port for the backend server.  Example: `8080`
        :param pulumi.Input[str] target_id: The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        :param pulumi.Input[int] weight: (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackendArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Backend resource in Oracle Cloud Infrastructure Network Load Balancer service.

        Adds a backend server to a backend set.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_backend = oci.network_load_balancer.Backend("test_backend",
            backend_set_name=test_backend_set["name"],
            network_load_balancer_id=test_network_load_balancer["id"],
            port=backend_port,
            ip_address=backend_ip_address,
            is_backup=backend_is_backup,
            is_drain=backend_is_drain,
            is_offline=backend_is_offline,
            name=backend_name,
            target_id=test_target["id"],
            weight=backend_weight)
        ```

        ## Import

        Backends can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:NetworkLoadBalancer/backend:Backend test_backend "networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        ```

        :param str resource_name: The name of the resource.
        :param BackendArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackendArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_set_name: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 is_backup: Optional[pulumi.Input[bool]] = None,
                 is_drain: Optional[pulumi.Input[bool]] = None,
                 is_offline: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackendArgs.__new__(BackendArgs)

            if backend_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'backend_set_name'")
            __props__.__dict__["backend_set_name"] = backend_set_name
            __props__.__dict__["ip_address"] = ip_address
            __props__.__dict__["is_backup"] = is_backup
            __props__.__dict__["is_drain"] = is_drain
            __props__.__dict__["is_offline"] = is_offline
            __props__.__dict__["name"] = name
            if network_load_balancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_load_balancer_id'")
            __props__.__dict__["network_load_balancer_id"] = network_load_balancer_id
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            __props__.__dict__["target_id"] = target_id
            __props__.__dict__["weight"] = weight
        super(Backend, __self__).__init__(
            'oci:NetworkLoadBalancer/backend:Backend',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backend_set_name: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            is_backup: Optional[pulumi.Input[bool]] = None,
            is_drain: Optional[pulumi.Input[bool]] = None,
            is_offline: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_load_balancer_id: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            target_id: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'Backend':
        """
        Get an existing Backend resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_set_name: The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        :param pulumi.Input[str] ip_address: The IP address of the backend server. Example: `10.0.0.3`
        :param pulumi.Input[bool] is_backup: (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        :param pulumi.Input[bool] is_drain: (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        :param pulumi.Input[bool] is_offline: (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        :param pulumi.Input[str] name: Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[int] port: The communication port for the backend server.  Example: `8080`
        :param pulumi.Input[str] target_id: The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        :param pulumi.Input[int] weight: (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackendState.__new__(_BackendState)

        __props__.__dict__["backend_set_name"] = backend_set_name
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["is_backup"] = is_backup
        __props__.__dict__["is_drain"] = is_drain
        __props__.__dict__["is_offline"] = is_offline
        __props__.__dict__["name"] = name
        __props__.__dict__["network_load_balancer_id"] = network_load_balancer_id
        __props__.__dict__["port"] = port
        __props__.__dict__["target_id"] = target_id
        __props__.__dict__["weight"] = weight
        return Backend(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendSetName")
    def backend_set_name(self) -> pulumi.Output[str]:
        """
        The name of the backend set to which to add the backend server.  Example: `example_backend_set`
        """
        return pulumi.get(self, "backend_set_name")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The IP address of the backend server. Example: `10.0.0.3`
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isBackup")
    def is_backup(self) -> pulumi.Output[bool]:
        """
        (Updatable) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "isBackup" fail the health check policy.  Example: `false`
        """
        return pulumi.get(self, "is_backup")

    @property
    @pulumi.getter(name="isDrain")
    def is_drain(self) -> pulumi.Output[bool]:
        """
        (Updatable) Whether the network load balancer should drain this server. Servers marked "isDrain" receive no incoming traffic.  Example: `false`
        """
        return pulumi.get(self, "is_drain")

    @property
    @pulumi.getter(name="isOffline")
    def is_offline(self) -> pulumi.Output[bool]:
        """
        (Updatable) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`
        """
        return pulumi.get(self, "is_offline")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        """
        return pulumi.get(self, "network_load_balancer_id")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        The communication port for the backend server.  Example: `8080`
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[str]:
        """
        The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[int]:
        """
        (Updatable) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies).  Example: `3` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "weight")

