import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from Artist import Artist  #name of file     name of class
from Playlist import Playlist
from Track import Track
from Album import Album
import pandas as pd

# documentation on spotipy -> https://spotipy.readthedocs.io/en/master/#spotipy.client.Spotify.artist_top_tracks

# spotify developers website -> log in -> create an app -> get the cid and c_secret
cid = "e6a64ab8b2b74845b0604ede513c1cbe"
c_secret = "25834f05b8bd490087cd482018ac50ee"
scope = ["user-top-read", "ugc-image-upload", "user-modify-playback-state", "user-read-playback-state", "user-read-currently-playing", "user-follow-modify", "user-follow-read", "user-read-recently-played", "user-read-playback-position", "user-top-read", "playlist-read-collaborative", "playlist-modify-public", "playlist-read-private", "playlist-modify-private", "app-remote-control", "streaming", "user-read-email", "user-read-private", "user-library-modify", "user-library-read"]

# used https://spotipy.readthedocs.io/en/2.19.0/
# authentication give you an id to allow you to access your data
client_credentials_manager = SpotifyOAuth(client_id=cid, client_secret=c_secret, scope = scope, redirect_uri="http://localhost:8888/callback")

sp = spotipy.Spotify(client_credentials_manager= client_credentials_manager)

# https://spotipy.readthedocs.io/en/2.19.0/ then go to examples

urn = 'spotify:artist:20sxb77xiYeusSH8cVdatc'

artist = sp.artists("20sxb77xiYeusSH8cVdatc")
#print(artist)

df = pd.read_csv("artist-uris.csv.csv")
# print(df)

user = sp.user("hvz0hy2bkt2sqyteo81p5ac6s")
#print(user)

#current_user_saved_tracks_contain


a = ["https://open.spotify.com/track/3QO1m6i0nsrp8aOnapvbkx?si=6e45c7a24c9e4760"]

# cst = sp.current_user_recently_played()
# print(cst)
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# t2 = cst.keys()
# print(t2)
#
# print("\n\n")
# print("\n\n")
# print("\n\n")

# print(cst["items"][0]["track"][])

#spotify -> song -> control click -> share -> copy song link

#current_user_top_artists
current_tracks = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')

print(current_tracks) #api response
# print(len(current_tracks)) #num of key value pairs

print("ARTIST OBJECTS")
print("\n")
print(current_tracks["items"])

count = 0
a = [] #a is a list containing all the artist objects

for i in current_tracks["items"]: #i is the dictionary
    count+=1
    print(f"{count}. {i['name']}") #can't print count+=1 the process so calc above
    a.append(Artist(i["id"], i["name"], i["followers"]["total"], i["genres"], i["popularity"])) #creating an object out of the first track -> like you are are initialising something
print('\n')
print(a)

print("mango")

for i in a:
    print(i)
    print("\n")

print("lychee")

print(a[1].followers)
print(a[2].genres)
print(a[2].genres_property())


# print(a[0]) #for the dataframe value -> use list comprehension to select all the column items from a -> line 68 -> is what is already assigning the values to the parameters used to initialise the class -> so now to access these values -> as self.name = "Kanye West " -> use . -> get the property of the class from the variable that holds this value
da = {"ID":[i.id for i in a], "artist":[i.name for i in a],"followers":[i.followers for i in a],"genres":[i.genres for i in a], "popularity":[i.popularity for i in a]} #when making a df -> make a dict -> where the key is the column name and the value is the list so what goes into the column
df = pd.DataFrame(da) # key:value -> key is column name
print(df)



#for loop
#append property of class in the abcd list


#
# da = {"ID":e, "artist":a,"followers":b,"genres":c, "popularity":d}

# print(current_tracks)
print("\n\n")
print("\n\n")
print("\n\n")
print(current_tracks["items"][0].keys())
print(current_tracks["items"][0]["followers"])
print(current_tracks["items"][0]["genres"])
print(current_tracks["items"][0]["popularity"])
print(current_tracks["items"][0]["id"])

#create a dataframe -> where each of the row is a singer/artist -> where each thing will be a new column

# df = pd.DataFrame(da) # key:value -> key is column name
# print(df)
df.to_csv("artist_info.csv")

#each artist is a class -> initialise properties with data

# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][0]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][1]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][2]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][3]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][4]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][5]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][6]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][7]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][8]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print(current_tracks["items"][9]["name"])
# print("\n\n")
# print("\n\n")
# print("\n\n")

#current_user_top_tracks
#Artist(i["id"], i["name"], i["followers"]["total"], i["genres"], i["popularity"])
print("user top track")
top_tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
print(top_tracks)
print("\n\n")
print(top_tracks["items"][0]["artists"][0]["name"])
print("\n\n")
print(top_tracks["items"][0]["name"]) #name of track
print("\n\n")
print(top_tracks["items"][0]["album"]["name"])
print("\n\n")
print(top_tracks["items"][0]["artists"][0]["id"])
print("\n\n")
print(top_tracks["items"][0]["id"]) #id of the track
print("\n\n")
print(top_tracks["items"][0]["popularity"])
print("\n\n")
print(top_tracks["items"][0]["type"])

#instead of initialising all the objects in Artist.py
#create a  list in main -> that will use the class Artist.py to append all the objects in a list
#use a for loop to go through the list of objects
#use indexing -> b[i] -> where i is the number of the track -> b[0], b[1], b[2]
#where each of the above is an object -> have access to the dot properties -> line 186

print("watercress")
print("\n")
print(top_tracks["items"])
#each dictionary in the list contains all the info for the class -> search each dict for the id's only
#how the for loop works -> go through the first dict -> select the id, artist name, name, album name, artist id, popularity and type for one object in the api list
#use the information from the first dictionary to initialise the class then this will activate the str function
#the information from the first dictionary will be appended to the list
#use the for loop -> where each value of i will go through the next object in the api list -> repeat the steps above and append it to the existing list
#the list should contain a list of objects where each object contains the id, artist name, name, album name, artist id, popularity and type

b = [] #list of objects
for i in top_tracks["items"]:
    b.append(Track(i["id"], i["artists"][0]["name"], i["name"], i["album"]["name"], i["artists"][0]["id"], i["popularity"], i["type"])) #append the same order as the class

print("starfish")

for i in b: #i is each object in the list -> when printing -> looping through the list or use a data frame -> trigger the str function -> print in the terminal as formatted in the str function
    print(i) #printing out each object in list -> one by one -> print object -> will automatically print out the str function
    print()

print(b[1].artist_name)


db = {"ID":[i.id for i in b], "Artist Name":[i.artist_name for i in b], "Track Name":[i.track_name for i in b], "Album Name":[i.album_name for i in b], "Artist ID":[i.artist_id for i in b], "Popularity":[i.popularity for i in b], "Type":[i.type for i in b]}
df1 = pd.DataFrame(db) #key:value -> key is column name
print(df1)

df1.to_csv("track_info.csv")

#current_user_top_playlists
print("\n")
top_playlists= sp.current_user_playlists(limit=50, offset=0)
print(top_playlists)
print("\n\n")
print(top_playlists.keys())
print("\n\n")
print("cherry897")
print(top_playlists["items"][0].keys())
print("\n\n")
print("collaborative")
print(top_playlists["items"][0]["collaborative"])
print("\n\n")
print("description")
print(top_playlists["items"][0]["description"])
print("\n\n")
print("external_urls")
print(top_playlists["items"][0]["external_urls"])
print("\n\n")
print("href")
print(top_playlists["items"][0]["href"])
print("\n\n")
print("id")
print(top_playlists["items"][0]["id"])
print("\n\n")
print("images")
print(top_playlists["items"][0]["images"])
print("\n\n")
print("name")
print(top_playlists["items"][0]["name"]) #playlist name
print("\n\n")
print("owner")
print(top_playlists["items"][0]["owner"])
print("primary_color")
print(top_playlists["items"][0]["primary_color"])
print("\n\n")
print("public")
print(top_playlists["items"][0]["public"])
print("\n\n")
print("snapshot_id")
print(top_playlists["items"][0]["snapshot_id"])
print("\n\n")
print("tracks")
print(top_playlists["items"][0]["tracks"])
print("\n\n")
print("type")
print(top_playlists["items"][0]["type"])
print("\n\n")
print("uri")
print(top_playlists["items"][0]["uri"])



