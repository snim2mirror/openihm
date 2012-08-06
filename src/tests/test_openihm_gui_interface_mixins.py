import unittest
from database_helper import DatabaseHelper
from openihm.gui.interface.mixins import TableViewMixin, MDIDialogMixin, MySQLMixin


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
        mdi = FakeMDI()
        m_di_dialog_mixin.setMdi(mdi)
        self.assertEqual(mdi, m_di_dialog_mixin.mdi)


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
