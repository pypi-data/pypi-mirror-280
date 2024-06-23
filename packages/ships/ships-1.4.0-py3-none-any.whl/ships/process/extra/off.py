

'''
	from ships.process.extra.off import turn_off_extra_process
	turn_off_extra_process ({
		"identities_path": "process_identities.JSON"
	})

'''

import os
import json

class turn_off_extra_process:
	def __init__ (the_class, packet):
		identities_path = packet ["identities_path"]
	
		process_identities = the_class.scan ({
			"identities_path": identities_path
		})
	
		for process_zone in process_identities:
			the_class.stop (process_zone)
			
		the_class.deallocate_fabric ({
			"identities_path": identities_path
		})	
			
		return;
	
	def scan (the_class, packet):
		identities_path = packet ["identities_path"]
	
		with open (identities_path, "r") as json_file:
			the_identities = json.load (json_file)
	
		return the_identities ["process identities"]
		
	def stop (the_class, process_zone):
		pid = process_zone ["process identity"]
	
		try:
			os.kill (pid, 9)
			print ("Process with PID", pid, "is off.")
		except OSError:
			print ("Process with PID", pid, "is not off.")
			
			
	
	def deallocate_fabric (the_class, process_zone):
		os.remove (process_zone ["identities_path"])	