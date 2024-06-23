

'''
	from movies_ogv.activities.fernet_1.memory_encrypted_to_memory import memory_encrypted_to_memory
	from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
	
	fernet_1_key = scan_fernet_1_key ("");
	
	fernet_1_crypt_decrypt ({
		"fernet_1_key": fernet_1_key,
		"strand": 
	})
'''


from cryptography.fernet import Fernet

import io

def memory_encrypted_to_memory (packet):
	fernet_key = packet ["fernet_1_key"]
	strand = packet ["strand"]
	
	decrypted_text = fernet_key.decrypt (strand)
	
	return decrypted_text

