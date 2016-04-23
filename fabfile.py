
import os, sys

from fabric.api import env, local, run, cd, sudo, warn_only, prompt


HERE_PATH =  os.path.abspath( os.path.dirname( __file__ )	 ) 


def remove_crap():
	"""Remove not required packages from `apt/remove.txt` """
	
	with open(HERE_PATH + "/apt/remove.txt", "r") as f:
		contents = f.read()
	items = contents.split("\n")
	lst = []
	for i in items:
		ii = i.strip()
		if ii == "" or ii[0] == "#":
			continue 
		lst.append(ii)

	cmd = "sudo apt-get remove %s" % " ".join(lst)
	#print cmd
	local(cmd)

def upgrade():
	"""Update to latest patches"""
	local("sudo apt-get update")
	local("sudo apt-get upgrade")