import pandas as pd


class Playlist:
    def __init__(self, id, playlist_name, owner, followers, collaborative, public, artist_name, track_name, album_name, track_popularity, total_tracks):
        self.id = id
        self.playlist_name = playlist_name
        self.owner = owner
        self.followers = followers
        self.collaborative = collaborative
        self.public = public
        self.artist_name = artist_name
        self.track_name = track_name
        self.album_name = album_name
        self.track_popularity = track_popularity
        self.total_tracks = total_tracks #total number of tracks of songs for an album in a playlist?

    def __str__(self):
            return f"ID:{self.id}\nPlaylist Name:{self.playlist_name}\nOwner:{self.owner}\nFollowers:{self.followers}\nCollaborative:{self.collaborative}\nPublic:{self.public}\nArtist Name: {self.artist_name}\nTrack Name: {self.track_name}\nAlbum Name: {self.album_name} \nTrack Popularity: {self.track_popularity}\nTotal Tracks: {self.total_tracks}"  #self.owner can be this parameter when you initialise it you put in self.owner and only the name display_name

    #alternative ways to remove duplicated:
    #append the list into an empty list -> and check if the value exists in an empty list
    #list comprehension
    #set method

    #method print out the artist
    def name_of_artist(self):
    #give unique values of list
        artist_name1 = self.artist_name.copy() #copy vs reference when changing the original variable
        artist_name2 = self.artist_name.copy()

        for i in self.artist_name: #shouldn't loop through artist_name2 as it is removing items/shifting will be weird?
            artist_name2.remove(i) #removing removes one item of that "type" at a time
            if i in artist_name2:
                artist_name1.remove(i) #you can't remove from self.artist? -> have to make a copy artist_name1?

        for i in artist_name1:
            print(i)

    #method print the track_name
    def name_of_track(self):
        track_name1 = self.track_name.copy()
        track_name2 = self.track_name.copy()

        for i in self.track_name:
            track_name2.remove(i)
            if i in track_name2:
                track_name1.remove(i)

        for i in track_name1:
            print(i)

    #method print the album_name -> in this particular playlist each track belongs to a different album -> but in the case that they shatre the same playlist:
    def name_of_album(self):
        album_name1 = self.album_name.copy()
        album_name2 = self.album_name.copy()

        for i in self.album_name:
            album_name2.remove(i)
            if i in album_name2:
                album_name1.remove(i)

        for i in album_name1:
            print(i)

    #create a dataframe that has 4 columns -> artist, track, album, popularity,
    def dataframe(self):
        da = {"Artist Name": self.artist_name, "Track Name": self.track_name, " Album Name": self.album_name, "Popularity": self.track_popularity}
        df = pd.DataFrame(da)
        print(df)
        df.to_csv("playlist_info.csv")

# HOW TO GET THE INFO OF ALL THE PLAYLISTS AUTOMATICALLY NOT JUST THE ONES YOU ENTER BELOW??????


p1 = Playlist("2OIvSnHA4OVkBAiXrCN8gc", "70s", "Kartik", 0, "False", "True", ['Electric Light Orchestra', 'Sam Cooke', 'The Jackson 5', 'Marvin Gaye', 'Redbone', 'Rupert Holmes', 'The Jackson 5', 'Marvin Gaye', 'Marvin Gaye', 'Marvin Gaye', 'Marvin Gaye'], ['Mr. Blue Sky', 'Bring It On Home to Me', 'I Want You Back', "Ain't No Mountain High Enough - Mono Version", 'Come And Get Your Love', 'Escape (The Pina Colada Song)', 'I Want You Back', 'I Heard It Through The Grapevine', 'Sexual Healing', "What's Going On", "Let's Get It On"], ['Out of the Blue', 'The Man Who Invented Soul', 'Greatest Hits', 'Anthology', 'The Best Of Redbone', 'Partners In Crime', 'Diana Ross Presents The Jackson 5', 'In The Groove', 'Midnight Love', "What's Going On", "Let's Get It On (Deluxe Edition)"], [80, 66, 61, 0, 63, 75, 76, 70, 70, 69, 66], [17, 96, 11, 47, 12, 10, 12, 12, 9, 9, 37])
print("monkey")
print("\n")
print(p1) #should see the str function working
print("\n")
p1.name_of_artist()
print("\n")
p1.name_of_track()
print("\n")
p1.name_of_album()
print("\n")
p1.dataframe()
#create one playlist -> then go through other ones
#find the playlist name


