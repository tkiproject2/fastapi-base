# ===== Module & Library
import re

import phonenumbers
from bson.objectid import ObjectId
from loguru import logger

from model.enum.enum_exception import BadRequestExceptionMessage
from util.util_http_exception import BadRequestException

# ===== Header
regexEmail = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)

# ===== Function

# ===== Class

# ===== Main
# def ValidatePhoneNumber(strPhoneNumber: str, min: int = 7, max: int = 14):
#     """Function to validate phone number"""

#     if not strPhoneNumber.isnumeric():
#         raise BadRequestException("Nomor telepon bukan berupa angka.")

#     if not min < len(strPhoneNumber) < max:
#         raise BadRequestException(f"Panjang nomor telepon antara {min} - {max} angka.")

#     return True


def ValidatePhoneNumber(phone_number: str):
    """Function to validate phone number"""
    phoneFormat = (
        format(int(phone_number[:-1]), ",").replace(",", "-") + phone_number[-1]
    )

    validPhone = False
    try:
        my_number = phonenumbers.parse(phoneFormat, "ID")
    except:
        raise BadRequestException(BadRequestExceptionMessage.INVALID_PHONE_NUMBER)

    try:
        validPhone = phonenumbers.is_valid_number(my_number)
    except:
        raise BadRequestException(BadRequestExceptionMessage.INVALID_PHONE_NUMBER)

    if not validPhone:
        return False

    if 7 < len(phone_number) < 14:
        return phone_number.isnumeric()
    else:
        return False


def ValidateEmail(strEmail: str):
    """Function to validate email"""

    if not re.fullmatch(regexEmail, strEmail):
        raise BadRequestException(BadRequestExceptionMessage.INVALID_EMAIL)

    return True


def ValidatePassword(pwd: str, min: int = 6, max: int = 24):
    """Function to validate password"""

    if not min <= len(pwd) <= max:
        # raise BadRequestException(f"Panjang password antara {min} - {max} karakter.")
        raise BadRequestException(BadRequestExceptionMessage.INVALID_PASSWORD_LENGTH)

    return True


def ValidateObjectId(strObjectId: str, varName: str):
    """Function to validate ObjectId"""

    if not ObjectId.is_valid(strObjectId):
        # raise BadRequestException(f"ObjectId '{varName}' tidak valid.")
        raise BadRequestException(BadRequestExceptionMessage.INVALID_OBJECT_ID)

    try:
        oid = ObjectId(strObjectId)
        return oid
    except Exception as err:
        logger.warning(err)
        raise BadRequestException(BadRequestExceptionMessage.INVALID_OBJECT_ID)
