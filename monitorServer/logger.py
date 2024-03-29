# encoding: utf-8

from loguru import logger as log



import time
from loguru import logger
from pathlib import Path

project_path = Path.cwd().parent
log_path = Path(project_path, "log")
t = time.strftime("%Y_%m_%d")


class Loggings:
    __instance = None
    logger.add(
        f"log.log",
        rotation="500MB",
        encoding="utf-8",
        enqueue=True,
        retention="10 days",
        level='INFO',
        # format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {filename}|  {lineno}| {message}"
    )

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)

    def exception(self, message):
        return logger.exception(message)


log = Loggings()

if __name__ == '__main__':
    log.info('info message')
    log.warning('warn message')
    log.error('log message')









