# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkspaceKeyArgs', 'WorkspaceKey']

@pulumi.input_type
class WorkspaceKeyArgs:
    def __init__(__self__, *,
                 active: pulumi.Input[bool],
                 synapse_workspace_id: pulumi.Input[str],
                 cusomter_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_versionless_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceKey resource.
        """
        pulumi.set(__self__, "active", active)
        pulumi.set(__self__, "synapse_workspace_id", synapse_workspace_id)
        if cusomter_managed_key_name is not None:
            warnings.warn("""As this property name contained a typo originally, please switch to using 'customer_managed_key_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""cusomter_managed_key_name is deprecated: As this property name contained a typo originally, please switch to using 'customer_managed_key_name' instead.""")
        if cusomter_managed_key_name is not None:
            pulumi.set(__self__, "cusomter_managed_key_name", cusomter_managed_key_name)
        if customer_managed_key_name is not None:
            pulumi.set(__self__, "customer_managed_key_name", customer_managed_key_name)
        if customer_managed_key_versionless_id is not None:
            pulumi.set(__self__, "customer_managed_key_versionless_id", customer_managed_key_versionless_id)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: pulumi.Input[bool]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "synapse_workspace_id")

    @synapse_workspace_id.setter
    def synapse_workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "synapse_workspace_id", value)

    @property
    @pulumi.getter(name="cusomterManagedKeyName")
    def cusomter_managed_key_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cusomter_managed_key_name")

    @cusomter_managed_key_name.setter
    def cusomter_managed_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cusomter_managed_key_name", value)

    @property
    @pulumi.getter(name="customerManagedKeyName")
    def customer_managed_key_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "customer_managed_key_name")

    @customer_managed_key_name.setter
    def customer_managed_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key_name", value)

    @property
    @pulumi.getter(name="customerManagedKeyVersionlessId")
    def customer_managed_key_versionless_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "customer_managed_key_versionless_id")

    @customer_managed_key_versionless_id.setter
    def customer_managed_key_versionless_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key_versionless_id", value)


@pulumi.input_type
class _WorkspaceKeyState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 cusomter_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_versionless_id: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceKey resources.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if cusomter_managed_key_name is not None:
            warnings.warn("""As this property name contained a typo originally, please switch to using 'customer_managed_key_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""cusomter_managed_key_name is deprecated: As this property name contained a typo originally, please switch to using 'customer_managed_key_name' instead.""")
        if cusomter_managed_key_name is not None:
            pulumi.set(__self__, "cusomter_managed_key_name", cusomter_managed_key_name)
        if customer_managed_key_name is not None:
            pulumi.set(__self__, "customer_managed_key_name", customer_managed_key_name)
        if customer_managed_key_versionless_id is not None:
            pulumi.set(__self__, "customer_managed_key_versionless_id", customer_managed_key_versionless_id)
        if synapse_workspace_id is not None:
            pulumi.set(__self__, "synapse_workspace_id", synapse_workspace_id)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="cusomterManagedKeyName")
    def cusomter_managed_key_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cusomter_managed_key_name")

    @cusomter_managed_key_name.setter
    def cusomter_managed_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cusomter_managed_key_name", value)

    @property
    @pulumi.getter(name="customerManagedKeyName")
    def customer_managed_key_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "customer_managed_key_name")

    @customer_managed_key_name.setter
    def customer_managed_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key_name", value)

    @property
    @pulumi.getter(name="customerManagedKeyVersionlessId")
    def customer_managed_key_versionless_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "customer_managed_key_versionless_id")

    @customer_managed_key_versionless_id.setter
    def customer_managed_key_versionless_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key_versionless_id", value)

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "synapse_workspace_id")

    @synapse_workspace_id.setter
    def synapse_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "synapse_workspace_id", value)


class WorkspaceKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 cusomter_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_versionless_id: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a WorkspaceKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a WorkspaceKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WorkspaceKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 cusomter_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_name: Optional[pulumi.Input[str]] = None,
                 customer_managed_key_versionless_id: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceKeyArgs.__new__(WorkspaceKeyArgs)

            if active is None and not opts.urn:
                raise TypeError("Missing required property 'active'")
            __props__.__dict__["active"] = active
            if cusomter_managed_key_name is not None and not opts.urn:
                warnings.warn("""As this property name contained a typo originally, please switch to using 'customer_managed_key_name' instead.""", DeprecationWarning)
                pulumi.log.warn("""cusomter_managed_key_name is deprecated: As this property name contained a typo originally, please switch to using 'customer_managed_key_name' instead.""")
            __props__.__dict__["cusomter_managed_key_name"] = cusomter_managed_key_name
            __props__.__dict__["customer_managed_key_name"] = customer_managed_key_name
            __props__.__dict__["customer_managed_key_versionless_id"] = customer_managed_key_versionless_id
            if synapse_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'synapse_workspace_id'")
            __props__.__dict__["synapse_workspace_id"] = synapse_workspace_id
        super(WorkspaceKey, __self__).__init__(
            'azure:synapse/workspaceKey:WorkspaceKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            cusomter_managed_key_name: Optional[pulumi.Input[str]] = None,
            customer_managed_key_name: Optional[pulumi.Input[str]] = None,
            customer_managed_key_versionless_id: Optional[pulumi.Input[str]] = None,
            synapse_workspace_id: Optional[pulumi.Input[str]] = None) -> 'WorkspaceKey':
        """
        Get an existing WorkspaceKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceKeyState.__new__(_WorkspaceKeyState)

        __props__.__dict__["active"] = active
        __props__.__dict__["cusomter_managed_key_name"] = cusomter_managed_key_name
        __props__.__dict__["customer_managed_key_name"] = customer_managed_key_name
        __props__.__dict__["customer_managed_key_versionless_id"] = customer_managed_key_versionless_id
        __props__.__dict__["synapse_workspace_id"] = synapse_workspace_id
        return WorkspaceKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="cusomterManagedKeyName")
    def cusomter_managed_key_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cusomter_managed_key_name")

    @property
    @pulumi.getter(name="customerManagedKeyName")
    def customer_managed_key_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "customer_managed_key_name")

    @property
    @pulumi.getter(name="customerManagedKeyVersionlessId")
    def customer_managed_key_versionless_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "customer_managed_key_versionless_id")

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "synapse_workspace_id")

