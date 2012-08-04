import unittest
from openihm.gui.interface.mixins import *
from database_helper import DatabaseHelper


class Fake(TableViewMixin):

    pass


class FakeMDI(MDIDialogMixin):

    def closeActiveSubWindow(self):
        pass

    def parent(self):
        pass

    def close(self):
        pass


class FakeView(object):

    def selectedIndexes(self):
        return [FakeRow() for x in range(10)]

    def currentIndex(self):
        return FakeRow()


class FakeRow(object):

    def row(self):
        return 'test'


class TestTableViewMixin(unittest.TestCase):
    def test_countRowsSelected(self):
        table_view_mixin = Fake()
        view = FakeView()
        self.assertEqual(1, table_view_mixin.countRowsSelected(view))

    def test_getCurrentRow(self):
        table_view_mixin = Fake()
        view = FakeView()
        self.assertEqual('test', table_view_mixin.getCurrentRow(view))

    def test_getSelectedRows(self):
        table_view_mixin = Fake()
        view = FakeView()
        self.assertEqual(['test'], table_view_mixin.getSelectedRows(view))


class TestMDIDialogMixin(unittest.TestCase):
    def test_mdiClose(self):
        m_di_dialog_mixin = FakeMDI()
        # FIXME: get more coverage
        m_di_dialog_mixin.mdiClose()

    def test_setMdi(self):
        m_di_dialog_mixin = FakeMDI()
        m_di_dialog_mixin.setMdi(mdi)
        self.assertEqual(expected, m_di_dialog_mixin.mdi)


class TestMySQLMixin(unittest.TestCase):
    """
    In order to use these tests you need to have a config file named
    test_openihm.cfg in the directory you are running the tests from
    (i.e. the src directory).

        [database]
        superuser = root
        superuser_password = s00pers3cur3
        database = test_openihm
        user = openihm
        password = ihm2012

    This should contain database credentials for a database that exists
    in mysql for testing.  This database will be toyed around with a lot.
    Obviously avoid pointing it at a database you care about...

    """

    def setUp(self):
        import pdb; pdb.set_trace()
        self.helper = DatabaseHelper(self)
        self.helper.start_tests()
        

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test_executeMultipleResultsQueries(self):
        # my_sql_mixin = MySQLMixin()
        # self.assertEqual(expected, my_sql_mixin.executeMultipleResultsQueries(queries))
        assert False # TODO: implement your test here

    def test_executeMultipleUpdateQueries(self):
        my_sql_mixin = MySQLMixin()
        queries = [
        """
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                ('test', 2012-06-04, 2013-07-03, 'a simple test', 'GBP')""",
        """
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                ('test2', 2012-06-04, 2013-07-03, 'simple test', 'AUS')""",
        ]
        my_sql_mixin.executeMultipleUpdateQueries(queries)
        expected = [
            (u'test', None, None, u'a simple test', u'GBP'),
            (u'test2', None, None, u'a simple test', u'GBP')
        ]
        query = """
        select projectname, startdate, enddate, description, currency
        from projects
        """
        # FIXME: the None's look hinky.
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))
        assert False # TODO: implement your test here

    def test_executeResultsQuery(self):
        my_sql_mixin = MySQLMixin()
        my_sql_mixin.executeUpdateQuery("""
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                ('test', 2012-06-04, 2013-07-03, 'a simple test', 'GBP')""")
        expected = [(2, u'test', None, None, u'a simple test', u'GBP')]
        query = 'select * from projects'
        # FIXME: the None's look hinky.
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))

    def test_executeUpdateQuery(self):
        my_sql_mixin = MySQLMixin()
        my_sql_mixin.executeUpdateQuery("""
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                ('test', 2012-06-04, 2013-07-03, 'a simple test', 'GBP')""")
        expected = [(2, u'test', None, None, u'a simple test', u'GBP')]
        query = 'select * from projects'
        # FIXME: the None's look hinky.
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))


class TestDataEntryMixin(unittest.TestCase):
    def test_getDbString(self):
        # data_entry_mixin = DataEntryMixin()
        # self.assertEqual(expected, data_entry_mixin.getDbString(strSeed))
        assert False # TODO: implement your test here

    def test_getIntMonth(self):
        # data_entry_mixin = DataEntryMixin()
        # self.assertEqual(expected, data_entry_mixin.getIntMonth(month))
        assert False # TODO: implement your test here

    def test_getStringMonth(self):
        # data_entry_mixin = DataEntryMixin()
        # self.assertEqual(expected, data_entry_mixin.getStringMonth(month))
        assert False # TODO: implement your test here

    def test_getViewString(self):
        # data_entry_mixin = DataEntryMixin()
        # self.assertEqual(expected, data_entry_mixin.getViewString(strSeed))
        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
