#!/usr/bin/env python3

"""
Client handler for providing the day and time
"""

from time import ctime
from threading import Thread
from codecs import decode

class TimeClientHandler(Thread):
    """Handles a clients requests."""
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.send(bytes(ctime() + "\nAll your base are belong to us! Have a nice day, Shane!", "ascii"))

        self.client.close()