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
    'GetPublicationResult',
    'AwaitableGetPublicationResult',
    'get_publication',
    'get_publication_output',
]

@pulumi.output_type
class GetPublicationResult:
    """
    A collection of values returned by getPublication.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, freeform_tags=None, icons=None, id=None, is_agreement_acknowledged=None, listing_type=None, long_description=None, name=None, package_details=None, package_type=None, publication_id=None, short_description=None, state=None, support_contacts=None, supported_operating_systems=None, system_tags=None, time_created=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if icons and not isinstance(icons, list):
            raise TypeError("Expected argument 'icons' to be a list")
        pulumi.set(__self__, "icons", icons)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_agreement_acknowledged and not isinstance(is_agreement_acknowledged, bool):
            raise TypeError("Expected argument 'is_agreement_acknowledged' to be a bool")
        pulumi.set(__self__, "is_agreement_acknowledged", is_agreement_acknowledged)
        if listing_type and not isinstance(listing_type, str):
            raise TypeError("Expected argument 'listing_type' to be a str")
        pulumi.set(__self__, "listing_type", listing_type)
        if long_description and not isinstance(long_description, str):
            raise TypeError("Expected argument 'long_description' to be a str")
        pulumi.set(__self__, "long_description", long_description)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_details and not isinstance(package_details, list):
            raise TypeError("Expected argument 'package_details' to be a list")
        pulumi.set(__self__, "package_details", package_details)
        if package_type and not isinstance(package_type, str):
            raise TypeError("Expected argument 'package_type' to be a str")
        pulumi.set(__self__, "package_type", package_type)
        if publication_id and not isinstance(publication_id, str):
            raise TypeError("Expected argument 'publication_id' to be a str")
        pulumi.set(__self__, "publication_id", publication_id)
        if short_description and not isinstance(short_description, str):
            raise TypeError("Expected argument 'short_description' to be a str")
        pulumi.set(__self__, "short_description", short_description)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if support_contacts and not isinstance(support_contacts, list):
            raise TypeError("Expected argument 'support_contacts' to be a list")
        pulumi.set(__self__, "support_contacts", support_contacts)
        if supported_operating_systems and not isinstance(supported_operating_systems, list):
            raise TypeError("Expected argument 'supported_operating_systems' to be a list")
        pulumi.set(__self__, "supported_operating_systems", supported_operating_systems)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where the publication exists.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def icons(self) -> Sequence['outputs.GetPublicationIconResult']:
        """
        The model for upload data for images and icons.
        """
        return pulumi.get(self, "icons")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique identifier for the publication in Marketplace.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAgreementAcknowledged")
    def is_agreement_acknowledged(self) -> bool:
        return pulumi.get(self, "is_agreement_acknowledged")

    @property
    @pulumi.getter(name="listingType")
    def listing_type(self) -> str:
        """
        The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.
        """
        return pulumi.get(self, "listing_type")

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> str:
        """
        A long description of the publication to use in the listing.
        """
        return pulumi.get(self, "long_description")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the operating system.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageDetails")
    def package_details(self) -> Sequence['outputs.GetPublicationPackageDetailResult']:
        return pulumi.get(self, "package_details")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> str:
        """
        The listing's package type.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter(name="publicationId")
    def publication_id(self) -> str:
        return pulumi.get(self, "publication_id")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> str:
        """
        A short description of the publication to use in the listing.
        """
        return pulumi.get(self, "short_description")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The lifecycle state of the publication.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportContacts")
    def support_contacts(self) -> Sequence['outputs.GetPublicationSupportContactResult']:
        """
        Contact information for getting support from the publisher for the listing.
        """
        return pulumi.get(self, "support_contacts")

    @property
    @pulumi.getter(name="supportedOperatingSystems")
    def supported_operating_systems(self) -> Sequence['outputs.GetPublicationSupportedOperatingSystemResult']:
        """
        The list of operating systems supported by the listing.
        """
        return pulumi.get(self, "supported_operating_systems")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the publication was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")


class AwaitableGetPublicationResult(GetPublicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicationResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            freeform_tags=self.freeform_tags,
            icons=self.icons,
            id=self.id,
            is_agreement_acknowledged=self.is_agreement_acknowledged,
            listing_type=self.listing_type,
            long_description=self.long_description,
            name=self.name,
            package_details=self.package_details,
            package_type=self.package_type,
            publication_id=self.publication_id,
            short_description=self.short_description,
            state=self.state,
            support_contacts=self.support_contacts,
            supported_operating_systems=self.supported_operating_systems,
            system_tags=self.system_tags,
            time_created=self.time_created)


def get_publication(publication_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicationResult:
    """
    This data source provides details about a specific Publication resource in Oracle Cloud Infrastructure Marketplace service.

    Gets the details of the specified publication.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_publication = oci.Marketplace.get_publication(publication_id=test_publication_oci_marketplace_publication["id"])
    ```


    :param str publication_id: The unique identifier for the publication.
    """
    __args__ = dict()
    __args__['publicationId'] = publication_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Marketplace/getPublication:getPublication', __args__, opts=opts, typ=GetPublicationResult).value

    return AwaitableGetPublicationResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        icons=pulumi.get(__ret__, 'icons'),
        id=pulumi.get(__ret__, 'id'),
        is_agreement_acknowledged=pulumi.get(__ret__, 'is_agreement_acknowledged'),
        listing_type=pulumi.get(__ret__, 'listing_type'),
        long_description=pulumi.get(__ret__, 'long_description'),
        name=pulumi.get(__ret__, 'name'),
        package_details=pulumi.get(__ret__, 'package_details'),
        package_type=pulumi.get(__ret__, 'package_type'),
        publication_id=pulumi.get(__ret__, 'publication_id'),
        short_description=pulumi.get(__ret__, 'short_description'),
        state=pulumi.get(__ret__, 'state'),
        support_contacts=pulumi.get(__ret__, 'support_contacts'),
        supported_operating_systems=pulumi.get(__ret__, 'supported_operating_systems'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'))


@_utilities.lift_output_func(get_publication)
def get_publication_output(publication_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicationResult]:
    """
    This data source provides details about a specific Publication resource in Oracle Cloud Infrastructure Marketplace service.

    Gets the details of the specified publication.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_publication = oci.Marketplace.get_publication(publication_id=test_publication_oci_marketplace_publication["id"])
    ```


    :param str publication_id: The unique identifier for the publication.
    """
    ...
