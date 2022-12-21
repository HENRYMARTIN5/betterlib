# Quik

This module contains the QuikServer class, which is a simple and easy to set up HTTP server that can be used to serve files or dynamically generated content.

## QuikServer

The QuikServer class is a simple HTTP server that can be used to serve files or dynamically generated content. It allows for simple set-up of the complex systems set in place by Python's `http.server` in all but a few lines of code.

### Constructor

The constructor for the QuikServer class takes the following arguments:

- `host` - The host to bind to. Defaults to `localhost`.
- `port` - The port to bind to. Defaults to `80`.
- `logger` - A `logging.Logger` object to use for logging. Defaults to `None`, causing subsequent logging to be piped to a standard `print` instead.

### Methods

The QuikServer class has the following methods:

- `start()` - Starts the server. Loops indefinitely until a keyboard interrupt is received.
- `add_handler()` - Adds a handler to the server. See the section on handlers for more information.

### Handlers

Handlers are functions that are called when a request is received by the server. They are triggered on specific paths and can be set to recieve only certain request methods. They return a `QuikResponse` object, which takes the default parameters of the response content and the status code. Handlers are added to the server using the `add_handler()` method.

For instance:

```py
def handler():
    return QuikResponse("Hello, world!", 200)
server.add_handler("/", handler) # Assuming server is an instance of QuikServer
```

This will add a handler that will be called when a request is made to the root path (`/`) and will return a response with the content "Hello, world!" and a status code of 200.

Handlers can also be set to only be called on certain request methods. For instance:

```py
def handler():
    return QuikResponse("Hello, world!", 200)
server.add_handler("/", handler, methods=["GET"]) # Once again, assuming server is an instance of QuikServer
```

This will only be called if the request method is `GET`. If the request method is not `GET`, the handler will not be called and the server will return a 405 error.

In order to recieve a request body, the handler must take a parameter called `body`. If one is not specified and the request method is `POST`, the server will return a 500 error.

Example:

```py
def handler(body=None):
    return QuikResponse(body, 200)
server.add_handler("/", handler, methods=["POST"])
```

## QuikResponse

The QuikResponse class is a simple class that represents a response to a request. It takes the following arguments:

- `content` - The content of the response. Defaults to an empty string.
- `code` - The status code of the response. Defaults to 200.
- `content_type` - The content type of the response. Defaults to `text/html`.
- `encoding` - The encoding of the response. Defaults to `utf-8`.
