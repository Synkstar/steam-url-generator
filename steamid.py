from steam import steamid
from discord_webhook import DiscordWebhook
import requests
import itertools
import string
import random

Chars = ("abcdefghijklmnopqrstuvwxyz1234567890-_") # All possible characters in a steam profile url
Length = 3
webhook = "" # Insert discord webhook here
Chars = list(Chars)
random.shuffle(Chars)
Chars = ''.join(Chars)
print(Chars)
times = 0
f = list(itertools.permutations(Chars, Length)) # Creates a list with all of the possible combinations. I don't recommend setting the length to over 4 because it could eat your ram

for i in f: # Loops through the list to find urls that aren't taken
    i = "".join(i)
    sid = steamid.steam64_from_url("https://steamcommunity.com/id/" + i,http_timeout=30)
    if sid == None: 
        sid = steamid.steam64_from_url("https://steamcommunity.com/id/" + i,http_timeout=30)
        if sid == None:
            r = requests.get("https://steamcommunity.com/id/" + i)
            if "The specified profile could not be found." in r.text :       
                f = open("steamids.txt","a")
                f.write(i + "\n")
                f.close
                webhook = DiscordWebhook(webhook,content='Found steamid ' + str(i))
                webhook.execute()
                print("FOUND STEAMID")
            else:
                times += 1
                print("https://steamcommunity.com/profiles/" + str(sid) + " Times:" + str(times))                
        else:
            times += 1
            print("https://steamcommunity.com/profiles/" + str(sid) + " Times:" + str(times))
    else:
        times += 1
        print("https://steamcommunity.com/profiles/" + str(sid) + " Times:" + str(times) )
print("Exhausted all options. Exiting!")