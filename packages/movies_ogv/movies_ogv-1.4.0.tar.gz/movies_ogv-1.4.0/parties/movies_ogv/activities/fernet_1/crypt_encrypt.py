

'''

	from movies_ogv.activities.fernet_1.crypt_encrypt import fernet_1_crypt_encrypt
	from movies_ogv.activities.fernet_1.read_key import read_fernet_1_key
	
	fernet_1_key = read_fernet_1_key ("");
	
	fernet_1_crypt_encrypt ({
		"fernet_1_key": fernet_1_key,
		
		"from_file": "region.HTML",
		"to_file": "region.HTML.fernet"
	})
'''



from movies_ogv.activities.FS.file.etch import etch_file
from movies_ogv.activities.FS.file.scan import scan_file

from cryptography.fernet import Fernet

def fernet_1_crypt_encrypt (packet):
	fernet_key = packet ["fernet_1_key"]
	
	from_file = packet ["from_file"]
	to_file = packet ["to_file"]
	
	strand = scan_file ({
		"path": from_file
	})

	print ('strand text', type (strand), strand)
	


	#cipher_text = fernet_key.encrypt (strand.encode ())
	cipher_text = fernet_key.encrypt (strand)

	print ('cipher text', type (cipher_text), cipher_text)

	etch_file ({
		"path": to_file,
		"strand": cipher_text
	})
	
	return;