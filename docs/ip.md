# IP

This module contains the `ipAdress` class, a class that represents an IP address and its various properties.

## Disclaimer

By using this module, you agree to the terms of service of the [ip-api](https://ip-api.com/) API.

## Usage

To use the `ipAddress` class, import it and create a new `ipAddress` object. By default, if no IP address is passed, it will fetch and use your public IP.

```py
from betterlib import ip

myip = ip.ipAddress()
```

Then, you can use the `myip` object to get various properties of the IP address.

```py
print(myip.address) # Your public IP
print(myip.continent) # e.g. "North America"
print(myip.country) # e.g. "United States"
print(myip.reigonName) # e.g. "California"
```

To see a full list of supported attributes, check the section below.

## Methods

### Constructor

- `address=None` - The IP address to use. Defaults to your public IP.
  
## Attributes

- `address` - The IP address that was passed to the constructor. If none was provided, this will be your public IP.
- `status` - The status of the API request. If the request was successful, the value will be `success`.
- `continent` - The continent that the IP address is located in. E.g. "North America".
- `continentCode` - The code that represents the continent that the IP address is located in. E.g. "NA" (North America)
- `country` - The country that the IP address is located in. E.g. "United States".
- `countryCode` - The country code that represents the country that the IP address is located in. E.g. "US" (United States).
- `region` - The region that the IP address is located in. E.g. "CA".
- `regionName` - The name of said region. E.g "California".
- `city` - The city where the IP is located. E.g "Los Angeles".
- `district` - The district/subset of the city where the IP is. E.g. "Los Angeles County".
- `zip` - The zip code of the IP address. E.g. "90001".
- `lat` - The approximate latitude of the IP.
- `lon` - The approximate longitude of the IP.
- `timezone` - The timezone of the IP address. E.g. "America/Los_Angeles".
- `offset` - The timezone UTC DST offset in seconds.
- `currency` - The currency used where the IP is located. E.g. "USD" or "EUR".
- `isp` - The IP's ISP (internet service provider).
- `org` - The IP's organization name.
- `asname` - The IP's AS number and organization, separated by space (RIR). Empty for IP blocks not being announced in BGP tables.
- `reverse` - Reverse DNS of the IP.
- `mobile` - True if the IP is a mobile connection, false otherwise.
- `proxy` - Whether or not the IP is a proxy, VPN, or Tor exit address.
- `hosting` - The IP's hosting, colocated or data center.
- `query` - The IP used to make the query to the API.