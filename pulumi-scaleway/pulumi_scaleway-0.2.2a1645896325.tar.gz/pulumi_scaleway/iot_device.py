# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IotDeviceArgs', 'IotDevice']

@pulumi.input_type
class IotDeviceArgs:
    def __init__(__self__, *,
                 hub_id: pulumi.Input[str],
                 allow_insecure: Optional[pulumi.Input[bool]] = None,
                 allow_multiple_connections: Optional[pulumi.Input[bool]] = None,
                 certificate: Optional[pulumi.Input['IotDeviceCertificateArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 message_filters: Optional[pulumi.Input['IotDeviceMessageFiltersArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IotDevice resource.
        :param pulumi.Input[str] hub_id: The ID of the hub on which this device will be created.
        :param pulumi.Input[bool] allow_insecure: Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        :param pulumi.Input[bool] allow_multiple_connections: Allow more than one simultaneous connection using the same device credentials.
        :param pulumi.Input['IotDeviceCertificateArgs'] certificate: The certificate bundle of the device.
        :param pulumi.Input[str] description: The description of the IoT device (e.g. `living room`).
        :param pulumi.Input['IotDeviceMessageFiltersArgs'] message_filters: Rules that define which messages are authorized or denied based on their topic.
        :param pulumi.Input[str] name: The name of the IoT device you want to create (e.g. `my-device`).
        :param pulumi.Input[str] region: The region you want to attach the resource to
        """
        pulumi.set(__self__, "hub_id", hub_id)
        if allow_insecure is not None:
            pulumi.set(__self__, "allow_insecure", allow_insecure)
        if allow_multiple_connections is not None:
            pulumi.set(__self__, "allow_multiple_connections", allow_multiple_connections)
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if message_filters is not None:
            pulumi.set(__self__, "message_filters", message_filters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="hubId")
    def hub_id(self) -> pulumi.Input[str]:
        """
        The ID of the hub on which this device will be created.
        """
        return pulumi.get(self, "hub_id")

    @hub_id.setter
    def hub_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_id", value)

    @property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        """
        return pulumi.get(self, "allow_insecure")

    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_insecure", value)

    @property
    @pulumi.getter(name="allowMultipleConnections")
    def allow_multiple_connections(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow more than one simultaneous connection using the same device credentials.
        """
        return pulumi.get(self, "allow_multiple_connections")

    @allow_multiple_connections.setter
    def allow_multiple_connections(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_multiple_connections", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input['IotDeviceCertificateArgs']]:
        """
        The certificate bundle of the device.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input['IotDeviceCertificateArgs']]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the IoT device (e.g. `living room`).
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="messageFilters")
    def message_filters(self) -> Optional[pulumi.Input['IotDeviceMessageFiltersArgs']]:
        """
        Rules that define which messages are authorized or denied based on their topic.
        """
        return pulumi.get(self, "message_filters")

    @message_filters.setter
    def message_filters(self, value: Optional[pulumi.Input['IotDeviceMessageFiltersArgs']]):
        pulumi.set(self, "message_filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IoT device you want to create (e.g. `my-device`).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region you want to attach the resource to
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _IotDeviceState:
    def __init__(__self__, *,
                 allow_insecure: Optional[pulumi.Input[bool]] = None,
                 allow_multiple_connections: Optional[pulumi.Input[bool]] = None,
                 certificate: Optional[pulumi.Input['IotDeviceCertificateArgs']] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hub_id: Optional[pulumi.Input[str]] = None,
                 is_connected: Optional[pulumi.Input[bool]] = None,
                 last_activity_at: Optional[pulumi.Input[str]] = None,
                 message_filters: Optional[pulumi.Input['IotDeviceMessageFiltersArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IotDevice resources.
        :param pulumi.Input[bool] allow_insecure: Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        :param pulumi.Input[bool] allow_multiple_connections: Allow more than one simultaneous connection using the same device credentials.
        :param pulumi.Input['IotDeviceCertificateArgs'] certificate: The certificate bundle of the device.
        :param pulumi.Input[str] created_at: The date and time the device was created.
        :param pulumi.Input[str] description: The description of the IoT device (e.g. `living room`).
        :param pulumi.Input[str] hub_id: The ID of the hub on which this device will be created.
        :param pulumi.Input[bool] is_connected: The current connection status of the device.
        :param pulumi.Input[str] last_activity_at: The last MQTT activity of the device.
        :param pulumi.Input['IotDeviceMessageFiltersArgs'] message_filters: Rules that define which messages are authorized or denied based on their topic.
        :param pulumi.Input[str] name: The name of the IoT device you want to create (e.g. `my-device`).
        :param pulumi.Input[str] region: The region you want to attach the resource to
        :param pulumi.Input[str] status: The current status of the device.
        :param pulumi.Input[str] updated_at: The date and time the device resource was updated.
        """
        if allow_insecure is not None:
            pulumi.set(__self__, "allow_insecure", allow_insecure)
        if allow_multiple_connections is not None:
            pulumi.set(__self__, "allow_multiple_connections", allow_multiple_connections)
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if hub_id is not None:
            pulumi.set(__self__, "hub_id", hub_id)
        if is_connected is not None:
            pulumi.set(__self__, "is_connected", is_connected)
        if last_activity_at is not None:
            pulumi.set(__self__, "last_activity_at", last_activity_at)
        if message_filters is not None:
            pulumi.set(__self__, "message_filters", message_filters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        """
        return pulumi.get(self, "allow_insecure")

    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_insecure", value)

    @property
    @pulumi.getter(name="allowMultipleConnections")
    def allow_multiple_connections(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow more than one simultaneous connection using the same device credentials.
        """
        return pulumi.get(self, "allow_multiple_connections")

    @allow_multiple_connections.setter
    def allow_multiple_connections(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_multiple_connections", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input['IotDeviceCertificateArgs']]:
        """
        The certificate bundle of the device.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input['IotDeviceCertificateArgs']]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the device was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the IoT device (e.g. `living room`).
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="hubId")
    def hub_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the hub on which this device will be created.
        """
        return pulumi.get(self, "hub_id")

    @hub_id.setter
    def hub_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hub_id", value)

    @property
    @pulumi.getter(name="isConnected")
    def is_connected(self) -> Optional[pulumi.Input[bool]]:
        """
        The current connection status of the device.
        """
        return pulumi.get(self, "is_connected")

    @is_connected.setter
    def is_connected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_connected", value)

    @property
    @pulumi.getter(name="lastActivityAt")
    def last_activity_at(self) -> Optional[pulumi.Input[str]]:
        """
        The last MQTT activity of the device.
        """
        return pulumi.get(self, "last_activity_at")

    @last_activity_at.setter
    def last_activity_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_activity_at", value)

    @property
    @pulumi.getter(name="messageFilters")
    def message_filters(self) -> Optional[pulumi.Input['IotDeviceMessageFiltersArgs']]:
        """
        Rules that define which messages are authorized or denied based on their topic.
        """
        return pulumi.get(self, "message_filters")

    @message_filters.setter
    def message_filters(self, value: Optional[pulumi.Input['IotDeviceMessageFiltersArgs']]):
        pulumi.set(self, "message_filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IoT device you want to create (e.g. `my-device`).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region you want to attach the resource to
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The current status of the device.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the device resource was updated.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class IotDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_insecure: Optional[pulumi.Input[bool]] = None,
                 allow_multiple_connections: Optional[pulumi.Input[bool]] = None,
                 certificate: Optional[pulumi.Input[pulumi.InputType['IotDeviceCertificateArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hub_id: Optional[pulumi.Input[str]] = None,
                 message_filters: Optional[pulumi.Input[pulumi.InputType['IotDeviceMessageFiltersArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        IoT devices can be imported using the `{region}/{id}`, e.g. bash

        ```sh
         $ pulumi import scaleway:index/iotDevice:IotDevice device01 fr-par/11111111-1111-1111-1111-111111111111
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_insecure: Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        :param pulumi.Input[bool] allow_multiple_connections: Allow more than one simultaneous connection using the same device credentials.
        :param pulumi.Input[pulumi.InputType['IotDeviceCertificateArgs']] certificate: The certificate bundle of the device.
        :param pulumi.Input[str] description: The description of the IoT device (e.g. `living room`).
        :param pulumi.Input[str] hub_id: The ID of the hub on which this device will be created.
        :param pulumi.Input[pulumi.InputType['IotDeviceMessageFiltersArgs']] message_filters: Rules that define which messages are authorized or denied based on their topic.
        :param pulumi.Input[str] name: The name of the IoT device you want to create (e.g. `my-device`).
        :param pulumi.Input[str] region: The region you want to attach the resource to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        IoT devices can be imported using the `{region}/{id}`, e.g. bash

        ```sh
         $ pulumi import scaleway:index/iotDevice:IotDevice device01 fr-par/11111111-1111-1111-1111-111111111111
        ```

        :param str resource_name: The name of the resource.
        :param IotDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_insecure: Optional[pulumi.Input[bool]] = None,
                 allow_multiple_connections: Optional[pulumi.Input[bool]] = None,
                 certificate: Optional[pulumi.Input[pulumi.InputType['IotDeviceCertificateArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hub_id: Optional[pulumi.Input[str]] = None,
                 message_filters: Optional[pulumi.Input[pulumi.InputType['IotDeviceMessageFiltersArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IotDeviceArgs.__new__(IotDeviceArgs)

            __props__.__dict__["allow_insecure"] = allow_insecure
            __props__.__dict__["allow_multiple_connections"] = allow_multiple_connections
            __props__.__dict__["certificate"] = certificate
            __props__.__dict__["description"] = description
            if hub_id is None and not opts.urn:
                raise TypeError("Missing required property 'hub_id'")
            __props__.__dict__["hub_id"] = hub_id
            __props__.__dict__["message_filters"] = message_filters
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
            __props__.__dict__["created_at"] = None
            __props__.__dict__["is_connected"] = None
            __props__.__dict__["last_activity_at"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        super(IotDevice, __self__).__init__(
            'scaleway:index/iotDevice:IotDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_insecure: Optional[pulumi.Input[bool]] = None,
            allow_multiple_connections: Optional[pulumi.Input[bool]] = None,
            certificate: Optional[pulumi.Input[pulumi.InputType['IotDeviceCertificateArgs']]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            hub_id: Optional[pulumi.Input[str]] = None,
            is_connected: Optional[pulumi.Input[bool]] = None,
            last_activity_at: Optional[pulumi.Input[str]] = None,
            message_filters: Optional[pulumi.Input[pulumi.InputType['IotDeviceMessageFiltersArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'IotDevice':
        """
        Get an existing IotDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_insecure: Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        :param pulumi.Input[bool] allow_multiple_connections: Allow more than one simultaneous connection using the same device credentials.
        :param pulumi.Input[pulumi.InputType['IotDeviceCertificateArgs']] certificate: The certificate bundle of the device.
        :param pulumi.Input[str] created_at: The date and time the device was created.
        :param pulumi.Input[str] description: The description of the IoT device (e.g. `living room`).
        :param pulumi.Input[str] hub_id: The ID of the hub on which this device will be created.
        :param pulumi.Input[bool] is_connected: The current connection status of the device.
        :param pulumi.Input[str] last_activity_at: The last MQTT activity of the device.
        :param pulumi.Input[pulumi.InputType['IotDeviceMessageFiltersArgs']] message_filters: Rules that define which messages are authorized or denied based on their topic.
        :param pulumi.Input[str] name: The name of the IoT device you want to create (e.g. `my-device`).
        :param pulumi.Input[str] region: The region you want to attach the resource to
        :param pulumi.Input[str] status: The current status of the device.
        :param pulumi.Input[str] updated_at: The date and time the device resource was updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IotDeviceState.__new__(_IotDeviceState)

        __props__.__dict__["allow_insecure"] = allow_insecure
        __props__.__dict__["allow_multiple_connections"] = allow_multiple_connections
        __props__.__dict__["certificate"] = certificate
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["hub_id"] = hub_id
        __props__.__dict__["is_connected"] = is_connected
        __props__.__dict__["last_activity_at"] = last_activity_at
        __props__.__dict__["message_filters"] = message_filters
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        __props__.__dict__["status"] = status
        __props__.__dict__["updated_at"] = updated_at
        return IotDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow plain and server-authenticated TLS connections in addition to mutually-authenticated ones.
        """
        return pulumi.get(self, "allow_insecure")

    @property
    @pulumi.getter(name="allowMultipleConnections")
    def allow_multiple_connections(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow more than one simultaneous connection using the same device credentials.
        """
        return pulumi.get(self, "allow_multiple_connections")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output['outputs.IotDeviceCertificate']:
        """
        The certificate bundle of the device.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date and time the device was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the IoT device (e.g. `living room`).
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hubId")
    def hub_id(self) -> pulumi.Output[str]:
        """
        The ID of the hub on which this device will be created.
        """
        return pulumi.get(self, "hub_id")

    @property
    @pulumi.getter(name="isConnected")
    def is_connected(self) -> pulumi.Output[bool]:
        """
        The current connection status of the device.
        """
        return pulumi.get(self, "is_connected")

    @property
    @pulumi.getter(name="lastActivityAt")
    def last_activity_at(self) -> pulumi.Output[str]:
        """
        The last MQTT activity of the device.
        """
        return pulumi.get(self, "last_activity_at")

    @property
    @pulumi.getter(name="messageFilters")
    def message_filters(self) -> pulumi.Output[Optional['outputs.IotDeviceMessageFilters']]:
        """
        Rules that define which messages are authorized or denied based on their topic.
        """
        return pulumi.get(self, "message_filters")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the IoT device you want to create (e.g. `my-device`).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region you want to attach the resource to
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The current status of the device.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The date and time the device resource was updated.
        """
        return pulumi.get(self, "updated_at")

