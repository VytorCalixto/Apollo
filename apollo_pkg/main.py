#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Apollo - Your CLI musical library manager

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

class Song(object):
    def __init__(self, name=None, length=None, trackNumber=None):
        self.name = name
        self.length = length
        self.trackNumber = trackNumber
    def printSong(self):
        print "%d - %s:%s" % (self.trackNumber, self.name.title(), self.length)

class Album(object):
    def __init__(self, name=None, songs=None, year=0, isLive=None):
        self.name = name
        self.songs = songs or []
        self.year = year
        self.isLive = isLive or False
    def printAlbum(self):
        live = ", live" if self.isLive else ""
        print Fore.GREEN + "%d - %s, %d songs%s" % (self.year, self.name.title(), len(self.songs), live) + Style.RESET_ALL
    def printAlbumSongs(self):
        for song in self.songs:
            if isinstance(song, Song):
                song.printSong()
            else:
                print song
    def findSongs(self):
        pass

class Artist(object):
    def __init__(self, name=None, albums=None):
        self.name = name
        self.albums = albums or []
    def printArtist(self):
        print Fore.YELLOW + self.name.title() + Style.RESET_ALL
    def printAlbums(self):
        for album in self.albums:
            if isinstance(album, Album):
                album.printAlbum()
            else:
                print album

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
        artists = []
        for a in library:
            try:
                artist = Artist(a['artist'])
                albums = []
                for b in a['albums']:
                    try:
                        album = Album(b['name'])
                        album.year = b['year']
                        album.isLive = b['isLive']
                    except KeyError:
                        pass
                    albums.append(album)
            except KeyError:
                pass
            try:
                artist.albums = albums if 'albums' in locals() else []
                artists.append(artist)
            except UnboundLocalError:
                pass
        for artist in artists:
            artist.printArtist()
            artist.printAlbums()
    else:
        print "New Library"

if __name__ == "__main__":
    main()
