

'''
	# ".tar" is appended to the drive_tar path by "shutil"

	from movies_ogv.activities.tar.drive_directory_to_drive_tar import drive_directory_to_drive_tar
	drive_directory_to_drive_tar ({
		"drive_directory":
		"drive_tar": 
	})
'''

import shutil
import os

def drive_directory_to_drive_tar (packet):
	drive_directory = packet ["drive_directory"]
	drive_tar = packet ["drive_tar"]

	shutil.make_archive (
		drive_tar, 
		'tar', 
		
		root_dir = os.path.dirname (drive_directory),
		base_dir = os.path.basename (drive_directory)
	)
	
	os.chmod (drive_tar + ".tar", 0o777)

