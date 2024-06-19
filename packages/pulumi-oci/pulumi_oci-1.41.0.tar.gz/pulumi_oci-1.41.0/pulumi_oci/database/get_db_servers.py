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
    'GetDbServersResult',
    'AwaitableGetDbServersResult',
    'get_db_servers',
    'get_db_servers_output',
]

@pulumi.output_type
class GetDbServersResult:
    """
    A collection of values returned by getDbServers.
    """
    def __init__(__self__, compartment_id=None, db_servers=None, display_name=None, exadata_infrastructure_id=None, filters=None, id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if db_servers and not isinstance(db_servers, list):
            raise TypeError("Expected argument 'db_servers' to be a list")
        pulumi.set(__self__, "db_servers", db_servers)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if exadata_infrastructure_id and not isinstance(exadata_infrastructure_id, str):
            raise TypeError("Expected argument 'exadata_infrastructure_id' to be a str")
        pulumi.set(__self__, "exadata_infrastructure_id", exadata_infrastructure_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Sequence['outputs.GetDbServersDbServerResult']:
        """
        The list of db_servers.
        """
        return pulumi.get(self, "db_servers")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The user-friendly name for the Db server. The name does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exadataInfrastructureId")
    def exadata_infrastructure_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        """
        return pulumi.get(self, "exadata_infrastructure_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDbServersFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current state of the Db server.
        """
        return pulumi.get(self, "state")


class AwaitableGetDbServersResult(GetDbServersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbServersResult(
            compartment_id=self.compartment_id,
            db_servers=self.db_servers,
            display_name=self.display_name,
            exadata_infrastructure_id=self.exadata_infrastructure_id,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_db_servers(compartment_id: Optional[str] = None,
                   display_name: Optional[str] = None,
                   exadata_infrastructure_id: Optional[str] = None,
                   filters: Optional[Sequence[pulumi.InputType['GetDbServersFilterArgs']]] = None,
                   state: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbServersResult:
    """
    This data source provides the list of Db Servers in Oracle Cloud Infrastructure Database service.

    Lists the Exadata DB servers in the ExadataInfrastructureId and specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_servers = oci.Database.get_db_servers(compartment_id=compartment_id,
        exadata_infrastructure_id=test_exadata_infrastructure["id"],
        display_name=db_server_display_name,
        state=db_server_state)
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the entire display name given. The match is not case sensitive.
    :param str exadata_infrastructure_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ExadataInfrastructure.
    :param str state: A filter to return only resources that match the given lifecycle state exactly.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['exadataInfrastructureId'] = exadata_infrastructure_id
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getDbServers:getDbServers', __args__, opts=opts, typ=GetDbServersResult).value

    return AwaitableGetDbServersResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        db_servers=pulumi.get(__ret__, 'db_servers'),
        display_name=pulumi.get(__ret__, 'display_name'),
        exadata_infrastructure_id=pulumi.get(__ret__, 'exadata_infrastructure_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_db_servers)
def get_db_servers_output(compartment_id: Optional[pulumi.Input[str]] = None,
                          display_name: Optional[pulumi.Input[Optional[str]]] = None,
                          exadata_infrastructure_id: Optional[pulumi.Input[str]] = None,
                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDbServersFilterArgs']]]]] = None,
                          state: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbServersResult]:
    """
    This data source provides the list of Db Servers in Oracle Cloud Infrastructure Database service.

    Lists the Exadata DB servers in the ExadataInfrastructureId and specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_servers = oci.Database.get_db_servers(compartment_id=compartment_id,
        exadata_infrastructure_id=test_exadata_infrastructure["id"],
        display_name=db_server_display_name,
        state=db_server_state)
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the entire display name given. The match is not case sensitive.
    :param str exadata_infrastructure_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ExadataInfrastructure.
    :param str state: A filter to return only resources that match the given lifecycle state exactly.
    """
    ...
