

'''

	from movies_ogv.activities.fernet_1.crypt_decrypt import fernet_1_crypt_decrypt
	from movies_ogv.activities.fernet_1.read_key import read_fernet_1_key
	
	fernet_1_key = read_fernet_1_key ("");
	
	fernet_1_crypt_decrypt ({
		"fernet_1_key": fernet_1_key,
		
		"from_file": "region.HTML.fernet",
		"to_file": "region.HTML"
	})
'''



from movies_ogv.activities.FS.file.etch import etch_file
from movies_ogv.activities.FS.file.scan import scan_file

from cryptography.fernet import Fernet

def fernet_1_crypt_decrypt (packet):
	fernet_key = packet ["fernet_1_key"]
	
	from_file = packet ["from_file"]
	to_file = packet ["to_file"]
	
	strand = scan_file ({
		"path": from_file
	})
	
	decrypted_text = fernet_key.decrypt (strand)
	#decrypted_text = fernet_key.decrypt (strand).decode()

	etch_file ({
		"path": to_file,
		"strand": decrypted_text
	})
	
	return;