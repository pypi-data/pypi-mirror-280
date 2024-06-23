
''''
	from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
	from movies_ogv.activities.fernet_1_tar.drive_fernet_to_drive_directory import drive_fernet_to_drive_directory
	
	drive_fernet_to_drive_directory ({
		"fernet_1_key": scan_fernet_1_key (fernet_key_path),
		
		"tar_fernet_path": "",
		"directory_path": ""
	})
"'''


#/
#
from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
from movies_ogv.activities.fernet_1.memory_encrypted_to_memory import memory_encrypted_to_memory
#
#
from ships.paths.directory.tar.memory_tar_to_drive_directory import memory_tar_to_drive_directory
from ships.paths.files.scan import scan_file
#
#
import io
import os
#
#\


def drive_fernet_to_drive_directory (packet):
	fernet_1_key = packet ["fernet_1_key"]
	
	tar_fernet_path = packet ["tar_fernet_path"]
	directory_path = packet ["directory_path"]
	
	if (os.path.exists (directory_path)):
		raise Exception (f"There's already something at: '{ directory_path }'")
	
	decrypted = memory_encrypted_to_memory ({
		"fernet_1_key": fernet_1_key,
		"strand": scan_file ({
			"path": tar_fernet_path
		})
	})
	
	bytes_io = io.BytesIO (b"")
	bytes_io.write (decrypted)
	bytes_io.seek (0)
	
	tar_stream = bytes_io
	
	memory_tar_to_drive_directory ({
		"tar_stream": tar_stream,
		"directory_path": directory_path
	})
	
	os.chmod (directory_path, 0o777)
	