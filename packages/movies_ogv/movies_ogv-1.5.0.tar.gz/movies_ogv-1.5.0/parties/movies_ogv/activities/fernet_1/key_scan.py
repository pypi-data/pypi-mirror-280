

'''
	from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
	fernet_key = scan_fernet_1_key ("");
'''

from cryptography.fernet import Fernet

import json

def scan_fernet_1_key (key_path):
	with open (key_path, mode = 'rb') as FP:
		fernet_key_dict = json.loads (FP.read ())
		fernet_key = bytes.fromhex (fernet_key_dict ["fernet_key"])
	
		return Fernet (fernet_key)
		
	raise Exception (f"Could not read fernet key at { key_path }")