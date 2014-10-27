#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json
from pprint import pprint

def usage():
    print "Usage: main.py <file>.json"

try:
    filepath = sys.argv[1]
    if os.path.exists(filepath):
        #print os.path.basename(filepath)
        with open(filepath) as json_data:
            d = json.load(json_data)
            json_data.close()
            for artists in d:
                print artists['artist']
                for (i,album) in enumerate(artists['albums']):
                    print str(i+1) + " - " + album['name']
            #pprint(d)
except IndexError:
    usage()
