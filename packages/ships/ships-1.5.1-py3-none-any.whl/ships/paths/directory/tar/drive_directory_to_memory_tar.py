

''''
	considerations:
		[ ] files, directories, symlinks
		[ ] relative paths that are outside of directory,
			because someone created the tar archive with weird paths.
"'''


from ships.paths.directory.for_each_path import for_each_path

import os
import tarfile
import io
import glob
	
from pprint import pprint

def drive_directory_to_memory_tar (packet):
	directory_path = packet ["directory_path"]
	
	print ()
	
	tar_stream = io.BytesIO ()
	
	with tarfile.open (fileobj = tar_stream, mode='w') as tar:
		def for_each (packet):
			full_path = packet ["full_path"]
			rel_path = packet ["rel_path"]
			variety = packet ["variety"]
			
			arcname = rel_path
			
			#print ("
			
			if (variety == "symlink"):
				print ("adding symlink:", full_path)
			
				tar_info = tar.gettarinfo (full_path, arcname)
				tar_info.type = tarfile.SYMTYPE
				tar_info.linkname = os.readlink (full_path)
				tar.addfile (tar_info)
			
			elif (variety == "file"):
				print ("adding file:", full_path)
				tar.add (full_path, arcname = arcname)
				
			elif (variety == "directory"):
				print ("adding dir:", full_path)
				tar.add (full_path, arcname = arcname)
				
			else:
				raise Exception (f"The kind of this path could not be found: '{ full_path }'")
				
			
		for_each_path ({
			"directory_path": directory_path,
			"for_each": for_each
		})
	

	print ()
	
	tar_stream.seek (0)
	
	return tar_stream
