

'''
	python3 status.proc.py "paths/directory/tar/_status/drive_dir_to_drive_tar/status_1.py"
'''


#/
#
#
from ships.paths.directory.tar.drive_directory_to_drive_tar import drive_directory_to_drive_tar	
from ships.paths.directory.tar.drive_tar_to_drive_directory import drive_tar_to_drive_directory
from ships.paths.files.delete_abandon import delete_abandon_file	
import ships.paths.directory.deallocate as dellocate_dir
#
#
import ships.paths.directory.check_equality as check_equality
#
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

def abandon_file_attempt (file_path):
	try:
		delete_abandon_file (file_path)
	except Exception:
		pass;

def abandon_directory_attempt (directory_path):
	try:
		dellocate_dir.beautifully (directory_path)
	except Exception:
		pass;

def check_1 ():
	abandon_file_attempt (tar_path)
	abandon_directory_attempt (reversed_directory_path)

	drive_directory_to_drive_tar ({
		"original_directory_path": original_directory_path,
		"tar_path": tar_path_without_extension,
		
		"reversal check": "yes",
		"reversal path": reversed_directory_path
	})
	
	delete_abandon_file (tar_path)
	
	
	
	
checks = {
	'check 1': check_1
}