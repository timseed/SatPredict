import daiquiri
from Ham.Sat.Glob import config_dir
from os.path import exists, expanduser
from glob import glob


class ReadTle():

    def __init__(self, config_dir=config_dir):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug(f"Init {__name__}")
        self.tle = {}
        self.tle_files = []

    def find_tle_files(self,config_dir=config_dir):

        tle_files = glob(expanduser(config_dir + "/*.txt"))
        self.logger.debug(tle_files)
        for f in tle_files:
            self.logger.info(f"Processing file {f}")
            self.tle_files.append(f)
            self.read_in(f)
            self.logger.info(f"Processed file {f}")


    def read_in(self, filename) -> dict:
        """
        Read in a TLE file, return a dictionary
        :param filename:
        :return: TLE Dictionary. Key is Sat name, followed by ['Line1'] and ['line2']
        """
        self.logger.debug(f"Reading {filename}")
        with open(filename, "rt") as tle_input:
            data = tle_input.readlines()
        for n in range(0, len(data), 3):
            self.tle[data[n].rstrip()] = {}
            self.tle[data[n].rstrip()]['Line1'] = data[n + 1].rstrip()
            self.tle[data[n].rstrip()]['Line2'] = data[n + 2].rstrip()
        return self.tle

    @property
    def satcount(self):
        return len(self.tle.keys())

    def find_sat(self, sat_name) -> tuple:
        for n in self.tle.keys():
            if sat_name in n:
                self.logger.debug(f"Matched {sat_name} with {n}")
                return n, self.tle[n]['Line1'], self.tle[n]['Line2']
        self.logger.error(f"Could not find {sat_name}")
        return None, None, None
