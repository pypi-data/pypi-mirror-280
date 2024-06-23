
'''
	python3 status.proc.py "activities/fernet_1_tar/_status_1/status_1.py"
'''

from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
from movies_ogv.activities.fernet_1_tar.drive_directory_to_drive_fernet import drive_directory_to_drive_fernet
from movies_ogv.activities.fernet_1_tar.drive_fernet_to_drive_directory import drive_fernet_to_drive_directory
from movies_ogv.activities.fernet_1.key_produce import produce_fernet_1_key

import ships.paths.directory.check_equality as check_equality

import shutil
from os.path import dirname, join, normpath
import pathlib
import sys
import zipfile
	
this_folder = pathlib.Path (__file__).parent.resolve ()
original_directory_path = str (normpath (join (this_folder, "constants/directory_1")))

fernet_key_path = str (normpath (join (this_folder, "variance/fernet.key.JSON")))
tar_fernet_path = str (normpath (join (this_folder, "variance/directory_1.tar.fernet")))
tar_fernet_reversal_path = str (normpath (join (this_folder, "variance/directory_1.tar.fernet.reversal")))

tar_fernet_decrypt_path = str (normpath (join (this_folder, "variance/directory_1.tar.fernet.decrypted")))

import ships.paths.directory.deallocate as dellocate_dir
from ships.paths.files.delete_abandon import delete_abandon_file
	

def check_1 ():
	delete_abandon_file (fernet_key_path, ignore_non_existence = True)
	delete_abandon_file (tar_fernet_path, ignore_non_existence = True)
	dellocate_dir.beautifully (tar_fernet_decrypt_path, ignore_non_existence = True)

	produce_fernet_1_key ({
		"write_outputs": "yes",
		"outputs": {
			"fernet_key_path": fernet_key_path
		}
	});
	
	drive_directory_to_drive_fernet ({
		"fernet_1_key": scan_fernet_1_key (fernet_key_path),
		
		"directory_path": original_directory_path,
		"tar_fernet_file_path": tar_fernet_path,
		
		"reversal check": "yes",
		"reversal_directory_path": tar_fernet_reversal_path
	})
	
	drive_fernet_to_drive_directory ({
		"fernet_1_key": scan_fernet_1_key (fernet_key_path),
		
		"tar_fernet_path": tar_fernet_path,
		"directory_path": tar_fernet_decrypt_path
	})
	
	report = check_equality.start (
		original_directory_path,
		tar_fernet_decrypt_path
	)	
	assert (
		report ==
		{'1': {}, '2': {}}
	), report
	
	delete_abandon_file (fernet_key_path)
	delete_abandon_file (tar_fernet_path)
	dellocate_dir.beautifully (tar_fernet_decrypt_path)
	
checks = {
	'check 1': check_1
}