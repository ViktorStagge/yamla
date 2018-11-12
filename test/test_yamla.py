import unittest

from yamla import load_yaml
from yamla import AttributeDict


class AttributeDictTestCases(unittest.TestCase):
    def test_get_item(self):
        self.assertEqual(self.config.c, True, 'fails to get a simple item')

    def test_get_chained_item(self):
        self.assertEqual(self.config.b, AttributeDict(dict(dinner='no', lunch='yes')))
        self.assertEqual(self.config.b.dinner, 'no')
        self.assertEqual(self.config.b.lunch, 'yes')
        self.assertEqual(self.config.a, AttributeDict(dict(horse=1, cat=2, dog=3)))
        self.assertEqual(self.config.a.horse, 1)
        self.assertEqual(self.config.a.cat, 2)
        self.assertEqual(self.config.a.dog, 3)

    def test_crash_on_key_error(self):
        with self.assertRaises(KeyError):
            self.config.definitely_not_in_the_dictionary

    def test_set_item(self):
        some_value = 'some value'
        self.config['new_key'] = some_value
        self.assertEqual(self.config.new_key, some_value, 'cant add a new item')

    def test_set_item_as_attribute(self):
        some_value = 'some value'
        self.config.new_key = some_value
        self.assertEqual(self.config.new_key, some_value, 'cant add a new item from attribute')

    def test_delete_attribute(self):
        self.assertTrue(self.config.a)
        del self.config.a
        with self.assertRaises(KeyError):
            self.config.a
        with self.assertRaises(KeyError):
            self.config['a']

    def test_add_dictionary(self):
        pass

    def test_create_AttributeDict(self):
        pass

    def setUp(self):
        path = 'test/test_config/test_config1.yml'
        self.config = load_yaml(path)


if __name__ == '__main__':
    unittest.main()
