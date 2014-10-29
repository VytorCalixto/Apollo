#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Apollo - Your musical library manager

https://github.com/vytorcalixto/apollo
"""
import sys
import os
import json
try:
    from colorama import init as init_colorama, Fore, Style
    has_colorama = True
except ImportError:
    has_colorama = False

class Album(object):
    def __init__(self, name=None, songs=None):
        self.name = name
        self.songs = songs or []

class Artist(object):
    def __init__(self, name=None, albums=None):
        self.name = name
        self.albums= albums or []

isNewLibrary = False
try:
    filepath = sys.argv[1]
    if os.path.exists(filepath):
        #print os.path.basename(filepath)
        with open(filepath) as json_data:
            library = json.load(json_data)
            json_data.close()
            if len(library) == 0:
                isNewLibrary = True
except IndexError:
    isNewLibrary = True

def main():
    """Main loop"""
    if not isNewLibrary:
        for artists in library:
            print artists['artist']
    else:
        print "New Library"
    print Fore.GREEN + "Colorama" + Style.RESET_ALL if has_colorama else Fore.RED + "No colorama" + Style.RESET_ALL

if __name__ == "__main__":
    main()
