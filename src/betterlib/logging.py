"""
A simple but powerful logging class that outputs to the console (with color!) and to a file in realtime.
"""
import datetime, os
from colorama import Fore, Style, init


class Logger():
	"""
	The Logger class is a simple but powerful logging class that outputs to the console (with color!) and to a file in realtime.
	"""
	def __init__(self, log_file, name, use_colorama=True):
		"""
		Initializes a new Logger object. Parameters:

		log_file: The file to log to. If the directory doesn't exist, it will be created.
		name: The name of the logger. This will be displayed in the console and in the log file.
		use_colorama: Whether or not to use colorama to color the console output. Defaults to True.
		"""
		if use_colorama:
			init()
			
		self.config = {
			"logfilelevel": "debug",
			"consolelevel": "info",
			"file": log_file,
			"infileformat": "[%(name)s] [%(level)s] %(asctime)s: %(message)s",
			"consoleformat": "[%(name)s] [%(level)s] %(message)s",
			"validlevels": ["debug", "info", "warn", "error", "critical"],
			"colors": ["blue", "white", "orange", "red", "boldred"],
			"name": name,
			"usecolorama": use_colorama
		}

		self.colorkey = {
			"white": Style.RESET_ALL,
			"blue": Fore.BLUE,
			"orange": Fore.YELLOW,
			"red": Fore.RED,
			"boldred": Fore.RED + Style.BRIGHT
		}

		# Check if the directory exists
		if not os.path.exists(os.path.dirname(self.config.get("file"))):
			print("Creating directory " + self.config.get("file") + "...")
			os.makedirs(os.path.dirname(self.config.get("file")))

		# Open the file, overwrite any contents, then close it and reopen it in append mode
		self.log_file = self.config.get("file")
		self.file = open(self.log_file, 'w')
		self.file.truncate()
		self.file.close()
		self.file = open(self.log_file, 'a')
		self.file.write("Log file created at " + str(datetime.datetime.now()) + "\n")

		self.active = True

	def close(self):
		"""
		Closes the log file and sets the logger to inactive mode. In this state, the logger will not actually log anything.
		"""

		self.file.close()
		self.active = False

	def reopen(self):
		"""
		Reopens the log file and sets the logger to active mode.
		"""

		self.file = open(self.log_file, 'a')
		self.active = True
	
	def log(self, message, level="info"):
		"""
		Logs a message to the console and to the log file. Parameters:

		message: The message to log.
		level: The level of the message. Defaults to "info". Valid levels (by default, can be changed in the config) are "debug", "info", "warn", "error", and "critical". (Note: "debug" is the lowest level, "critical" is the highest level.
		"""

		if level not in self.config.get("validlevels"):
			level = "info"
		
		if self.active:
			# Use console level to determine if we should log to console
			levelindex = self.config.get("validlevels").index(level)
			consolelevelindex = self.config.get("validlevels").index(self.config.get("consolelevel"))
			logfilelevelindex = self.config.get("validlevels").index(self.config.get("logfilelevel"))
			if levelindex >= consolelevelindex:
				if self.config.get("usecolorama"):
					print(
						self.colorkey.get(self.config.get("colors")[levelindex]) +
						self.config.get("consoleformat").replace("%(name)s", self.config.get("name")).replace("%(level)s", level.upper()).replace("%(message)s", message)
						+ Style.RESET_ALL
					)
				else:
					print (
						self.config.get("consoleformat").replace("%(name)s", self.config.get("name")).replace("%(level)s", level.upper()).replace("%(message)s", message)
					)
			if levelindex >= logfilelevelindex:
				self.file.write(
					self.config.get("infileformat").replace("%(name)s", self.config.get("name")).replace("%(level)s", level.upper()).replace("%(asctime)s", str(datetime.datetime.now())).replace("%(message)s", message) + "\n"
				)
			
			self.reloadfile()
		else:
			return False

	def reloadfile(self):
		"""
		Closes and reopens the log file to make sure the logger is writing to the latest version.
		"""
		# Close and reopen the file to make sure we're writing to the latest version
		self.close()
		self.reopen()

	def info(self, message):
		"""
		A shortcut for self.log(message, level="info")
		"""

		self.log(message, level="info")
	
	def warn(self, message):
		"""
		A shortcut for self.log(message, level="warn")
		"""

		self.log(message, level="warn")
	
	def error(self, message):
		"""
		A shortcut for self.log(message, level="error")
		"""	

		self.log(message, level="error")
	
	def critical(self, message):
		"""
		A shortcut for self.log(message, level="critical")
		"""

		self.log(message, level="critical")

	def debug(self, message):
		"""
		A shortcut for self.log(message, level="debug")
		"""

		self.log(message, level="debug")

if __name__ == '__main__':
    print("This module is not meant to be run directly.")
    exit(1)