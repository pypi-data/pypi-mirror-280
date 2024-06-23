








from movies_ogv.activities.fernet_1.key_produce import produce_fernet_1_key
from movies_ogv.activities.fernet_1.key_scan import scan_fernet_1_key
from movies_ogv.activities.fernet_1_tar.drive_directory_to_drive_fernet import drive_directory_to_drive_fernet
from movies_ogv.activities.fernet_1_tar.drive_fernet_to_drive_directory import drive_fernet_to_drive_directory
	
	

import click

import os
from os.path import normpath, join

fernet_key_name = "fernet.key.JSON"

def clique ():
	@click.group ("fernet_1_tar")
	def group ():
		pass

	@group.command ("produce_key")
	#@click.option ('--example-option', required = True)
	def search ():
		CWD = os.getcwd ()
		fernet_key_path = str (normpath (join (CWD, fernet_key_name)))
	
		produce_fernet_1_key ({
			"write_outputs": "yes",
			"outputs": {
				"fernet_key_path": fernet_key_path
			}
		});
		
		print (f"A fernet key was built at: '{ fernet_key_path }'")
	
		return;
		
	@group.command ("encrypt")
	@click.option ('--dir', required = True)
	@click.option ('--fernet-key-path', default = fernet_key_name)
	@click.option ('--reversal-directory-path', default = "directory.tar.fernet.reversal")
	def encrypt (dir, fernet_key_path, reversal_directory_path):	
		if (fernet_key_path [0] != "/"):
			CWD = os.getcwd ()
			fernet_key_path = str (normpath (join (CWD, fernet_key_name)))
	
		if (reversal_directory_path [0] != "/"):
			CWD = os.getcwd ()
			reversal_directory_path = str (normpath (join (CWD, reversal_directory_path)))
	
		if (dir [0] != "/"):
			CWD = os.getcwd ()
			dir = str (normpath (join (CWD, dir)))
		
		tar_fernet_file_path = dir + ".tar.fernet"
	
		drive_directory_to_drive_fernet ({
			"fernet_1_key": scan_fernet_1_key (fernet_key_path),
			
			"directory_path": dir,
			"tar_fernet_file_path": tar_fernet_file_path,
			
			"reversal check": "yes",
			"reversal_directory_path": reversal_directory_path
		})
		
	@group.command ("decrypt")
	@click.option ('--file', required = True)
	@click.option ('--fernet-key-path', default = fernet_key_name)
	def encrypt (file, fernet_key_path):	
		if (fernet_key_path [0] != "/"):
			CWD = os.getcwd ()
			fernet_key_path = str (normpath (join (CWD, fernet_key_name)))

		if (file [0] != "/"):
			CWD = os.getcwd ()
			file = str (normpath (join (CWD, file)))
		
		directory_path = file.split (".tar.fernet") [0] + ".decrypted"
	
		drive_fernet_to_drive_directory ({
			"fernet_1_key": scan_fernet_1_key (fernet_key_path),
			
			"tar_fernet_path": file,
			"directory_path": directory_path
		})

	return group




