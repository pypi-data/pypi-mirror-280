



'''
	from movies_ogv.activities.FS.directory.delete_abandon import delete_abandon_directory
	delete_abandon_directory ()
'''

import shutil
import os

def delete_abandon_directory (directory_path):
	print ('abandoning directory:', directory_path)

	if os.path.exists (directory_path):
		shutil.rmtree (directory_path)
		return;
		
	raise Exception (f"directory at path '{ directory_path }' was not found.")