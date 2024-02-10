
class Track:
    def __init__(self, id, artist_name, track_name, album_name, artist_id, popularity, type): #initilising
        self.id = id #assigning parameters to use in the return function
        self.artist_name = artist_name
        self.track_name = track_name
        self.album_name = album_name
        self.artist_id = artist_id
        self.popularity = popularity
        self.type = type


    def __str__(self): #when print the main in the class see this
        return f"ID: {self.id}\nArtist Name: {self.artist_name}\nTrack name: {self.track_name}\nAlbum name: {self.album_name}\nArtist id: {self.artist_id}\nTrack id: {self.id}\nTrack Type: {self.type}\n"

#should see the str function working
t1 = Track("4lQ87x6SYGR9E8v28xqhh2", "Central Cee", "Little Bit of This", "Little Bit of This", "5H4yInM5zmHqpKIoMNAx4r", 62, "track") #just to experiment in this class without the main
print(t1)