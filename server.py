#!/usr/bin/python2

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main() :

	# dummy authorizer for managing users
	authorizer = DummyAuthorizer()

	# new user with full permissions
	authorizer.add_user('admin','password123','files/',perm='elradfmwMT')

	# anonymous user
	authorizer.add_anonymous(os.getcwd() + '/files')

	# FTP handler
	handler = FTPHandler
	handler.authorizer = authorizer

	# Welcome string when client connects
	handler.banner = "FTP Server ready"

	# listen address port > 1024 (otherwise use sudo)
	address = ('127.0.0.1',2121)
	server = FTPServer(address, handler)

	# limits for connections
	server.max_cons = 256
	server.max_cons_per_ip = 5

	# start ftp server
	server.serve_forever()

if __name__ == '__main__' :
	main()