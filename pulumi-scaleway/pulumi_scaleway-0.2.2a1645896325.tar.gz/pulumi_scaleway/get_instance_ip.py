# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetInstanceIpResult',
    'AwaitableGetInstanceIpResult',
    'get_instance_ip',
    'get_instance_ip_output',
]

@pulumi.output_type
class GetInstanceIpResult:
    """
    A collection of values returned by getInstanceIp.
    """
    def __init__(__self__, address=None, id=None, organization_id=None, project_id=None, reverse=None, server_id=None, zone=None):
        if address and not isinstance(address, str):
            raise TypeError("Expected argument 'address' to be a str")
        pulumi.set(__self__, "address", address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if reverse and not isinstance(reverse, str):
            raise TypeError("Expected argument 'reverse' to be a str")
        pulumi.set(__self__, "reverse", reverse)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The IP address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the IP.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The organization ID the IP is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def reverse(self) -> str:
        """
        The reverse dns attached to this IP
        """
        return pulumi.get(self, "reverse")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> str:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetInstanceIpResult(GetInstanceIpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceIpResult(
            address=self.address,
            id=self.id,
            organization_id=self.organization_id,
            project_id=self.project_id,
            reverse=self.reverse,
            server_id=self.server_id,
            zone=self.zone)


def get_instance_ip(address: Optional[str] = None,
                    id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceIpResult:
    """
    Gets information about an instance IP.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    my_ip = scaleway.get_instance_ip(id="fr-par-1/11111111-1111-1111-1111-111111111111")
    ```


    :param str address: The IPv4 address to retrieve
           Only one of `address` and `id` should be specified.
    :param str id: The ID of the IP address to retrieve
           Only one of `address` and `id` should be specified.
    """
    __args__ = dict()
    __args__['address'] = address
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('scaleway:index/getInstanceIp:getInstanceIp', __args__, opts=opts, typ=GetInstanceIpResult).value

    return AwaitableGetInstanceIpResult(
        address=__ret__.address,
        id=__ret__.id,
        organization_id=__ret__.organization_id,
        project_id=__ret__.project_id,
        reverse=__ret__.reverse,
        server_id=__ret__.server_id,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_instance_ip)
def get_instance_ip_output(address: Optional[pulumi.Input[Optional[str]]] = None,
                           id: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceIpResult]:
    """
    Gets information about an instance IP.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    my_ip = scaleway.get_instance_ip(id="fr-par-1/11111111-1111-1111-1111-111111111111")
    ```


    :param str address: The IPv4 address to retrieve
           Only one of `address` and `id` should be specified.
    :param str id: The ID of the IP address to retrieve
           Only one of `address` and `id` should be specified.
    """
    ...
