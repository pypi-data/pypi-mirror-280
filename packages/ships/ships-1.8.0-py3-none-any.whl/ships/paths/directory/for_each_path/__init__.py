

''''
	from ships.paths.directory.for_each_path import for_each_path
	
	def for_each (packet):
		full_path = packet ["full_path"]
		rel_path = packet ["rel_path"]
		variety = packet ["variety"]

	
	for_each_path ({
		"directory_path": "",
		"for_each": for_each
	})
"'''


import os

from ships.paths.variety import path_variety
	

def for_each_path (packet):
	directory_path = packet ["directory_path"]
	for_each = packet ["for_each"]
	
	def scan_directory (this_directory_path):
		with os.scandir (this_directory_path) as entries:
			for entry in entries:
				absolute_path = os.path.join (this_directory_path, entry.name)
				relative_path = os.path.relpath (absolute_path, directory_path)
				
				#print ('absolute path:', absolute_path)
				variety = path_variety (absolute_path);
				
				if (variety == "directory"):
					for_each ({
						"rel_path": relative_path,
						"variety": variety,
						"full_path": absolute_path,
					})
					
					scan_directory (absolute_path)
					
					
				if (variety in [ "symlink", "file" ]):
					for_each ({
						"rel_path": relative_path,
						"variety": variety,
						"full_path": absolute_path,
					})

	scan_directory (directory_path)
			
		
	return;