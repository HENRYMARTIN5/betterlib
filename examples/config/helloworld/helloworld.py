from betterlib import config, logging

logger = logging.Logger("helloworld.log", "configexample")
conf = config.ConfigFile("config.json")

logger.info("Ensuring that the config file has the correct values...")

conf.ensureList(["value1", "value2", "value3"])

logger.info(conf.get("value1") + conf.get("value2") + conf.get("value3"))