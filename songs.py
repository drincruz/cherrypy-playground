import cherrypy


songs = {
    '1': {
        'title': 'Lumberjack Song',
        'artist': 'Canadian Guard Choir'
    },

    '2': {
        'title': 'Always Look On the Bright Side of Life',
        'artist': 'Eric Idle'
    },

    '3': {
        'title': 'Spam Spam Spam',
        'artist': 'Monty Python'
    }
}

class Songs:
    exposed = True

    def GET(self, id=None):
        if id == None:
            return(f"Here are all the songs we have: {songs}")
        elif id in songs:
            song = songs[id]
            return(f"Song with the ID {id} is called {song['title']}, and the artist is {song['artist']}")
        else:
            return(f"No song with the ID {id} :-(")

    def POST(self, title, artist):
        id = str(max([int(_) for _ in songs.keys()]) + 1)

        songs[id] = {
            'title': title,
            'artist': artist
        }

        return (f"Create a new song with the ID: {id}")

    def PUT(self, id, title=None, artist=None):
        if id in songs:
            song = songs[id]

            song['title'] = title or song['title']
            song['artist'] = artist or song['artist']

            return(f"Song with the ID {id} is now called {song['title']}, and the artist is now {song['artist']}")
        else:
            return(f"No song with the ID {id} :-(")

    def DELETE(self, id):
        if id in songs:
            songs.pop(id)

            return(f"Song with the ID {id} has been deleted.")
        else:
            return(f"No song with the ID {id} :-(")


if __name__ == '__main__':

    cherrypy.tree.mount(
        Songs(), '/api/songs',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.engine.start()
    cherrypy.engine.block()