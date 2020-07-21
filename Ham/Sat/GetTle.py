import requests
import daiquiri
import os
from os import path
from Ham.Sat.Glob import config_dir


class GetTle:

    def __init__(self):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug("Init GetTle")

    def config_dir(self) -> str:
        """
        Check Directory ~/.mysat exists
        :return: True
        """
        cdir = path.expanduser(config_dir)
        if not os.path.exists(cdir):
            self.logger.debug(f"Need to Create a Directory {cdir}")
            os.mkdir(cdir)
        else:
            self.logger.debug(f"config dir {cdir} already there")
        return cdir

    def fetch(self,urls=['https://www.celestrak.com/NORAD/elements/amateur.txt'],
              user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
              ):
        headers = {'User-Agent': user_agent}
        cdir = self.config_dir()
        for url in urls:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                # Success
                self.logger.debug(f"Url {url} downloaded")
                filename = url.split('/')[-1]
                self.logger.debug(f"Need to write to {cdir}/{filename}")
                with open(cdir+"/"+filename,"wt") as tle_file:
                    tle_file.write(response.text)
                    self.logger.debug("Filename written")
            else:
                self.logger.error(f"Unable to find {url}")
                raise ValueError
