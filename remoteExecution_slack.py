#! /usr/bin/python
# Author: ShamiLakhani@hotmail.com
# Version:  0.1 - Draft.
# Objective: Reads and executes a command set in a channel within the Slack service. 
# Functionality uses the legacy key set in Slack (https://api.slack.com/custom-integrations/legacy-tokens)

import requests, json
channelID = "[enter channel ID here]"
tokenID = "xoxp-[enter token number here]"

page = requests.get ("https://digitalengineering.slack.com/api/channels.history?token=" + tokenID + "&channel=" + channelID)

if page.status_code == 200:
    j = json.loads (page.content)
    executeCommand = (j['messages'][0]['text'])
    from subprocess import Popen
    # Debug: print (executeCommand)
    Popen (executeCommand) 
    exit()
else:
    print (page.status_code)
    exit()
