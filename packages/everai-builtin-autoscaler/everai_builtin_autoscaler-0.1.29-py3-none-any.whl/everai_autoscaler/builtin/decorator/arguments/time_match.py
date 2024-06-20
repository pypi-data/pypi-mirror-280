from __future__ import annotations

import logging
import re
import typing
import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from crontab import CronTab


class TimeMatchDecorator:
    tz: datetime.tzinfo
    match_keys: typing.List[typing.Tuple[str, str]]

    def __init__(self, timezone: typing.Optional[str] = None, **kwargs) -> None:
        """
        assume basic arguments is:
        min_workers: 1
        max_workers: 3
        max_queue_size: 2
        max_idle_time: 120
        scale_up_step: 2

        # match condition and decide prefix, prefixed arguments(only set what is needed) will overwrite basic arguments
        timezone: null  # default is utc
        match(* 9-22 * * 1-5): weekday_day_
        match(* 23,0-8 * * 1-5): weekday_night_
        match(* 9-23,0 * * 6,7): weekend_day_
        match(* 1-8 * * 6,7): weekend_night_
        weekday_day_min_workers: 5
        weekday_day_max_workers: 50

        weekday_night_min_worker: 2
        weekday_night_max_worker: 5

        weekend_day_min_worker: 10
        weekend_day_max_worker: 80
        weekend_day_max_idle_time: 300
        weekend_day_scale_up_step: 5

        weekend_night_min_worker: 2
        weekend_night_max_worker: 5
        """
        try:
            self.tz = datetime.timezone.utc if timezone is None else ZoneInfo(timezone)
        except ZoneInfoNotFoundError:
            logging.warning(f'invalid time zone `{timezone}`, use utc')
            self.tz = datetime.timezone.utc

        self.match_keys = []

        for k in kwargs.keys():
            result = re.match("^match[(]([0-9,*/-]+(?: [0-9,*/-]+){4})[)]$", k)
            if result is None:
                continue

            keys = list(result.groups())
            if len(keys) == 1:
                self.match_keys.append((keys[0], kwargs[k]))

    def __call__(self, arguments: typing.Dict[str, str]) -> typing.Dict[str, str]:
        now = datetime.datetime.utcnow().replace(tzinfo=self.tz)
        timestamp = int(now.timestamp())
        for match_key in self.match_keys:
            matcher = CronTab(f'* {match_key[0]} *')
            if matcher.test(timestamp):
                print('match')
            else:
                print('unmatch')

        return arguments

    @classmethod
    def name(cls) -> str:
        return 'time-match'

    @classmethod
    def from_arguments(cls, arguments: typing.Dict[str, str]) -> TimeMatchDecorator:
        return TimeMatchDecorator(**arguments)
