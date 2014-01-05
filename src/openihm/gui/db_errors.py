class ErrorMessage(object):

    def duplicate_entry(self, message):
        """
        This will be called when there is a database error indicating that
        the item already exists in the database.  This can be via an insert
        or an update.

        Note that the original exception error message is passed in.  This 
        could be logged, or it could be thrown away.
        """
        pass
