
'''
	from ships.paths.directory.tar.pack import tar_folder_to_memory

	folder_to_tar = '/path/to/your/folder'
	tarfile_in_memory = tar_folder_to_memory(folder_to_tar)
'''

import tarfile
import io
import os

def create_tar_xz (source_dir, output_filename):
    with tarfile.open(output_filename, "w:xz") as tar:
        tar.add (source_dir, arcname='')

def directory_to_memory_as_tar (folder_path):
    # Create an in-memory byte stream
    memfile = io.BytesIO ()
    
    # Create a tar archive in memory
    with tarfile.open (fileobj = memfile, mode = 'w') as tar:
        # Add all files and subdirectories in the folder to the tar archive
        for root, dirs, files in os.walk (folder_path):
			print ("files:", files)
		
            for file in files:
                file_path = os.path.join (root, file)
                tar.add (
					file_path, 
					arcname = os.path.relpath (
						file_path, 
						folder_path
					)
				)

    # Reset the position of the in-memory file pointer to the beginning
    memfile.seek (0)
    
		
	
    return memfile


