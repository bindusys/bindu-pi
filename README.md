BinduSYS RaspberryPi 
=================================

This repos contains some scripts and utils to setup an RPI.
by getting rid of crap, installing essentials,
and minor configuration, for a first time install.

Note: The "default" user is `pi` and the pass is `raspberry`

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

To complete tap in `fab all` which executes a series of commands
and could take a while. When complete it will reboot.

    fab all

For more "fab commands" exec `fab -l`

4: Bonus
==============================

SSH in from remote machine with

    ssh pi@<ip>
    > pass = raspberry

To set passwordless login

    ssh-copy-id pi@<ip>

then below should work with no pass

    ssh pi@<ip>

 
 






