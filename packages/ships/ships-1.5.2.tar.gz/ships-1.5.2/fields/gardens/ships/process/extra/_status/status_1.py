
'''
	python3 status.proc.py "process/extra/_status/status_1.py"
'''



import pathlib
from os.path import dirname, join, normpath
import sys

from ships.process.extra.on import turn_on_extra_process
from ships.process.extra.off import turn_off_extra_process

this_folder = str (pathlib.Path (__file__).parent.resolve ())

import time

def check_1 ():
	process_identities_path = str (normpath (join (
		this_folder, 
		"process_identities.JSON"
	)))


	The_process = str (normpath (join (this_folder, "proc.1.py")));
	records = str (normpath (join (this_folder, "records.UTF8")));
	
	process = [ 
		f'python3',
		f'"{ The_process }"' 
	] 

	turn_on_extra_process ({
		"identities_path": process_identities_path,
		"processes": [
			{
				"process": process,
				"Popen": {}
			}
		]
	})
	
	
	time.sleep (5)
	
	turn_off_extra_process ({
		"identities_path": process_identities_path
	})
	
	
	
	
checks = {
	'check one process': check_1
}