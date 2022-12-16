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

	def handle_quik_request(self, path, method):
		if path in handlers:
			if method not in allowed_methods[path]:
				self.send_response(405)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes("405 Method Not Allowed<br>Betterlib Quik " + QUIKVERSION, "utf-8"))
				return

			response = handlers[path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("404 Not Found<br>Betterlib Quik " + QUIKVERSION, "utf-8"))

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

		self.handle_quik_request(self.path, "POST")
	
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

if __name__ == "__main__":
	# This is just a test server.
	server = QuikServer(8080)

	def handler():
		return QuikResponse("Hello, world!", 200)
	server.add_handler("/", handler)

	server.start()