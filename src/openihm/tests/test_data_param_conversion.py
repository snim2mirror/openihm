import unittest
from data.param_conversion import ParamsUtility


class QFakeTextBox(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class TestParamsUtility(unittest.TestCase):

    def test_make_parameters_safe(self):
        params = [1, 'test', QFakeTextBox('simple')]
        expected = [1, 'test', 'simple']
        self.assertEqual(expected, ParamsUtility.make_parameters_safe(params))

    def test_make_parameters_safe_none(self):
        self.assertEqual(None, ParamsUtility.make_parameters_safe(None))


if __name__ == '__main__':
    unittest.main()
