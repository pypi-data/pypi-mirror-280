
''''
	from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
	from movies_ogv.activities.fernet_1_tar.drive_directory_to_drive_fernet import drive_directory_to_drive_fernet
	
	drive_directory_to_drive_fernet ({
		"fernet_1_key": scan_fernet_1_key (fernet_key_path),
		
		"directory_path": "",
		"tar_fernet_file_path": "",
		
		"reversal check": "yes",
		"reversal_directory_path": ""
	})
"'''

#/
#
from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
from movies_ogv.activities.fernet_1.memory_to_memory_encrypted import memory_to_memory_encrypted
from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
from movies_ogv.activities.fernet_1_tar.drive_fernet_to_drive_directory import drive_fernet_to_drive_directory
#
from ships.paths.directory.tar.drive_directory_to_memory_tar import drive_directory_to_memory_tar
from ships.paths.files.etch import etch_file
#
#
import os
#
#\

def drive_directory_to_drive_fernet (packet):
	fernet_1_key = packet ["fernet_1_key"]

	directory_path = packet ["directory_path"]
	tar_fernet_file_path = packet ["tar_fernet_file_path"]

	if (os.path.exists (tar_fernet_file_path)):
		raise Exception (f"There's already something at: '{ tar_fernet_file_path }'")

	memory_encrypted = memory_to_memory_encrypted ({
		"fernet_1_key": fernet_1_key,
		"bytes_io": drive_directory_to_memory_tar ({
			"directory_path": directory_path
		})
	})
	etch_file ({
		"path": tar_fernet_file_path,
		"strand": memory_encrypted
	})
	
	os.chmod (tar_fernet_file_path, 0o777)
	
	if (
		"revesal check" in packet and 
		packet ["revesal check"] == "yes"
	):
		reversal_directory_path = packet ["reversal_directory_path"]
	
		drive_fernet_to_drive_directory ({
			"fernet_1_key": fernet_1_key,
			
			"tar_fernet_path": tar_fernet_file_path,
			"directory_path": ""
		})
		
		return;
	