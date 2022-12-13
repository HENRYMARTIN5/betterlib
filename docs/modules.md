# Betterlib Modules

## [`betterlib.logging`](https://henrymartin5.github.io/betterlib/logging)

This module contains a collection of utilities for logging. It is a powerful system that fully implements the standards set forth by the Python logging library, but with a few extra features, such as the ability to log to a file and to the console with color output via `colorama`. This module is the most versitile of all of them, and is generally recommended for all projects.

Contained in this module are the following classes:

- `Logger` - A class that sort of implements the Python logging library's `Logger` class, but with a few extra features.

## [`betterlib.config`](https://henrymartin5.github.io/betterlib/config)

This module contains a high-level abstraction that allows you to easily manage json configuration files.

Contained in this module are the following classes:

- `ConfigFile` - A class that represents a json configuration file.

## [`betterlib.ip`](https://henrymartin5.github.io/betterlib/ip)

This module contains various utilities for working with IP and MAC addresses.

Contained in this module are the following functions:

- `getIp()`
- `getPubIp()`
- `getHostname()`
- `getMac()`
- `getMacVendor(address)`
- `getLatLong(ip=None)`
- `isBehindProxy()`
- `isVpn(ip)`
- `isTor(ip)`

## [`betterlib.quik`](https://henrymartin5.github.io/betterlib/quik)

This module contains the QuikServer class, which is a simple and easy to set up HTTP server that can be used to serve files or dynamically generated content.

Contained in this module are the following classes:

- `QuikServer` - The simple HTTP server.
- `QuikHandler` - The internal request handler for Python's built in `http.server`.
- `QuikResponse` - A class that represents an response to a request.

## [`betterlib.threader`](https://henrymartin5.github.io/betterlib/threader)

This module contains the Threader class, which is a simple and easy to use thread manager that can also be used to get the output of a function in a thread.

Contained in this module are the following classes:

- `Threader` - The thread manager.
- `BetterThread` - The internal thread class.