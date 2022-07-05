# ===== Module & Library
from datetime import datetime
from config.config import Settings
from model.enum.enum_exception import BadRequestExceptionMessage

import pytz

from util.util_http_exception import BadRequestException
from loguru import logger

# ===== Header
INDONESIA_TIMEZONE = pytz.timezone(Settings().TIMEZONE)
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
# ===== Function
def DateNow():
    """Function to get current date """

    dt = datetime.strptime(
        datetime.now(tz=INDONESIA_TIMEZONE).strftime(DATETIME_FORMAT), DATETIME_FORMAT
    )
    return dt.date()


def DateNowStr():
    """Function to get current string date """

    dt = datetime.now(tz=INDONESIA_TIMEZONE).strftime(DATE_FORMAT)
    return dt


def StrDateToDate(strDate: str):
    """Function to convert current string date to datetime date"""

    try:
        dt = datetime.strptime(strDate, DATE_FORMAT)
        return dt.date()
    except Exception as err:
        logger.warning(err)
        raise BadRequestException(BadRequestExceptionMessage.INVALID_DATE_FORMAT)


def TimeNow():
    """Function to get current time """

    dt = datetime.strptime(
        datetime.now(tz=INDONESIA_TIMEZONE).strftime(DATETIME_FORMAT), DATETIME_FORMAT
    )
    return dt.time()


def TimeNowStr():
    """Function to get current string time """

    dt = datetime.now(tz=INDONESIA_TIMEZONE).strftime(TIME_FORMAT)
    return dt


def strTimeToTime(strTime: str):
    """Function to convert current string time to datetime time"""

    try:
        time = datetime.strptime(strTime, TIME_FORMAT)
        return time.time()
    except Exception as err:
        logger.warning(err)
        raise BadRequestException(BadRequestExceptionMessage.INVALID_DATE_FORMAT)


def DateTimeNow():
    """Function to get current datetime """

    dt = datetime.strptime(
        datetime.now(tz=INDONESIA_TIMEZONE).strftime(DATETIME_FORMAT), DATETIME_FORMAT
    )
    return dt


def DatetimeNowStr():
    """Function to get current string time """

    dt = datetime.now(tz=INDONESIA_TIMEZONE).strftime(DATETIME_FORMAT)
    return dt


def StrDateTimeToDateTime(strDateTime: str):
    """Function to convert current string datetime to datetime"""

    try:
        dt = datetime.strptime(strDateTime, DATETIME_FORMAT)
        return dt
    except Exception as err:
        logger.warning(err)
        raise BadRequestException(BadRequestExceptionMessage.INVALID_DATE_FORMAT)


# ===== Class

# ===== Main
