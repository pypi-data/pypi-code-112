# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EndpointEventhubArgs', 'EndpointEventhub']

@pulumi.input_type
class EndpointEventhubArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 endpoint_uri: Optional[pulumi.Input[str]] = None,
                 entity_path: Optional[pulumi.Input[str]] = None,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 iothub_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EndpointEventhub resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] authentication_type: Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        :param pulumi.Input[str] connection_string: The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        :param pulumi.Input[str] endpoint_uri: URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] entity_path: Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] identity_id: ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        :param pulumi.Input[str] iothub_id: The IoTHub ID for the endpoint.
        :param pulumi.Input[str] iothub_name: The IoTHub name for the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authentication_type is not None:
            pulumi.set(__self__, "authentication_type", authentication_type)
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)
        if endpoint_uri is not None:
            pulumi.set(__self__, "endpoint_uri", endpoint_uri)
        if entity_path is not None:
            pulumi.set(__self__, "entity_path", entity_path)
        if identity_id is not None:
            pulumi.set(__self__, "identity_id", identity_id)
        if iothub_id is not None:
            pulumi.set(__self__, "iothub_id", iothub_id)
        if iothub_name is not None:
            warnings.warn("""Deprecated in favour of `iothub_id`""", DeprecationWarning)
            pulumi.log.warn("""iothub_name is deprecated: Deprecated in favour of `iothub_id`""")
        if iothub_name is not None:
            pulumi.set(__self__, "iothub_name", iothub_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[str]]:
        """
        URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        """
        return pulumi.get(self, "endpoint_uri")

    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_uri", value)

    @property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        """
        return pulumi.get(self, "entity_path")

    @entity_path.setter
    def entity_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_path", value)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        """
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter(name="iothubId")
    def iothub_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IoTHub ID for the endpoint.
        """
        return pulumi.get(self, "iothub_id")

    @iothub_id.setter
    def iothub_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iothub_id", value)

    @property
    @pulumi.getter(name="iothubName")
    def iothub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The IoTHub name for the endpoint.
        """
        return pulumi.get(self, "iothub_name")

    @iothub_name.setter
    def iothub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iothub_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _EndpointEventhubState:
    def __init__(__self__, *,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 endpoint_uri: Optional[pulumi.Input[str]] = None,
                 entity_path: Optional[pulumi.Input[str]] = None,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 iothub_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EndpointEventhub resources.
        :param pulumi.Input[str] authentication_type: Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        :param pulumi.Input[str] connection_string: The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        :param pulumi.Input[str] endpoint_uri: URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] entity_path: Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] identity_id: ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        :param pulumi.Input[str] iothub_id: The IoTHub ID for the endpoint.
        :param pulumi.Input[str] iothub_name: The IoTHub name for the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        """
        if authentication_type is not None:
            pulumi.set(__self__, "authentication_type", authentication_type)
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)
        if endpoint_uri is not None:
            pulumi.set(__self__, "endpoint_uri", endpoint_uri)
        if entity_path is not None:
            pulumi.set(__self__, "entity_path", entity_path)
        if identity_id is not None:
            pulumi.set(__self__, "identity_id", identity_id)
        if iothub_id is not None:
            pulumi.set(__self__, "iothub_id", iothub_id)
        if iothub_name is not None:
            warnings.warn("""Deprecated in favour of `iothub_id`""", DeprecationWarning)
            pulumi.log.warn("""iothub_name is deprecated: Deprecated in favour of `iothub_id`""")
        if iothub_name is not None:
            pulumi.set(__self__, "iothub_name", iothub_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[str]]:
        """
        URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        """
        return pulumi.get(self, "endpoint_uri")

    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_uri", value)

    @property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        """
        return pulumi.get(self, "entity_path")

    @entity_path.setter
    def entity_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_path", value)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        """
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter(name="iothubId")
    def iothub_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IoTHub ID for the endpoint.
        """
        return pulumi.get(self, "iothub_id")

    @iothub_id.setter
    def iothub_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iothub_id", value)

    @property
    @pulumi.getter(name="iothubName")
    def iothub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The IoTHub name for the endpoint.
        """
        return pulumi.get(self, "iothub_name")

    @iothub_name.setter
    def iothub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iothub_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class EndpointEventhub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 endpoint_uri: Optional[pulumi.Input[str]] = None,
                 entity_path: Optional[pulumi.Input[str]] = None,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 iothub_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an IotHub EventHub Endpoint

        > **NOTE:** Endpoints can be defined either directly on the `iot.IoTHub` resource, or using the `azurerm_iothub_endpoint_*` resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a `azurerm_iothub_endpoint_*` resource and another endpoint of a different type directly on the `iot.IoTHub` resource is not supported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Basic")
        example_event_hub = azure.eventhub.EventHub("exampleEventHub",
            namespace_name=example_event_hub_namespace.name,
            resource_group_name=example_resource_group.name,
            partition_count=2,
            message_retention=1)
        example_authorization_rule = azure.eventhub.AuthorizationRule("exampleAuthorizationRule",
            namespace_name=example_event_hub_namespace.name,
            eventhub_name=example_event_hub.name,
            resource_group_name=example_resource_group.name,
            listen=False,
            send=True,
            manage=False)
        example_io_t_hub = azure.iot.IoTHub("exampleIoTHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku=azure.iot.IoTHubSkuArgs(
                name="B1",
                capacity=1,
            ),
            tags={
                "purpose": "example",
            })
        example_endpoint_eventhub = azure.iot.EndpointEventhub("exampleEndpointEventhub",
            resource_group_name=example_resource_group.name,
            iothub_name=example_io_t_hub.name,
            connection_string=example_authorization_rule.primary_connection_string)
        ```

        ## Import

        IoTHub EventHub Endpoint can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/endpointEventhub:EndpointEventhub eventhub1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Devices/IotHubs/hub1/Endpoints/eventhub_endpoint1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_type: Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        :param pulumi.Input[str] connection_string: The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        :param pulumi.Input[str] endpoint_uri: URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] entity_path: Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] identity_id: ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        :param pulumi.Input[str] iothub_id: The IoTHub ID for the endpoint.
        :param pulumi.Input[str] iothub_name: The IoTHub name for the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointEventhubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an IotHub EventHub Endpoint

        > **NOTE:** Endpoints can be defined either directly on the `iot.IoTHub` resource, or using the `azurerm_iothub_endpoint_*` resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a `azurerm_iothub_endpoint_*` resource and another endpoint of a different type directly on the `iot.IoTHub` resource is not supported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Basic")
        example_event_hub = azure.eventhub.EventHub("exampleEventHub",
            namespace_name=example_event_hub_namespace.name,
            resource_group_name=example_resource_group.name,
            partition_count=2,
            message_retention=1)
        example_authorization_rule = azure.eventhub.AuthorizationRule("exampleAuthorizationRule",
            namespace_name=example_event_hub_namespace.name,
            eventhub_name=example_event_hub.name,
            resource_group_name=example_resource_group.name,
            listen=False,
            send=True,
            manage=False)
        example_io_t_hub = azure.iot.IoTHub("exampleIoTHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku=azure.iot.IoTHubSkuArgs(
                name="B1",
                capacity=1,
            ),
            tags={
                "purpose": "example",
            })
        example_endpoint_eventhub = azure.iot.EndpointEventhub("exampleEndpointEventhub",
            resource_group_name=example_resource_group.name,
            iothub_name=example_io_t_hub.name,
            connection_string=example_authorization_rule.primary_connection_string)
        ```

        ## Import

        IoTHub EventHub Endpoint can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/endpointEventhub:EndpointEventhub eventhub1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Devices/IotHubs/hub1/Endpoints/eventhub_endpoint1
        ```

        :param str resource_name: The name of the resource.
        :param EndpointEventhubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointEventhubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 endpoint_uri: Optional[pulumi.Input[str]] = None,
                 entity_path: Optional[pulumi.Input[str]] = None,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 iothub_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = EndpointEventhubArgs.__new__(EndpointEventhubArgs)

            __props__.__dict__["authentication_type"] = authentication_type
            __props__.__dict__["connection_string"] = connection_string
            __props__.__dict__["endpoint_uri"] = endpoint_uri
            __props__.__dict__["entity_path"] = entity_path
            __props__.__dict__["identity_id"] = identity_id
            __props__.__dict__["iothub_id"] = iothub_id
            if iothub_name is not None and not opts.urn:
                warnings.warn("""Deprecated in favour of `iothub_id`""", DeprecationWarning)
                pulumi.log.warn("""iothub_name is deprecated: Deprecated in favour of `iothub_id`""")
            __props__.__dict__["iothub_name"] = iothub_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(EndpointEventhub, __self__).__init__(
            'azure:iot/endpointEventhub:EndpointEventhub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication_type: Optional[pulumi.Input[str]] = None,
            connection_string: Optional[pulumi.Input[str]] = None,
            endpoint_uri: Optional[pulumi.Input[str]] = None,
            entity_path: Optional[pulumi.Input[str]] = None,
            identity_id: Optional[pulumi.Input[str]] = None,
            iothub_id: Optional[pulumi.Input[str]] = None,
            iothub_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'EndpointEventhub':
        """
        Get an existing EndpointEventhub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_type: Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        :param pulumi.Input[str] connection_string: The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        :param pulumi.Input[str] endpoint_uri: URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] entity_path: Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        :param pulumi.Input[str] identity_id: ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        :param pulumi.Input[str] iothub_id: The IoTHub ID for the endpoint.
        :param pulumi.Input[str] iothub_name: The IoTHub name for the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EndpointEventhubState.__new__(_EndpointEventhubState)

        __props__.__dict__["authentication_type"] = authentication_type
        __props__.__dict__["connection_string"] = connection_string
        __props__.__dict__["endpoint_uri"] = endpoint_uri
        __props__.__dict__["entity_path"] = entity_path
        __props__.__dict__["identity_id"] = identity_id
        __props__.__dict__["iothub_id"] = iothub_id
        __props__.__dict__["iothub_name"] = iothub_name
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return EndpointEventhub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type used to authenticate against the Event Hub endpoint. Possible values are `keyBased` and `identityBased`. Defaults to `keyBased`.
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[Optional[str]]:
        """
        The connection string for the endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `keyBased`.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> pulumi.Output[Optional[str]]:
        """
        URI of the Event Hubs Namespace endpoint. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        """
        return pulumi.get(self, "endpoint_uri")

    @property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the Event Hub. This attribute can only be specified and is mandatory when `authentication_type` is `identityBased`.
        """
        return pulumi.get(self, "entity_path")

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the User Managed Identity used to authenticate against the Event Hub endpoint.
        """
        return pulumi.get(self, "identity_id")

    @property
    @pulumi.getter(name="iothubId")
    def iothub_id(self) -> pulumi.Output[str]:
        """
        The IoTHub ID for the endpoint.
        """
        return pulumi.get(self, "iothub_id")

    @property
    @pulumi.getter(name="iothubName")
    def iothub_name(self) -> pulumi.Output[str]:
        """
        The IoTHub name for the endpoint.
        """
        return pulumi.get(self, "iothub_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group under which the Event Hub has been created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

