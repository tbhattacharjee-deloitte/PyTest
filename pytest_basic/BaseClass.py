import inspect
import logging


class BaseClass:
    def get_logger(self):
        testName = inspect.stack()[1][3]
        file_handler = logging.FileHandler("logfile.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s"))

        logger = logging.getLogger(testName)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
