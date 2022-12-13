from betterlib.quik import *

server = QuikServer(8080)

def handler():
    return QuikResponse("Hello, world!", 200)
server.add_handler("/", handler)

server.start()