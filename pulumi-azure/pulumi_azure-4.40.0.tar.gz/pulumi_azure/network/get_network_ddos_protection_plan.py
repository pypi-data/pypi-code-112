# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetNetworkDdosProtectionPlanResult',
    'AwaitableGetNetworkDdosProtectionPlanResult',
    'get_network_ddos_protection_plan',
    'get_network_ddos_protection_plan_output',
]

@pulumi.output_type
class GetNetworkDdosProtectionPlanResult:
    """
    A collection of values returned by getNetworkDdosProtectionPlan.
    """
    def __init__(__self__, id=None, location=None, name=None, resource_group_name=None, tags=None, virtual_network_ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if virtual_network_ids and not isinstance(virtual_network_ids, list):
            raise TypeError("Expected argument 'virtual_network_ids' to be a list")
        pulumi.set(__self__, "virtual_network_ids", virtual_network_ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Specifies the supported Azure location where the resource exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualNetworkIds")
    def virtual_network_ids(self) -> Sequence[str]:
        """
        A list of ID's of the Virtual Networks associated with this DDoS Protection Plan.
        """
        return pulumi.get(self, "virtual_network_ids")


class AwaitableGetNetworkDdosProtectionPlanResult(GetNetworkDdosProtectionPlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkDdosProtectionPlanResult(
            id=self.id,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags,
            virtual_network_ids=self.virtual_network_ids)


def get_network_ddos_protection_plan(name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     tags: Optional[Mapping[str, str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkDdosProtectionPlanResult:
    """
    Use this data source to access information about an existing Azure Network DDoS Protection Plan.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_network_ddos_protection_plan(name=azurerm_network_ddos_protection_plan["example"]["name"],
        resource_group_name=azurerm_network_ddos_protection_plan["example"]["resource_group_name"])
    pulumi.export("ddosProtectionPlanId", example.id)
    ```


    :param str name: The name of the Network DDoS Protection Plan.
    :param str resource_group_name: The name of the resource group where the Network DDoS Protection Plan exists.
    :param Mapping[str, str] tags: A mapping of tags assigned to the resource.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:network/getNetworkDdosProtectionPlan:getNetworkDdosProtectionPlan', __args__, opts=opts, typ=GetNetworkDdosProtectionPlanResult).value

    return AwaitableGetNetworkDdosProtectionPlanResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        tags=__ret__.tags,
        virtual_network_ids=__ret__.virtual_network_ids)


@_utilities.lift_output_func(get_network_ddos_protection_plan)
def get_network_ddos_protection_plan_output(name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkDdosProtectionPlanResult]:
    """
    Use this data source to access information about an existing Azure Network DDoS Protection Plan.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_network_ddos_protection_plan(name=azurerm_network_ddos_protection_plan["example"]["name"],
        resource_group_name=azurerm_network_ddos_protection_plan["example"]["resource_group_name"])
    pulumi.export("ddosProtectionPlanId", example.id)
    ```


    :param str name: The name of the Network DDoS Protection Plan.
    :param str resource_group_name: The name of the resource group where the Network DDoS Protection Plan exists.
    :param Mapping[str, str] tags: A mapping of tags assigned to the resource.
    """
    ...