#search artist

# name = "Kanye West"
# search_artist = sp.search(q='artist:' + name, type='artist')
# print(search_artist)
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# k1 = search_artist.keys()
#
# print(k1)
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
#
# print(search_artist["artists"].keys())
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(search_artist["artists"]["items"][0].keys())
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
#
# print(search_artist["artists"]["items"][0]["followers"]["total"])

# print(search_artist["artists"]["items"][0]['genres'])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")



# track_results = sp.search(q="year:2020", type = "track", limit = 50)
#
# print(track_results)
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# t2 = track_results.keys()
#
# print(t2)
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"].keys())
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"]["href"])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
# print("BANANA")
#
# print(track_results["tracks"]["items"])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"]["items"][0])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"]["items"][0].keys())
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"]["items"][0]["album"])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"]["items"][0]["album"]['artists'])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
# print(track_results["tracks"]["items"][0]["album"]['artists'][0])
#
# print("\n\n")
# print("\n\n")
# print("\n\n")
#
#
# print(track_results["tracks"]["items"][0]["album"]['artists'][0]['external_urls'])

#

# weirdly erroring but should not be

# print("\n\n\n\n")
# print("specific playlist")
# playlists = sp.playlist(playlist_id = top_playlists["items"][0]["uri"], fields=None, market=None, additional_types=('track', ))
# print("balloon")
# print(playlists)
# print("\n")
# print(playlists.keys())
# print("\n")
# print('pineapplemania')
# print(playlists["collaborative"]) #maybe means if you sharing with someone
# print("\n")
# print(playlists["description"])
# print("\n")
# print(playlists["external_urls"])
# print("\n")
# print("FOLLOWERS!")
# print(playlists["followers"]["total"]) #see the number of people following the playlist -> get the total not the href
# print("\n")
# print(playlists["href"])
# print("\n")
# print("ID")
# print(playlists["id"]) #id of the playlist
# print("\n")
# print(playlists["images"])
# print("\n")
# print("PLAYLIST NAME")
# print(playlists["name"]) #useful
# print("\n")
# print("OWNER")
# print(playlists["owner"]["display_name"]) #display_name
# print("\n")
# print(playlists["primary_color"])
# print("\n")
# print("PUBLIC")
# print(playlists["public"]) #if everyone can see it
# print("\n")
# print(playlists["snapshot_id"])
# print("\n")
# print("banana")
# print(playlists["tracks"]) #give a lot of info -> artist name, track name, album name, popularity, total_tracks
# print("\n")
#
# print(playlists["type"])
# print("\n")
# print(playlists["uri"])
#
# print("blossom")
# tl = []
# print("\n\n\n")
# print("KEYS")
#
# print("bluebutterfly")
# for i in playlists["tracks"]:
#     print(i)
#
#     # d = {"artist_name": }
# print("\n\n\n")
#
# print("VALUES")
# for i in playlists["tracks"]:
#   print(playlists["tracks"][i]) #where i is the key -> get all the values
#   print("\n\n\n")
#
# #get the name of the artist -> using the key items
# for i in playlists["tracks"]:
#     print("KEYS123!")
#     print(playlists["tracks"]["items"][0].keys()) #where i is the key -> get all the values
#     print("\n\n\n")
#     print("strawberry")
#     print(playlists["tracks"]["items"][0]["track"]["artists"]) #only one list -> always index 0
#     print("apple!")
#     print(playlists["tracks"]["items"][0]["track"]["artists"][0]["name"])
#
# #name of track
# for i in playlists["tracks"]:
#     print("KEYS!")
#     print(playlists["tracks"]["items"][0].keys()) #where i is the key -> get all the values
#     print("\n\n\n")
#     print("melonhead")
#     print(playlists["tracks"]["items"][0]["track"]["name"])
#
# #name of album
# for i in playlists["tracks"]:
#     print("KEYS!")
#     print(playlists["tracks"]["items"][0].keys()) #where i is the key -> get all the values
#     print("\n\n\n")
#     print("pineapplehead")
#     print(playlists["tracks"]["items"][0]["track"].keys())
#     print("\n\n\n")
#     print(playlists["tracks"]["items"][0]["track"]["album"].keys())
#     print("\n\n\n")
#     print(playlists["tracks"]["items"][0]["track"]["album"]["name"])
#
# #popularity -> how often and how recent the album is played
# for i in playlists["tracks"]:
#     print("KEYS!")
#     print(playlists["tracks"]["items"][0].keys()) #where i is the key -> get all the values
#     print("\n\n\n")
#     print("melonhead")
#     print(playlists["tracks"]["items"][0]["track"].keys())
#     print("\n\n\n")
#     print(playlists["tracks"]["items"][0]["track"]["popularity"])
#
# #total tracks in album?
# for i in playlists["tracks"]:
#     print("KEYS!")
#     print(playlists["tracks"]["items"][0].keys()) #where i is the key -> get all the values
#     print("\n\n\n")
#     print("pineapplehead")
#     print(playlists["tracks"]["items"][0]["track"].keys())
#     print("\n\n\n")
#     print(playlists["tracks"]["items"][0]["track"]["album"].keys())
#     print("\n\n\n")
#     print(playlists["tracks"]["items"][0]["track"]["album"]["total_tracks"])
#
# track_list = [] #[{}, {}, {}] -> each {} holds info for a track
# for i in range(len(playlists["tracks"]["items"])): #loop through the thing that is before the i
#     track_info = {}
#     track_info["Artist name"] = playlists["tracks"]["items"][i]["track"]["artists"][0]["name"]
#     track_info["Track name"] = playlists["tracks"]["items"][i]["track"]["name"]
#     track_info["Album name"] = playlists["tracks"]["items"][i]["track"]["album"]["name"]
#     track_info["Popularity"] = playlists["tracks"]["items"][i]["track"]["popularity"]
#     track_info["Total tracks"] = playlists["tracks"]["items"][i]["track"]["album"]["total_tracks"]
#     track_list.append(track_info)
# print("\n\n\n")
# print(track_list)
#
# artist_names = []
# for i in range(len(track_list)):
#     artist_names.append(track_list[i]["Artist name"])
#
# print("wavy")
# print(artist_names)
# print("\n")
#
# track_names = []
# for i in range(len(track_list)):
#     track_names.append(track_list[i]["Track name"])
# print(track_names)
# print("\n")
#
# album_names = []
# for i in range(len(track_list)):
#     album_names.append(track_list[i]["Album name"])
# print(album_names)
# print("\n")
#
# popularity = []
# for i in range(len(track_list)):
#     popularity.append(track_list[i]["Popularity"])
# print(popularity)
# print("\n")
#
# total_tracks = []
# for i in range(len(track_list)):
#     total_tracks.append(track_list[i]["Total tracks"])
# print(total_tracks)

##############################

#a bit confused with playlists/top playlists





c = []

for i in top_playlists["items"]:
   pl = sp.playlist(playlist_id=i["uri"], fields=None, market=None,
                           additional_types=('track',))
   al = []  #artist list #look at class -> initialise with the track list -> need to create a track list to initalise the Playlist class below
   tl = [] #track list
   alb_l = [] #album list
   tp = [] #total popularity list
   tt = [] #total track list

    # if you use in -> can replace pl["tracks"]["items"] with j
    #if you use range -> you have to do it as you would above -> line 494
   for j in pl["tracks"]["items"]: #the pl["tracks"]["items"] for that specific i
       al.append(j["track"]["artists"][0]["name"])
       tl.append(j["track"]["name"])
       alb_l.append(j["track"]["album"]["name"])
       tp.append(j["track"]["popularity"])

    #printed print(j["track"]["album"]) -> saw that not every track in the playlist has a ["total_tracks"]
    #because a track in the playlist could belong to an album that only has itself as a track and therefore does not have a total number of tracks but only one track
    # try except below -> try works as an if statement where you try to append the total_tracks into the list and if it does not exist then you append that number 1 instead
    #where 1 is one track in the album
       try:
           tt.append(j["track"]["album"]["total_tracks"])
       except:
           tt.append(1) #for one song



   c.append(Playlist(pl["id"], pl["name"], pl["owner"]["display_name"], pl["followers"]["total"], pl["collaborative"], pl["public"], al, tl, alb_l, tp, tt)) #append the same order as the class

