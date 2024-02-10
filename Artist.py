
class Artist:
    def __init__(self, id, name, followers, genres, popularity): #what goes in depends on what we put in a1
        self.id = id
        self.name = name
        self.followers = followers
        self.genres = genres
        self.popularity = popularity

    def genres_property(self):
        return ", ".join(self.genres) #better to return and send back to the caller  than to print as can store in a variable and may not always want to print

    #hard to for loop in a string -> so join it
    def __str__(self): #breaking down the things in a1 to get what we want to be presented to the user
        return f"ID: {self.id}\nName: {self.name}\nFollowers: {self.followers}\nGenres: {', '.join(self.genres)}\nPopularitys: {self.popularity} "

#should see the str function working
a1 = Artist('5K4W6rqBFWDnAN6FQUkS6x', 'Kanye West', 17190393, ['chicago rap', 'rap'], 84) #selected from the api response


#attributes and methods must have different names