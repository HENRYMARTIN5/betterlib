# Betterlib Logging

This module contains the `Logger` class, which is a simple and easy to use logging class that can be used to log messages to a file and to the terminal with color via `colorama`.

## Usage

To use this module, simply import it and create a new `Logger` object.

```py
from betterlib import logging

logger = logging.Logger("./myapp.log", "MyApp")
```

Then, you can use the `logger` object to log messages.

```py
logger.info("Hello, world!")
```

## Methods

### Constructor

- `file` - The path to the log file.
- `name` - The name of the logger.
- `use_colorama` - Whether or not to use colorama to color the output. Defaults to `True`.

### `close()`

Closes the logger and sets the `active` property to `False`.

### `reopen()`

Reopens the logger and sets the `active` property to `True`.

### `log(message, level="INFO")`

Logs a message to the log file and to the console.

- `message` - The message to log.
- `level` - The level of the message. Defaults to `INFO`.

### `reloadFile()`

Reloads the log file. (Internaly used.)

### `info(message)`

Logs a message with the INFO level.

- `message` - The message to log.

### `warn(message)`

Logs a message with the WARN level.

- `message` - The message to log.

### `error(message)`

Logs a message with the ERROR level.

- `message` - The message to log.

### `critical(message)`

Logs a message with the CRITICAL level.

- `message` - The message to log.

### `debug(message)`

Logs a message with the DEBUG level.

- `message` - The message to log.
