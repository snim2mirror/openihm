# -*- coding: utf-8 -*-

class Config(object):
    """ Configures the mysql database connector which is then called as below:
    
        includes.mysql.connector.Connect(**Config.dbinfo())
    """
    
    HOST = 'localhost'
    DATABASE = 'openihmdb'
    USER = 'openihm'
    PASSWORD = 'ihm2010'
    PORT = 3306
    
    CHARSET = 'utf8'
    UNICODE = True
    WARNINGS = True
    
    @classmethod
    def dbinfo(cls):
        return {
            'host'          : cls.HOST,
            'database'      : cls.DATABASE,
            'user'          : cls.USER,
            'password'      : cls.PASSWORD,
            'charset'       : cls.CHARSET,
            'use_unicode'   : cls.UNICODE,
            'get_warnings'  : cls.WARNINGS,
            }
    
