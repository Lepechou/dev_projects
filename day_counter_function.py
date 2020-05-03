# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:29:19 2020

@author: Ricky
"""

def readable_timedelta(days):
    weeks = 0     # days_lefts = 0 was useless cos not incremented
    while days >= 7 :
        days = days - 7
        weeks += 1
    days_lefts = days
    return '{} week(s) and {} days(s).'.format(weeks,days_lefts)

# test your function
print(readable_timedelta(364))