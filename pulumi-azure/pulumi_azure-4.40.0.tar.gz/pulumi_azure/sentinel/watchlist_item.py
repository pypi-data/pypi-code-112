# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WatchlistItemArgs', 'WatchlistItem']

@pulumi.input_type
class WatchlistItemArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 watchlist_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WatchlistItem resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The key value pairs of the Sentinel Watchlist Item.
        :param pulumi.Input[str] watchlist_id: The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        :param pulumi.Input[str] name: The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "watchlist_id", watchlist_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        The key value pairs of the Sentinel Watchlist Item.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> pulumi.Input[str]:
        """
        The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        return pulumi.get(self, "watchlist_id")

    @watchlist_id.setter
    def watchlist_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "watchlist_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _WatchlistItemState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 watchlist_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WatchlistItem resources.
        :param pulumi.Input[str] name: The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The key value pairs of the Sentinel Watchlist Item.
        :param pulumi.Input[str] watchlist_id: The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if watchlist_id is not None:
            pulumi.set(__self__, "watchlist_id", watchlist_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The key value pairs of the Sentinel Watchlist Item.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        return pulumi.get(self, "watchlist_id")

    @watchlist_id.setter
    def watchlist_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "watchlist_id", value)


class WatchlistItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 watchlist_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Sentinel Watchlist Item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_analytics_solution = azure.operationalinsights.AnalyticsSolution("exampleAnalyticsSolution",
            solution_name="SecurityInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            workspace_resource_id=example_analytics_workspace.id,
            workspace_name=example_analytics_workspace.name,
            plan=azure.operationalinsights.AnalyticsSolutionPlanArgs(
                publisher="Microsoft",
                product="OMSGallery/SecurityInsights",
            ))
        example_watchlist = azure.sentinel.Watchlist("exampleWatchlist",
            log_analytics_workspace_id=example_analytics_solution.workspace_resource_id,
            display_name="example-wl")
        example_watchlist_item = azure.sentinel.WatchlistItem("exampleWatchlistItem",
            watchlist_id=example_watchlist.id,
            properties={
                "k1": "v1",
                "k2": "v2",
            })
        ```

        ## Import

        Sentinel Watchlist Items can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/watchlistItem:WatchlistItem example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/watchlists/list1/watchlistItems/item1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The key value pairs of the Sentinel Watchlist Item.
        :param pulumi.Input[str] watchlist_id: The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WatchlistItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Sentinel Watchlist Item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_analytics_solution = azure.operationalinsights.AnalyticsSolution("exampleAnalyticsSolution",
            solution_name="SecurityInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            workspace_resource_id=example_analytics_workspace.id,
            workspace_name=example_analytics_workspace.name,
            plan=azure.operationalinsights.AnalyticsSolutionPlanArgs(
                publisher="Microsoft",
                product="OMSGallery/SecurityInsights",
            ))
        example_watchlist = azure.sentinel.Watchlist("exampleWatchlist",
            log_analytics_workspace_id=example_analytics_solution.workspace_resource_id,
            display_name="example-wl")
        example_watchlist_item = azure.sentinel.WatchlistItem("exampleWatchlistItem",
            watchlist_id=example_watchlist.id,
            properties={
                "k1": "v1",
                "k2": "v2",
            })
        ```

        ## Import

        Sentinel Watchlist Items can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/watchlistItem:WatchlistItem example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/watchlists/list1/watchlistItems/item1
        ```

        :param str resource_name: The name of the resource.
        :param WatchlistItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WatchlistItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 watchlist_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = WatchlistItemArgs.__new__(WatchlistItemArgs)

            __props__.__dict__["name"] = name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if watchlist_id is None and not opts.urn:
                raise TypeError("Missing required property 'watchlist_id'")
            __props__.__dict__["watchlist_id"] = watchlist_id
        super(WatchlistItem, __self__).__init__(
            'azure:sentinel/watchlistItem:WatchlistItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            watchlist_id: Optional[pulumi.Input[str]] = None) -> 'WatchlistItem':
        """
        Get an existing WatchlistItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The key value pairs of the Sentinel Watchlist Item.
        :param pulumi.Input[str] watchlist_id: The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WatchlistItemState.__new__(_WatchlistItemState)

        __props__.__dict__["name"] = name
        __props__.__dict__["properties"] = properties
        __props__.__dict__["watchlist_id"] = watchlist_id
        return WatchlistItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name in UUID format which should be used for this Sentinel Watchlist Item. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The key value pairs of the Sentinel Watchlist Item.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> pulumi.Output[str]:
        """
        The ID of the Sentinel Watchlist that this Item resides in. Changing this forces a new Sentinel Watchlist Item to be created.
        """
        return pulumi.get(self, "watchlist_id")

