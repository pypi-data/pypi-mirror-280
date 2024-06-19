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
    'AnnouncementSubscriptionFilterGroups',
    'AnnouncementSubscriptionFilterGroupsFilter',
    'AnnouncementSubscriptionsFilterGroupFilter',
    'GetAnnouncementSubscriptionFilterGroupResult',
    'GetAnnouncementSubscriptionFilterGroupFilterResult',
    'GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionResult',
    'GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemResult',
    'GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupResult',
    'GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupFilterResult',
    'GetAnnouncementSubscriptionsFilterResult',
]

@pulumi.output_type
class AnnouncementSubscriptionFilterGroups(dict):
    def __init__(__self__, *,
                 filters: Sequence['outputs.AnnouncementSubscriptionFilterGroupsFilter'],
                 name: Optional[str] = None):
        """
        :param Sequence['AnnouncementSubscriptionFilterGroupsFilterArgs'] filters: A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group.
        :param str name: The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        pulumi.set(__self__, "filters", filters)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def filters(self) -> Sequence['outputs.AnnouncementSubscriptionFilterGroupsFilter']:
        """
        A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class AnnouncementSubscriptionFilterGroupsFilter(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: The type of filter.
        :param str value: The value of the filter.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of filter.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the filter.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class AnnouncementSubscriptionsFilterGroupFilter(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: (Updatable) The type of filter.
        :param str value: (Updatable) The value of the filter.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        (Updatable) The type of filter.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        (Updatable) The value of the filter.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetAnnouncementSubscriptionFilterGroupResult(dict):
    def __init__(__self__, *,
                 filters: Sequence['outputs.GetAnnouncementSubscriptionFilterGroupFilterResult'],
                 name: str):
        """
        :param Sequence['GetAnnouncementSubscriptionFilterGroupFilterArgs'] filters: A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group. You also cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group.
        :param str name: The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        pulumi.set(__self__, "filters", filters)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def filters(self) -> Sequence['outputs.GetAnnouncementSubscriptionFilterGroupFilterResult']:
        """
        A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group. You also cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetAnnouncementSubscriptionFilterGroupFilterResult(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: The type of filter.
        :param str value: The value of the filter.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of filter.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the filter.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionResult(dict):
    def __init__(__self__, *,
                 items: Sequence['outputs.GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemResult']):
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemResult']:
        return pulumi.get(self, "items")


@pulumi.output_type
class GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemResult(dict):
    def __init__(__self__, *,
                 compartment_id: str,
                 defined_tags: Mapping[str, Any],
                 description: str,
                 display_name: str,
                 filter_groups: Sequence['outputs.GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupResult'],
                 freeform_tags: Mapping[str, Any],
                 id: str,
                 lifecycle_details: str,
                 ons_topic_id: str,
                 preferred_language: str,
                 preferred_time_zone: str,
                 state: str,
                 system_tags: Mapping[str, Any],
                 time_created: str,
                 time_updated: str):
        """
        :param str compartment_id: The OCID of the compartment.
        :param Mapping[str, Any] defined_tags: Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param str description: A description of the announcement subscription. Avoid entering confidential information.
        :param str display_name: A filter to return only resources that match the entire display name given.
        :param Sequence['GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupArgs'] filter_groups: A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for matching purposes.
        :param Mapping[str, Any] freeform_tags: Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param str id: The OCID of the announcement subscription.
        :param str lifecycle_details: A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a resource in a Failed state.
        :param str ons_topic_id: The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.
        :param str preferred_language: (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.
        :param str preferred_time_zone: The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.
        :param str state: A filter to return only announcement subscriptions that match the given lifecycle state.
        :param Mapping[str, Any] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param str time_created: The date and time that the announcement subscription was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        :param str time_updated: The date and time that the announcement subscription was updated, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "defined_tags", defined_tags)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "filter_groups", filter_groups)
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        pulumi.set(__self__, "ons_topic_id", ons_topic_id)
        pulumi.set(__self__, "preferred_language", preferred_language)
        pulumi.set(__self__, "preferred_time_zone", preferred_time_zone)
        pulumi.set(__self__, "state", state)
        pulumi.set(__self__, "system_tags", system_tags)
        pulumi.set(__self__, "time_created", time_created)
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the announcement subscription. Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A filter to return only resources that match the entire display name given.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filterGroups")
    def filter_groups(self) -> Sequence['outputs.GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupResult']:
        """
        A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for matching purposes.
        """
        return pulumi.get(self, "filter_groups")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the announcement subscription.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a resource in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="onsTopicId")
    def ons_topic_id(self) -> str:
        """
        The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.
        """
        return pulumi.get(self, "ons_topic_id")

    @property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> str:
        """
        (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.
        """
        return pulumi.get(self, "preferred_language")

    @property
    @pulumi.getter(name="preferredTimeZone")
    def preferred_time_zone(self) -> str:
        """
        The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.
        """
        return pulumi.get(self, "preferred_time_zone")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        A filter to return only announcement subscriptions that match the given lifecycle state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time that the announcement subscription was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time that the announcement subscription was updated, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_updated")


@pulumi.output_type
class GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupResult(dict):
    def __init__(__self__, *,
                 filters: Sequence['outputs.GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupFilterResult'],
                 name: str):
        """
        :param Sequence['GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupFilterArgs'] filters: A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group. You also cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group.
        :param str name: The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        pulumi.set(__self__, "filters", filters)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def filters(self) -> Sequence['outputs.GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupFilterResult']:
        """
        A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group. You also cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetAnnouncementSubscriptionsAnnouncementSubscriptionCollectionItemFilterGroupFilterResult(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: The type of filter.
        :param str value: The value of the filter.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of filter.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the filter.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetAnnouncementSubscriptionsFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")


