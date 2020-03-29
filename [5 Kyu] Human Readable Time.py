# Write a function, which takes a non-negative integer (seconds) as input and returns
# the time in a human-readable format (HH:MM:SS)
from decimal import *
def make_readable(seconds):
    hours = seconds / 3600
    hours_section = '%02d' % hours
    minutes = float(hours % 1) * 60
    minutes_section = '%02d' % minutes
    seconds_section = '%02d' % round(minutes % 1 * 60)
    return str(hours_section) + ":" + str(minutes_section) + ":" + str(seconds_section)

print(make_readable(86399))