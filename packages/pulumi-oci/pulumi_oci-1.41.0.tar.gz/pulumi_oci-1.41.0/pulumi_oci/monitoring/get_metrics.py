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
    'GetMetricsResult',
    'AwaitableGetMetricsResult',
    'get_metrics',
    'get_metrics_output',
]

@pulumi.output_type
class GetMetricsResult:
    """
    A collection of values returned by getMetrics.
    """
    def __init__(__self__, compartment_id=None, compartment_id_in_subtree=None, dimension_filters=None, filters=None, group_bies=None, id=None, metrics=None, name=None, namespace=None, resource_group=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if dimension_filters and not isinstance(dimension_filters, dict):
            raise TypeError("Expected argument 'dimension_filters' to be a dict")
        pulumi.set(__self__, "dimension_filters", dimension_filters)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if group_bies and not isinstance(group_bies, list):
            raise TypeError("Expected argument 'group_bies' to be a list")
        pulumi.set(__self__, "group_bies", group_bies)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metrics and not isinstance(metrics, list):
            raise TypeError("Expected argument 'metrics' to be a list")
        pulumi.set(__self__, "metrics", metrics)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the resources monitored by the metric.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="dimensionFilters")
    def dimension_filters(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "dimension_filters")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMetricsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "group_bies")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metrics(self) -> Sequence['outputs.GetMetricsMetricResult']:
        """
        The list of metrics.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the metric.  Example: `CpuUtilization`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The source service or application emitting the metric.  Example: `oci_computeagent`
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[str]:
        """
        Resource group provided with the posted metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).  Example: `frontend-fleet`
        """
        return pulumi.get(self, "resource_group")


class AwaitableGetMetricsResult(GetMetricsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetricsResult(
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            dimension_filters=self.dimension_filters,
            filters=self.filters,
            group_bies=self.group_bies,
            id=self.id,
            metrics=self.metrics,
            name=self.name,
            namespace=self.namespace,
            resource_group=self.resource_group)


def get_metrics(compartment_id: Optional[str] = None,
                compartment_id_in_subtree: Optional[bool] = None,
                dimension_filters: Optional[Mapping[str, Any]] = None,
                filters: Optional[Sequence[pulumi.InputType['GetMetricsFilterArgs']]] = None,
                group_bies: Optional[Sequence[str]] = None,
                name: Optional[str] = None,
                namespace: Optional[str] = None,
                resource_group: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetricsResult:
    """
    This data source provides the list of Metrics in Oracle Cloud Infrastructure Monitoring service.

    Returns metric definitions that match the criteria specified in the request. Compartment OCID required.
    For more information, see
    [Listing Metric Definitions](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
    For information about metrics, see
    [Metrics Overview](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview).
    For important limits information, see
    [Limits on Monitoring](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).

    Transactions Per Second (TPS) per-tenancy limit for this operation: 10.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_metrics = oci.Monitoring.get_metrics(compartment_id=compartment_id,
        compartment_id_in_subtree=metric_compartment_id_in_subtree,
        dimension_filters=metric_dimension_filters,
        group_bies=metric_group_by,
        name=metric_name,
        namespace=metric_namespace,
        resource_group=metric_resource_group)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.  Example: `ocid1.compartment.oc1..exampleuniqueID`
    :param bool compartment_id_in_subtree: When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.
    :param Mapping[str, Any] dimension_filters: Qualifiers that you want to use when searching for metric definitions. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.  Example: `{"resourceId": "instance.region1.phx.exampleuniqueID"}`
    :param Sequence[str] group_bies: Group metrics by these fields in the response. For example, to list all metric namespaces available in a compartment, groupBy the "namespace" field. Supported fields: namespace, name, resourceGroup. If `groupBy` is used, then `dimensionFilters` is ignored.
           
           Example - group by namespace: `[ "namespace" ]`
    :param str name: The metric name to use when searching for metric definitions.  Example: `CpuUtilization`
    :param str namespace: The source service or application to use when searching for metric definitions.  Example: `oci_computeagent`
    :param str resource_group: Resource group that you want to match. A null value returns only metric data that has no resource groups. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).  Example: `frontend-fleet`
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['dimensionFilters'] = dimension_filters
    __args__['filters'] = filters
    __args__['groupBies'] = group_bies
    __args__['name'] = name
    __args__['namespace'] = namespace
    __args__['resourceGroup'] = resource_group
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Monitoring/getMetrics:getMetrics', __args__, opts=opts, typ=GetMetricsResult).value

    return AwaitableGetMetricsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        dimension_filters=pulumi.get(__ret__, 'dimension_filters'),
        filters=pulumi.get(__ret__, 'filters'),
        group_bies=pulumi.get(__ret__, 'group_bies'),
        id=pulumi.get(__ret__, 'id'),
        metrics=pulumi.get(__ret__, 'metrics'),
        name=pulumi.get(__ret__, 'name'),
        namespace=pulumi.get(__ret__, 'namespace'),
        resource_group=pulumi.get(__ret__, 'resource_group'))


@_utilities.lift_output_func(get_metrics)
def get_metrics_output(compartment_id: Optional[pulumi.Input[str]] = None,
                       compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                       dimension_filters: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMetricsFilterArgs']]]]] = None,
                       group_bies: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       name: Optional[pulumi.Input[Optional[str]]] = None,
                       namespace: Optional[pulumi.Input[Optional[str]]] = None,
                       resource_group: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetricsResult]:
    """
    This data source provides the list of Metrics in Oracle Cloud Infrastructure Monitoring service.

    Returns metric definitions that match the criteria specified in the request. Compartment OCID required.
    For more information, see
    [Listing Metric Definitions](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
    For information about metrics, see
    [Metrics Overview](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview).
    For important limits information, see
    [Limits on Monitoring](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).

    Transactions Per Second (TPS) per-tenancy limit for this operation: 10.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_metrics = oci.Monitoring.get_metrics(compartment_id=compartment_id,
        compartment_id_in_subtree=metric_compartment_id_in_subtree,
        dimension_filters=metric_dimension_filters,
        group_bies=metric_group_by,
        name=metric_name,
        namespace=metric_namespace,
        resource_group=metric_resource_group)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.  Example: `ocid1.compartment.oc1..exampleuniqueID`
    :param bool compartment_id_in_subtree: When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.
    :param Mapping[str, Any] dimension_filters: Qualifiers that you want to use when searching for metric definitions. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.  Example: `{"resourceId": "instance.region1.phx.exampleuniqueID"}`
    :param Sequence[str] group_bies: Group metrics by these fields in the response. For example, to list all metric namespaces available in a compartment, groupBy the "namespace" field. Supported fields: namespace, name, resourceGroup. If `groupBy` is used, then `dimensionFilters` is ignored.
           
           Example - group by namespace: `[ "namespace" ]`
    :param str name: The metric name to use when searching for metric definitions.  Example: `CpuUtilization`
    :param str namespace: The source service or application to use when searching for metric definitions.  Example: `oci_computeagent`
    :param str resource_group: Resource group that you want to match. A null value returns only metric data that has no resource groups. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).  Example: `frontend-fleet`
    """
    ...
