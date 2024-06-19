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
    'GetPeerResult',
    'AwaitableGetPeerResult',
    'get_peer',
    'get_peer_output',
]

@pulumi.output_type
class GetPeerResult:
    """
    A collection of values returned by getPeer.
    """
    def __init__(__self__, ad=None, alias=None, blockchain_platform_id=None, host=None, id=None, ocpu_allocation_params=None, peer_id=None, peer_key=None, role=None, state=None):
        if ad and not isinstance(ad, str):
            raise TypeError("Expected argument 'ad' to be a str")
        pulumi.set(__self__, "ad", ad)
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        pulumi.set(__self__, "alias", alias)
        if blockchain_platform_id and not isinstance(blockchain_platform_id, str):
            raise TypeError("Expected argument 'blockchain_platform_id' to be a str")
        pulumi.set(__self__, "blockchain_platform_id", blockchain_platform_id)
        if host and not isinstance(host, str):
            raise TypeError("Expected argument 'host' to be a str")
        pulumi.set(__self__, "host", host)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ocpu_allocation_params and not isinstance(ocpu_allocation_params, list):
            raise TypeError("Expected argument 'ocpu_allocation_params' to be a list")
        pulumi.set(__self__, "ocpu_allocation_params", ocpu_allocation_params)
        if peer_id and not isinstance(peer_id, str):
            raise TypeError("Expected argument 'peer_id' to be a str")
        pulumi.set(__self__, "peer_id", peer_id)
        if peer_key and not isinstance(peer_key, str):
            raise TypeError("Expected argument 'peer_key' to be a str")
        pulumi.set(__self__, "peer_key", peer_key)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def ad(self) -> str:
        """
        Availability Domain of peer
        """
        return pulumi.get(self, "ad")

    @property
    @pulumi.getter
    def alias(self) -> str:
        """
        peer alias
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="blockchainPlatformId")
    def blockchain_platform_id(self) -> str:
        return pulumi.get(self, "blockchain_platform_id")

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        Host on which the Peer exists
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ocpuAllocationParams")
    def ocpu_allocation_params(self) -> Sequence['outputs.GetPeerOcpuAllocationParamResult']:
        """
        OCPU allocation parameter
        """
        return pulumi.get(self, "ocpu_allocation_params")

    @property
    @pulumi.getter(name="peerId")
    def peer_id(self) -> str:
        return pulumi.get(self, "peer_id")

    @property
    @pulumi.getter(name="peerKey")
    def peer_key(self) -> str:
        """
        peer identifier
        """
        return pulumi.get(self, "peer_key")

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        Peer role
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the peer.
        """
        return pulumi.get(self, "state")


class AwaitableGetPeerResult(GetPeerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPeerResult(
            ad=self.ad,
            alias=self.alias,
            blockchain_platform_id=self.blockchain_platform_id,
            host=self.host,
            id=self.id,
            ocpu_allocation_params=self.ocpu_allocation_params,
            peer_id=self.peer_id,
            peer_key=self.peer_key,
            role=self.role,
            state=self.state)


def get_peer(blockchain_platform_id: Optional[str] = None,
             peer_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPeerResult:
    """
    This data source provides details about a specific Peer resource in Oracle Cloud Infrastructure Blockchain service.

    Gets information about a peer identified by the specific id

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_peer = oci.Blockchain.get_peer(blockchain_platform_id=test_blockchain_platform["id"],
        peer_id=test_peer_oci_blockchain_peer["id"])
    ```


    :param str blockchain_platform_id: Unique service identifier.
    :param str peer_id: Peer identifier.
    """
    __args__ = dict()
    __args__['blockchainPlatformId'] = blockchain_platform_id
    __args__['peerId'] = peer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Blockchain/getPeer:getPeer', __args__, opts=opts, typ=GetPeerResult).value

    return AwaitableGetPeerResult(
        ad=pulumi.get(__ret__, 'ad'),
        alias=pulumi.get(__ret__, 'alias'),
        blockchain_platform_id=pulumi.get(__ret__, 'blockchain_platform_id'),
        host=pulumi.get(__ret__, 'host'),
        id=pulumi.get(__ret__, 'id'),
        ocpu_allocation_params=pulumi.get(__ret__, 'ocpu_allocation_params'),
        peer_id=pulumi.get(__ret__, 'peer_id'),
        peer_key=pulumi.get(__ret__, 'peer_key'),
        role=pulumi.get(__ret__, 'role'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_peer)
def get_peer_output(blockchain_platform_id: Optional[pulumi.Input[str]] = None,
                    peer_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPeerResult]:
    """
    This data source provides details about a specific Peer resource in Oracle Cloud Infrastructure Blockchain service.

    Gets information about a peer identified by the specific id

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_peer = oci.Blockchain.get_peer(blockchain_platform_id=test_blockchain_platform["id"],
        peer_id=test_peer_oci_blockchain_peer["id"])
    ```


    :param str blockchain_platform_id: Unique service identifier.
    :param str peer_id: Peer identifier.
    """
    ...
