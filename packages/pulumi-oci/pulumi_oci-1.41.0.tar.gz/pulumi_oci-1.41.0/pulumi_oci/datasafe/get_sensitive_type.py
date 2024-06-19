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
    'GetSensitiveTypeResult',
    'AwaitableGetSensitiveTypeResult',
    'get_sensitive_type',
    'get_sensitive_type_output',
]

@pulumi.output_type
class GetSensitiveTypeResult:
    """
    A collection of values returned by getSensitiveType.
    """
    def __init__(__self__, comment_pattern=None, compartment_id=None, data_pattern=None, default_masking_format_id=None, defined_tags=None, description=None, display_name=None, entity_type=None, freeform_tags=None, id=None, is_common=None, name_pattern=None, parent_category_id=None, search_type=None, sensitive_type_id=None, short_name=None, source=None, state=None, system_tags=None, time_created=None, time_updated=None):
        if comment_pattern and not isinstance(comment_pattern, str):
            raise TypeError("Expected argument 'comment_pattern' to be a str")
        pulumi.set(__self__, "comment_pattern", comment_pattern)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if data_pattern and not isinstance(data_pattern, str):
            raise TypeError("Expected argument 'data_pattern' to be a str")
        pulumi.set(__self__, "data_pattern", data_pattern)
        if default_masking_format_id and not isinstance(default_masking_format_id, str):
            raise TypeError("Expected argument 'default_masking_format_id' to be a str")
        pulumi.set(__self__, "default_masking_format_id", default_masking_format_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if entity_type and not isinstance(entity_type, str):
            raise TypeError("Expected argument 'entity_type' to be a str")
        pulumi.set(__self__, "entity_type", entity_type)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_common and not isinstance(is_common, bool):
            raise TypeError("Expected argument 'is_common' to be a bool")
        pulumi.set(__self__, "is_common", is_common)
        if name_pattern and not isinstance(name_pattern, str):
            raise TypeError("Expected argument 'name_pattern' to be a str")
        pulumi.set(__self__, "name_pattern", name_pattern)
        if parent_category_id and not isinstance(parent_category_id, str):
            raise TypeError("Expected argument 'parent_category_id' to be a str")
        pulumi.set(__self__, "parent_category_id", parent_category_id)
        if search_type and not isinstance(search_type, str):
            raise TypeError("Expected argument 'search_type' to be a str")
        pulumi.set(__self__, "search_type", search_type)
        if sensitive_type_id and not isinstance(sensitive_type_id, str):
            raise TypeError("Expected argument 'sensitive_type_id' to be a str")
        pulumi.set(__self__, "sensitive_type_id", sensitive_type_id)
        if short_name and not isinstance(short_name, str):
            raise TypeError("Expected argument 'short_name' to be a str")
        pulumi.set(__self__, "short_name", short_name)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="commentPattern")
    def comment_pattern(self) -> str:
        """
        A regular expression to be used by data discovery for matching column comments.
        """
        return pulumi.get(self, "comment_pattern")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the sensitive type.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dataPattern")
    def data_pattern(self) -> str:
        """
        A regular expression to be used by data discovery for matching column data values.
        """
        return pulumi.get(self, "data_pattern")

    @property
    @pulumi.getter(name="defaultMaskingFormatId")
    def default_masking_format_id(self) -> str:
        """
        The OCID of the library masking format that should be used to mask the sensitive columns associated with the sensitive type.
        """
        return pulumi.get(self, "default_masking_format_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the sensitive type.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the sensitive type.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> str:
        """
        The entity type. It can be either a sensitive type with regular expressions or a sensitive category used for grouping similar sensitive types.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the sensitive type.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCommon")
    def is_common(self) -> bool:
        """
        Specifies whether the sensitive type is common. Common sensitive types belong to  library sensitive types which are frequently used to perform sensitive data discovery.
        """
        return pulumi.get(self, "is_common")

    @property
    @pulumi.getter(name="namePattern")
    def name_pattern(self) -> str:
        """
        A regular expression to be used by data discovery for matching column names.
        """
        return pulumi.get(self, "name_pattern")

    @property
    @pulumi.getter(name="parentCategoryId")
    def parent_category_id(self) -> str:
        """
        The OCID of the parent sensitive category.
        """
        return pulumi.get(self, "parent_category_id")

    @property
    @pulumi.getter(name="searchType")
    def search_type(self) -> str:
        """
        The search type indicating how the column name, comment and data patterns should be used by data discovery. [Learn more](https://docs.oracle.com/en/cloud/paas/data-safe/udscs/sensitive-types.html#GUID-1D1AD98E-B93F-4FF2-80AE-CB7D8A14F6CC).
        """
        return pulumi.get(self, "search_type")

    @property
    @pulumi.getter(name="sensitiveTypeId")
    def sensitive_type_id(self) -> str:
        return pulumi.get(self, "sensitive_type_id")

    @property
    @pulumi.getter(name="shortName")
    def short_name(self) -> str:
        """
        The short name of the sensitive type.
        """
        return pulumi.get(self, "short_name")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        Specifies whether the sensitive type is user-defined or predefined.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the sensitive type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the sensitive type was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the sensitive type was last updated, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetSensitiveTypeResult(GetSensitiveTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSensitiveTypeResult(
            comment_pattern=self.comment_pattern,
            compartment_id=self.compartment_id,
            data_pattern=self.data_pattern,
            default_masking_format_id=self.default_masking_format_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            entity_type=self.entity_type,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_common=self.is_common,
            name_pattern=self.name_pattern,
            parent_category_id=self.parent_category_id,
            search_type=self.search_type,
            sensitive_type_id=self.sensitive_type_id,
            short_name=self.short_name,
            source=self.source,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_sensitive_type(sensitive_type_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSensitiveTypeResult:
    """
    This data source provides details about a specific Sensitive Type resource in Oracle Cloud Infrastructure Data Safe service.

    Gets the details of the specified sensitive type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sensitive_type = oci.DataSafe.get_sensitive_type(sensitive_type_id=test_sensitive_type_oci_data_safe_sensitive_type["id"])
    ```


    :param str sensitive_type_id: The OCID of the sensitive type.
    """
    __args__ = dict()
    __args__['sensitiveTypeId'] = sensitive_type_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSensitiveType:getSensitiveType', __args__, opts=opts, typ=GetSensitiveTypeResult).value

    return AwaitableGetSensitiveTypeResult(
        comment_pattern=pulumi.get(__ret__, 'comment_pattern'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        data_pattern=pulumi.get(__ret__, 'data_pattern'),
        default_masking_format_id=pulumi.get(__ret__, 'default_masking_format_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        entity_type=pulumi.get(__ret__, 'entity_type'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_common=pulumi.get(__ret__, 'is_common'),
        name_pattern=pulumi.get(__ret__, 'name_pattern'),
        parent_category_id=pulumi.get(__ret__, 'parent_category_id'),
        search_type=pulumi.get(__ret__, 'search_type'),
        sensitive_type_id=pulumi.get(__ret__, 'sensitive_type_id'),
        short_name=pulumi.get(__ret__, 'short_name'),
        source=pulumi.get(__ret__, 'source'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_sensitive_type)
def get_sensitive_type_output(sensitive_type_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSensitiveTypeResult]:
    """
    This data source provides details about a specific Sensitive Type resource in Oracle Cloud Infrastructure Data Safe service.

    Gets the details of the specified sensitive type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sensitive_type = oci.DataSafe.get_sensitive_type(sensitive_type_id=test_sensitive_type_oci_data_safe_sensitive_type["id"])
    ```


    :param str sensitive_type_id: The OCID of the sensitive type.
    """
    ...
