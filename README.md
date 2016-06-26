bindu-rpi
===================

These are some scripts and utils to setup and RPI, 
by getting rid of crap, installing essentials,
and minor configuration.

1: Install git and clone this repos
=======================================

Kick up a terminal and tap in

  sudo apt-get install git
  git clone https://daffodil@bitbucket.org/bindusys/bindu-rpi.git


2: Install bootstrap essentials
===============================

Enter the bindu-sys dir and run the script "initial-setup.sh"
which install some python headers and fabric

  cd bindu-sys
  ./initial-setup.sh


3: Run `fab` commands
===============================

To complete tap in which executes a series of commands
and could take a while.

  fab setup

For more "fab commands"

  fab -l
 
 






