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
    'GetManagementAgentGetAutoUpgradableConfigResult',
    'AwaitableGetManagementAgentGetAutoUpgradableConfigResult',
    'get_management_agent_get_auto_upgradable_config',
    'get_management_agent_get_auto_upgradable_config_output',
]

@pulumi.output_type
class GetManagementAgentGetAutoUpgradableConfigResult:
    """
    A collection of values returned by getManagementAgentGetAutoUpgradableConfig.
    """
    def __init__(__self__, compartment_id=None, id=None, is_agent_auto_upgradable=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_agent_auto_upgradable and not isinstance(is_agent_auto_upgradable, bool):
            raise TypeError("Expected argument 'is_agent_auto_upgradable' to be a bool")
        pulumi.set(__self__, "is_agent_auto_upgradable", is_agent_auto_upgradable)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAgentAutoUpgradable")
    def is_agent_auto_upgradable(self) -> bool:
        """
        true if the agents can be upgraded automatically; false if they must be upgraded manually.
        """
        return pulumi.get(self, "is_agent_auto_upgradable")


class AwaitableGetManagementAgentGetAutoUpgradableConfigResult(GetManagementAgentGetAutoUpgradableConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementAgentGetAutoUpgradableConfigResult(
            compartment_id=self.compartment_id,
            id=self.id,
            is_agent_auto_upgradable=self.is_agent_auto_upgradable)


def get_management_agent_get_auto_upgradable_config(compartment_id: Optional[str] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementAgentGetAutoUpgradableConfigResult:
    """
    This data source provides details about a specific Management Agent Get Auto Upgradable Config resource in Oracle Cloud Infrastructure Management Agent service.

    Get the AutoUpgradable configuration for all agents in a tenancy.
    The supplied compartmentId must be a tenancy root.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_management_agent_get_auto_upgradable_config = oci.ManagementAgent.get_management_agent_get_auto_upgradable_config(compartment_id=compartment_id)
    ```


    :param str compartment_id: The OCID of the compartment to which a request will be scoped.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ManagementAgent/getManagementAgentGetAutoUpgradableConfig:getManagementAgentGetAutoUpgradableConfig', __args__, opts=opts, typ=GetManagementAgentGetAutoUpgradableConfigResult).value

    return AwaitableGetManagementAgentGetAutoUpgradableConfigResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        is_agent_auto_upgradable=pulumi.get(__ret__, 'is_agent_auto_upgradable'))


@_utilities.lift_output_func(get_management_agent_get_auto_upgradable_config)
def get_management_agent_get_auto_upgradable_config_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagementAgentGetAutoUpgradableConfigResult]:
    """
    This data source provides details about a specific Management Agent Get Auto Upgradable Config resource in Oracle Cloud Infrastructure Management Agent service.

    Get the AutoUpgradable configuration for all agents in a tenancy.
    The supplied compartmentId must be a tenancy root.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_management_agent_get_auto_upgradable_config = oci.ManagementAgent.get_management_agent_get_auto_upgradable_config(compartment_id=compartment_id)
    ```


    :param str compartment_id: The OCID of the compartment to which a request will be scoped.
    """
    ...
