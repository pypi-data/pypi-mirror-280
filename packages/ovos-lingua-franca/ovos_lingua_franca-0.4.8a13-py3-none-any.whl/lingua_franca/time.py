#
# Copyright 2018 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from datetime import datetime
from dateutil.tz import gettz, tzlocal


# used to calculate timespans
DAYS_IN_1_YEAR = 365.2425
DAYS_IN_1_MONTH = 30.42

__default_tz = None


def set_default_tz(tz):
    global __default_tz
    if isinstance(tz, str):
        tz = gettz(tz)
    __default_tz = tz


def default_timezone():
    """ Get the default timezone

    either a value set by downstream user with
    lingua_franca.internal.set_default_tz
    or default system value

    Returns:
        (datetime.tzinfo): Definition of the default timezone
    """
    return __default_tz or tzlocal()


def now_utc():
    """ Retrieve the current time in UTC

    Returns:
        (datetime): The current time in Universal Time, aka GMT
    """
    return datetime.utcnow().replace(tzinfo=gettz("UTC"))


def now_local(tz=None):
    """ Retrieve the current time

    Args:
        tz (datetime.tzinfo, optional): Timezone, default to user's settings

    Returns:
        (datetime): The current time
    """
    tz = tz or default_timezone()
    return datetime.now(tz)


def to_utc(dt):
    """ Convert a datetime with timezone info to a UTC datetime

    Args:
        dt (datetime): A datetime (presumably in some local zone)
    Returns:
        (datetime): time converted to UTC
    """
    tz = gettz("UTC")
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=default_timezone())
    return dt.astimezone(tz)


def to_local(dt):
    """ Convert a datetime to the user's local timezone

    Args:
        dt (datetime): A datetime (if no timezone, defaults to UTC)
    Returns:
        (datetime): time converted to the local timezone
    """
    tz = default_timezone()
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=default_timezone())
    return dt.astimezone(tz)


def to_system(dt):
    """Convert a datetime to the system's local timezone

    Args:
        dt (datetime): A datetime (if no timezone, assumed to be UTC)
    Returns:
        (datetime): time converted to the operation system's timezone
    """
    tz = tzlocal()
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=default_timezone())
    return dt.astimezone(tz)


def is_leap_year(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))


def get_next_leap_year(year):
    next_year = year + 1
    if is_leap_year(next_year):
        return next_year
    else:
        return get_next_leap_year(next_year)

