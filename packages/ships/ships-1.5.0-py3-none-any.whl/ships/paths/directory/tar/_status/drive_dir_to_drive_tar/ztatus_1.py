

'''
	python3 status.proc.py "activities/tar/_status/status_1.py"
'''

'''
	steps:
		* tar to memory 
		* write the tar file in memory to a drive
		* read the tar file from the drive into memory
		* unpack the tar file
		* save the unpack to the drive
		* check that the unpacked version = the packed version
'''


from movies_ogv.activities.tar.pack import directory_to_memory_as_tar

import json
import pathlib
from os.path import dirname, join, normpath

this_directory = pathlib.Path (__file__).parent.resolve ()
directory_1 = str (normpath (join (
	this_directory, 
	'static/directory_1'
)))
directory_1_tar = str (normpath (join (
	this_directory, 
	'dynamic/directory_1.tar'
)))
directory_2 = str (normpath (join (
	this_directory, 
	'dynamic/directory_1'
)))

import tarfile
import io
import os
import shutil
def tar_file_to_memory (tar_path):
	print (f"""
		tar_file_to_memory
		
		{ tar_path }
	
	""")

	with tarfile.open (tar_path, "r") as tar:
		memfile = io.BytesIO ()
		
		for member in tar.getmembers ():
			print ('adding to memory', member)
		
			content = tar.extractfile (member).read ()
			memfile.write (content)

	memfile.seek(0)
	
	return memfile;

def extract_tar_to_directory (tar_file_in_memory, output_dir):
	memfile = tar_file_in_memory
	
	os.makedirs (output_dir, exist_ok = True)
	
	with tarfile.open (
		fileobj = memfile, 
		mode = "r"
	) as tar:
		for member in tar.getmembers ():
			member_path = os.path.join (output_dir, member.name)
			
			if member.isdir():  # If the member is a directory, create it
				os.makedirs(member_path, exist_ok=True)
			else:  # If the member is a file, extract it
				# Extract the file to the appropriate location
				tar.extract(member, path=output_dir)

def make_tar_gz ():
	

	compressed_file = shutil.make_archive (
		# archive file name w/o extension
		base_name = 'archive',   
		
		# available formats: zip, gztar, bztar, xztar, tar
		format = 'gztar',        
		
		# directory to compress
		root_dir = 'path/to/dir' 
	)


def rm_dir (directory_path):
	try:
		os.rmdir (directory_path)
		print("Directory removed successfully.")
	except OSError as e:
		print(f"Error: {directory_path} : {e.strerror}")

def rm_file (file_path):
	try:
		os.remove (file_path)
		print("Directory removed successfully.")
	except OSError as e:
		print(f"Error: {file_path} : {e.strerror}")

def check_1 ():
	rm_dir (directory_2)
	rm_file (directory_1_tar)

	tar_file_in_memory_1 = directory_to_memory_as_tar (directory_1)

	print ("tar_file_in_memory_1:", tar_file_in_memory_1)

	with open (directory_1_tar, "wb") as f:
		f.write (tar_file_in_memory_1.getvalue ())
		
	os.chmod (directory_1_tar, 0o777)

	
	tar_file_in_memory_2 = tar_file_to_memory (directory_1_tar)
	
	
	
	extract_tar_to_directory (
		tar_file_in_memory_2,
		directory_2
	)
	
	return;


checks = {
	'check 1': check_1
}