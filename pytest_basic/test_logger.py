import logging


def test_logger():
    file_handler = logging.FileHandler("logfile.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s"))

    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    logger.debug("Debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