print("tulip")

for i in c: #i is each object in the list -> when printing -> looping through the list or use a data frame -> trigger the str function -> print in the terminal as formatted in the str function
    print(i) #printing out each object in list -> one by one -> print object -> will automatically print out the str function
    print()

# artist_top_tracks(artist_id, country='US')
# Get Spotify catalog information about an artist’s top 10 tracks by country.
#
# Parameters:
# artist_id - the artist ID, URI or URL
# country - limit the response to one particular country.

#don't want actions -> only want functions that return something
#artist_top_tracks -> get the artist id -> use as a variable and test put in the api

#country_codes= ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']


artist_id = {"Stormzy":"2SrSdSvpminqmStGELCSNd", "Bruno Mars":"0du5cEVh5yTK9QJze8zA0C", "Anderson .Paak": "3jK9MiCrA42lLAdMGUZpwa", "Frank Ocean": "2h93pZq0e7k5yf4dywlkpM"}
print("starfish23")

top_artist_tracks = dict() #name of artist: list of all top tracks
for k,v in artist_id.items():
    artist_top_tracks = sp.artist_top_tracks(v, country = "US") #US, UK, DE (germany), FR, IT
    e = []
    for j in artist_top_tracks["tracks"]:
        e.append(Track(j["id"], j["artists"][0]['name'], j["name"], j["album"]["name"], j["artists"][0]['id'], j["popularity"], j["type"]))
    top_artist_tracks[k] = e #the list is made up of track objects

print("snowflake")

for k,v in top_artist_tracks.items():
    print(k)
    print(": ")
    for i in v: #can't print v as is a list containing all of the artists tracks as a result need to use a for loop to through it
        print(i)
    print("\n")

print("\n")
print("tomato")

for i in top_artist_tracks.values(): #values is a compilation of all the lists -> want to go through one list at a time
    for j in i:
        print(j.id)

print("\n")
print("minigolf")

for i in top_artist_tracks["Stormzy"]:
    print(i.id)

#make a dataframe of each artist first
#then concate all the dataframes

print("\n")
print("grapevine2")
print("\n")

dc = {"Rank" : [1,2,3,4,5,6,7,8,9,10], "ID":[i.id for i in top_artist_tracks["Stormzy"]], "Artist Name": [i.artist_name for i in top_artist_tracks["Stormzy"]], "Track Name":[i.track_name for i in top_artist_tracks["Stormzy"]], "Album Name":[i.album_name for i in top_artist_tracks["Stormzy"]], "Artist ID":[i.artist_id for i in top_artist_tracks["Stormzy"]], "Popularity":[i.popularity for i in top_artist_tracks["Stormzy"]], "Type":[i.type for i in top_artist_tracks["Stormzy"]]}
df2 = pd.DataFrame(dc)
print(df2)
df2.to_csv("Stormzy_top_tracks.csv")

dd = {"Rank" : [1,2,3,4,5,6,7,8,9,10], "ID":[i.id for i in top_artist_tracks["Bruno Mars"]], "Artist Name": [i.artist_name for i in top_artist_tracks["Bruno Mars"]], "Track Name":[i.track_name for i in top_artist_tracks["Bruno Mars"]], "Album Name":[i.album_name for i in top_artist_tracks["Bruno Mars"]], "Artist ID":[i.artist_id for i in top_artist_tracks["Bruno Mars"]], "Popularity":[i.popularity for i in top_artist_tracks["Bruno Mars"]], "Type":[i.type for i in top_artist_tracks["Bruno Mars"]]}
df3 = pd.DataFrame(dd)
print(df3)
df3.to_csv("Bruno Mars_top_tracks.csv")

de = {"Rank" : [1,2,3,4,5,6,7,8,9,10], "ID":[i.id for i in top_artist_tracks["Anderson .Paak"]], "Artist Name": [i.artist_name for i in top_artist_tracks["Anderson .Paak"]], "Track Name":[i.track_name for i in top_artist_tracks["Anderson .Paak"]], "Album Name":[i.album_name for i in top_artist_tracks["Anderson .Paak"]], "Artist ID":[i.artist_id for i in top_artist_tracks["Anderson .Paak"]], "Popularity":[i.popularity for i in top_artist_tracks["Anderson .Paak"]], "Type":[i.type for i in top_artist_tracks["Anderson .Paak"]]}
df4 = pd.DataFrame(de)
print(df4)
df4.to_csv("Anderson .Paak_top_tracks.csv")

df = {"Rank" : [1,2,3,4,5,6,7,8,9,10], "ID":[i.id for i in top_artist_tracks["Frank Ocean"]], "Artist Name": [i.artist_name for i in top_artist_tracks["Frank Ocean"]], "Track Name":[i.track_name for i in top_artist_tracks["Frank Ocean"]], "Album Name":[i.album_name for i in top_artist_tracks["Frank Ocean"]], "Artist ID":[i.artist_id for i in top_artist_tracks["Frank Ocean"]], "Popularity":[i.popularity for i in top_artist_tracks["Frank Ocean"]], "Type":[i.type for i in top_artist_tracks["Frank Ocean"]]}
df5 = pd.DataFrame(df)
print(df5)
df5.to_csv("Frank Ocean_top_tracks.csv")

#merge the df
cp = pd.concat([df2, df3, df4, df5])
print(cp)
cp.to_csv("All artists_top_tracks.csv")





print(artist_top_tracks)
print("\n\n")

print("length")
#get the number of tracks from the api
print(len(artist_top_tracks["tracks"]))

print("\n\n")
print(artist_top_tracks.keys())
print("\n\n")
print(artist_top_tracks["tracks"][0].keys())
#'album', 'artists', 'disc_number', 'id', 'name', 'popularity', 'type', 'uri'


print("\n\n")
print(artist_top_tracks["tracks"][0]["album"].keys())
print("\n\n")
#KEYS FOR ALBUM : 'album_type', 'artists', 'id',  'name', 'total_tracks'*, 'type', 'uri'
print(artist_top_tracks["tracks"][0]["album"]["album_type"])
print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["artists"][0].keys())
print("\n\n")
#Keys for artists: 'external_urls', 'id', 'name', 'type', 'uri'
print(artist_top_tracks["tracks"][0]["album"]["artists"][0]["external_urls"]) #link that takes you to the website page
print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["artists"][0]["id"]) #
print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["artists"][0]["name"]) #
print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["artists"][0]["type"])
print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["artists"][0]["uri"]) #api used to do for tracks -> uri is like an online id

print("redcard")
print("\n\n")

print(artist_top_tracks["tracks"][0]["album"]["id"])

print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["name"]) #

print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["total_tracks"])

print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["type"])

print("\n\n")
print(artist_top_tracks["tracks"][0]["album"]["uri"])

print("\n\n")
print(artist_top_tracks["tracks"][0]["artists"][0].keys())

#ORIGINAL KEYS: 'album', 'artists', 'disc_number', 'id', 'name', 'popularity', 'type', 'uri'

#KEYS FOR Artists after tracks : 'external_urls', 'id', 'name', 'type', 'uri' -> refer to line 600
print("\n\n")
print(artist_top_tracks["tracks"][0]["artists"][0]['external_urls'])
print("\n\n")
print(artist_top_tracks["tracks"][0]["artists"][0]['id'])
print("\n\n")
print(artist_top_tracks["tracks"][0]["artists"][0]['name'])
print("\n\n")
print(artist_top_tracks["tracks"][0]["artists"][0]['type'])
print("\n\n")
print(artist_top_tracks["tracks"][0]["artists"][0]['uri'])

