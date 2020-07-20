import daiquiri
from Ham.Sat.Glob import config_file, config_dir
from Ham.Sat.MyStation import MyStation
from Ham.Sat.ReadTle import ReadTle
from os.path import exists, expanduser
from glob import glob

class Passes:

    def __init__(self,config=config_file):
        self.logger = daiquiri.getLogger(__name__)
        self.config = MyStation(config)
        self.tle_reader = ReadTle(config_dir)