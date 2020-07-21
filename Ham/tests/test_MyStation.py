from unittest import TestCase
from unittest.mock import patch
from Ham.Sat.MyStation import MyStation
import configparser
from Ham.tests import cfg, cfg_as_dict

class TestMyStation(TestCase):


    def setUp(self) -> None:
        self.test_station = MyStation()
        self.assertIsInstance(self.test_station, MyStation)

    def test_default_config(self):
        self.assertEqual(self.test_station.DefaultConfig(), cfg)

    def test_dump(self):
        config = configparser.ConfigParser()
        config.read_string(cfg)
        self.test_station.config = config
        self.assertEqual(self.test_station.Dump(), cfg_as_dict)

    def test_check_config(self):
        config = configparser.ConfigParser()
        config.read_string(cfg)
        self.test_station.config = config
        self.assertEqual(self.test_station.CheckConfig(), cfg_as_dict)
