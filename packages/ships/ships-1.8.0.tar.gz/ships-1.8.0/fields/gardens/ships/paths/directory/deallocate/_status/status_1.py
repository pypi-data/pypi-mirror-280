
''''
	python3 status.proc.py "paths/directory/deallocate/_status/status_1.py"
"'''

import ships.paths.directory.deallocate as dellocate_dir

import os
from os.path import normpath, join
import pathlib

def check_1 ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	directory_path = normpath (join (this_folder, "variance/directory_1"));

	dellocate_dir.beautifully (directory_path, ignore_non_existence = True)

	os.makedirs (directory_path)
	
	dellocate_dir.beautifully (directory_path)

	assert (os.path.exists (directory_path) == False)
	
checks = {
	'check 1': check_1
}