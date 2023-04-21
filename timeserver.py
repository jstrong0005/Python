#!/usr/bin/env python3

"""
Server for providing the day and time. Uses client handlers to handle clients request.
"""

from socket import *
from timeclienthandler import TimeClientHandler

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now waits for connections from clients and hands off sockets to the client handlers

while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("...connected from: ", address)
    handler = TimeClientHandler(client)
    handler.start()