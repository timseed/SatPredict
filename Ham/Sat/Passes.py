import daiquiri
from Ham.Sat.Glob import config_file, config_dir
from Ham.Sat.MyStation import MyStation
from Ham.Sat.ReadTle import ReadTle
from pprint import pprint
import predict
import time
from datetime import datetime
from pytz import timezone
from dataclasses import dataclass, asdict


@dataclass
class Prediction:
    name: str
    delay: str
    start: str
    duration: int
    max_ele: int

class Passes:

    def __init__(self,config=config_file):
        self.logger = daiquiri.getLogger(__name__)
        self.config = MyStation(config)
        self.tle_reader = ReadTle(config_dir)
        self.tle_reader.find_tle_files(config_dir)

    def secs_to_hms(self,seconds):
        hours=0
        mins=0
        secs=0
        seconds = int(seconds)
        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        mins = int(seconds / 60)
        seconds = seconds - mins * 60
        return f"{hours:02}:{mins:02}:{seconds:02}"

    def predict(self, days=2.0, max_passes=10) -> list :
        """

        :param max_passes:
        :param days:
        :return: List of Predictions
        """
        predictions=[]
        utc_now_seconds = float(datetime.now(tz=timezone('UTC')).timestamp())
        self.logger.info(f"Time now in UTC is {datetime.now(tz=timezone('UTC')).isoformat()}")
        self.logger.info(f"Checking for {self.config.Lat}N {self.config.Lon}E {self.config.Lat}m ")
        for sat in self.config.Sats:
            self.logger.debug(f"Checking for {sat}")
            sat, line1, line2 = self.tle_reader.find_sat(sat)
            pass_count = 0
            if sat:

                self.logger.debug(f"We have TLE for {sat}")
                tle = f"{sat}\n{line1}\n{line2}\n"
                predict.observe(tle, self.config.Qth)
                try:

                    p = predict.transits(tle, self.config.Qth, ending_after=utc_now_seconds - 900.0,
                                         ending_before=utc_now_seconds+days*24.0*3600.0)
                    passes = list(p)

                    for orbit in passes:
                        if orbit.peak()['elevation'] > self.config.MinAlt:
                            when = datetime.fromtimestamp(orbit.start)
                            #local_time = when.astimezone(timezone(self.config.TimeZone))
                            when_utc_str = when.strftime("%Y-%m-%d %H:%M:%S %Z%z")
                            delay_str  = self.secs_to_hms(orbit.start - utc_now_seconds)
                            self.logger.info(f"{sat} Delay: {delay_str} Start: {when_utc_str} Duration: {int(orbit.duration()):4} Max Ele: {int(orbit.peak()['elevation']):3} ")
                            predictions.append(Prediction(sat,delay_str,when_utc_str,int(orbit.duration()),int(orbit.peak()['elevation'])))
                            pass_count += 1
                            if pass_count >= max_passes:
                                self.logger.info(f"Max pass count of {max_passes} reached for {sat}")
                                break

                    self.logger.debug(f"We have {len(passes)} Passes for {sat}")
                except:
                    self.logger.warning(f"Count not calculate passes for {sat}")
        return predictions