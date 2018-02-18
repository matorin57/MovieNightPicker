import random
import json

class Genre(object):
    def __init__(self,name):
        self.name = name
        self.movies = []
        return

    def randomlyPickMovie(self):
        return self.movies[random.randint(0,len(self.movies)-1)]

    def randomlyPickSubset(self, size=3):
        if size >= len(self.movies):
            return self.movies
        randomMovies = []
        i = 0
        while i < size:
            pickedMovie = self.randomlyPickMovie();
            if pickedMovie not in randomMovies:
                randomMovies.append(pickedMovie)
                i = i + 1
        return randomMovies

    def printMovies(self):
        for i in range(0,len(self.movies)):
            print(""+str(i)+": "+self.movies[i]+"\n")
        return

    def addMovie(self,movie):
        self.movies.append(movie)
        writeGenre(self)
        return

    def deleteMovie(self):
        self.printMovies()
        print("Enter the number of the movie to delete: ")
        i = input("")
        index = int(i)
        del self.movies[index]
        writeGenre(self)
        return

def readInGenre(name):
    readInGenre = {}
    with open("movies\\"+name+".txt", mode='r') as f:
        readInGenre = json.load(f)
    genre = Genre(readInGenre["name"])
    genre.movies = [g for g in readInGenre["movies"]]
    return genre
def writeGenre(genre):
    writeDict = {"name":genre.name, "movies":genre.movies}
    with open("movies\\"+genre.name+".txt", mode='w') as f:
        genre = json.dump(writeDict,f)
    return genre
