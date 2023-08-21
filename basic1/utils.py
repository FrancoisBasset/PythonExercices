"""All utils methods needed by functions."""

import sys
import datetime
import math
import builtins
import calendar
import locale

def get_twinkle_text():
    """Return the Twinkle text."""
    return """\
Twinkle, twinkle, little star,
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are"""

def get_python_version():
    """Return the Python version."""
    return sys.version.split(" (")[0]

def get_formatted_date():
    """Return a formatted date."""
    date = datetime.datetime.now()
    return datetime.datetime.strftime(date, "%d/%m/%Y %H:%M:%S")

def get_circle_area(radius: float) -> float:
    """Return the circle area from radius."""
    return math.pi * (radius ** 2)

def get_reverse_names(first_name: str, last_name: str) -> str:
    """Return the reverse of names."""
    return f"{first_name[::-1]} {last_name[::-1]}"

def get_list_and_tuple(sequence: str) -> dict:
    """Return list and tuple from comma separated string."""
    return {
        "list": sequence.split(","),
        "tuple": tuple(sequence.split(","))
    }

def get_extension(file_name: str) -> str:
    """Return file extension from file name"""
    index = file_name.rindex(".") + 1
    return file_name[index::]

def get_date(day: int, month: int, year: int) -> str:
    """Return date from day, month and year"""
    return f"{day} / {month} / {year}"

def n_nn_nnn(n: int) -> str:
    """Return n + nn + nnn"""
    return n + int(str(n) * 2) + int(str(n) * 3)

def get_doc(function_name: str) -> str:
    "Return doc of function"
    f = getattr(builtins, function_name)
    return function_name + get_signature(f) + "\n" + get_docstring(f)

def get_signature(f: object) -> str:
    """Return signature of function"""
    return f.__text_signature__.replace("$module, ", "")

def get_docstring(f: object) -> str:
    """Return docstring of function"""
    return f.__doc__

def get_calendar(month: int, year: int) -> str:
    locale.setlocale(category=locale.LC_ALL, locale=locale.getlocale())
    return calendar.month(year, month)

def get_diff_date(date1, date2) -> int:
    d1 = datetime.date(date1[0], date1[1], date1[2])
    d2 = datetime.date(date2[0], date2[1], date2[2])

    return (d2 - d1).days

def get_sphere_area(radius: float) -> float:
    return (4 / 3) * math.pi * (radius ** 3)

def get_absolute_twice(n1: int, n2: int) -> int:
    a = abs(n1 - n2)

    return a * 2 if a > 17 else a

def near_thousand(n: float) -> bool:
    return abs(1000 - n) <= 100 or abs(2000 - n) <= 100

def sum_three_times(n1: int, n2: int, n3: int) -> int:
    s = n1 + n2 + n3
    return s * 3 if n1 == n2 == n3 else s
