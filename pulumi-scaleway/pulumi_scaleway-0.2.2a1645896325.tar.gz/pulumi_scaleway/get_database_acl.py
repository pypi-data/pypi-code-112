# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetDatabaseAclResult',
    'AwaitableGetDatabaseAclResult',
    'get_database_acl',
    'get_database_acl_output',
]

@pulumi.output_type
class GetDatabaseAclResult:
    """
    A collection of values returned by getDatabaseAcl.
    """
    def __init__(__self__, acl_rules=None, id=None, instance_id=None, region=None):
        if acl_rules and not isinstance(acl_rules, list):
            raise TypeError("Expected argument 'acl_rules' to be a list")
        pulumi.set(__self__, "acl_rules", acl_rules)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Sequence['outputs.GetDatabaseAclAclRuleResult']:
        """
        A list of ACLs (structure is described below)
        """
        return pulumi.get(self, "acl_rules")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")


class AwaitableGetDatabaseAclResult(GetDatabaseAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseAclResult(
            acl_rules=self.acl_rules,
            id=self.id,
            instance_id=self.instance_id,
            region=self.region)


def get_database_acl(instance_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseAclResult:
    """
    Gets information about the RDB instance network Access Control List.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    my_acl = scaleway.get_database_acl(instance_id="fr-par/11111111-1111-1111-1111-111111111111")
    ```


    :param str instance_id: The RDB instance ID.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('scaleway:index/getDatabaseAcl:getDatabaseAcl', __args__, opts=opts, typ=GetDatabaseAclResult).value

    return AwaitableGetDatabaseAclResult(
        acl_rules=__ret__.acl_rules,
        id=__ret__.id,
        instance_id=__ret__.instance_id,
        region=__ret__.region)


@_utilities.lift_output_func(get_database_acl)
def get_database_acl_output(instance_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseAclResult]:
    """
    Gets information about the RDB instance network Access Control List.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    my_acl = scaleway.get_database_acl(instance_id="fr-par/11111111-1111-1111-1111-111111111111")
    ```


    :param str instance_id: The RDB instance ID.
    """
    ...
