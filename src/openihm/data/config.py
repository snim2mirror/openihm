# -*- coding: utf-8 -*-

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


class Config(object):
    """ Configures the mysql database connector which is then called as below:
        includes.mysql.connector.Connect(**Config.dbinfo())
    """

    @classmethod
    def set_config(cls, config_object):
        """
        Set the OpenIHMConfig object with the config options.
        """
        cls.config = config_object

    @classmethod
    def dbinfo(cls):
        """
        Return the database configuration.
        """
        return cls.config.dbinfo()
