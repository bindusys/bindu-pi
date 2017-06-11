Bindu raspberry-pi-setup 
=================================

A small collection of scripts to setup and rpi. Gets rid
of the games and other stuff (see [apt/remove.txt](apt/remove.txt))
and install pyqt3 and others (see [apt/install.txt](apt/install.txt))


Note: 

- the "default" user is `pi`
- the default password is is a `raspberry`


## 1: Install git and clone this repos

Kick up a terminal and tap in

```
sudo apt-get install git
git clone https://daffodil@bitbucket.org/bindusys/bindu-rpi.git
```

## 2: Install fabric and initial setup

Enter the bindu-sys dir and run the script "initial-setup.sh"
which install some python headers and fabric

```
cd bindu-sys
./initial-setup.sh
```

## 3: Run `fab` commands

To complete tap in `fab all` which executes a series of commands
and could take a while. When complete it will reboot.

```
fab all
```

Optionally install "conky", which will
create an overlay with the machine's ip address etc 
(useful when no keyboard and require remote access)

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

 
 






