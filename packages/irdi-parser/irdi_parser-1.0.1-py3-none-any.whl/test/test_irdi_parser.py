import unittest
from parser.irdi_parser import IRDIParser


class TestIRDIParser(unittest.TestCase):
    def setUp(self):
        self.parser = IRDIParser()

    def test_valid_irdi_with_optional_info(self):
        irdi_string = "1234-AB12-CD34#AB-123456#1"
        expected_output = {
            'icd': '1234',
            'org_id': 'AB12',
            'add_info': 'CD34',
            'csi': 'AB',
            'item_code': '123456',
            'version': '1'
        }
        self.assertEqual(self.parser.parse(irdi_string), expected_output)

    def test_valid_irdi_without_optional_info(self):
        irdi_string = "1234-AB12#AB-123456#1"
        expected_output = {
            'icd': '1234',
            'org_id': 'AB12',
            'add_info': None,
            'csi': 'AB',
            'item_code': '123456',
            'version': '1'
        }
        self.assertEqual(self.parser.parse(irdi_string), expected_output)

    def test_invalid_irdi_format(self):
        irdi_string = "123-AB12#AB-123456#1"
        with self.assertRaises(ValueError):
            self.parser.parse(irdi_string)

    def test_invalid_characters_in_irdi(self):
        irdi_string = "1234-AB!2#AB-123456#1"
        with self.assertRaises(ValueError):
            self.parser.parse(irdi_string)

    def test_missing_version(self):
        irdi_string = "1234-AB12-CD34#AB-123456#"
        with self.assertRaises(ValueError):
            self.parser.parse(irdi_string)


if __name__ == '__main__':
    unittest.main()
