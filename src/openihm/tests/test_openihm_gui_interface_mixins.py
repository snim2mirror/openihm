import unittest
try:
    import PyQt4.QtCore
    import PyQt4.QtGui
except:
    raise unittest.SkipTest("Need PyQt4 installed to do gui tests")
from gui.interface.mixins import TableViewMixin, MDIDialogMixin, DataEntryMixin


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
        data_entry_mixin = DataEntryMixin()
        self.assertEqual("donxxxt really want this",
            data_entry_mixin.getDbString("don't really want this"))

    def test_getIntMonth(self):
        data_entry_mixin = DataEntryMixin()
        self.assertEqual("6", data_entry_mixin.getIntMonth("June"))

    def test_getStringMonth(self):
        data_entry_mixin = DataEntryMixin()
        self.assertEqual('June', data_entry_mixin.getStringMonth("6"))

    def test_getViewString(self):
        data_entry_mixin = DataEntryMixin()
        self.assertEqual("don't really want this",
            data_entry_mixin.getViewString("donxxxt really want this"))

if __name__ == '__main__':
    unittest.main()
