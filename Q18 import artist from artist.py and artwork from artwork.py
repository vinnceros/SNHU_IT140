# If the input is:
# Brice Marden
# 1938
# -1
# Distant Muses
# 2000
# The output is:
# Artist: Brice Marden, born 1938
# Title: Distant Muses, 2000

class Artist:
    def __init__(self, name = "None", birthYear = 0, deathYear = 0):
        self.name = name
        self.birthYear = birthYear
        self.deathYear = deathYear
    def displayInfo(self):
        if self.deathYear == -1:
            print('Artist: {}, born {}'.format(self.name, self.birthYear))
        else:
            print('Artist: {} ({}---{})'.format(self.name, self.birthYear, self.deathYear))

class Artwork:
    def __init__(self, title = "None", yearCreated =0, artist = Artist()):
        self.title = title
        self.yearCreated = yearCreated
        self.artist = artist

    def displayInfo(self):
        self.artist.displayInfo()
        print("Title: %s. %d" % (self.title, self.yearCreated))

# import artist from artist.py and artwork from artwork.py

from Artist import *
from Artwork import *

# the user input will be 

if ___name___ == "___main___":
    artistName = input()
    birthYear = input ()
    deathYear = input ()
    title = input ()
    yearCreated = int(input())

# the method to call displayInfo

    userArtist = Artist(artistName, birthYear, deathYear)
    artwork = Artwork(title, yearCreated, userArtist)
    artwork.displayInfo()


