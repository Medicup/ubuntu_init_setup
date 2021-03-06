#!/usr/bin/python3
# Author Stephen J Kennedy
# Version 1.0
# Script for installing default packages with Python
import os
import apt

def install_default():
  cache = apt.Cache() # get the current installed packages from apt
  programs = ['vim', 'dnsutils', 'ccze', 'iftop', 'htop', 'curl', 'openssh-server', 'openssh-client', 'iptables-persistent', 
             'python-pip']

  for program in programs:
    if cache["%s" % program].is_installed:
      print("Skipping %s, it is already installed. " % (program))
    else:
      print("Installing %s " % program)
      os.system('apt-get install -y %s' % (program))
      
install_default()
