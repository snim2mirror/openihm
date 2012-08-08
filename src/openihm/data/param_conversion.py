class ParamsUtility(object):
    """
    This is a utility class for parameter related logic.
    """

    @classmethod
    def make_parameters_safe(cls, params):
        """
        This function takes a list of parameters (or None) and ensures
        they are safe to pass to MySQL.  Actually, it just finds the
        QT Text boxes that are passed directly as parameters and
        converts them to strings.

        The reason I need to do this is that the existing code can
        rely on an implicit conversion to string when it puts the
        text fields into the queries.  When we do it properly
        passing the parameters in a list however this does not happen
        and so the conversion never happens, and the underlying
        MySQL library doesn't know what to do with the parameter.
        """
        if params:
            # I should probably be spanked for this, but I'm going
            # to make an assumption that an object with a class beginning
            # with a Q came from something QT related and therefore
            # needs converting to string.
            converted_qt = [(x.__class__.__name__[0] == 'Q' and str(x)) or x
                                                        for x in params]
            return converted_qt

        return None