print("\n\n")
print(artist_top_tracks["tracks"][0]["disc_number"])

print("\n\n")
print(artist_top_tracks["tracks"][0]["id"]) #

print("\n\n")
print(artist_top_tracks["tracks"][0]["name"])

print("\n\n")
print(artist_top_tracks["tracks"][0]["popularity"]) #

print("\n\n")
print(artist_top_tracks["tracks"][0]["type"]) #

print("\n\n")
print(artist_top_tracks["tracks"][0]["uri"])

#each item in the list is the object of the track class
#id, artist_name, track_name, album_name, artist_id, popularity, type

# for j in e: #i is each object in the list -> when printing -> looping through the list or use a data frame -> trigger the str function -> print in the terminal as formatted in the str function
#     print(j) #printing out each object in list -> one by one -> print object -> will automatically print out the str function
#     print()

# print("limekiwi")
# artist_top_tracks2 = sp.artist_top_tracks(artist_id, country = "DE") #germany
# print(artist_top_tracks2)
# print("\n\n")
# print(artist_top_tracks2["tracks"][0].keys())
# print("\n\n")
# #'external_urls', 'id', 'name', 'type', 'uri'
# print(artist_top_tracks2["tracks"][0]["album"]["artists"][0]["external_urls"]) #link that takes you to the website page
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["artists"][0]["id"])
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["artists"][0]["name"])
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["artists"][0]["type"])
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["artists"][0]["uri"]) #api used to do for tracks -> uri is like an online id
#
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["id"])
#
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["name"])
#
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["type"])
#
# print("\n\n")
# print(artist_top_tracks2["tracks"][0]["album"]["uri"])
#
# f = []
# for i in artist_top_tracks["tracks"]:
#     f.append(Track(i["id"], i["artists"][0]['name'], i["name"], i["album"]["name"], i["artists"][0]['id'], i["popularity"], i["type"]))
#
# for i in f: #i is each object in the list -> when printing -> looping through the list or use a data frame -> trigger the str function -> print in the terminal as formatted in the str function
#     print(i) #printing out each object in list -> one by one -> print object -> will automatically print out the str function
#     print()

#
# print("pineapplemagic")
# artist_top_tracks3 = sp.artist_top_tracks(artist_id, country = "FR")
# print(artist_top_tracks3)
# print("\n\n")
# print(artist_top_tracks3["tracks"][0].keys())
# print("\n\n")
# #'external_urls', 'id', 'name', 'type', 'uri'
# print(artist_top_tracks3["tracks"][0]["album"]["artists"][0]["external_urls"]) #link that takes you to the website page
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["artists"][0]["id"])
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["artists"][0]["name"])
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["artists"][0]["type"])
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["artists"][0]["uri"]) #api used to do for tracks -> uri is like an online id
#
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["id"])
#
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["name"])
#
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["type"])
#
# print("\n\n")
# print(artist_top_tracks3["tracks"][0]["album"]["uri"])
#
# print("mangomadness")
#
# artist_top_tracks4 = sp.artist_top_tracks(artist_id, country = "IT")
# print(artist_top_tracks4)
# print("\n\n")
# print(artist_top_tracks4["tracks"][0].keys())
# print("\n\n")
# #'external_urls', 'id', 'name', 'type', 'uri'
# print(artist_top_tracks4["tracks"][0]["album"]["artists"][0]["external_urls"]) #link that takes you to the website page
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["artists"][0]["id"])
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["artists"][0]["name"])
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["artists"][0]["type"])
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["artists"][0]["uri"]) #api used to do for tracks -> uri is like an online id
#
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["id"])
#
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["name"])
#
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["type"])
#
# print("\n\n")
# print(artist_top_tracks4["tracks"][0]["album"]["uri"])
#
# #doesn't work for uk
# artist_top_tracks5 = sp.artist_top_tracks(artist_id, country = "GB")
# print(artist_top_tracks5)
# print(artist_top_tracks5["tracks"][0].keys())
# print("\n\n")
# #'external_urls', 'id', 'name', 'type', 'uri'
# print(artist_top_tracks5["tracks"][0]["album"]["artists"][0]["external_urls"]) #link that takes you to the website page
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["artists"][0]["id"])
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["artists"][0]["name"])
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["artists"][0]["type"])
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["artists"][0]["uri"]) #api used to do for tracks -> uri is like an online id
#
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["id"])
#
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["name"])
#
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["type"])
#
# print("\n\n")
# print(artist_top_tracks5["tracks"][0]["album"]["uri"])
#
#
#
#
#
#
#
#
#
#
#
#

print("\n\n")
print("bird")
#current_user_playing_track() or currently_playing -> just look at the track class and see what is needed
#id, artist_name, track_name, album_name, artist_id, popularity, type
# current_track = sp.current_user_playing_track()
# print(current_track)
# print("\n\n")
# print(current_track.keys()) #nonetype object has no attribute keys -> it is a nonetype object as you are not playing any song
# print("\n\n")
# print(current_track["timestamp"])
# print("\n\n")
# print(current_track["context"])
# print("\n\n")
# print(current_track['progress_ms'])
# print("\n\n")
# print(current_track['item'].keys())
# print("\n\n")
#all the keys: 'album', 'artists', 'available_markets', 'explicit', 'id', 'is_local', 'name', 'popularity', 'type', 'uri'
# print(current_track['item']["album"].keys())
# #['album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri']
# print("\n\n")
# print(current_track['item']["album"]["album_type"])
# print("\n\n")
# print("golf")
# print("\n\n")
# print(current_track['item']["album"]['artists'])
# print("\n\n")
# print(current_track['item']["album"]['artists'][0].keys())
# #['external_urls', 'href', 'id', 'name', 'type', 'uri']
# print("\n\n")
# print(current_track['item']["album"]['artists'][0]['external_urls'])
# print("\n\n")
# print(current_track['item']["album"]['artists'][0]['href'])
# print("\n\n")
# print(current_track['item']["album"]['artists'][0]['id']) #*
# print("\n\n")
# print(current_track['item']["album"]['artists'][0]['name']) #*
# print("\n\n")
# print(current_track['item']["album"]['artists'][0]['type'])
# print("\n\n")
# print(current_track['item']["album"]['artists'][0]['uri'])
# print("\n\n")
# print(current_track['item']["album"]["album_type"])
# print("\n\n")
# print(current_track['item']["id"]) #*
# print("\n\n")
# print(current_track['item']["album"]["name"]) #*
# print("\n\n")
# print(current_track['item']["name"]) #* track_name
# print("\n\n")
# print(current_track['item']["popularity"]) #*
# print("\n\n")
# print(current_track['item']["type"]) #*
#
# #there is only one track the current track in this case so a for loop and dict is not needed -> do not need a list -> create an object variable
#
#
# CT = (Track(current_track['item']["id"], current_track['item']["album"]['artists'][0]['name'], current_track['item']["name"], current_track['item']["album"]["name"], current_track['item']["album"]['artists'][0]['id'], current_track['item']["popularity"], current_track['item']["type"]))
#
# print(CT)
#
# #id, artist_name, track_name, album_name, artist_id, popularity, type
# dh = {"ID":[CT.id], "Artist Name":[CT.artist_name], "Track Name":[CT.track_name], "Album Name":[CT.album_name], "Artist ID":[CT.artist_id], "Popularity":[CT.popularity], "Type":[CT.type]}
# df6 = pd.DataFrame(dh) #key:value -> key is column name
# print("\n\n")
# print("dataframe6")
# print("\n\n")
# print(df1)
#
# df6.to_csv("current_track_info.csv")



