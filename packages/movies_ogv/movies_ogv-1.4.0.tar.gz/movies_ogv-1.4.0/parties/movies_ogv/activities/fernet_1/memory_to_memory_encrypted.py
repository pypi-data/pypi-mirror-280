

'''
	buffer = io.BytesIO ();

	from movies_ogv.activities.fernet_1.memory_to_memory_encrypted import memory_to_memory_encrypted
	from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
	
	fernet_1_key = read_fernet_1_key ("");
	
	fernet_1_crypt_encrypt ({
		"fernet_1_key": fernet_1_key,
		"bytes_io": buffer
	})
'''



from movies_ogv.activities.FS.file.etch import etch_file
from movies_ogv.activities.FS.file.scan import scan_file

from cryptography.fernet import Fernet

import io

def memory_to_memory_encrypted (packet):
	fernet_key = packet ["fernet_1_key"]
	bytes_io = packet ["bytes_io"]
	
	plaintext_data = bytes_io.read ()
	encrypted = fernet_key.encrypt (plaintext_data)
	
	return encrypted