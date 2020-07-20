import daiquiri
from Ham.Sat.Glob import config_file
from os.path import exists, expanduser

class MyStation:

    def __init__(self):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug(f"Module {__name__} loaded")

    def CheckConfig(self, config=config_file):
        """

        :return:
        """
        config  = expanduser(config)
        if exists(config):
            self.logger.debug(f"Found config {config} will process")
        else:
            self.logger.warning(f"No config file creating default in {config}")
            with open(config,"wt") as cfg_file:
                cfg_file.write(self.DefaultConfig())
                self.logger.debug("Config file created")


    def DefaultConfig(self):
        """
        This will create a basic Config file in the Config directory. You can then manualy adjust it to suit your requirements.

        :return:
        """
        cfg = """[DEFAULT]
        UNUSED=1

        [Location]
        Lat = 15.3
        Lon = 120.2
        Alt = 50
        Name = "Arayat"

        [Track]
        AO-92
        SO-50
        ISS
        
        [Pass]
        MinAlt = 20.0
        """
        return cfg