#audio_analysis?
# print("\n\n")
# print("shoe")
# audio_analysis = sp.audio_analysis("62vpWI1CHwFy7tMIcSStl8")
# print(audio_analysis)
# print("\n\n")
# print(audio_analysis.keys())
# #['meta', 'track', 'bars', 'beats', 'sections', 'segments', 'tatums']
#
# print("\n\n")
# print("starlight7")
# print("\n\n")
# print(audio_analysis['meta'])
# print("\n\n")
# print(audio_analysis['track'])
# print("\n\n")
# print(audio_analysis['bars'][0])
# print("\n\n")
# print(audio_analysis['sections'][0])
# print("\n\n")
# print(audio_analysis['segments'][0])
# print("\n\n")
# print(audio_analysis['tatums'][0])
#
#
# #audio_features -> audio_features(tracks=[]) -> tracks
# print("\n\n")
# print("shoe2")
# audio_features = sp.audio_features("62vpWI1CHwFy7tMIcSStl8") #could have a list of audio features in here
# print(audio_features[0].keys())
# #['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
# print("\n\n")
# print(audio_features[0]['danceability'])
# print("\n\n")
# print(audio_features[0]['energy'])
# print("\n\n")
# print(audio_features[0]['key'])
# print("\n\n")
# print(audio_features[0]['loudness'])
# print("\n\n")
# print(audio_features[0]['mode'])
# print("\n\n")
# print(audio_features[0]['speechiness'])
# print("\n\n")
# print(audio_features[0]['acousticness'])
# print("\n\n")
# print(audio_features[0]['instrumentalness'])
# print("\n\n")
# print(audio_features[0]['liveness'])
# print("\n\n")
# print(audio_features[0]['valence'])
# print("\n\n")
# print(audio_features[0]['tempo'])
# print("\n\n")
# print(audio_features[0]['type'])
# print("\n\n")
# print(audio_features[0]['id'])
# print("\n\n")
# print(audio_features[0]['uri'])
# print("\n\n")
# print(audio_features[0]['track_href'])
# print("\n\n")
# print(audio_features[0]['analysis_url'])
# print("\n\n")
# print(audio_features[0]['duration_ms'])
# print("\n\n")
# print(audio_features[0]['time_signature'])

# new_releases
#new_releases(country=None, limit=20, offset=0)

print("\n\n")
print("rabbit9")
new_releases = sp.new_releases(country="US", limit=20, offset=0) #None, US, GB
print(new_releases.keys())

print(new_releases["albums"].keys())
#'href', 'items', 'limit', 'next', 'offset', 'previous', 'total'
print("\n")
print(new_releases["albums"]["href"])

print("\n\n")
print("artist7")
print(new_releases["albums"]["items"][0].keys())
#keys in items -> dict_keys(['album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri'])
print("\n\n")
print(new_releases["albums"]["items"][0]['album_type'])
print("\n\n")
print(new_releases["albums"]["items"][0]['artists'][0]["external_urls"])
print("\n\n")
print(new_releases["albums"]["items"][0]['artists'][0]["href"])
print("\n\n")
print(new_releases["albums"]["items"][0]['artists'][0]["id"]) #artist_id
print("\n\n")
print(new_releases["albums"]["items"][0]['artists'][0]["name"]) #artist_name
print("\n\n")
print(new_releases["albums"]["items"][0]['artists'][0]["type"])
print("\n\n")
print(new_releases["albums"]["items"][0]['artists'][0]["uri"])


print("\n\n")
print(new_releases["albums"]["items"][0]['available_markets'])
print("\n\n")
print(new_releases["albums"]["items"][0]['external_urls'])
print("\n\n")
print(new_releases["albums"]["items"][0]['href'])
print("\n\n")
print(new_releases["albums"]["items"][0]['id']) #album_id
print("\n\n")
print(new_releases["albums"]["items"][0]['images'][0].keys())
#['height', 'url', 'width']
print(new_releases["albums"]["items"][0]['images'][0]["height"])
print("\n\n")
print(new_releases["albums"]["items"][0]['images'][0]["url"])
print("\n\n")
print(new_releases["albums"]["items"][0]['images'][0]["width"])

print("\n\n")
print(new_releases["albums"]["items"][0]['name']) #album_name
print("\n\n")
print(new_releases["albums"]["items"][0]['release_date']) #release_date
print("\n\n")
print(new_releases["albums"]["items"][0]['release_date_precision'])
print("\n\n")
print(new_releases["albums"]["items"][0]['total_tracks']) #total_tracks
print("\n\n")
print(new_releases["albums"]["items"][0]['type']) #album_type
print("\n\n")
print(new_releases["albums"]["items"][0]['uri'])


print("\n\n")
print(new_releases["albums"]["limit"])
print("\n\n")
print(new_releases["albums"]["next"])
print("\n\n")
print(new_releases["albums"]["offset"])
print("\n\n")
print(new_releases["albums"]["previous"])
print("\n\n")
print(new_releases["albums"]["total"])

new_release_albums = []
for i in range(len(new_releases["albums"])):
    new_release_albums.append(Album(new_releases["albums"]["items"][i]['id'], new_releases["albums"]["items"][i]['name'], new_releases["albums"]["items"][i]['type'], new_releases["albums"]["items"][i]['type'], new_releases["albums"]["items"][i]['artists'][0]["id"], new_releases["albums"]["items"][i]['artists'][0]["name"], "none", new_releases["albums"]["items"][i]['release_date'], new_releases["albums"]["items"][i]['total_tracks'], "none"))

for i in new_release_albums:
    print(i)
    print("\n")




# d8 = {"Track ID":[i.id for i in new_release_albums], "Album Name":[i.album_name for i in new_release_albums],"Album Type":[i.artist_id for i in new_release_albums],"Artist ID":[i.artist_id for i in track_objects], "Album Name":[i.album_name for i in track_objects], "Artist ID":[i.artist_id for i in track_objects], "Popularity":[i.popularity for i in track_objects], "Type":[i.type for i in track_objects]}
# print("\n")
# df8 = pd.DataFrame(d8)
# print("dataframe7")
# print("\n")
# print(df8) #print dataframe7
#
# df8.to_csv("current_user_saved_tracks.csv")


#current_user_followed_artists(limit=20, after=None)
print("\n\n")
print("coffee3")
cufa = sp.current_user_followed_artists(limit=20, after=None) #None, US, GB
print(cufa["artists"].keys())
#dict_keys(['items', 'next', 'total', 'cursors', 'limit', 'href'])
print(cufa["artists"]["items"][0].keys())
#dict_keys(['external_urls', 'followers', 'genres', 'href', 'id', 'images', 'name', 'popularity', 'type', 'uri'])
print("\n\n")
print(cufa["artists"]["items"][0]["external_urls"])
print("\n\n")
print(cufa["artists"]["items"][0]["followers"])
print("\n\n")
print(cufa["artists"]["items"][0]["genres"])
print("\n\n")
print(cufa["artists"]["items"][0]["href"])
print("\n\n")
print(cufa["artists"]["items"][0]["id"])
print("\n\n")
print("i9g")
print(cufa["artists"]["items"][0]["images"][0].keys())
print("\n\n")
print(cufa["artists"]["items"][0]["images"][0]["height"])
print("\n\n")
print(cufa["artists"]["items"][0]["images"][0]["url"])
print("\n\n")
print(cufa["artists"]["items"][0]["images"][0]["width"])
print("\n\n")
print(cufa["artists"]["items"][0]["name"])
print("\n\n")
print(cufa["artists"]["items"][0]["popularity"])
print("\n\n")
print(cufa["artists"]["items"][0]["type"])
print("\n\n")
print(cufa["artists"]["items"][0]["uri"])

print("\n\n")
print(cufa["artists"]["next"])
print("\n\n")
print(cufa["artists"]["total"])
print("\n\n")
print(cufa["artists"]["cursors"]["after"])
print("\n\n")
print(cufa["artists"]["limit"])
print("\n\n")
print(cufa["artists"]["href"])


#current_user_saved_albums -> album class
print("\n\n")
print("quicksilver")
#only takes the liked songs/ones that have been downloaded to the playlist
cusa = sp.current_user_saved_albums(limit=20, offset=0, market=None) #None, US, GB

print("\n\n")
print(cusa)
print("\n\n")
print("raspberries90")
print("\n\n")
print(cusa.keys())
print("\n\n")


