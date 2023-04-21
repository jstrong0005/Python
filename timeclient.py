#!/usr/bin/env python3

"""
Client for obtaining the day and time. Recovers from connection errors.
"""

from socket import *
from codecs import decode
HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

try:
    server = socket(AF_INET, SOCK_STREAM)   # Creates a socket
    server.connect(ADDRESS)                 # Connect it to a host
    dayAndTime = decode(server.recv(BUFSIZE), "ascii")  # Read a string from the server
    print(dayAndTime)
    server.close()
except ConnectionRefusedError:
    print("Error connecting to the server.")
