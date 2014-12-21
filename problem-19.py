"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime

def count_months(yr_min, yr_max):
    """
    >>> sum(count_months(2013, 2013))
    2
    """
    for yr in xrange(yr_min, yr_max+1):
        for mn in xrange(1, 13):
            d = datetime.date(yr, mn, 1)
            yield d.weekday() == 6

if __name__ == '__main__':
    print sum(count_months(1901, 2000))