# #dict_keys(['href', 'items', 'limit', 'next', 'offset', 'previous', 'total'])
print(cusa["href"])
print("\n\n")
print(cusa["items"][0].keys())
print(cusa["items"][0]["added_at"])
print("\n\n")
print(cusa["items"][0]["album"].keys())
print("\n\n")
print("Superhero7")
print("\n\n")
#['album_type', 'artists', 'available_markets', 'copyrights', 'external_ids', 'external_urls', 'genres', 'href', 'id', 'images', 'label', 'name', 'popularity', 'release_date', 'release_date_precision', 'total_tracks', 'tracks', 'type', 'uri']
print(cusa["items"][0]["album"]["album_type"]) #*1
print("\n\n")
print(cusa["items"][0]["album"]["id"]) #*1
print("\n\n")
print(cusa["items"][0]["album"]["name"]) #*1
print("\n\n")
#dict_keys(['external_urls', 'href', 'id', 'name', 'type', 'uri'])
print(cusa["items"][0]["album"]["artists"][0]["external_urls"])
print("\n\n")
print(cusa["items"][0]["album"]["artists"][0]["href"])
print("\n\n")
print(cusa["items"][0]["album"]["artists"][0]["id"])#*1
print("\n\n")
print(cusa["items"][0]["album"]["artists"][0]["name"])#*1
print("\n\n")
print(cusa["items"][0]["album"]["artists"][0]["type"])
print("\n\n")
print(cusa["items"][0]["album"]["artists"][0]["uri"])
print("\n\n")
print(cusa["items"][0]["album"]["available_markets"])
print("\n\n")
#dict_keys(['text', 'type'])
print(cusa["items"][0]["album"]["copyrights"][0]["text"])
print("\n\n")
print(cusa["items"][0]["album"]["copyrights"][0]["type"])
print("\n\n")
print(cusa["items"][0]["album"]["external_ids"]["upc"])
print("\n\n")
print(cusa["items"][0]["album"]["genres"])
print("\n\n")
print(cusa["items"][0]["album"]["href"])
print("\n\n")
print("a1")
print("\n\n")
print("orange7")
print("\n\n")
print(cusa["items"][0]["album"]["id"]) #*1
print("\n\n")
print(cusa["items"][0]["album"]["images"])
print("\n\n")
print(cusa["items"][0]["album"]["label"])
print("\n\n")
print("b1")
print("\n\n")
print(cusa["items"][0]["album"]["name"]) #*1
print("\n\n")
print("c1")
print("\n\n")
print(cusa["items"][0]["album"]["popularity"]) #*1
print("\n\n")
print("d1")
print("\n\n")
print(cusa["items"][0]["album"]["release_date"]) #*1
print("\n\n")
print(cusa["items"][0]["album"]["release_date_precision"])
print("\n\n")
print(cusa["items"][0]["album"]["release_date_precision"])
print("\n\n")
print("e1")
print("\n\n")
print(cusa["items"][0]["album"]["total_tracks"]) #*1
print("\n\n")
print("tracks90210")
print("\n\n")
print(cusa["items"][0]["album"]["tracks"].keys())
#['href', 'items', 'limit', 'next', 'offset', 'previous', 'total']
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["href"])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0].keys())
#dict_keys(['artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_urls', 'href', 'id', 'is_local', 'name', 'preview_url', 'track_number', 'type', 'uri'])
print(cusa["items"][0]["album"]["tracks"]["items"][0]['artists'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['available_markets'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['disc_number'])
print("\n\n")
print("f1")
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['duration_ms']) #*1
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['explicit'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['external_urls']["spotify"])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['href'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['id'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['is_local'])
print("\n\n")
print("g1")
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['name']) #*1
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['preview_url'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['track_number'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['type'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["items"][0]['uri'])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["limit"])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["next"])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["offset"])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["previous"])
print("\n\n")
print(cusa["items"][0]["album"]["tracks"]["total"])
print("\n\n")
print(cusa["items"][0]["album"]["type"])
print("\n\n")
print(cusa["items"][0]["album"]["uri"])

print("\n\n")
print(cusa["limit"])

print("\n\n")
print(cusa["next"])

print("\n\n")
print(cusa["offset"])

print("\n\n")
print(cusa["previous"])

print("\n\n")
print(cusa["total"])

print("\n\n")
print("lemontart1")
print("\n\n")


track_objects1 = []
for i in range(len(cusa["items"])):
         track_objects1.append(Album(cusa["items"][i]["album"]["id"], cusa["items"][i]["album"]["name"], cusa["items"][i]["album"]["album_type"], cusa["items"][i]["album"]["artists"][0]["id"], cusa["items"][i]["album"]["artists"][0]["name"], cusa["items"][i]["album"]["tracks"]["items"][0]['name'], cusa["items"][i]["album"]["release_date"], cusa["items"][i]["album"]["total_tracks"], cusa["items"][i]["album"]["tracks"]["items"][0]['duration_ms'], cusa["items"][i]["album"]["popularity"]))

print("\n")
print("fp1")
print("\n")
for i in track_objects1:
    print(i)
    print("\n")

d6 = {"Album ID":[i.album_id for i in track_objects1], "Album Name":[i.album_name for i in track_objects1],"Album Type":[i.album_type for i in track_objects1],"Artist ID":[i.artist_id for i in track_objects1], "Artist Name":[i.artist_name for i in track_objects1], "Track Name":[i.track_name for i in track_objects1], "Release Date":[i.release_date for i in track_objects1], "Total Tracks":[i.total_tracks for i in track_objects1], "Duration Ms":[i.duration_ms for i in track_objects1], "Popularity":[i.popularity for i in track_objects1]}
print("\n")
df6 = pd.DataFrame(d6)
print("dataframe7")
print("\n")
print(df6) #print dataframe7

df6.to_csv("current_user_saved_albums.csv")

