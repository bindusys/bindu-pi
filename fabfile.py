
import os, sys

from fabric.api import env, local, run, cd, sudo, warn_only, prompt


HERE_PATH =  os.path.abspath( os.path.dirname( __file__ )	 ) 


def _read_apt_file(file_name):
	with open(HERE_PATH + "/apt/%s" % file_name, "r") as f:
		contents = f.read()
	items = contents.split("\n")
	lst = []
	for i in items:
		ii = i.strip()
		if ii == "" or ii[0] == "#":
			continue 
		lst.append(ii)
	return lst

def remove_crap():
	"""Remove not required packages from `apt/remove.txt` """
	
	lst =_read_apt_file("remove.txt")
	cmd = "sudo apt-get -y remove %s" % " ".join(lst)
	#print cmd
	local(cmd)

def upgrade():
	"""Update to latest patches"""
	local("sudo apt-get update")
	local("sudo apt-get -y upgrade")
	local("sudo apt-get -y autoremove")
	local("sudo apt-get clean")
	
	
def install_essentials():
	"""Install essentials"""
	
	lst =_read_apt_file("install.txt")
	cmd = "sudo apt-get -y install %s" % " ".join(lst)
	#print cmd
	local(cmd)