"""
The QuikServer class is a simple HTTP server that can be used to serve files and dynamically generated content.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

QUIKVERSION = "0.2a"

handlers = {}
allowed_methods = {}

class QuikServer():
	"""
	A simple HTTP server that can be used to serve files and dynamically generated content.
	"""
	
	def __init__(self, port, host="127.0.0.1"):
		"""
		Initializes a new QuikServer object. Parameters:
		
		port: The port to listen on.
		host: The host to listen on. Defaults to "127.0.0.1" aka localhost.
		"""

		self.port = port
		self.host = host
	
	def add_handler(self, path, handler, methods=["GET"]):
		"""
		Adds a handler to the server. Parameters:
		
		path: The path to handle.
		handler: The handler function.
		"""

		handlers[path] = handler
		allowed_methods[path] = methods

	def start(self):
		with HTTPServer((self.host, self.port), QuikHandler) as httpd:

			print("Quik is up and running on http://%s:%s" % (self.host, self.port))
			try:
				httpd.serve_forever()
			except KeyboardInterrupt:
				pass


class QuikHandler(BaseHTTPRequestHandler):
	"""
	A handler for the socketserver.TCPServer class.
	"""

	# The following functions are super redundant, but I'm not sure how to make them more efficient.
	def do_GET(self):
		"""
		Handles GET requests.
		"""

		if self.path in handlers:
			if "GET" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))

	def do_POST(self):
		"""
		Handles POST requests.
		"""

		if self.path in handlers:
			if "POST" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_HEAD(self):
		"""
		Handles HEAD requests.
		"""

		if self.path in handlers:
			if "HEAD" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_PUT(self):
		"""
		Handles PUT requests.
		"""
		
		if self.path in handlers:
			if "PUT" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_DELETE(self):
		"""
		Handles DELETE requests.
		"""

		if self.path in handlers:
			if "DELETE" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_CONNECT(self):
		"""
		Handles CONNECT requests.
		"""

		if self.path in handlers:
			if "CONNECT" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_OPTIONS(self):
		"""
		Handles OPTIONS requests.
		"""

		if self.path in handlers:
			if "OPTIONS" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_TRACE(self):
		"""
		Handles TRACE requests.
		"""

		if self.path in handlers:
			if "TRACE" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	
	def do_PATCH(self):
		"""
		Handles PATCH requests.
		"""

		if self.path in handlers:
			if "PATCH" not in allowed_methods[self.path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
	


class QuikResponse():
	"""
	A response object that can be returned by a handler.
	"""


	def __init__(self, content, code, content_type="text/html", encoding="utf-8"):
		"""
		Initializes a new QuikResponse object. Parameters:
		
		code: The HTTP status code to send.
		content: The content to send.
		"""

		self.code = code
		self.content = content
		self.content_type = content_type
		self.encoding = encoding