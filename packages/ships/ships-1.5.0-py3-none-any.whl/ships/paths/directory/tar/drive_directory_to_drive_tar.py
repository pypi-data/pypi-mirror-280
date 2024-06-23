

'''
	# ".tar" is appended to the drive_tar path by "shutil"

	from movies_ogv.activities.tar.drive_directory_to_drive_tar import drive_directory_to_drive_tar
	drive_directory_to_drive_tar ({
		"original_directory_path":
		"drive_tar": 
		
		"reversal check": "yes"
		"reversal path": ""
	})
'''

#/
#
from ships.paths.directory.tar.drive_tar_to_drive_directory import drive_tar_to_drive_directory
import ships.paths.directory.deallocate as dellocate_dir
#
#
import ships.paths.directory.check_equality as check_equality
#
#
import shutil
import os
#
#\

def drive_directory_to_drive_tar (packet):
	original_directory_path = packet ["original_directory_path"]
	tar_path = packet ["tar_path"]
	
	if ("reversal check" in packet):
		reversal_check = packet ["reversal check"]
	else:
		reversal_check = "no"

	'''
		gztar
	'''
	
	actual_tar_path = tar_path + ".tar"
	
	shutil.make_archive (
		tar_path, 
		'tar', 
		
		root_dir = os.path.dirname (original_directory_path),
		#base_dir = os.path.basename (original_directory_path)
	)
	
	os.chmod (actual_tar_path, 0o777)
	
	if (reversal_check == "yes"):
		reversal_path = packet ["reversal path"]

		drive_tar_to_drive_directory ({
			"tar_path": actual_tar_path,
			"directory_path": reversal_path
		})
		
		report = check_equality.start (
			original_directory_path,
			reversal_path
		)	
		assert (
			report ==
			{'1': {}, '2': {}}
		), report
		
		dellocate_dir.beautifully (reversal_path)