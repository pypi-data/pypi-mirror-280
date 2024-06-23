


'''
	import ships.paths.directory.deallocate as dellocate_dir
	dellocate_dir.beautifully (path, ignore_non_existence = True)
'''

from ships.paths.variety import path_variety

import shutil
import os

def beautifully (path, ignore_non_existence = False):
	if (os.path.exists (path)):
		if (path_variety (path) == "directory"):
			shutil.rmtree (path)
			return;
			
		else:
			raise Exception (f"The path '{ path }' is not a directory.")
	
	if (ignore_non_existence):
		return;
		
	raise Exception (f"There's nothing at path '{ path }'.")


