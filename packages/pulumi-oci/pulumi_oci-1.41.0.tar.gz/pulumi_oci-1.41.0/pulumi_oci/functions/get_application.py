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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    """
    A collection of values returned by getApplication.
    """
    def __init__(__self__, application_id=None, compartment_id=None, config=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, image_policy_configs=None, network_security_group_ids=None, shape=None, state=None, subnet_ids=None, syslog_url=None, time_created=None, time_updated=None, trace_configs=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_policy_configs and not isinstance(image_policy_configs, list):
            raise TypeError("Expected argument 'image_policy_configs' to be a list")
        pulumi.set(__self__, "image_policy_configs", image_policy_configs)
        if network_security_group_ids and not isinstance(network_security_group_ids, list):
            raise TypeError("Expected argument 'network_security_group_ids' to be a list")
        pulumi.set(__self__, "network_security_group_ids", network_security_group_ids)
        if shape and not isinstance(shape, str):
            raise TypeError("Expected argument 'shape' to be a str")
        pulumi.set(__self__, "shape", shape)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if syslog_url and not isinstance(syslog_url, str):
            raise TypeError("Expected argument 'syslog_url' to be a str")
        pulumi.set(__self__, "syslog_url", syslog_url)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if trace_configs and not isinstance(trace_configs, list):
            raise TypeError("Expected argument 'trace_configs' to be a list")
        pulumi.set(__self__, "trace_configs", trace_configs)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> str:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the application.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def config(self) -> Mapping[str, Any]:
        """
        Application configuration for functions in this application (passed as environment variables). Can be overridden by function configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.  Example: `{"MY_FUNCTION_CONFIG": "ConfVal"}`
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the application. The display name is unique within the compartment containing the application.
        """
        return pulumi.get(self, "display_name")

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
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the application.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imagePolicyConfigs")
    def image_policy_configs(self) -> Sequence['outputs.GetApplicationImagePolicyConfigResult']:
        """
        Define the image signature verification policy for an application.
        """
        return pulumi.get(self, "image_policy_configs")

    @property
    @pulumi.getter(name="networkSecurityGroupIds")
    def network_security_group_ids(self) -> Sequence[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application to.
        """
        return pulumi.get(self, "network_security_group_ids")

    @property
    @pulumi.getter
    def shape(self) -> str:
        """
        Valid values are `GENERIC_X86`, `GENERIC_ARM` and `GENERIC_X86_ARM`. Default is `GENERIC_X86`. Setting this to `GENERIC_X86`, will run the functions in the application on X86 processor architecture. Setting this to `GENERIC_ARM`, will run the functions in the application on ARM processor architecture. When set to `GENERIC_X86_ARM`, functions in the application are run on either X86 or ARM processor architecture. Accepted values are: `GENERIC_X86`, `GENERIC_ARM`, `GENERIC_X86_ARM`
        """
        return pulumi.get(self, "shape")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the application.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the application.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="syslogUrl")
    def syslog_url(self) -> str:
        """
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls. The syslog URL must be reachable from all of the subnets configured for the application. Note: If you enable the Oracle Cloud Infrastructure Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the Oracle Cloud Infrastructure Logging service, and not to the syslog URL.  Example: `tcp://logserver.myserver:1234`
        """
        return pulumi.get(self, "syslog_url")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the application was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2018-09-12T22:47:12.613Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the application was updated, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2018-09-12T22:47:12.613Z`
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="traceConfigs")
    def trace_configs(self) -> Sequence['outputs.GetApplicationTraceConfigResult']:
        """
        Define the tracing configuration for an application.
        """
        return pulumi.get(self, "trace_configs")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            application_id=self.application_id,
            compartment_id=self.compartment_id,
            config=self.config,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            image_policy_configs=self.image_policy_configs,
            network_security_group_ids=self.network_security_group_ids,
            shape=self.shape,
            state=self.state,
            subnet_ids=self.subnet_ids,
            syslog_url=self.syslog_url,
            time_created=self.time_created,
            time_updated=self.time_updated,
            trace_configs=self.trace_configs)


def get_application(application_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    This data source provides details about a specific Application resource in Oracle Cloud Infrastructure Functions service.

    Retrieves an application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_application = oci.Functions.get_application(application_id=test_application_oci_functions_application["id"])
    ```


    :param str application_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this application.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getApplication:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        application_id=pulumi.get(__ret__, 'application_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        config=pulumi.get(__ret__, 'config'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        image_policy_configs=pulumi.get(__ret__, 'image_policy_configs'),
        network_security_group_ids=pulumi.get(__ret__, 'network_security_group_ids'),
        shape=pulumi.get(__ret__, 'shape'),
        state=pulumi.get(__ret__, 'state'),
        subnet_ids=pulumi.get(__ret__, 'subnet_ids'),
        syslog_url=pulumi.get(__ret__, 'syslog_url'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        trace_configs=pulumi.get(__ret__, 'trace_configs'))


@_utilities.lift_output_func(get_application)
def get_application_output(application_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    This data source provides details about a specific Application resource in Oracle Cloud Infrastructure Functions service.

    Retrieves an application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_application = oci.Functions.get_application(application_id=test_application_oci_functions_application["id"])
    ```


    :param str application_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this application.
    """
    ...
