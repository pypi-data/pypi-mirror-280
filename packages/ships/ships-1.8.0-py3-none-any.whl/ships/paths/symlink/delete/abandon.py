

import os

def delete_abandon_symlink (symlink_path):
	os.unlink (symlink_path)