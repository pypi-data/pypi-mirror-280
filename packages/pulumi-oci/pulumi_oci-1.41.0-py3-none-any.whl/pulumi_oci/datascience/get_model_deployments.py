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
    'GetModelDeploymentsResult',
    'AwaitableGetModelDeploymentsResult',
    'get_model_deployments',
    'get_model_deployments_output',
]

@pulumi.output_type
class GetModelDeploymentsResult:
    """
    A collection of values returned by getModelDeployments.
    """
    def __init__(__self__, compartment_id=None, created_by=None, display_name=None, filters=None, id=None, model_deployments=None, project_id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_deployments and not isinstance(model_deployments, list):
            raise TypeError("Expected argument 'model_deployments' to be a list")
        pulumi.set(__self__, "model_deployments", model_deployments)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the model deployment.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetModelDeploymentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelDeployments")
    def model_deployments(self) -> Sequence['outputs.GetModelDeploymentsModelDeploymentResult']:
        """
        The list of model_deployments.
        """
        return pulumi.get(self, "model_deployments")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the model deployment.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the model deployment.
        """
        return pulumi.get(self, "state")


class AwaitableGetModelDeploymentsResult(GetModelDeploymentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelDeploymentsResult(
            compartment_id=self.compartment_id,
            created_by=self.created_by,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            model_deployments=self.model_deployments,
            project_id=self.project_id,
            state=self.state)


def get_model_deployments(compartment_id: Optional[str] = None,
                          created_by: Optional[str] = None,
                          display_name: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetModelDeploymentsFilterArgs']]] = None,
                          id: Optional[str] = None,
                          project_id: Optional[str] = None,
                          state: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelDeploymentsResult:
    """
    This data source provides the list of Model Deployments in Oracle Cloud Infrastructure Datascience service.

    Lists all model deployments in the specified compartment. Only one parameter other than compartmentId may also be included in a query. The query must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_model_deployments = oci.DataScience.get_model_deployments(compartment_id=compartment_id,
        created_by=model_deployment_created_by,
        display_name=model_deployment_display_name,
        id=model_deployment_id,
        project_id=test_project["id"],
        state=model_deployment_state)
    ```


    :param str compartment_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str created_by: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the resource.
    :param str display_name: <b>Filter</b> results by its user-friendly name.
    :param str id: <b>Filter</b> results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.
    :param str project_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project.
    :param str state: <b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['createdBy'] = created_by
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['projectId'] = project_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataScience/getModelDeployments:getModelDeployments', __args__, opts=opts, typ=GetModelDeploymentsResult).value

    return AwaitableGetModelDeploymentsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_by=pulumi.get(__ret__, 'created_by'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        model_deployments=pulumi.get(__ret__, 'model_deployments'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_model_deployments)
def get_model_deployments_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                 created_by: Optional[pulumi.Input[Optional[str]]] = None,
                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetModelDeploymentsFilterArgs']]]]] = None,
                                 id: Optional[pulumi.Input[Optional[str]]] = None,
                                 project_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 state: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelDeploymentsResult]:
    """
    This data source provides the list of Model Deployments in Oracle Cloud Infrastructure Datascience service.

    Lists all model deployments in the specified compartment. Only one parameter other than compartmentId may also be included in a query. The query must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_model_deployments = oci.DataScience.get_model_deployments(compartment_id=compartment_id,
        created_by=model_deployment_created_by,
        display_name=model_deployment_display_name,
        id=model_deployment_id,
        project_id=test_project["id"],
        state=model_deployment_state)
    ```


    :param str compartment_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str created_by: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the resource.
    :param str display_name: <b>Filter</b> results by its user-friendly name.
    :param str id: <b>Filter</b> results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.
    :param str project_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project.
    :param str state: <b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
