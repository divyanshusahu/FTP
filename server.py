#!/usr/bin/python2

import os, sys
import logging
from hashlib import sha256

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class DummySHA256Authorizer(DummyAuthorizer) :

	def validate_authentication(self, username, password, handler) :
		hash = sha256(password).hexdigest()

		try :
			if self.user_table[username]['pwd'] != hash :
				raise KeyError
		except KeyError :
			raise AuthenticationFailed

class CustomHandler(FTPHandler) :
	
	def on_connect(self) :
		print "%s:%s" % (self.remote_ip, self.remote_port)

	def on_dissconnect(self) :
		pass

	def on_login(self, username) :
		pass

	def on_logout(self, username) :
		pass

	def on_file_received(self, file) :
		pass

	def on_incomplete_file_sent(self, file) :
		pass

	def on_incomplete_file_received(self, file) :
		os.remove(file)

def main() :

	hash_password = sha256('password123').hexdigest()

	# dummy authorizer for managing users
	authorizer = DummyAuthorizer()

	# new user with full permissions
	authorizer.add_user('admin', 'password123', os.getcwd() + '/files',perm='elradfmwMT')

	# anonymous user
	authorizer.add_anonymous(os.getcwd() + '/files')

	# FTP handler
	handler = CustomHandler
	handler.authorizer = authorizer

	# server logging
	logging.basicConfig(filename = 'log_server.log', level=logging.INFO)

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