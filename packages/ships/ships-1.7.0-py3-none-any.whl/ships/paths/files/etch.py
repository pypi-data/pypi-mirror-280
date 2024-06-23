



'''
	from ships.paths.files.etch import etch_file
	etch_file ({
		"path": "",
		"strand": ""
	})
'''

import os

def etch_file (packet):
	path = packet ["path"]
	strand = packet ["strand"]

	with open (path, 'wb') as FP:
		os.chmod (path, 0o777)
		FP.write (strand)
		return;
		
	raise Exception (f"File was not etched at path: '{ path }'.")