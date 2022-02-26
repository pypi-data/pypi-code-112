# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRegistryImageResult',
    'AwaitableGetRegistryImageResult',
    'get_registry_image',
    'get_registry_image_output',
]

@pulumi.output_type
class GetRegistryImageResult:
    """
    A collection of values returned by getRegistryImage.
    """
    def __init__(__self__, id=None, image_id=None, name=None, namespace_id=None, organization_id=None, project_id=None, region=None, size=None, tags=None, visibility=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace_id and not isinstance(namespace_id, str):
            raise TypeError("Expected argument 'namespace_id' to be a str")
        pulumi.set(__self__, "namespace_id", namespace_id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if visibility and not isinstance(visibility, str):
            raise TypeError("Expected argument 'visibility' to be a str")
        pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[str]:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> str:
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The organization ID the image is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the registry image.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        The tags associated with the registry image
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def visibility(self) -> str:
        """
        The privacy policy of the registry image.
        """
        return pulumi.get(self, "visibility")


class AwaitableGetRegistryImageResult(GetRegistryImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryImageResult(
            id=self.id,
            image_id=self.image_id,
            name=self.name,
            namespace_id=self.namespace_id,
            organization_id=self.organization_id,
            project_id=self.project_id,
            region=self.region,
            size=self.size,
            tags=self.tags,
            visibility=self.visibility)


def get_registry_image(image_id: Optional[str] = None,
                       name: Optional[str] = None,
                       namespace_id: Optional[str] = None,
                       project_id: Optional[str] = None,
                       region: Optional[str] = None,
                       tags: Optional[Sequence[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryImageResult:
    """
    Gets information about a registry image.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    my_image = scaleway.get_registry_image(image_id="11111111-1111-1111-1111-111111111111",
        namespace_id="11111111-1111-1111-1111-111111111111")
    ```


    :param str image_id: The image ID.
           Only one of `name` and `image_id` should be specified.
    :param str name: The image name.
           Only one of `name` and `image_id` should be specified.
    :param str namespace_id: The namespace ID in which the image is.
    :param str project_id: `project_id`) The ID of the project the image is associated with.
    :param str region: `region`) The region in which the image exists.
    :param Sequence[str] tags: The tags associated with the registry image
    """
    __args__ = dict()
    __args__['imageId'] = image_id
    __args__['name'] = name
    __args__['namespaceId'] = namespace_id
    __args__['projectId'] = project_id
    __args__['region'] = region
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('scaleway:index/getRegistryImage:getRegistryImage', __args__, opts=opts, typ=GetRegistryImageResult).value

    return AwaitableGetRegistryImageResult(
        id=__ret__.id,
        image_id=__ret__.image_id,
        name=__ret__.name,
        namespace_id=__ret__.namespace_id,
        organization_id=__ret__.organization_id,
        project_id=__ret__.project_id,
        region=__ret__.region,
        size=__ret__.size,
        tags=__ret__.tags,
        visibility=__ret__.visibility)


@_utilities.lift_output_func(get_registry_image)
def get_registry_image_output(image_id: Optional[pulumi.Input[Optional[str]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              namespace_id: Optional[pulumi.Input[Optional[str]]] = None,
                              project_id: Optional[pulumi.Input[Optional[str]]] = None,
                              region: Optional[pulumi.Input[Optional[str]]] = None,
                              tags: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryImageResult]:
    """
    Gets information about a registry image.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    my_image = scaleway.get_registry_image(image_id="11111111-1111-1111-1111-111111111111",
        namespace_id="11111111-1111-1111-1111-111111111111")
    ```


    :param str image_id: The image ID.
           Only one of `name` and `image_id` should be specified.
    :param str name: The image name.
           Only one of `name` and `image_id` should be specified.
    :param str namespace_id: The namespace ID in which the image is.
    :param str project_id: `project_id`) The ID of the project the image is associated with.
    :param str region: `region`) The region in which the image exists.
    :param Sequence[str] tags: The tags associated with the registry image
    """
    ...
