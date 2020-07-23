import logging
import daiquiri
import sys

def set_logging():
    format_str = "Sat %(asctime)-19s - Level %(levelname)-8s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter1 = logging.Formatter(format_str, date_format)
    daiquiri.setup(
        level=logging.DEBUG,
        outputs=(
            daiquiri.output.Stream(sys.stdout, formatter=formatter1),
            daiquiri.output.File(
                "./sat_log.log", formatter=formatter1
            ),
        ),
    )
    logger = daiquiri.getLogger()
    return logger
