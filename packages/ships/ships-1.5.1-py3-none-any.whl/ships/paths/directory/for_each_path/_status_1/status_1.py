
''''
	python3 status.proc.py "paths/directory/for_each_path/_status_1/status_1.py"
"'''

#/
#
from ships.paths.directory.for_each_path import for_each_path
#
from os.path import dirname, join, normpath
import pathlib
import sys
#
#\

this_folder = pathlib.Path (__file__).parent.resolve ()
original_directory_path = str (normpath (join (this_folder, "constants/directory_1")))

tar_path_without_extension = str (normpath (join (this_folder, "variance/directory_1")))
tar_path = str (normpath (join (this_folder, "variance/directory_1.tar")))

reversed_directory_path = str (normpath (join (this_folder, "variance/directory_1")))

def check_1 ():
	found = {
		'leaf.tx': 'file',
		'place': 'directory',
		'place/move.tx': 'file',
		'place/room': 'directory',
		'place/room/machine.tx': 'file',
		'place_symlink': 'symlink',
		'symlink_to_leaf.tx': 'symlink'
	}

	def for_each (packet):
		full_path = packet ["full_path"]
		rel_path = packet ["rel_path"]
		variety = packet ["variety"]
		
		if (rel_path in found and found [ rel_path ] == variety):
			pass;
		else:
			raise Exception (f"rel_path '{ rel_path }' was not found.")
		
		del found [ rel_path ]
	
	for_each_path ({
		"directory_path": original_directory_path,
		"for_each": for_each
	})
	
	assert (len (found) == 0)
	
checks = {
	'check_1': check_1
}