


import subprocess

# Command to execute with output redirection using shell
command = "python3 proc.1.py > records.UTF8 &"

# Start the process with shell=True to enable shell features
process = subprocess.Popen (command, shell=True)