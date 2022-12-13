from betterlib import ip, logging

logger = logging.Logger("./example.log", "ipinfoexample")

logger.info("Your public IP address is %s" % ip.getPubIp())
logger.info("Your private IP address is %s" % ip.getIp())
logger.info("Your hostname is %s" % ip.getHostname())
logger.info("Your MAC address is %s" % ip.getMac())
logger.info("Your approximate location is %s" % str(ip.getLatLong(ip.getPubIp())))
logger.info("Your MAC vendor is %s" % ip.getMacVendor(ip.getMac()))
logger.info("Behind proxy: %s" % ip.isBehindProxy())
logger.info("Behind tor: %s" % ip.isTor(ip.getPubIp()))
logger.info("Behind VPN: %s" % ip.isVpn(ip.getPubIp()))