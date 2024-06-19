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
    'GetModelEvaluationResultsResult',
    'AwaitableGetModelEvaluationResultsResult',
    'get_model_evaluation_results',
    'get_model_evaluation_results_output',
]

@pulumi.output_type
class GetModelEvaluationResultsResult:
    """
    A collection of values returned by getModelEvaluationResults.
    """
    def __init__(__self__, evaluation_result_collections=None, filters=None, id=None, model_id=None):
        if evaluation_result_collections and not isinstance(evaluation_result_collections, list):
            raise TypeError("Expected argument 'evaluation_result_collections' to be a list")
        pulumi.set(__self__, "evaluation_result_collections", evaluation_result_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_id and not isinstance(model_id, str):
            raise TypeError("Expected argument 'model_id' to be a str")
        pulumi.set(__self__, "model_id", model_id)

    @property
    @pulumi.getter(name="evaluationResultCollections")
    def evaluation_result_collections(self) -> Sequence['outputs.GetModelEvaluationResultsEvaluationResultCollectionResult']:
        """
        The list of evaluation_result_collection.
        """
        return pulumi.get(self, "evaluation_result_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetModelEvaluationResultsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelId")
    def model_id(self) -> str:
        return pulumi.get(self, "model_id")


class AwaitableGetModelEvaluationResultsResult(GetModelEvaluationResultsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelEvaluationResultsResult(
            evaluation_result_collections=self.evaluation_result_collections,
            filters=self.filters,
            id=self.id,
            model_id=self.model_id)


def get_model_evaluation_results(filters: Optional[Sequence[pulumi.InputType['GetModelEvaluationResultsFilterArgs']]] = None,
                                 model_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelEvaluationResultsResult:
    """
    This data source provides the list of Model Evaluation Results in Oracle Cloud Infrastructure Ai Language service.

    Get a (paginated) list of evaluation results for a given model.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_model_evaluation_results = oci.AiLanguage.get_model_evaluation_results(model_id=test_model["id"])
    ```


    :param str model_id: unique model OCID.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['modelId'] = model_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:AiLanguage/getModelEvaluationResults:getModelEvaluationResults', __args__, opts=opts, typ=GetModelEvaluationResultsResult).value

    return AwaitableGetModelEvaluationResultsResult(
        evaluation_result_collections=pulumi.get(__ret__, 'evaluation_result_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        model_id=pulumi.get(__ret__, 'model_id'))


@_utilities.lift_output_func(get_model_evaluation_results)
def get_model_evaluation_results_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetModelEvaluationResultsFilterArgs']]]]] = None,
                                        model_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelEvaluationResultsResult]:
    """
    This data source provides the list of Model Evaluation Results in Oracle Cloud Infrastructure Ai Language service.

    Get a (paginated) list of evaluation results for a given model.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_model_evaluation_results = oci.AiLanguage.get_model_evaluation_results(model_id=test_model["id"])
    ```


    :param str model_id: unique model OCID.
    """
    ...
