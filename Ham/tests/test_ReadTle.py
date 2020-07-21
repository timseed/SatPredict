from unittest import TestCase
from unittest.mock import patch, mock_open
from Ham.Sat.ReadTle import ReadTle
from Ham.tests import fake_tle

class TestReadTle(TestCase):

    def setUp(self) -> None:
        self.test_read_tle = ReadTle()
        self.assertIsInstance(self.test_read_tle, ReadTle)

    @patch('Ham.Sat.ReadTle.glob',return_value=['/tmp/amateur.txt'])
    @patch('Ham.Sat.ReadTle.open', mock_open(read_data=fake_tle))
    def test_find_tle_files(self, fake_glob):
        self.test_read_tle.find_tle_files()
        # This should have processed the file definition in  TestGlob ...
        # which means there should be 5 keys in the data file
        self.assertEqual(self.test_read_tle.satcount, 5)

    @patch('Ham.Sat.ReadTle.glob',return_value=['/tmp/amateur.txt'])
    @patch('Ham.Sat.ReadTle.open', mock_open(read_data=fake_tle))
    def test_find_tle_files(self, fake_glob):
        self.test_read_tle.find_tle_files()
        # We should have these Sats in the data file
        valid = ['ISS (ZARYA)','ISS','ZARYA']
        invalid = ['Apollo','Mercury','Bob']

        for v in valid:
            sat,line1,line2 = self.test_read_tle.find_sat(v)
            self.assertNotEqual(sat, None)
        for v in invalid:
            sat, line1, line2 = self.test_read_tle.find_sat(v)
            self.assertEqual(sat, None)


