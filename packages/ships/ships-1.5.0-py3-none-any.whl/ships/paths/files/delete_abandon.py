



'''
	from ships.paths.files.delete_abandon import delete_abandon_file
	delete_abandon_file ()
'''

import os

def delete_abandon_file (file_path):
	#print ('abandoning file:', file_path)

	if os.path.exists (file_path):
		os.remove (file_path)
		return;
		
	raise Exception (f"file at path '{ file_path }' was not found.")