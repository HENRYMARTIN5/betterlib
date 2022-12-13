from betterlib import logging

logger = logging.Logger("./example.log", "hellologgerexample")

logger.info("Hello, world!")
logger.info("Info")
logger.warn("Warning")
logger.error("Error")
logger.critical("Critical")
logger.debug("Debug")