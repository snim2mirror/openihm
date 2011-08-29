#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""


def getDbString(strSeed):
     return strSeed.replace("'", "xxx")
     
def getViewString(strSeed):
     return strSeed.replace("xxx", "'")
     
def getStringMonth(month):
     months = {"1" : "January","2" : "February", "3" : "March","4" : "April","5" : "May","6" : "June",
                    "7" : "July","8" : "August","9" : "September","10" : "October","11" : "November","12" : "December"}
     for key, val in months.items():
         if str(month) == key:
             return val
     
def getIntMonth(month):
     months = {"1" : "January","2" : "February", "3" : "March","4" : "April","5" : "May","6" : "June",
                    "7" : "July","8" : "August","9" : "September","10" : "October","11" : "November","12" : "December"}
     for key, val in months.items():
         if month == val:
             return key
