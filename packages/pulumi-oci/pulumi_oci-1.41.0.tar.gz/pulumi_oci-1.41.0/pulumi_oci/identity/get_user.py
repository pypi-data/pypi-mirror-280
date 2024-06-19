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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, capabilities=None, compartment_id=None, db_user_name=None, defined_tags=None, description=None, email=None, email_verified=None, external_identifier=None, freeform_tags=None, id=None, identity_provider_id=None, inactive_state=None, last_successful_login_time=None, name=None, previous_successful_login_time=None, state=None, time_created=None, user_id=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if db_user_name and not isinstance(db_user_name, str):
            raise TypeError("Expected argument 'db_user_name' to be a str")
        pulumi.set(__self__, "db_user_name", db_user_name)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if email_verified and not isinstance(email_verified, bool):
            raise TypeError("Expected argument 'email_verified' to be a bool")
        pulumi.set(__self__, "email_verified", email_verified)
        if external_identifier and not isinstance(external_identifier, str):
            raise TypeError("Expected argument 'external_identifier' to be a str")
        pulumi.set(__self__, "external_identifier", external_identifier)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_provider_id and not isinstance(identity_provider_id, str):
            raise TypeError("Expected argument 'identity_provider_id' to be a str")
        pulumi.set(__self__, "identity_provider_id", identity_provider_id)
        if inactive_state and not isinstance(inactive_state, str):
            raise TypeError("Expected argument 'inactive_state' to be a str")
        pulumi.set(__self__, "inactive_state", inactive_state)
        if last_successful_login_time and not isinstance(last_successful_login_time, str):
            raise TypeError("Expected argument 'last_successful_login_time' to be a str")
        pulumi.set(__self__, "last_successful_login_time", last_successful_login_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if previous_successful_login_time and not isinstance(previous_successful_login_time, str):
            raise TypeError("Expected argument 'previous_successful_login_time' to be a str")
        pulumi.set(__self__, "previous_successful_login_time", previous_successful_login_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def capabilities(self) -> Sequence['outputs.GetUserCapabilityResult']:
        """
        Properties indicating how the user is allowed to authenticate.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the tenancy containing the user.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dbUserName")
    def db_user_name(self) -> str:
        """
        DB username of the DB credential. Has to be unique across the tenancy.
        """
        return pulumi.get(self, "db_user_name")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description you assign to the user. Does not have to be unique, and it's changeable.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address you assign to the user. The email address must be unique across all users in the tenancy.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="emailVerified")
    def email_verified(self) -> bool:
        """
        Whether the email address has been validated.
        """
        return pulumi.get(self, "email_verified")

    @property
    @pulumi.getter(name="externalIdentifier")
    def external_identifier(self) -> str:
        """
        Identifier of the user in the identity provider
        """
        return pulumi.get(self, "external_identifier")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the user.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityProviderId")
    def identity_provider_id(self) -> str:
        """
        The OCID of the `IdentityProvider` this user belongs to.
        """
        return pulumi.get(self, "identity_provider_id")

    @property
    @pulumi.getter(name="inactiveState")
    def inactive_state(self) -> str:
        """
        Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user is inactive:
        * bit 0: SUSPENDED (reserved for future use)
        * bit 1: DISABLED (reserved for future use)
        * bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)
        """
        return pulumi.get(self, "inactive_state")

    @property
    @pulumi.getter(name="lastSuccessfulLoginTime")
    def last_successful_login_time(self) -> str:
        """
        The date and time of when the user most recently logged in the format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`). If there is no login history, this field is null.
        """
        return pulumi.get(self, "last_successful_login_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name you assign to the user during creation. This is the user's login for the Console. The name must be unique across all users in the tenancy and cannot be changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="previousSuccessfulLoginTime")
    def previous_successful_login_time(self) -> str:
        """
        The date and time of when the user most recently logged in the format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`). If there is no login history, this field is null.
        """
        return pulumi.get(self, "previous_successful_login_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The user's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        Date and time the user was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        return pulumi.get(self, "user_id")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            capabilities=self.capabilities,
            compartment_id=self.compartment_id,
            db_user_name=self.db_user_name,
            defined_tags=self.defined_tags,
            description=self.description,
            email=self.email,
            email_verified=self.email_verified,
            external_identifier=self.external_identifier,
            freeform_tags=self.freeform_tags,
            id=self.id,
            identity_provider_id=self.identity_provider_id,
            inactive_state=self.inactive_state,
            last_successful_login_time=self.last_successful_login_time,
            name=self.name,
            previous_successful_login_time=self.previous_successful_login_time,
            state=self.state,
            time_created=self.time_created,
            user_id=self.user_id)


def get_user(user_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    This data source provides details about a specific User resource in Oracle Cloud Infrastructure Identity service.

    Gets the specified user's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_user = oci.Identity.get_user(user_id=test_user_oci_identity_user["id"])
    ```


    :param str user_id: The OCID of the user.
    """
    __args__ = dict()
    __args__['userId'] = user_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        capabilities=pulumi.get(__ret__, 'capabilities'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        db_user_name=pulumi.get(__ret__, 'db_user_name'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        email=pulumi.get(__ret__, 'email'),
        email_verified=pulumi.get(__ret__, 'email_verified'),
        external_identifier=pulumi.get(__ret__, 'external_identifier'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        identity_provider_id=pulumi.get(__ret__, 'identity_provider_id'),
        inactive_state=pulumi.get(__ret__, 'inactive_state'),
        last_successful_login_time=pulumi.get(__ret__, 'last_successful_login_time'),
        name=pulumi.get(__ret__, 'name'),
        previous_successful_login_time=pulumi.get(__ret__, 'previous_successful_login_time'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        user_id=pulumi.get(__ret__, 'user_id'))


@_utilities.lift_output_func(get_user)
def get_user_output(user_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserResult]:
    """
    This data source provides details about a specific User resource in Oracle Cloud Infrastructure Identity service.

    Gets the specified user's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_user = oci.Identity.get_user(user_id=test_user_oci_identity_user["id"])
    ```


    :param str user_id: The OCID of the user.
    """
    ...
