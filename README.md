# BetterLib

BetterLib is a useful collection of utilities for Python developers to use in their projects. It is licensed under the Unlicense, so you can use it in any project, commercial or otherwise, without any restrictions whatsoever. (Yes, that means you can steal it and pass it off as your own. I won't judge.)

## Installation

BetterLib is available on PyPI, so you can install it with pip:

```sh
pip install betterlib
```

## Usage

BetterLib is split into several modules, each of which contains a collection of related utilities. You can import the entire library, or just the modules you need.

```py
# Import the entire library...
import betterlib
# or import just the modules you need.
from betterlib import logging, config, ip...
```

## Modules

### `betterlib.logging`

This module contains a collection of utilities for logging. It is a powerful system that fully implements the standards set forth by the Python logging library, but with a few extra features, such as the ability to log to a file and to the console with color output via `colorama`. This module is the most versitile of all of them, and is generally recommended for all projects.

### `betterlib.config`

This module contains a high-level abstraction that allows you to easily manage json configuration files.

### `betterlib.ip`

This module contains various utilities for working with IP and MAC addresses.

### `betterlib.quik`

This module contains the QuikServer class, which is a simple and easy to set up HTTP server that can be used to serve files or dynamically generated content.