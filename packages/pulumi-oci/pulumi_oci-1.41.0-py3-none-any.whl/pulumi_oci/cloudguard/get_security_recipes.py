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
    'GetSecurityRecipesResult',
    'AwaitableGetSecurityRecipesResult',
    'get_security_recipes',
    'get_security_recipes_output',
]

@pulumi.output_type
class GetSecurityRecipesResult:
    """
    A collection of values returned by getSecurityRecipes.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, security_recipe_collections=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if security_recipe_collections and not isinstance(security_recipe_collections, list):
            raise TypeError("Expected argument 'security_recipe_collections' to be a list")
        pulumi.set(__self__, "security_recipe_collections", security_recipe_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the recipe
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The recipe's display name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSecurityRecipesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that can’t be changed after creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="securityRecipeCollections")
    def security_recipe_collections(self) -> Sequence['outputs.GetSecurityRecipesSecurityRecipeCollectionResult']:
        """
        The list of security_recipe_collection.
        """
        return pulumi.get(self, "security_recipe_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current lifecycle state of the recipe
        """
        return pulumi.get(self, "state")


class AwaitableGetSecurityRecipesResult(GetSecurityRecipesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityRecipesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            security_recipe_collections=self.security_recipe_collections,
            state=self.state)


def get_security_recipes(compartment_id: Optional[str] = None,
                         display_name: Optional[str] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetSecurityRecipesFilterArgs']]] = None,
                         id: Optional[str] = None,
                         state: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityRecipesResult:
    """
    This data source provides the list of Security Recipes in Oracle Cloud Infrastructure Cloud Guard service.

    Returns a list of security zone recipes (SecurityRecipeSummary resources) in a
    compartment, identified by compartmentId.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_security_recipes = oci.CloudGuard.get_security_recipes(compartment_id=compartment_id,
        display_name=security_recipe_display_name,
        id=security_recipe_id,
        state=security_recipe_state)
    ```


    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: The unique identifier of the security zone recipe. (`SecurityRecipe`)
    :param str state: The field lifecycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudGuard/getSecurityRecipes:getSecurityRecipes', __args__, opts=opts, typ=GetSecurityRecipesResult).value

    return AwaitableGetSecurityRecipesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        security_recipe_collections=pulumi.get(__ret__, 'security_recipe_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_security_recipes)
def get_security_recipes_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSecurityRecipesFilterArgs']]]]] = None,
                                id: Optional[pulumi.Input[Optional[str]]] = None,
                                state: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityRecipesResult]:
    """
    This data source provides the list of Security Recipes in Oracle Cloud Infrastructure Cloud Guard service.

    Returns a list of security zone recipes (SecurityRecipeSummary resources) in a
    compartment, identified by compartmentId.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_security_recipes = oci.CloudGuard.get_security_recipes(compartment_id=compartment_id,
        display_name=security_recipe_display_name,
        id=security_recipe_id,
        state=security_recipe_state)
    ```


    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: The unique identifier of the security zone recipe. (`SecurityRecipe`)
    :param str state: The field lifecycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.
    """
    ...
