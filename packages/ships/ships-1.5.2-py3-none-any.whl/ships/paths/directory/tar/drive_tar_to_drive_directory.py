

'''
	# ".tar" is appended to the drive_tar path by "shutil"

	from ships.paths.directory.tar.drive_tar_to_drive_directory import drive_tar_to_drive_directory
	drive_tar_to_drive_directory ({
		"tar_path": 
		
		"directory_path":
		
		
	})
'''

'''
	don't extract from untrusted sources...
	
		https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall
'''

import shutil
import os
import tarfile

from pprint import pprint

def drive_tar_to_drive_directory (packet):
	directory_path = packet ["directory_path"]
	tar_path = packet ["tar_path"]
	

		
	#os.mkdir (directory_path)
	#os.chmod (directory_path, 0o777)
	
	'''
	with tarfile.TarFile (tar_path, 'r') as tar:
		tar.extractall (
			path = directory_path,
			filter = "data"
		)
	'''

	pprint ({
		"move": "drive:tar to drive:directory",
		"tar path": tar_path
	})
	
	with tarfile.open (tar_path, 'r') as tar:
		# Iterate through each member in the archive
		for member in tar.getmembers():
			print ("member.name", member.name)
			original_name = member.name

			# Construct the target path by appending member name to extract_root
			member.name = str (os.path.normpath (
				os.path.join (directory_path, "..", member.name)
			))
			print ("member.name", member.name)
			
			if (directory_path not in member.name and original_name != "."):
				raise Exception (f"""
	
	directory_path: '{ directory_path }'
	
	original path in archive: '{ original_name }'
	modified path in archive: '{ member.name }'
	
	does not seem to be inside the directory_path
	that it is supposed to be extracted to.				
				
				""")
			
			# Extract the member to the target path
			tar.extract (member, path = directory_path)
	
	print ("tar_path:", tar_path)
	print ("directory_path:", directory_path)
	
	#shutil.unpack_archive (tar_path, directory_path)
	
	'''
	with tarfile.open (tar_path, 'r') as tar:
		tar.extractall (
			path = directory_path,
			filter = "data"
		)
	'''
	
	os.chmod (directory_path, 0o777)
	
	#print (f'Files extracted to "{extract_dir}"')

