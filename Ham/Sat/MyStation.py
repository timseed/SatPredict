import daiquiri
from Ham.Sat.Glob import config_file
from os.path import exists, expanduser
import configparser

class MyStation:

    def __init__(self,config_file_path=config_file):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug(f"Module {__name__} loaded")
        self.config = configparser.ConfigParser()
        self.config_dict = self.CheckConfig(config_file_path=config_file_path)

    def CheckConfig(self, config_file_path=config_file) -> dict:
        """

        :return:
        """
        cf = expanduser(config_file_path)
        if exists(cf):
            self.logger.debug(f"Found config {cf} will process")
            self.config.read(cf)

            self.logger.debug("config file read")
        else:
            self.logger.warning(f"No config file creating default in {cf}")
            with open(cf,"wt") as cfg_file:
                cfg_file.write(self.DefaultConfig())
                self.logger.debug("Config file created")
            # File is now created - so call Check-Config again
            self.CheckConfig()
        return self.Dump()


    def Dump(self) -> dict:
        """
        Dump the config, returning a Python style Dictionary
        :return:
        """
        thedict = {}
        for section in self.config.sections():
            thedict[section] = {}
            for key, val in self.config.items(section):
                thedict[section][key] = val
        thedict['Track']['sats'] = [n.strip().upper() for n in thedict['Track']['sats'].split(',') if len(n) > 1]
        self.logger.debug(f"Config is {thedict}")
        return thedict

    @property
    def Sats(self) -> list:
        try:
            return self.config_dict['Track']['sats']
        except ValueError:
            return []
    @property
    def Lat(self) -> float:
        return float(self.config_dict['Location']['lat'])

    @property
    def Lon(self) -> float:
        return float(self.config_dict['Location']['lon'])

    @property
    def Alt(self) -> float:
        return float(self.config_dict['Location']['alt'])

    @property
    def Qth(self) -> tuple:
        return self.Lat, self.Lon, self.Alt

    @property
    def MinAlt(self):
        return float(self.config['Pass']['minalt'])

    @property
    def TimeZone(self):
        return self.config['Location']['tz']

    def DefaultConfig(self) -> str:
        """
        This will create a basic Config file in the Config directory. You can then manualy adjust it to suit your requirements.

        Note the Items (lat, lon) are ALL lowercase.
        The Sats are converted into a list on the way in - removing any empty strings. Sats are Trimmed, and forced to upper-case.

        WARNING: East Longitude has to be NEGATIVE !!!

        :return:
        """
        cfg = \
"""[Location]
lat = 15.3
lon = -120.2
alt = 50
name = Arayat
tz = Asia/Manila

[Track]
sats = AO-92,SO-50,ISS,FO-29,FOX-1B,IO-86,AO-7,AO-27,AO-73,XW-2B,XW-2F,LILACSAT-2

[Pass]
minalt = 20.0

[Tle]
files = 'https://www.celestrak.com/NORAD/elements/amateur.txt,'
"""
        return cfg

