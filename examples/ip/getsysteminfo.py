from betterlib import ip, logging

logger = logging.Logger("./example.log", "ipinfoexample")

myip = ip.ipAddress()
logger.info("Your public IP is: %s" % myip.address)
logger.info("Your IP is from: %s" % myip.country)
logger.info("Your IP is from: %s" % myip.city)
logger.info("Your IP is from: %s" % myip.region)
logger.info("Your ISP is: %s" % myip.isp)