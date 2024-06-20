

'''
	from movies_ogv.activites.RSA.key_create import create_RSA_key
	gains = create_RSA_key ({
		"key_size": 2048,
		
		"write_keys": "yes",
		"write_keys_to_paths": {
			"RSA_private_key": "",
			"RSA_public_key": 	""
		}
	});
'''

'''
	@public
		@hot
	
	@private
		@cold
		@secret
		
	@inputs
		@from
		
	
	@outputs
		@to
'''

#/
#
import rsa
#
#
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode
#
#
import os
from os.path import dirname
#
#\

def write_RSA_private_key (
	RSA_private_key_path,
	RSA_private_key
):
	os.makedirs (dirname (RSA_private_key_path), exist_ok = True)

	with open (RSA_private_key_path, 'wb+') as f:
		binary_strand = rsa.PrivateKey.save_pkcs1 (RSA_private_key, format = 'PEM')
		f.write (binary_strand)
		
def write_RSA_public_key (
	RSA_public_key_path,
	RSA_public_key
):
	os.makedirs (dirname (RSA_public_key_path), exist_ok = True)
	
	with open (RSA_public_key_path, 'wb+') as f:
		binary_strand = rsa.PublicKey.save_pkcs1 (RSA_public_key, format = 'PEM')
		f.write (binary_strand)


def create_RSA_key (packet):
	key_size = packet ["key_size"]
	write_keys = packet ["write_keys"]
	write_keys_to_paths = packet ["write_keys_to_paths"]
	
	RSA_public_key, RSA_private_key = rsa.newkeys (key_size)
	
	if (write_outputs == "yes"):
		write_RSA_public_key (
			write_keys_to_paths ["RSA_public_key"],
			RSA_public_key
		)
		write_RSA_private_key (
			write_keys_to_paths ["RSA_private_key"],
			RSA_private_key
		)

	return {
		"RSA_public_key": RSA_public_key,
		"RSA_private_key": RSA_private_key
	}
	

