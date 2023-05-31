"""All utils methods needed by functions"""

import sys
import datetime
import math

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
    """Return the Python version"""
    return sys.version.split(" (")[0]

def get_formatted_date():
    """Return a formatted date."""
    date = datetime.datetime.now()
    return datetime.datetime.strftime(date, "%d/%m/%Y %H:%M:%S")

def get_circle_area(radius: float) -> float:
    """Return the circle area from radius"""
    return math.pi * (radius ** 2)
