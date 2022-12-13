# Betterlib Config

This module contains the `ConfigFile` class, which is a simple and easy to use abstraction for json configuration files.

## Usage

To use this module, simply import it and create a new `ConfigFile` object.

```py
from betterlib import config
conf = config.ConfigFile("./config.json")
```

Then, you can use the `conf` object to get and set values.

```py
# Get a value
print(conf.get("key"))
# Set a value
conf.set("key", "value")
# And get the new value
print(conf.get("key"))
# The file saves automatically, so next time around, the value you set will still be there.
```

## Methods

### Constructor

- `file` - The path to the config file.

### `get(key)`

Gets a value from the config file.

- `key` - The key of the value to get.

### `set(key, value)`

Sets a value in the config file.

- `key` - The key of the value to set.
- `value` - The value to set.

### `reload()`

Reloads the config file to ensure that the values are up to date.

### `ensure(key, reload=False)`

Ensures that a key exists in the config file. If it doesn't, it will be created with the default value of `None`.

- `key` - The key to ensure.
- `reload` - Whether or not to reload the config file before performing the action. Defaults to `False`.

### `ensureList(keys)`

Ensures that a list of keys exist in the config file. If they don't, they will be created with the default value of `None`.

- `keys` - A list of keys to ensure.
- `reload` - Whether or not to reload the config file before performing the action. Defaults to `False`.

### `delete(key, reload=False)`

Deletes a key and its respective value from the config file.

- `key` - The key to delete.
- `reload` - Whether or not to reload the config file before performing the action. Defaults to `False`.

### `keys(reload=False)`

Returns a list of all keys in the config file.

- `reload` - Whether or not to reload the config file before performing the action. Defaults to `False`.

### `values(reload=False)`

Returns a list of all values in the config file.

- `reload` - Whether or not to reload the config file before performing the action. Defaults to `False`.

### `pairs(reload=False)`

Returns a list of tuples representing all keys and values in the config file.

- `reload` - Whether or not to reload the config file before performing the action. Defaults to `False`.
