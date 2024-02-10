class Album:
    def __init__(self, album_id, album_name, album_type, artist_id, artist_name, track_name,  release_date, total_tracks, duration_ms, popularity): #initilising
        self.album_id = album_id #assigning parameters to use in the return function -> 4uVXrwE4aSV2L2aqAHSOXa
        self.album_name = album_name # First Class
        self.album_type = album_type #single
        self.artist_id = artist_id #2LIk90788K0zvyj2JJVwkJ
        self.artist_name = artist_name #Jack Harlow
        self.track_name = track_name #First Class
        self.release_date = release_date #2022-04-08
        self.total_tracks = total_tracks #1
        self.duration_ms = duration_ms #173947
        self.popularity = popularity # 91

    def __str__(self): #when print the main in the class see this
        return f"Album ID: {self.album_id}\nAlbum Name: {self.album_name}\nAlbum Type: {self.album_type}\nArtist ID: {self.artist_id}\nArtist Name: {self.artist_name}\nTrack Name: {self.track_name}\nRelease Date: {self.release_date}\nTotal Tracks: {self.total_tracks}\nDuration MS: {self.duration_ms}\nPopularity: {self.popularity}\n"

a1 = Album("4uVXrwE4aSV2L2aqAHSOXa", "First Class", "single", "2LIk90788K0zvyj2JJVwkJ", "Jack Harlow", "First Class", "2022-04-08", "1", "173947", "91")
print(a1)