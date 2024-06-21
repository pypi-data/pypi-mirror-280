# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=unused-import
'''
    A module of utility methods used for getting current time/date data.

    These are really just convenience methods for accessing time and datetime that I always seem to forget.

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 10-14-2023 11:05:47
    `memberOf`: time_utils
'''
from math import floor
import re
from typing import Union
import datetime
import inflect
from datetime import timezone


# import colemen_utilities.string_utils as _csu
# import colemen_utilities.dict_utils as _obj


def unix_utc_int()->int:
    '''Get the current unix timestamp in the UTC timezone rounded to be an integer.'''
    return round(datetime.datetime.now(tz=timezone.utc).timestamp())


def timestamp_HMS(delimiter:str=":"):
    '''
        Get the current timestamp formatted as
        HH:MM:SS

        23:15:45

        ----------

        Arguments
        -------------------------
        `delimiter` {str}
            The string to use to separate the values in the timestamp.

        Return {str}
        ----------------------
        The current HH:MM:SS timestamp.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:19:48
        `memberOf`: current
        `version`: 1.0
        `method_name`: timestamp_HMS
        * @xxx [10-14-2023 11:21:17]: documentation for timestamp_HMS
    '''
    t = datetime.datetime.now()
    return t.strftime(f"%H{delimiter}%M{delimiter}%S")

def datestamp_YMD(delimiter:str="-"):
    '''
        Get the current date formatted as YYYY-MM-DD

        Arguments
        -------------------------
        `delimiter` {str}
            The string to use to separate the values in the timestamp.

        Return {str}
        ----------------------
        The current YYYY-MM-DD date stamp.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:22:48
        `memberOf`: current
        `version`: 1.0
        `method_name`: datestamp_YMD
        * @xxx [10-14-2023 11:24:36]: documentation for datestamp_YMD
    '''
    t = datetime.datetime.now()
    return t.strftime(f"%Y{delimiter}%m{delimiter}%d")

def datetimestamp_YMD(stripped:bool=False,date_delimiter:str="-",time_delimiter:str=":"):
    '''
        Get the current date & time formatted as YYYY-MM-DD HH:MM:SS

        Arguments
        -------------------------
        `date_delimiter` {str}
            The string to use to separate the values in the date.

        `time_delimiter` {str}
            The string to use to separate the values in the time.

        Return {str}
        ----------------------
        The current YYYY-MM-DD HH:MM:SS date time stamp.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:22:48
        `memberOf`: current
        `version`: 1.0
        `method_name`: datestamp_YMD
        * @xxx [10-14-2023 11:24:36]: documentation for datestamp_YMD
    '''
    # t = datetime.datetime()
    value = f"{datestamp_YMD(date_delimiter)} {timestamp_HMS(time_delimiter)}"
    if stripped is True:
        value = value.replace(" ","")
        value = value.replace(date_delimiter,"")
        value = value.replace(time_delimiter,"")
    return value

def year_as_words(dtime=None):
    '''Get the current year's name 
    2024 = twenty twenty-four
    '''
    year = str(four_digit_year())
    if dtime is not None:
        year = str(dtime.strftime("%Y"))
    p = inflect.engine()
    mil = p.number_to_words(int(year[:2]))
    dec = p.number_to_words(int(year[2:]))
    return f"{mil} {dec}"

def four_digit_year():
    '''
        Get the current year as a four digit number

        2023

        Return {int}
        ----------------------
        The current year as a four digit integer.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:09:04
        `memberOf`: current
        `version`: 1.0
        `method_name`: four_digit_year
        * @xxx [10-14-2023 11:09:43]: documentation for four_digit_year
    '''
    t = datetime.datetime.now()
    return int(t.strftime("%Y"))

def two_digit_year():
    '''
        Get the current year as a two digit number (without the century)

        23

        Return {int}
        ----------------------
        The current year as a two digit integer.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:09:04
        `memberOf`: current
        `version`: 1.0
        `method_name`: two_digit_year
        * @xxx [10-14-2023 11:09:43]: documentation for two_digit_year
    '''
    t = datetime.datetime.now()
    return t.strftime("%y")

def month(as_int:bool=False):
    '''
        Get the current month as a 2 digit zero padded number.


        Arguments
        -------------------------
        `as_int` {bool}
            if True, the return value will be an integer.

        Return {str,int}
        ----------------------
        The current month as a zero padded string.
        if is_int is True, the current month as an integer.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:11:31
        `memberOf`: current
        `version`: 1.0
        `method_name`: month
        * @xxx [10-14-2023 11:13:58]: documentation for month
    '''
    t = datetime.datetime()
    if as_int:
        return t.strftime("%-m")
    return t.strftime("%m")

def abbreviated_month_name()->str:
    t = datetime.datetime()
    return t.strftime("%b")

def month_name(abbrev:bool=False)->str:
    '''
        Get the current months name or its abbreviated name


        Arguments
        -------------------------
        `abbrev` {bool}
            if True, the return value will be the current month's abbreviated name.

        Return {str}
        ----------------------
        The current month's name
        if abbrev is True, the current month's abbreviated name

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 11:11:31
        `memberOf`: current
        `version`: 1.0
        `method_name`: month
        * @xxx [10-14-2023 11:13:58]: documentation for month_name
    '''
    t = datetime.datetime()
    if abbrev:
        return t.strftime("%b")
    return t.strftime("%B")






