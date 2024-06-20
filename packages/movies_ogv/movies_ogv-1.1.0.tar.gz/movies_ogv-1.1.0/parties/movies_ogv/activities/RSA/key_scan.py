

'''
	from movies_ogv.activities.RSA.key_scan import scan_fernet_key
	fernet_key = read_fernet_key ("");
'''


import rsa

def scan_fernet_key (key_path):
	with open (key_path, mode = 'rb') as FP:
		return FP.read ()
		
	raise Exception (f"Could not read fernet key at { key_path }")