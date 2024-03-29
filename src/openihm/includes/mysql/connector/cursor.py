# MySQL Connector/Python - MySQL driver written in Python.
# Copyright 2009 Sun Microsystems, Inc. All rights reserved
# Use is subject to license terms. (See COPYING)

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
# 
# There are special exceptions to the terms and conditions of the GNU
# General Public License as it is applied to this software. View the
# full text of the exception in file EXCEPTIONS-CLIENT in the directory
# of this software distribution or see the FOSS License Exception at
# www.mysql.com.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

"""Cursor classes
"""

import weakref

import connection
import protocol
import errors
import utils

class CursorBase(object):
    """
    Base for defining MySQLCursor. This class is a skeleton and defines
    methods and members as required for the Python Database API
    Specification v2.0.
    
    It's better to inherite from MySQLCursor.
    """
    
    def __init__(self):
        self.description = None
        self.rowcount = -1
        self.arraysize = 1
    
    def __del__(self):
        self.close()
    
    def callproc(self, procname, args=()):
        pass
    
    def close(self):
        pass
    
    def execute(self, operation, params=()):
        pass
    
    def executemany(self, operation, seqparams):
        pass
    
    def fetchone(self):
        pass
    
    def fetchmany(self, size=1):
        pass
    
    def fetchall(self):
        pass
    
    def nextset(self):
        pass
    
    def setinputsizes(self, sizes):
        pass
    
    def setoutputsize(self, size, column=None):
        pass
    
    def reset(self):
        pass
        
