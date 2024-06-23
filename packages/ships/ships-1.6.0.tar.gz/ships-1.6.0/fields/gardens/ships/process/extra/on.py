



'''
	from ships.process.extra.on import turn_on_extra_process
	turn_on_extra_process ({
		"identities_path": "process_identities.JSON",
		"processes": [
			{
				"process": "process_path.py",
				"Popen": {
					"cwd": "",
					"env": {}
				}
			},
			{
				"process": "process_path.py",
				"Popen": {
					"cwd": "",
					"env": {}
				}
			}
		]
	})
'''

'''
	{
		"process identities": []
	}
'''

from pydash import merge

import json
import os
import subprocess

	
class turn_on_extra_process:
	def __init__ (the_class, packet):
		the_processes = packet ["processes"]
		
		process_identities = {
			"process identities": []
		}
		for proc in the_processes:
			pid = the_class.on ({
				"process": proc
			})
			
			process_identities ["process identities"].append ({
				"process identity": pid
			})
	
		the_class.sculpt ({
			"identities_path": packet ["identities_path"],
			"process_identities": process_identities
		})
		
	def on (the_class, packet):
		
	
		if ("Popen" in packet ["process"]):
			Popen = packet ["process"] ["Popen"]
		else:
			Popen = {}
	
		keys = merge (Popen, {
			"preexec_fn": os.setpgrp
		})
	
		process = subprocess.Popen (
			packet ["process"] ["process"],
			** keys,
			
			#preexec_fn = os.setpgrp
		)
		
		pid = process.pid
		
		return pid
		
	def sculpt (the_class, packet):
		identities_path = packet ["identities_path"]
		process_identities = packet ["process_identities"]
	
		with open (identities_path, "w") as FP:
			json.dump (process_identities, FP, indent = 4)
	


