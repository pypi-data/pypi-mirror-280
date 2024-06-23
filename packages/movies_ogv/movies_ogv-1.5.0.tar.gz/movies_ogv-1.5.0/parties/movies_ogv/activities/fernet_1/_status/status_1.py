
'''
	python3 status.proc.py
'''

#/
#
from cryptography.fernet import Fernet
#
#
from movies_ogv.activities.fernet_1.crypt_encrypt import fernet_1_crypt_encrypt
from movies_ogv.activities.fernet_1.crypt_decrypt import fernet_1_crypt_decrypt
from movies_ogv.activities.fernet_1.key_produce import produce_fernet_1_key
from movies_ogv.activities.FS.file.scan import scan_file
from movies_ogv.activities.FS.file.delete_abandon import delete_abandon_file
from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
	
#
#
from os.path import dirname, join, normpath
import pathlib
import sys
#
#\

this_folder = pathlib.Path (__file__).parent.resolve ()
original_file = str (normpath (join (this_folder, "constants/strand.HTML")))
encrypted_file = str (normpath (join (this_folder, "variance/strand.HTML.fernet_1")))
decrypted_file = str (normpath (join (this_folder, "variance/strand.HTML")))
fernet_key_path = str (normpath (join (this_folder, "variance/fernet_key_path.JSON")))

def abandon_attempt (file_path):
	try:
		delete_abandon_file (file_path)
	except Exception:
		pass;

def check_1 ():
	abandon_attempt (encrypted_file)
	abandon_attempt (decrypted_file)
	abandon_attempt (fernet_key_path)

	produce_fernet_1_key ({
		"write_outputs": "yes",
		"outputs": {
			"fernet_key_path": fernet_key_path
		}
	});
	
	fernet_1_key = scan_fernet_1_key (fernet_key_path);

	fernet_1_crypt_encrypt ({
		"fernet_1_key": fernet_1_key,
		
		"from_file": original_file,
		"to_file": encrypted_file
	})

	fernet_1_crypt_decrypt ({
		"fernet_1_key": fernet_1_key,
		
		"from_file": encrypted_file,
		"to_file": decrypted_file
	})


	original = scan_file ({
		"path": original_file
	})
		
	decrypted = scan_file ({
		"path": decrypted_file
	})

	assert (original == decrypted)
	
	delete_abandon_file (encrypted_file)
	delete_abandon_file (decrypted_file)
	delete_abandon_file (fernet_key_path)
	
checks = {
	'fernet check 1': check_1
}