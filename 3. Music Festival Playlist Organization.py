# Objective:
# The aim of this assignment is to develop your skills in using Python 
# loops with sets, particularly for organizing and managing playlists 
# for a music festival. You will work with sets to handle various artists
# and genres, ensuring no duplicates and maintaining a well-organized collection.

# Task 1: Artist Lineup Compilation
# You are provided with a list of artist names scheduled to perform at 
# different stages of the music festival. Using a loop, compile these artist 
# names into a set to create a unique lineup without duplicates.

# Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for x in artist_names:
    if list(unique_artists).count(x) == 0:
        unique_artists.add(x)
    else:
        continue
else:
    print(unique_artists)

# Expected Outcome:
# A set containing unique artist names, such as {'The Lumineers', 'Tame Impala', 'Billie Eilish', 'Arctic Monkeys'}.

# Task 2: Genre Sorting
# You have a list of genres associated with each artist. Using a loop with sets, 
# categorize artists by their genres, creating a set for each genre.

# Example Code:

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}

def byGenre(artists):
    genreList = []
    for key, value in artists.items():     
        newSet = value  
        newSet = set()
        newSet.add(key)
        print(f"the {value} set contains {newSet}")
        
    
byGenre(artists_genres)

# Expected Outcome:
# A categorization of artists by genres, such as Genre: Folk, Artists: The Lumineers.

# Task 3: Playlist Duplication Check
# Create a Python script that takes multiple playlist sets and checks if any playlist 
# is a duplicate of another (i.e., contains the same set of songs).

# Example Code:

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]

#loop over the playlists list,
#check if current playlist and checking playlist have the same name, if so continue
#else check if they equal each other, if so return True
#else return False
setOfSets = set()

for x in range(len(playlists)):
    for y in range(x + 1, len(playlists)):
        if playlists[x] == playlists[y]:
            duplicatePlaylist = True
            print(f"duplicate playlist found = {True}")
            print(f"duplicate set: {playlists[x]} and {playlists[y]}")
            break
if bool(duplicatePlaylist) == False:
    print(f"duplicate playlist found = {False}")

