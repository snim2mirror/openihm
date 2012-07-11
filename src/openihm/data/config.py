#!/usr/bin/env python

"""
This file is part of open-ihm.

-*- coding: utf-8 -*-

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

class Config(object):
    """ Configures the mysql database connector which is then called as below:
    
        includes.mysql.connector.Connect(**Config.dbinfo())
    """
    
    """
    Set the OpenIHMConfig object with the config options.
    """
    @classmethod
    def set_config(cls, config_object):
        cls.config = config_object
    
    """
    Return the database configuration.
    """
    @classmethod
    def dbinfo(cls):
        return cls.config.dbinfo()
    
