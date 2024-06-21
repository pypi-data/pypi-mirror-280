# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=unused-import
'''
    A module of utility methods used for parsing and converting python types.

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 06-03-2022 10:22:15
    `memberOf`: type_utils
'''
from math import floor
import re
from typing import Union
# import colemen_utilities.string_utils as _csu
# import colemen_utilities.dict_utils as _obj




def num_to_weekday(value:Union[int,float]):
    '''
        Convert an integer/float to the named day of the week

        Raises a value error if a non int/float is provided or if the value is outside of the range.

        Arguments
        -------------------------
        `value` {int,float}
            The number value to convert, must be between 0 and 6

        Return {str}
        ----------------------
        The named day of the week:
        - 0 = Monday
        - 1 = Tuesday
        - 2 = Wednesday
        - 3 = Thursday
        - 4 = Friday
        - 5 = Saturday
        - 6 = Sunday

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 10-14-2023 10:58:44
        `memberOf`: convert
        `version`: 1.0
        `method_name`: num_to_weekday
        * @xxx [10-14-2023 11:03:08]: documentation for num_to_weekday
    '''
    if isinstance(value,(int,float)):
        raise ValueError(f"The value must be an integer or float. {type(value)} was provided.")
    if value > 6 or value < 0:
        raise ValueError(f"The value must be between 0 and 6.\n {value} was provided.")

    value = floor(value)

    if value == 0:
        return "Monday"
    elif value == 1:
        return "Tuesday"
    elif value == 2:
        return "Wednesday"
    elif value == 3:
        return "Thursday"
    elif value == 4:
        return "Friday"
    elif value == 5:
        return "Saturday"
    else:
        return "Sunday"


def month_name_to_number(value:str):
    '''
        Convert a month's name to its number.

        Arguments
        -------------------------
        `value` {str}
            The string name of the month

        Return {int}
        ----------------------
        The integer for that month

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 06-20-2024 12:11:31
        `memberOf`: convert
        `version`: 1.0
        `method_name`: month_name_to_number
        * @TODO []: documentation for month_name_to_number
    '''
    months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    val = value.lower()
    for idx,m in enumerate(months):
        if m.startswith(val):
            return idx + 1



def seconds(total_secs,leading_zeros:bool=False):
    '''
        Convert total seconds to hours minutes and seconds.

        Arguments
        -------------------------
        `total_secs` {int}
            The total number of seconds to convert
        `leading_zeros` {bool} = False
            If True, each value will below 10 will have a zero appended to it, this converts the values
            to strings.

        Return {tuple}
        ----------------------
        A tuple containing the hours, minutes and seconds

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 04-05-2024 11:00:17
        `memberOf`: convert
        `version`: 1.0
        `method_name`: seconds
        * @xxx [04-05-2024 11:02:10]: documentation for seconds
    '''
    hours = total_secs // 3600
    remaining_secs = total_secs % 3600

    minutes = remaining_secs // 60
    seconds = remaining_secs % 60
    hours = round(hours)
    minutes = round(minutes)
    seconds = round(seconds)

    if leading_zeros is True:
        if hours < 10:
            hours = f"0{hours}"

        if minutes < 10:
            minutes = f"0{minutes}"

        if seconds < 10:
            seconds = f"0{seconds}"

    return (hours,minutes,seconds)



