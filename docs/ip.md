# Betterlib IP

This module contains various utilities for working with IP and MAC addresses.

## Functions

### `getIp()`

Gets the local IP address of the computer.

### `getPubIp()`

Gets the public IP address of the computer.

### `getHostname()`

Gets the hostname of the computer.

### `getMac()`

Gets the MAC address of the computer.

### `getMacVendor(address)`

Gets the vendor of the given MAC address.

### `getLatLong(ip=None)`

Returns a tuple containing the approximate location of the given IP address, if one is passed. Otherwise, it returns the location of the current public IP address.

### `isBehindProxy()`

Returns `True` if the computer is behind a proxy, `False` or `None` otherwise.

### `isVpn(ip)`

Returns `True` if the given IP is behind a VPN, `False` or `None` otherwise.

### `isTor(ip)`

Returns `True` if the given IP is behind Tor, `False` or `None` otherwise.
