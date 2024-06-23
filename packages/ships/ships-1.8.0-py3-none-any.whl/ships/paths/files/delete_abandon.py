



'''
	from ships.paths.files.delete_abandon import delete_abandon_file
	delete_abandon_file ("", ignore_non_existence = True)
'''

import os

def delete_abandon_file (file_path, ignore_non_existence = False):
	#print ('abandoning file:', file_path)

	if os.path.exists (file_path):
		os.remove (file_path)
		return;
	
	if (ignore_non_existence):
		return;
	
	raise Exception (f"file at path '{ file_path }' was not found.")