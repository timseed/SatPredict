
from unittest import TestCase
from unittest.mock import patch
import requests_mock
from Ham.Sat import GetTle
from Ham.tests import cfg_dir, fake_tle
class TestGetTle(TestCase):

    """The purpose of this test. is to allow testing without needing the internet
    To accomplish this we need to fake the requests, and the config_dir section of the code
    """



    def setUp(self) -> None:
        self.test_gettle = GetTle()
        self.assertIsInstance(self.test_gettle, GetTle)

    @patch('Ham.Sat.GetTle.config_dir',return_value=cfg_dir)
    def test_config_dir(self, fake_config_dir):
        self.assertEqual(self.test_gettle.config_dir(), cfg_dir )


    @patch('Ham.Sat.GetTle.fetch', return_value=fake_tle)
    def test_fetch(self,fake_fetch):
        self.assertEqual(self.test_gettle.fetch(), fake_tle)

    @requests_mock.mock()
    def test_bad_fetch(self,fake_fetch):
        """
        Lets pretend that the Requests fails....
        """
        test_bad_url = 'https://www.celestrak.com/NORAD/elements/amateur.txt'
        fake_fetch.get(test_bad_url, text=None, status_code=404)
        self.assertRaises(ValueError, self.test_gettle.fetch)
