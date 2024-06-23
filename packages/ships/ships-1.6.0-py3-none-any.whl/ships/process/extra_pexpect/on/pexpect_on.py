

'''
	from .pexpect_on import turn_on_pexpect
	turn_on_pexpect ({
		"process_string": ""
	})
'''

import pexpect
import os

def turn_on_pexpect (packet):
	process_string = packet ["process_string"]

	if ("Popen" in packet ["process"]):
		Popen = packet ["process"] ["Popen"]
	else:
		Popen = {}

	pexpect_keys = merge (Popen, {
		"preexec_fn": os.setpgrp
	})

	p = pexpect.spawn (
		process_string,
		
		** pexpect_keys
		
		# encoding='utf-8'
	)
	def awareness_EOF (p):
		while not p.eof ():
			line = p.readline ()

			try:
				UTF8_line = line.decode ('UTF8')
				#UTF8_line = line.decode('ascii')				
				#UTF8_line = line;
				
				UTF8_parsed = "yes"
			except Exception:
				UTF8_line = ""
				UTF8_parsed = "no"
				
			try:
				hexadecimal_line = line.hex ()
				hexadecimal_parsed = "yes"
			except Exception:
				hexadecimal_line = ""
				hexadecimal_parsed = "no"
			
			
			line_parsed = {
				"UTF8": {
					"parsed": UTF8_parsed,
					"line": UTF8_line
				},
				"hexadecimal": {
					"parsed": hexadecimal_parsed,
					"line": hexadecimal_line
				}
			};
			

			

	awareness_EOF (p)