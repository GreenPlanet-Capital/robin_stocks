"""Holds the session header and other global variables."""

import sys
import os
import socket
from urllib3.connection import HTTPConnection

from requests import Session

# Keeps track on if the user is logged in or not.
LOGGED_IN = False
# The session object for making get and post requests.
SESSION = Session()
SESSION.headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US,en;q=1",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "X-Robinhood-API-Version": "1.431.4",
    "Connection": "keep-alive",
    "User-Agent": "*",
}

# FIXME: this is a possible fix for "Remote end closed connection without response" issue
HTTPConnection.default_socket_options = HTTPConnection.default_socket_options + [
    (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
    (socket.SOL_TCP, socket.TCP_KEEPIDLE, 45),
    (socket.SOL_TCP, socket.TCP_KEEPINTVL, 10),
    (socket.SOL_TCP, socket.TCP_KEEPCNT, 6),
]

# All print() statement direct their output to this stream
# by default, we use stdout which is the existing behavior
# but a client can change to any normal Python stream that
# print() accepts.  Common options are
# sys.stderr for standard error
# open(os.devnull,"w") for dev null
# io.StringIO() to go to a string for the client to inspect
OUTPUT = sys.stdout
