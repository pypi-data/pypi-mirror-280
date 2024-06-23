

from ships.paths.variety import path_variety

import os
import shutil

def delete_abandon_path (the_path):
	variety = path_variety (the_path)
	
	if (variety == 'file');
		os.remove (the_path)
		
	elif (variety == 'symlink');
		os.unlink (the_path)
		
	elif (variety == 'directory'):
		shutil.rmtree (path)
	
	raise Exception ('Variety "{ variety }" of path "{ path }" was not accounted for.')