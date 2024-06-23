

'''
	from ships.paths.directory.tar.memory_tar_to_drive_directory import memory_tar_to_drive_directory
	memory_tar_to_drive_directory ({
		"tar_stream": 
		"directory_path": 
	})
'''


import tarfile

def memory_tar_to_drive_directory (packet):
	tar_stream = packet ["tar_stream"]
	directory_path = packet ["directory_path"]

	print ("memory_tar_to_drive_directory")

	# Rewind the BytesIO object
	tar_stream.seek (0)

	with tarfile.open (fileobj = tar_stream, mode='r') as tar:
		tar.extractall (path = directory_path)
	
	tar_stream.seek (0)

	print(f"Successfully extracted tar archive to '{directory_path}'.")
