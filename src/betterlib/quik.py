"""
The QuikServer class is a simple HTTP server that can be used to serve files and dynamically generated content.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs

QUIKVERSION = "0.2a"

handlers = {}
allowed_methods = {}
error_handlers = {}

class QuikServer():
	"""
	A simple HTTP server that can be used to serve files and dynamically generated content.
	"""
	
	def __init__(self, port, host="127.0.0.1", logger=None):
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

		if path in handlers:
			raise Exception("Cannot add handler for path %s, it already exists!")
		handlers[path] = handler
		allowed_methods[path] = methods

	def add_error_handler(self, code, handler):
		"""
		Adds an error handler to the server. Parameters:

		code: The error code to handle.
		handler: The handler function.
		"""

		if code in error_handlers:
			raise Exception("Cannot add error handler for status code %s, it already exists!")
		error_handlers[code] = handler

	def start(self):
		"""
		Starts the server.
		"""

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

	def send_from_quikresponse(self, response):
		"""
		Sends a response from a QuikResponse object. Parameters:

		response: The QuikResponse object.
		"""

		self.send_response(response.code)
		self.send_header("Content-type", response.content_type)
		for header, value in response.headers:
			self.send_header(header, value)
		for cookie, value in response.cookies:
			self.send_header("Set-Cookie", cookie + "=" + value) # Header format is cookie=value
		for cookie in response.delete_cookies:
			self.send_header("Set-Cookie", cookie + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT") # Hacky way to delete, but hey, it works.
		self.end_headers()
		self.wfile.write(bytes(response.content, response.encoding))

	def send_from_string(self, string, encoding="utf-8", code=200, content_type="text/html"):
		"""
		Sends a response from a string. Status code is 200 by default. Parameters:

		string: The string to send.
		"""

		self.send_response(code)
		self.send_header("Content-type", content_type)
		self.end_headers()
		self.wfile.write(bytes(string, encoding))

	def handle_quik_request(self, path, method, body=None):
		global error_handlers

		"""
		Handles a Quik request. Internally used, don't touch. Parameters:

		path: The path to handle.
		method: The method to handle.
		"""

		try:
			if path in handlers:
				if method not in allowed_methods[path]:
					if not 405 in error_handlers:
						self.send_from_string("405 Method Not Allowed. You really couldn't help pentesting this site, could you?<br>Betterlib Quik " + QUIKVERSION, code=405)
						return 405
					else:
						response = error_handlers[405]()
						self.send_from_quikresponse(response)
						return 405

				if body is None:
					response = handlers[path](body=None) # The tiny little bit of logic that actually sends a valid request.
				else:
					response = handlers[path](body=body)
				self.send_from_quikresponse(response)
				return 200

			else:
				if not 404 in error_handlers:
					self.send_from_string("404 not found. Use a real URL next time.<br>Betterlib Quik " + QUIKVERSION, code=405)
					return 404
				else:
					response = error_handlers[404]()
					self.send_from_quikresponse(response)
					return 404
		except Exception as e:
			print(e)
			if not 500 in error_handlers:
				self.send_from_string("500 internal server error. Nice job, you broke something!<br>Betterlib Quik " + QUIKVERSION, code=405)
				return 500
			else:
				response = error_handlers[500]()
				self.send_from_quikresponse(response)
				return 500

	# The following functions are super redundant, but I'm not sure how to make them more efficient.
	def do_GET(self):
		"""
		Handles GET requests.
		"""

		self.handle_quik_request(self.path, "GET")

	def do_POST(self):
		"""
		Handles POST requests.
		"""

		# Currently, the only supported request type for a request body is POST. More to come soon.

		# Get request body and decode it.
		content_length = int(self.headers['Content-Length'])
		unparsed_body = self.rfile.read(content_length).decode("utf-8") # TODO: Make this encoding configurable.
		# Get the content type and parse it if neccecary.
		content_type = self.headers['Content-Type']
		if content_type == "application/x-www-form-urlencoded":
			# Parse it just like a query string.
			body = parse_qs(body)
		elif content_type == "application/json":
			# Parse it as JSON.
			body = json.loads(body)
		else:
			body = unparsed_body

		self.handle_quik_request(self.path, "POST", body=body)
	
	def do_HEAD(self):
		"""
		Handles HEAD requests.
		"""

		self.handle_quik_request(self.path, "HEAD")
	
	def do_PUT(self):
		"""
		Handles PUT requests.
		"""
		
		self.handle_quik_request(self.path, "PUT")
	
	def do_DELETE(self):
		"""
		Handles DELETE requests.
		"""

		self.handle_quik_request(self.path, "DELETE")
	
	def do_CONNECT(self):
		"""
		Handles CONNECT requests.
		"""

		self.handle_quik_request(self.path, "CONNECT")
	
	def do_OPTIONS(self):
		"""
		Handles OPTIONS requests.
		"""

		self.handle_quik_request(self.path, "OPTIONS")
	
	def do_TRACE(self):
		"""
		Handles TRACE requests.
		"""

		self.handle_quik_request(self.path, "TRACE")
	
	def do_PATCH(self):
		"""
		Handles PATCH requests.
		"""

		self.handle_quik_request(self.path, "PATCH")
	

class QuikResponse():
	"""
	A response object that can be returned by a handler.
	"""


	def __init__(self, content, code, content_type="text/html", encoding="utf-8", headers={}, cookies={}, delete_cookies=[]):
		"""
		Initializes a new QuikResponse object. Parameters:
		
		code: The HTTP status code to send.
		content: The content to send.
		"""

		self.code = code
		self.content = content
		self.content_type = content_type
		self.encoding = encoding
		self.headers = headers
		self.cookies = cookies
		self.delete_cookies = delete_cookies

if __name__ == "__main__":
	"""
	Runs a test server if this file is run directly.
	"""

	print("Running test server. Press Ctrl+C to stop.")
	server = QuikServer(8080)

	def test(body=None):
		return QuikResponse("Hello, world!", 200)
	server.add_handler("/", test)

	server.start()