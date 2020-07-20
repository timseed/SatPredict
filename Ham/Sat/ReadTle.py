import daiquiri
from Ham.Sat.Glob import config_dir
from os.path import exists, expanduser
from glob import glob


class ReadTle():

    def __init__(self, config_dir=config_dir):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug(f"Init {__name__}")
        tle_files = glob(expanduser(config_dir + "/*.txt"))
        self.logger.debug(tle_files)
        self.tle = {}
        for f in tle_files:
            self.read_in(f)


    def read_in(self, filename):
        self.logger.debug(f"Reading {filename}")
        with open(filename, "rt") as tle_input:
            data = tle_input.readlines()
        for n in range(0, len(data), 3):
            self.tle[data[n].rstrip()] = {}
            self.tle[data[n].rstrip()]['Line1'] = data[n + 1].rstrip()
            self.tle[data[n].rstrip()]['Line2'] = data[n + 2].rstrip()

        junk = 1

    def find_sat(self, sat_name) -> tuple:

        for n in self.tle.keys():
            if sat_name in n:
                self.logger.debug(f"Matched {sat_name} with {n}")
                return n, self.tle[n]['Line1'],self.tle[n]['Line1']
        self.logger.warning(f"Could not find {sat_name}")
        return None, None, None

