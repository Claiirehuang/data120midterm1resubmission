#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DATA120 Midterm 1 Revision
"""
# Question Three

# Consider a list of dates:
dates_list = ["February 6, 1992", "February 18, 1992", "February 27, 1992",
              "September 6, 1991", "December 1, 1993"]

# Write a function that takes a list of dates formatted as in dates_list and
# returns a list of the same dates in ISO-8601 format, "YYYY-MM-DD". Do not use
# pandas in your function, you should be able to write your answer using methods
# for lists, strings, tuples, dictionaries, or sets.

MONTHS = {"January": "01", "February": "02", "March": "03", "April": "04",
          "May": "05", "June": "06", "July": "07", "August": "08",
          "September": "09", "October": "10", "November": "11",
          "December": "12"}

SINGLE_DIGIT_DAYS = {"1": "01", "2": "02", "3": "03", "4": "04", "5": "05",
                     "6": "06", "7": "07", "8": "08", "9": "09"}

def dates_to_iso8601(list_of_dates):
    """Returns dates in ISO-8601 format"""
    replace = [date.replace(",", " ") for date in list_of_dates]
    split = [date.split(" ") for date in replace]
    numbers = [[MONTHS.get(date[0]), SINGLE_DIGIT_DAYS.get(date[1], date[1]),
                date[3]] for date in split]
    iso = [[year, month, day] for month, day, year in numbers]
    return [("-").join(date) for date in iso]


# Write a function that accepts a list of dates formatted as in dates_list and
# returns a list with the same dates, sorted in chronological order. Do not use
# pandas in your function, you should be able to write your answer using methods
# for list, strings, tuples, dictionaries, or sets.

def sort_dates(list_of_dates):
    """Returns dates in chronological order"""
    dates = {}
    for i, date in enumerate(list_of_dates):
        dates[dates_to_iso8601(list_of_dates)[i]] = date
    sorted_dates = sorted(dates.keys())
    return [dates.get(date) for date in sorted_dates]
