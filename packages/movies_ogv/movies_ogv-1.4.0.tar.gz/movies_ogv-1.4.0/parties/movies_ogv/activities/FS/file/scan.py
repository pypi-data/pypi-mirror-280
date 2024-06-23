

'''
	from movies_ogv.activities.FS.file.scan import scan_file
	strand = scan_file ({
		"path": ""
	})
'''

def scan_file (packet):
	path = packet ["path"]
	
	with open (path, 'rb') as FP:
		return FP.read ()
		
	raise Exception (f"File was not scanned at path: '{ path }'.")