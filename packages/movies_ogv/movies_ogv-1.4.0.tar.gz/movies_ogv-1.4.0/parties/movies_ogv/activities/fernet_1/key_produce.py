







'''
	from movies_ogv.activities.fernet_1.key_produce import produce_fernet_1_key

	fernet_key = produce_fernet_1_key ({
		"write_outputs": "yes",
		"outputs": {
			"fernet_key_path": ""
		}
	});
'''

''''
	@keys
		@enzymes
"'''

import rsa
import json

from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import os
from os.path import dirname

def generate_fernet_key_01 ():
	password = "password".encode ()

	#
	#	maybe this is like a key from os.urandom (16) 
	#
	salt = b'salt_'

	kdf = PBKDF2HMAC (
		algorithm		=	hashes.SHA256 (),
		length			=	32,
		salt			=	salt,
		iterations		=	100000,
		backend			=	default_backend ()
	)

	key = base64.urlsafe_b64encode (kdf.derive (password)) 
	
	return key;
	
# option 2
def generate_fernet_key_02 (): 
	return Fernet.generate_key ()


def produce_fernet_1_key (packet):
	write_outputs = packet ["write_outputs"]
	outputs = packet ["outputs"]


	#fernet_key = generate_fernet_key_01 ()
	fernet_key = generate_fernet_key_02 ()

	if (write_outputs == "yes"):
		os.makedirs (dirname (outputs ["fernet_key_path"]), exist_ok = True)
		
		with open (outputs ["fernet_key_path"], 'w') as FP:
			os.chmod (outputs ["fernet_key_path"], 0o777)
			FP.write (json.dumps ({
				"fernet_key": fernet_key.hex ()
			}, indent = 4))
	
	return Fernet (fernet_key)