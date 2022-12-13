"""
A high-level abstraction that allows you to easily manage json configuration files.
"""
import json

class ConfigFile():
	"""
	An object that represents a JSON configuration file.
	"""

	def __init__(self, path):
		"""
		Initializes a new ConfigFile object. Parameters:

		path: The path to the configuration file.
		"""

		self.path = path
		self.file = open(self.path, 'r')
		self.data = json.load(self.file)
		self.file.close()
	
	def get(self, key, reload=False):
		"""
		Gets a value from the configuration file. Parameters:

		key: The key to get the value of.
		reload: Whether or not to reload the configuration file before getting the value. Defaults to False.
		"""

		if reload:
			self.reload()
		return self.data[key]
	
	def set(self, key, value):
		"""
		Sets a value in the configuration file. Parameters:

		key: The key to set the value of.
		value: The value to set the key to.
		"""

		self.data[key] = value
		self.file = open(self.path, 'w')
		json.dump(self.data, self.file)
		self.file.close()

	def reload(self):
		"""
		Reloads the configuration file.
		"""

		self.file = open(self.path, 'r')
		self.data = json.load(self.file)
		self.file.close()

	def ensure(self, key, reload=False):
		"""
		Ensures that a key exists in the configuration file. Returns True if the key was created, False if it already existed. Parameters:

		key: The key to ensure.
		reload: Whether or not to reload the configuration file before checking for the key. Defaults to False.
		"""

		if reload:
			self.reload()

		if key in self.data:
			return False
		else:
			self.data[key] = None
			self.file = open(self.path, 'w')
			json.dump(self.data, self.file)
			self.file.close()
			return True

	def ensureList(self, keys, reload=False):
		"""
		Ensures that a list of keys exist in the configuration file. Returns a list of keys that were created. Parameters:

		keys: The keys to ensure.
		reload: Whether or not to reload the configuration file before checking for the keys. Defaults to False.
		"""

		created = []
		for key in keys:
			result = self.ensure(key, reload=reload)
			if result:
				created.append(key)
		return created

	def delete(self, key, reload=False):
		"""
		Deletes a key from the configuration file. Returns True if the key was deleted, False if it didn't exist. Parameters:

		key: The key to delete.
		reload: Whether or not to reload the configuration file before checking for the key. Defaults to False.
		"""

		if reload:
			self.reload()

		if key in self.data:
			del self.data[key]
			self.file = open(self.path, 'w')
			json.dump(self.data, self.file)
			self.file.close()
			return True
		else:
			return False

	def keys(self, reload=False):
		"""
		Returns a list of keys in the configuration file. Parameters:

		reload: Whether or not to reload the configuration file before getting the keys. Defaults to False.
		"""

		if reload:
			self.reload()
		return self.data.keys()

	def values(self, reload=False):
		"""
		Returns a list of values in the configuration file. Parameters:

		reload: Whether or not to reload the configuration file before getting the values. Defaults to False.
		"""

		if reload:
			self.reload()
		return self.data.values()

	def pairs(self, reload=False):
		"""
		Returns a list of key-value pairs in the configuration file. Parameters:

		reload: Whether or not to reload the configuration file before getting the pairs. Defaults to False.
		"""
	
		if reload:
			self.reload()
		return self.data.items()
	
	def truncate(self):
		"""
		Truncates the configuration file (creates an empty json object).
		"""

		self.file = open(self.path, 'w')
		self.file.truncate()
		self.file.write("{}")
		self.file.close()
		self.reload()
	
if __name__ == '__main__':
    print("This module is not meant to be run directly.")
    exit(1)