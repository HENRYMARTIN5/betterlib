"""
The QuikServer class is a simple HTTP server that can be used to serve files and dynamically generated content.
"""
import http.server
import socketserver

handlers = {}

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
	
	def add_handler(self, path, handler):
		"""
		Adds a handler to the server. Parameters:
		
		path: The path to handle.
		handler: The handler function.
		"""

		handlers[path] = handler

	def start(self):
		with socketserver.TCPServer((self.host, self.port), QuikHandler) as httpd:
			print("QuikServer up and running on http://" + self.host + ":" + str(self.port) + "/")
			httpd.serve_forever()


class QuikHandler(http.server.SimpleHTTPRequestHandler):
	"""
	A handler for the socketserver.TCPServer class.
	"""
	def do_GET(self):
		"""
		Handles GET requests.
		"""
		global handlers
		if self.path in handlers:
			response = handlers[self.path]()
			self.send_response(response.code)
			self.send_header("Content-type", response.content_type)
			self.send_header("Content-length", len(response.content))
			for header in response.headers:
				self.send_header(header, response.headers[header])
			self.end_headers()
			self.wfile.write(bytes(response.content, response.encoding))
		else:
			return http.server.SimpleHTTPRequestHandler.do_GET(self)

class QuikResponse():
	"""
	A response object that can be returned by a handler.
	"""

	def __init__(self, code, content, headers={}, content_type="text/html", encoding="utf-8", version="HTTP/1.1", status="OK"):
		"""
		Initializes a new QuikResponse object. Parameters:
		
		code: The HTTP status code to send.
		content: The content to send.
		"""

		self.code = code
		self.content = content
		self.headers = headers
		self.content_type = content_type
		self.encoding = encoding
		self.version = version
		self.status = status