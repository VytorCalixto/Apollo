Apollo
======

Apollo is a software to manage your musical library. It stores your artists, albums, musics in json files, saving all information (ID3 tags) and, if possible, where from you downloaded the musics, albums, etc. This way, Apollo can download all your library with just one touch.

Example of an Apollo library:
```json
[
    {
        "artist": "led zeppelin",
        "albums":[
            {"name":"led zeppelin i", "release-year":"1969", "remastered":"false"},
            {"name":"led zeppelin ii", "release-year":"1969", "remastered":"true"}
        ]
    },
    {
        "artist":"rival sons",
        "albums":[
            {"name":"rival sons", "release-year":"2011"}
        ]
    },
    {
        "artist":"tom jobim",
        "albums":[
            {"name":"wave", "release-year":"1967", "remastered":"false"}
        ]
    }
]
```

Inside the album folder you would have another json file:
```json
{
    "artist":"rival sons",
    "album":"rival sons",
    "year":"2011",
    "tracks":[
        {"name":"get what's coming", "duration":"248"},
        {"name":"torture", "duration":"216"},
        {"name":"radio", "duration":"185"},
        {"name":"sacred tongue", "duration":"204"},
        {"name":"sleepwalker", "duration":"330"},
        {"name":"soul", "duration":"376"}
    ]
}
```
Music duration in seconds.

Apollo is still under development. Feel free to help.

##Todo:
* Edit Json inside Apollo
* Set folders where Apollo will monitor your musics. If you add something new, it'll know
* Organize your musical library
* If you have imported a new library, show which tracks/albums are missing and let you (if possible) download them
* Export folders as an Apollo library (json file)