# #dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri'])
# print(cust["items"][0]["track"]["album"].keys())
# print("\n\n")
# print("spf7")
# #dict_keys(['album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri'])
# print(cust["items"][0]["track"]["album"]["album_type"]) # keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["artists"][0].keys())
# #dict_keys(['external_urls', 'href', 'id', 'name', 'type', 'uri'])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["artists"][0]["external_urls"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["artists"][0]["href"])
# print("\n\n")
# print("artist_id5")
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["artists"][0]["id"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["artists"][0]["name"])  #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["artists"][0]["type"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["artists"][0]["uri"])
#
#
#
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["available_markets"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["external_urls"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["href"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["id"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["images"][0])
# print("\n\n")
# print("album_name9")
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["name"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["release_date"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["release_date_precision"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["total_tracks"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["album"]["type"])
# print("\n\n")
# print(cust["items"][0]["track"]["album"]["uri"])
#
#
#
# print("Rosegold")
# print("\n\n")
# #dict_keys(['external_urls', 'href', 'id', 'name', 'type', 'uri'])
# print(cust["items"][0]["track"]["artists"][0]["external_urls"])
# print("\n\n")
# print(cust["items"][0]["track"]["artists"][0]["href"])
# print("\n\n")
# print(cust["items"][0]["track"]["artists"][0]["id"])
# print("\n\n")
# print(cust["items"][0]["track"]["artists"][0]["name"])
# print("\n\n")
# print(cust["items"][0]["track"]["artists"][0]["type"])
# print("\n\n")
# print(cust["items"][0]["track"]["artists"][0]["uri"])
# print("\n\n")
#
# print("goldsmith")
# print(cust["items"][0]["track"]["available_markets"])
# print("\n\n")
# print(cust["items"][0]["track"]["disc_number"])
# print("\n\n")
# print(cust["items"][0]["track"]["duration_ms"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["explicit"])
# print("\n\n")
# print(cust["items"][0]["track"]["external_ids"])
# print("\n\n")
# print(cust["items"][0]["track"]["external_urls"])
# print("\n\n")
# print(cust["items"][0]["track"]["href"])
# print("\n\n")
# print(cust["items"][0]["track"]["id"])
# print("\n\n")
# print(cust["items"][0]["track"]["is_local"])
# print("\n\n")
# print("track_name7")
# print("\n\n")
# print(cust["items"][0]["track"]["name"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["popularity"]) #keep
# print("\n\n*")
# print(cust["items"][0]["track"]["preview_url"])
# print("\n\n")
# print(cust["items"][0]["track"]["track_number"])
# print("\n\n")
# print(cust["items"][0]["track"]["type"])
# print("\n\n")
# print(cust["items"][0]["track"]["uri"])
#
# print("\n\n")
# print(cust["limit"])
#
# print("\n\n")
# print(cust["next"])
#
# print("\n\n")
# print(cust["offset"])
#
# print("\n\n")
# print(cust["previous"])
#
# print("\n\n")
# print(cust["total"])
# print("\n\n")

# #when using -> range length in a for loop
# #add the range(len)
# #in this case i represents the index number
# #instead of starting with i in Album-> we start with cust["items"]
#
# album_objects = []
# for i in range(len(cust["items"])):
#     album_objects.append(Album(cust["items"][i]["track"]["album"]["id"], cust["items"][i]["track"]["album"]["name"], cust["items"][i]["track"]["album"]["type"], cust["items"][i]["track"]["artists"][0]["id"], cust["items"][i]["track"]["artists"][0]["name"], cust["items"][i]["track"]["name"], cust["items"][i]["track"]["album"]["release_date"], cust["items"][i]["track"]["album"]["total_tracks"], cust["items"][i]["track"]["duration_ms"], cust["items"][i]["track"]["popularity"]))
#     print("\n")

#print(album_objects) prints the location of the objects -> hash code

# for i in album_objects:
#     print(i)
#     print("\n")


#When not using range(length) and just in
#can start with i
#like for loop in list -> each value of i will be a value in the list e.g. apple, banana
#i represents the the actually stuff in it -> not the index -> elaborate

# for i in cust["items"]:
#     album_objects.append(Album(i["track"]["album"]["id"], i["track"]["album"]["name"], i["track"]["album"]["type"], i["track"]["artists"][0]["id"], i["track"]["artists"][0]["name"], i["track"]["name"], i["track"]["album"]["release_date"],i["track"]["album"]["total_tracks"], i["track"]["duration_ms"], i["track"]["popularity"]))
#     print("\n")



# d7 = {"Album ID":[i.album_id for i in album_objects], "Album Name":[i.album_name for i in album_objects],"Album Type":[i.album_type for i in album_objects],"Artist ID":[i.artist_id for i in album_objects], "Artist Name":[i.artist_name for i in album_objects], "Track Name":[i.track_name for i in album_objects], "Release Date":[i.release_date for i in album_objects], "Total Tracks":[i.total_tracks for i in album_objects], "Duration MS":[i.duration_ms for i in album_objects], "Popularity":[i.popularity for i in album_objects]} #when making a df -> make a dict -> where the key is the column name and the value is the list so what goes into the column
# df7 = pd.DataFrame(d7) # key:value -> key is column name
# print("\n")
# print("dataframe7")
# print("\n")
# print(df7) #print dataframe7
#
# df7.to_csv("current_user_saved_albums.csv")

#artist_albums
#artist_id, album_type=None, country=None, limit=20, offset=0

print("\n\n")
print("rocket9")
artist_albums = sp.artist_albums(artist_id="2LIk90788K0zvyj2JJVwkJ", album_type=None, country=None, limit=20, offset=0)  #GB, US
print(artist_albums.keys())
#dict_keys(['href', 'items', 'limit', 'next', 'offset', 'previous', 'total'])
print("\n\n")
print(artist_albums['href'])
print("\n\n")
print(artist_albums['items'][0].keys())
#dict_keys(['album_group', 'album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri'])
print("\n\n")
print(artist_albums['items'][0]['album_group'])
print("\n\n")
print(artist_albums['items'][0]['album_type'])
print("\n\n")
print(artist_albums['items'][0]['artists'][0].keys())
#dict_keys(['external_urls', 'href', 'id', 'name', 'type', 'uri'])
print("\n\n")
print(artist_albums['items'][0]['artists'][0]["external_urls"])
print("\n\n")
print(artist_albums['items'][0]['artists'][0]["href"])
print("\n\n")
print(artist_albums['items'][0]['artists'][0]["id"])
print("\n\n")
print(artist_albums['items'][0]['artists'][0]["name"])
print("\n\n")
print(artist_albums['items'][0]['artists'][0]["type"])
print("\n\n")
print(artist_albums['items'][0]['artists'][0]["uri"])
print("\n\n")
print(artist_albums['items'][0]['available_markets'])
print("\n\n")
print(artist_albums['items'][0]['external_urls'])
print("\n\n")
print(artist_albums['items'][0]['href'])
print("\n\n")
print(artist_albums['items'][0]['id'])
print("\n\n")
print(artist_albums['items'][0]['images'])
print("\n\n")
print(artist_albums['items'][0]['name'])
print("\n\n")
print(artist_albums['items'][0]['release_date'])
print("\n\n")
print(artist_albums['items'][0]['release_date_precision'])
print("\n\n")
print(artist_albums['items'][0]['total_tracks'])
print("\n\n")
print(artist_albums['items'][0]['type'])
print("\n\n")
print(artist_albums['items'][0]['uri'])


#current_user_saved_tracks ->track class
print("\n\n")
print("rocket9")
cust = sp.current_user_saved_tracks(limit=20, offset=0, market=None) #None, US, GB

print("\n\n")
print(cust)
print("\n\n")
print(cust.keys())
print("\n\n")
#dict_keys(['href', 'items', 'limit', 'next', 'offset', 'previous', 'total'])
print(cust["href"])
print("\n\n")
print(cust["items"][0]["added_at"])
print("\n\n")
print(cust["items"][0]["track"].keys())
print("\n\n")
#dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri'])
print(cust["items"][0]["track"]["album"].keys())
print("\n\n")
print("spf7")
#dict_keys(['album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri'])
print(cust["items"][0]["track"]["album"]["album_type"]) # keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["artists"][0].keys())
#dict_keys(['external_urls', 'href', 'id', 'name', 'type', 'uri'])
print("\n\n")
print(cust["items"][0]["track"]["album"]["artists"][0]["external_urls"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["artists"][0]["href"])
print("\n\n")
print("artist_id5")
print("\n\n")
print(cust["items"][0]["track"]["album"]["artists"][0]["id"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["artists"][0]["name"])  #keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["artists"][0]["type"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["artists"][0]["uri"])



print("\n\n")
print(cust["items"][0]["track"]["album"]["available_markets"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["external_urls"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["href"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["id"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["images"][0])
print("\n\n")
print("album_name9")
print("\n\n")
print(cust["items"][0]["track"]["album"]["name"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["release_date"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["release_date_precision"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["total_tracks"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["album"]["type"])
print("\n\n")
print(cust["items"][0]["track"]["album"]["uri"])
print("\n\n")


print("Rosegold")
print("\n\n")
#dict_keys(['external_urls', 'href', 'id', 'name', 'type', 'uri'])
print(cust["items"][0]["track"]["artists"][0]["external_urls"])
print("\n\n")
print(cust["items"][0]["track"]["artists"][0]["href"])
print("\n\n")
print(cust["items"][0]["track"]["artists"][0]["id"])
print("\n\n")
print(cust["items"][0]["track"]["artists"][0]["name"])
print("\n\n")
print(cust["items"][0]["track"]["artists"][0]["type"])
print("\n\n")
print(cust["items"][0]["track"]["artists"][0]["uri"])
print("\n\n")

print("goldsmith")
print(cust["items"][0]["track"]["available_markets"])
print("\n\n")
print(cust["items"][0]["track"]["disc_number"])
print("\n\n")
print(cust["items"][0]["track"]["duration_ms"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["explicit"])
print("\n\n")
print(cust["items"][0]["track"]["external_ids"])
print("\n\n")
print(cust["items"][0]["track"]["external_urls"])
print("\n\n")
print(cust["items"][0]["track"]["href"])
print("\n\n")
print(cust["items"][0]["track"]["id"])
print("\n\n")
print(cust["items"][0]["track"]["is_local"])
print("\n\n")
print("track_name7")
print("\n\n")
print(cust["items"][0]["track"]["name"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["popularity"]) #keep
print("\n\n*")
print(cust["items"][0]["track"]["preview_url"])
print("\n\n")
print(cust["items"][0]["track"]["track_number"])
print("\n\n")
print(cust["items"][0]["track"]["type"])
print("\n\n")
print(cust["items"][0]["track"]["uri"])

print("\n\n")
print(cust["limit"])

print("\n\n")
print(cust["next"])

print("\n\n")
print(cust["offset"])

print("\n\n")
print(cust["previous"])

print("\n\n")
print(cust["total"])
print("\n\n")

#list index out of range -> error -> means indexing outside of the list
track_objects = []
for i in range(len(cust["items"])):
    track_objects.append(Track(cust["items"][i]["track"]["id"], cust["items"][i]["track"]["artists"][0]["name"], cust["items"][i]["track"]["name"], cust["items"][i]["track"]["album"]["name"], cust["items"][i]["track"]["album"]["artists"][0]["id"], cust["items"][i]["track"]["popularity"], cust["items"][i]["track"]["type"]))

#print(album_objects) prints the location of the objects -> hash code

for i in track_objects:
    print(i)
    print("\n")


d7 = {"Track ID":[i.id for i in track_objects], "Artist Name":[i.artist_name for i in track_objects],"Track Name":[i.track_name for i in track_objects],"Artist ID":[i.artist_id for i in track_objects], "Album Name":[i.album_name for i in track_objects], "Artist ID":[i.artist_id for i in track_objects], "Popularity":[i.popularity for i in track_objects], "Type":[i.type for i in track_objects]}
print("\n")
df7 = pd.DataFrame(d7)
print("dataframe7")
print("\n")
print(df7) #print dataframe7

df7.to_csv("current_user_saved_tracks.csv")



#artist_related_artists
#2h93pZq0e7k5yf4dywlkpM


print("\n\n")
print("cup9")
ara = sp.artist_related_artists("4LLpKhyESsyAXpc4laK94U")
print("\n\n")
print(ara)
print("\n\n")
print(ara.keys())
print("\n\n")
print(ara["artists"][0].keys())
print("\n\n")
print(ara["artists"][0]['external_urls']["spotify"])
print("\n\n")
print(ara["artists"][0]["followers"]["href"])
print("\n\n")
print(ara["artists"][0]["followers"]["total"]) #*
print("\n\n")
print(ara["artists"][0]["genres"]) #*
print("\n\n")
print(ara["artists"][0]["href"])
print("\n\n")
print(ara["artists"][0]["id"]) #*
print("\n\n")
print(ara["artists"][0]["images"][0])
print("\n\n")
print(ara["artists"][0]["name"]) #*
print("\n\n")
print(ara["artists"][0]["popularity"]) #*
print("\n\n")
print(ara["artists"][0]["type"])
print("\n\n")
print(ara["artists"][0]["uri"])

#dictionary -> all artist name on artist_info are the keys
#values -> are the result of this function in an object

# "Kanye West", "Mac Miller", "Dave", "KSI", "WizKid", "Pop Smoke", "J. Cole", "Kendrick Lamar", "Marvin Gaye", "Central Cee", "Bruno Mars", "Polo G", "Joseph Solomon", "Stormzy", "Adele", "Juice", "Doja Cat"]


#type error -> list indices must be integers or slices, not str -> trying to get a key of a list -> need to use a number
artist_nid = {"Frank Ocean":"2h93pZq0e7k5yf4dywlkpM", "Kanye West":"5K4W6rqBFWDnAN6FQUkS6x", "Mac Miller":"4LLpKhyESsyAXpc4laK94U", "Dave":"6Ip8FS7vWT1uKkJSweANQK", "KSI":"1nzgtKYFckznkcVMR3Gg4z", "WizKid":"3tVQdUvClmAT7URs9V3rsp", "Pop Smoke":"0eDvMgVFoNV3TpwtrVCoTj", "J. Cole":"6l3HvQ5sa6mXTsMTB19rO5", "Kendrick Lamar":"2YZyLoL8N0Wb9xBt1NhZWg", "Marvin Gaye":"3koiLjNrgRTNbOwViDipeA", "Central Cee":"5H4yInM5zmHqpKIoMNAx4r", "Bruno Mars":"0du5cEVh5yTK9QJze8zA0C", "Polo G":"6AgTAQt8XS6jRWi4sX7w49", "Joseph Solomon":"0hZEO1Bl2QRGUaeeSLWDYN", "Stormzy":"2SrSdSvpminqmStGELCSNd", "Adele":"4dpARuHxo51G3z768sgnrY", "Juice WRLD": "4MCBfE4596Uoi2O4DtmEMz", "Doja Cat":"5cj0lLjcoR7YOSnhnX0Po5"} #dictionaries use colons
ara1 = {}
for k, v in artist_nid.items(): #need items when unpacking a dict
    ara = sp.artist_related_artists(v)
    print("\n")
    print(ara)
    print("\n")
    print(len(ara))
    print("\n")
    ara2 = []
    for i in range(len(ara["artists"])): #len(ara) -> gives the len of the whole dict = 1 but len(ara["artists"]) = 20
        ara2.append(Artist(ara["artists"][i]["id"], ara["artists"][i]["name"], ara["artists"][i]["followers"]["total"], ara["artists"][i]["genres"], ara["artists"][i]["popularity"]))
    ara1[k] = ara2
print("t2t")


for k,v in ara1.items():
    print(k) #name of original artist
    print("\n")
    for i in v:
        print(i)
        print("\n")
    print("\n")

print("\n")
print("numbers")

# for k,v in ara1.items():
#     for i in range(20):
#         print(k)

print("\n")

#need a nested list comprehension
d8 = {"Main Artist": [k for k,v in ara1.items() for i in range(20)],"Related Artist ID":[i.id for k,v in ara1.items() for i in v], "Realted Artist Name":[i.name for k,v in ara1.items() for i in v],"Followers":[i.followers for k,v in ara1.items() for i in v],"Genres":[i.genres for k,v in ara1.items() for i in v], "Popularity":[i.popularity for k,v in ara1.items() for i in v]}

print("\n")
print("flappybird")
print("\n")

#checked all the lengths of the lists -> as the length of the main artist did not align with the length of the related artists
# print(len([k for k,v in ara1.items()]))
#
# print("\n")
#
# print(len([i.id for k,v in ara1.items() for i in v]))
#
# print("\n")
#
#
# print(len([i.name for k,v in ara1.items() for i in v]))
#
# print("\n")
#
# print(len([i.followers for k,v in ara1.items() for i in v]))
#
# print("\n")
#
# print(len([i.genres for k,v in ara1.items() for i in v]))
#
# print("\n")
#
# print(len([i.popularity for k,v in ara1.items() for i in v]))
#
# print("\n")


print("\n")
df8 = pd.DataFrame(d8)
print("dataframe8")
print("\n")
print(df8) #print dataframe7

df8.to_csv("artist_related_artists.csv")




#Saturday -> check the dataframe above and work on the action  e.g. -> previous_track -> action

#play a few secs of a track, play a few secs of the next track, run this code and then the literal previous track before the next track even though it has not been played should automatically play again
# print("\n\n")
# pt = sp.previous_track(device_id=None)

#should add the relevant albums to my music library desktop?
# print("\n\n")

#didn't really work -> try with
# lt = sp.current_user_saved_albums_add(albums=["392p3shh2jkxUxY2VHvlH8"])

print("\n\n")
#nt = sp.next_track(device_id=None)

print("\n\n")
# qt = sp.pause_playback(device_id=None)














# Complete:
#
# 1) New releases -> got all the data, created a a list of objects
#
# -> if something is not available in the data when creating object use “None”
#
# -> datadrames
#
# 2. Saved albums > got all the data, created a a list of objects
#
# -> dataframes
#
# Check:
# any uk vs us albums
#
# —————————————————————
# artist_related_artists -> what class should be used
#
# Action?
#
# How to organise data