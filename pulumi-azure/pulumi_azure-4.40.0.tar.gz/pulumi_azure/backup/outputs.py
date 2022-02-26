# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'PolicyFileShareBackup',
    'PolicyFileShareRetentionDaily',
    'PolicyFileShareRetentionMonthly',
    'PolicyFileShareRetentionWeekly',
    'PolicyFileShareRetentionYearly',
    'PolicyVMBackup',
    'PolicyVMRetentionDaily',
    'PolicyVMRetentionMonthly',
    'PolicyVMRetentionWeekly',
    'PolicyVMRetentionYearly',
]

@pulumi.output_type
class PolicyFileShareBackup(dict):
    def __init__(__self__, *,
                 frequency: str,
                 time: str):
        """
        :param str frequency: Sets the backup frequency. Currently, only `Daily` is supported
        :param str time: The time of day to perform the backup in 24-hour format. Times must be either on the hour or half hour (e.g. 12:00, 12:30, 13:00, etc.)
        """
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def frequency(self) -> str:
        """
        Sets the backup frequency. Currently, only `Daily` is supported
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        The time of day to perform the backup in 24-hour format. Times must be either on the hour or half hour (e.g. 12:00, 12:30, 13:00, etc.)
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class PolicyFileShareRetentionDaily(dict):
    def __init__(__self__, *,
                 count: int):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `10`
        """
        pulumi.set(__self__, "count", count)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `10`
        """
        return pulumi.get(self, "count")


@pulumi.output_type
class PolicyFileShareRetentionMonthly(dict):
    def __init__(__self__, *,
                 count: int,
                 weekdays: Sequence[str],
                 weeks: Sequence[str]):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `10`
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        :param Sequence[str] weeks: The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "weekdays", weekdays)
        pulumi.set(__self__, "weeks", weeks)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `10`
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def weekdays(self) -> Sequence[str]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")

    @property
    @pulumi.getter
    def weeks(self) -> Sequence[str]:
        """
        The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        return pulumi.get(self, "weeks")


@pulumi.output_type
class PolicyFileShareRetentionWeekly(dict):
    def __init__(__self__, *,
                 count: int,
                 weekdays: Sequence[str]):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `10`
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "weekdays", weekdays)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `10`
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def weekdays(self) -> Sequence[str]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")


@pulumi.output_type
class PolicyFileShareRetentionYearly(dict):
    def __init__(__self__, *,
                 count: int,
                 months: Sequence[str],
                 weekdays: Sequence[str],
                 weeks: Sequence[str]):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `10`
        :param Sequence[str] months: The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        :param Sequence[str] weeks: The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "months", months)
        pulumi.set(__self__, "weekdays", weekdays)
        pulumi.set(__self__, "weeks", weeks)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `10`
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def months(self) -> Sequence[str]:
        """
        The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.
        """
        return pulumi.get(self, "months")

    @property
    @pulumi.getter
    def weekdays(self) -> Sequence[str]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")

    @property
    @pulumi.getter
    def weeks(self) -> Sequence[str]:
        """
        The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        return pulumi.get(self, "weeks")


@pulumi.output_type
class PolicyVMBackup(dict):
    def __init__(__self__, *,
                 frequency: str,
                 time: str,
                 weekdays: Optional[Sequence[str]] = None):
        """
        :param str frequency: Sets the backup frequency. Must be either `Daily` or`Weekly`.
        :param str time: The time of day to perform the backup in 24hour format.
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "time", time)
        if weekdays is not None:
            pulumi.set(__self__, "weekdays", weekdays)

    @property
    @pulumi.getter
    def frequency(self) -> str:
        """
        Sets the backup frequency. Must be either `Daily` or`Weekly`.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        The time of day to perform the backup in 24hour format.
        """
        return pulumi.get(self, "time")

    @property
    @pulumi.getter
    def weekdays(self) -> Optional[Sequence[str]]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")


@pulumi.output_type
class PolicyVMRetentionDaily(dict):
    def __init__(__self__, *,
                 count: int):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `9999`
        """
        pulumi.set(__self__, "count", count)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `9999`
        """
        return pulumi.get(self, "count")


@pulumi.output_type
class PolicyVMRetentionMonthly(dict):
    def __init__(__self__, *,
                 count: int,
                 weekdays: Sequence[str],
                 weeks: Sequence[str]):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `9999`
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        :param Sequence[str] weeks: The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "weekdays", weekdays)
        pulumi.set(__self__, "weeks", weeks)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `9999`
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def weekdays(self) -> Sequence[str]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")

    @property
    @pulumi.getter
    def weeks(self) -> Sequence[str]:
        """
        The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        return pulumi.get(self, "weeks")


@pulumi.output_type
class PolicyVMRetentionWeekly(dict):
    def __init__(__self__, *,
                 count: int,
                 weekdays: Sequence[str]):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `9999`
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "weekdays", weekdays)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `9999`
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def weekdays(self) -> Sequence[str]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")


@pulumi.output_type
class PolicyVMRetentionYearly(dict):
    def __init__(__self__, *,
                 count: int,
                 months: Sequence[str],
                 weekdays: Sequence[str],
                 weeks: Sequence[str]):
        """
        :param int count: The number of yearly backups to keep. Must be between `1` and `9999`
        :param Sequence[str] months: The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November` and `December`.
        :param Sequence[str] weekdays: The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        :param Sequence[str] weeks: The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "months", months)
        pulumi.set(__self__, "weekdays", weekdays)
        pulumi.set(__self__, "weeks", weeks)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        The number of yearly backups to keep. Must be between `1` and `9999`
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def months(self) -> Sequence[str]:
        """
        The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November` and `December`.
        """
        return pulumi.get(self, "months")

    @property
    @pulumi.getter
    def weekdays(self) -> Sequence[str]:
        """
        The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
        """
        return pulumi.get(self, "weekdays")

    @property
    @pulumi.getter
    def weeks(self) -> Sequence[str]:
        """
        The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
        """
        return pulumi.get(self, "weeks")