class MySQLCursor(CursorBase):
    """
    Default cursor which fetches all rows and stores it for later
    usage. It uses the converter set for the MySQLConnection to map
    MySQL types to Python types automatically.
    
    This class should be inherited whenever other functionallity is
    required. An example would to change the fetch* member functions
    to return dictionaries instead of lists of values.
    
    Implements the Python Database API Specification v2.0.
    
    Possible parameters are:
    
    db
        A MySQLConnection instance.
    """

    def __init__(self, db=None):
        CursorBase.__init__(self)
        self.db = None
        self._result = []
        self._nextrow = (None, None)
        self.lastrowid = None
        self._warnings = None
        self._warning_count = 0
        self._executed = None
        self._have_result = False
        self._raise_on_warnings = True
        if db is not None:
            self.set_connection(db)
    
    def __iter__(self):
        """
        Iteration over the result set which calls self.fetchone()
        and returns the next row.
        """
        return iter(self.fetchone, None)
        
    def set_connection(self, db):
        try:
            if isinstance(db.conn.protocol,protocol.MySQLProtocol):
                self.db = weakref.ref(db)
                if self not in self.db().cursors:
                    self.db().cursors.append(self)
        except:
            raise errors.InterfaceError(errno=2048)

    def _reset_result(self):
        del self._result[:]
        self.rowcount = -1
        self._nextrow = (None, None)
        self._have_result = False
        try:
            self.db().unread_result = False
        except:
            pass
        self._warnings = None
        self._warning_count = 0
        self.description = ()
        self.reset()
        
    def next(self):
        """
        Used for iterating over the result set. Calles self.fetchone()
        to get the next row.
        """
        try:
            row = self.fetchone()
        except errors.InterfaceError:
            raise StopIteration
        if not row:
            raise StopIteration
        return row
    
    def close(self):
        """
        Close the cursor, disconnecting it from the MySQL object.
        
        Returns True when succesful, otherwise False.
        """
        if self.db is None:
            return False
        
        try:
            self._reset_result()
            self.db().remove_cursor(self)
            self.db = None
        except:
            return False
        
        return True
    
    def _process_params_dict(self, params):
        try:
            to_mysql = self.db().converter.to_mysql
            escape = self.db().converter.escape
            quote = self.db().converter.quote
            res = {}
            for k,v in params.items():
                c = v
                c = to_mysql(c)
                c = escape(c)
                c = quote(c)
                res[k] = c
        except StandardError, e:
            raise errors.ProgrammingError(
                "Failed processing pyformat-parameters; %s" % e)
        else:
            return res
            
        return None
    
    def _process_params(self, params):
        """
        Process the parameters which were given when self.execute() was
        called. It does following using the MySQLConnection converter:
        * Convert Python types to MySQL types
        * Escapes characters required for MySQL.
        * Quote values when needed.
        
        Returns a list.
        """
        if isinstance(params,dict):
            return self._process_params_dict(params)
        
        try:
            res = params

            to_mysql = self.db().converter.to_mysql
            escape = self.db().converter.escape
            quote = self.db().converter.quote

            res = map(to_mysql,res)
            res = map(escape,res)
            res = map(quote,res)
        except StandardError, e:
            raise errors.ProgrammingError(
                "Failed processing format-parameters; %s" % e)
        else:
            return tuple(res)
        return None
    
    def _get_description(self, res=None):
        """
        Gets the description of the fields out of a result we got from
        the MySQL Server. If res is None then self.description is
        returned (which can be None).
        
        Returns a list or None when no descriptions are available.
        """
        if not res:
            return self.description
        
        desc = []
        try:
            for fld in res[1]:
                if not isinstance(fld, protocol.FieldPacket):
                    raise errors.ProgrammingError(
                        "Can only get description from protocol.FieldPacket")
                desc.append(fld.get_description())
        except TypeError:
            raise errors.ProgrammingError(
                "_get_description needs a list as argument."
                )
        return desc

    def _row_to_python(self, rowdata, desc=None):
        res = ()
        try:
            to_python = self.db().converter.to_python
            if not desc:
                desc = self.description
            for idx,v in enumerate(rowdata):
                flddsc = desc[idx]
                res += (to_python(flddsc, v),)
        except StandardError, e:
            raise errors.InterfaceError(
                "Failed converting row to Python types; %s" % e)
        else:
            return res
    
        return None
        
    def _handle_noresultset(self, res):
        """Handles result of execute() when there is no result set."""
        try:
            self.rowcount = res.affected_rows
            self.lastrowid = res.insert_id
            self._warning_count = res.warning_count
            if self.db().get_warnings is True and self._warning_count:
                self._warnings = self._fetch_warnings()
        except errors.Error:
            raise
        except StandardError, e:
            raise errors.ProgrammingError(
                "Failed handling non-resultset; %s" % e)
    
    def _handle_resultset(self):
        pass
        
    def execute(self, operation, params=None):
        """
        Executes the given operation. The parameters given through params
        are used to substitute %%s in the operation string.
        For example, getting all rows where id is 5:
          cursor.execute("SELECT * FROM t1 WHERE id = %s", (5,))
        
        If warnings where generated, and db.get_warnings is True, then
        self._warnings will be a list containing these warnings.
        
        Raises exceptions when any error happens.
        """
        if not operation:
            return 0
        if self.db().unread_result is True:
            raise errors.InternalError("Unread result found.")
        
        self._reset_result()
        stmt = ''
        
        # Make sure we send the query in correct character set
        try:
            if isinstance(operation, unicode):
                operation.encode(self.db().charset_name)
            if params is not None:
                try:
                    stmt = operation % self._process_params(params)
                except TypeError:
                    raise errors.ProgrammingError(
                        "Wrong number of arguments during string formatting")
            else:
                stmt = operation
            
            res = self.db().protocol().cmd_query(stmt)
            if isinstance(res, protocol.OKResultPacket):
                self.db().unread_result = False
                self._have_result = False
                self._handle_noresultset(res)
            else:
                self.description = self._get_description(res)
                self.db().unread_result = True
                self._have_result = True
                self._handle_resultset()
        except errors.Error:
            raise
        except StandardError, e:
            raise errors.InterfaceError(
                "Failed executing the operation; %s" % e)
        else:
            self._executed = stmt
            return self.rowcount
            
        return 0
    
    def executemany(self, operation, seq_params):
        """Loops over seq_params and calls excute()"""
        if not operation:
            return 0
        if self.db().unread_result is True:
            raise errors.InternalError("Unread result found.")
        
        rowcnt = 0
        try:
            for params in seq_params:
                self.execute(operation, params)
                if self._have_result:
                    self.fetchall()
                rowcnt += self.rowcount
        except (ValueError,TypeError), e:
            raise errors.InterfaceError(
                "Failed executing the operation; %s" % e)
        except:
            # Raise whatever execute() raises
            raise
        
        self.rowcount = rowcnt
        return rowcnt
    
    def callproc(self, procname, args=()):
        """Calls a stored procedue with the given arguments
        
        The arguments will be set during this session, meaning
        they will be called like  _<procname>__arg<nr> where
        <nr> is an enumeration (+1) of the arguments.
        
        Coding Example:
          1) Definining the Stored Routine in MySQL:
          CREATE PROCEDURE multiply(IN pFac1 INT, IN pFac2 INT, OUT pProd INT)
          BEGIN
            SET pProd := pFac1 * pFac2;
          END
          
          2) Executing in Python:
          args = (5,5,0) # 0 is to hold pprod
          cursor.callproc(multiply, args)
          print cursor.fetchone()
          
          The last print should output ('5', '5', 25L)

        Does not return a value, but a result set will be
        available when the CALL-statement execute succesfully.
        Raises exceptions when something is wrong.
        """
        argfmt = "@_%s_arg%d"
        
        try:
            procargs = self._process_params(args)
            argnames = []
        
            for idx,arg in enumerate(procargs):
                argname = argfmt % (procname, idx+1)
                argnames.append(argname)
                setquery = "SET %s=%%s" % argname
                self.execute(setquery, (arg,))
        
            call = "CALL %s(%s)" % (procname,','.join(argnames))
            res = self.db().protocol().cmd_query(call)
            
            select = "SELECT %s" % ','.join(argnames)
            self.execute(select)
            
        except errors.Error:
            raise
        except StandardError, e:
            raise errors.InterfaceError(
                "Failed calling stored routine; %s" % e)
    
    def getlastrowid(self):
        return self.lastrowid
        
    def _fetch_warnings(self):
        """
        Fetch warnings doing a SHOW WARNINGS. Can be called after getting
        the result.

        Returns a result set or None when there were no warnings.
        """
        res = []
        try:
            c = self.db().cursor()
            cnt = c.execute("SHOW WARNINGS")
            res = c.fetchall()
            c.close()
        except StandardError, e:
            raise errors.InterfaceError(
                "Failed getting warnings; %s" % e)
        
        if self.db().raise_on_warnings is True:
            msg = '; '.join([ "(%s) %s" % (r[1],r[2]) for r in res])
            if res[0][1] == 1366:
                c = self.db().cursor()
                cnt = c.execute("SHOW CREATE TABLE mytable2")
                print c.fetchall()
                c.close()
            raise errors.get_mysql_exception(res[0][1],res[0][2])
        else:
            if len(res):
                return res
            
        return None
    
    def _handle_eof(self, eof):
        self._have_result = False
        self.db().unread_result = False
        self._nextrow = (None, None)
        self._warning_count = eof.warning_count
        if self.db().get_warnings is True and eof.warning_count:
            self._warnings = self._fetch_warnings()
    
    def _fetch_row(self):
        if self._have_result is False:
            return None
        row = None
        try:
            if self._nextrow == (None, None):
                (row, eof) = self.db().protocol().result_get_row()
            else:
                (row, eof) = self._nextrow
            if row:
                (foo, eof) = self._nextrow = self.db().protocol().result_get_row()
                if eof is not None:
                    self._handle_eof(eof)
                if self.rowcount == -1:
                    self.rowcount = 1
                else:
                    self.rowcount += 1
            if eof:
                self._handle_eof(eof)
        except:
            raise
        else:
            return row
            
        return None
    
    def fetchwarnings(self):
        return self._warnings
        
    def fetchone(self):
        row = self._fetch_row()
        if row:
            return self._row_to_python(row)
        return None
        
    def fetchmany(self,size=None):
        res = []
        cnt = (size or self.arraysize)
        while cnt > 0 and self._have_result:
            cnt -= 1
            row = self.fetchone()
            if row:
                res.append(row)
            
        return res
    
    def fetchall(self):
        if self._have_result is False:
            raise errors.InterfaceError("No result set to fetch from.")
        res = []
        row = None
        while self.db().unread_result:
            row = self.fetchone()
            if row:
                res.append(row)
        return res
        
    def __unicode__(self):
        fmt = "MySQLCursor: %s"
        if self._executed:
            if len(self._executed) > 30:
                res = fmt % (self._executed[:30] + '..')
            else:
                res = fmt % (self._executed)
        else:
            res = fmt % '(Nothing executed yet)'
        return res
    
    def __str__(self):
        return repr(self.__unicode__())

class MySQLCursorBuffered(MySQLCursor):
    """Cursor which fetches rows within execute()"""
    
    def __init__(self, db=None):
        MySQLCursor.__init__(self, db)
        self._rows = None
        self._next_row = 0
    
    def _handle_resultset(self):
        (self._rows, eof) = self.db().protocol().result_get_rows()
        self.rowcount = len(self._rows)
        self._handle_eof(eof)
        self._next_row = 0
        try:
            self.db().unread_result = False
        except:
            pass
            
    def reset(self):
        self._rows = None

    def _fetch_row(self):
        row = None
        try:
            row = self._rows[self._next_row]
        except:
            return None
        else:
            self._next_row += 1
            return row
        return None
    
    def fetchall(self):
        if self._rows is None:
            raise errors.InterfaceError("No result set to fetch from.")
        res = []
        for row in self._rows:
            res.append(self._row_to_python(row))
        self._next_row = len(self._rows)
        return res
    
    def fetchmany(self,size=None):
        res = []
        cnt = (size or self.arraysize)
        while cnt > 0:
            cnt -= 1
            row = self.fetchone()
            if row:
                res.append(row)

        return res
    

        