#! /usr/bin/python

import os.path
import argparse
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

FTP_ROOT = '/ftp_server'
USER='jetson'
PASSWORD='marvik@1234'
HOST='0.0.0.0'
PORT='21'

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    user_dir = os.path.join(FTP_ROOT, USER)
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    authorizer.add_user(USER, PASSWORD, user_dir, perm="elradfmw")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.permit_foreign_addresses = True
    handler.passive_ports = range(30000,30010)

    #Logging managment
    logging.basicConfig(filename='/var/log/pyftpd.log', level=logging.INFO)

    # Instantiate FTP server class and listen on HOST:PORT
    server = FTPServer((HOST, PORT), handler)

    # set a limit for connections
    server.max_cons = 256 
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()