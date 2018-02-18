import Genre
import random
import os

lastSelected = []
def main():
    genres = loadGenres()
    
    quit = False
    while not quit:
        lastSelected = loadLastSelected()
        print("Last Selected Set: "+str(lastSelected)+"\n")
        print("1.Manage Genres\n2.Select Movie Set\n3.Exit\n")
        choice = int(input("Choose Operation: "))
        if choice == 1:
            manageGenres(genres)
        elif choice == 2:
            selectMovieSet(genres)
        elif choice == 3:
            quit = True
    return


def loadGenres():
    genres = []
    try:
        with open(file = "genreList.txt",mode = 'r') as f:
            genres = [Genre.readInGenre(line.strip()) for line in f]
    except:
        open("genreList.txt","w+")
    return genres

def writeGenres(genres):
    with open(file = "genreList.txt", mode='w') as f:
        f.write("\n".join([g.name for g in genres]))
    return

def loadLastSelected():
    lastSelected = []
    try:
        with open(file = "lastSelected.txt", mode = 'r') as f:
            lastSelected = [line.strip() for line in f]
    except:
        lastSelected = []
    return lastSelected

def writeLastSelected(lastSelected):
    with open(file = "lastSelected.txt", mode ='w') as f:
        f.write("\n".join(lastSelected))
    return

def selectMovieSet(genres):
    pickedGenre = genres[random.randint(0,len(genres)-1)]
    selectedSet = pickedGenre.randomlyPickSubset()
    print("Chosen Genre: "+pickedGenre.name)
    print(selectedSet)
    writeLastSelected(selectedSet)
    return

def manageGenres(genres):
    quit = False
    while not quit:
        print("1.View Genres\n2.Add Genre\n3.Edit Genre\n4.Remove Genre\n5.Go Back\n")
        choice = int(input("Choose Operation: "))
        if choice == 1:
            printGenres(genres)
        elif choice == 2:
            addGenre(genres)
        elif choice == 3:
            selectGenre(genres)
        elif choice == 4:
            removeGenre(genres)
        elif choice == 5:
            quit = True
    return

def addGenre(genres):
    name = input("Enter Genre Name: ")
    newGenre = Genre.Genre(name)
    Genre.writeGenre(newGenre)
    genres.append(newGenre)
    writeGenres(genres)
    return

def selectGenre(genres):
    printGenres(genres)
    selected = int(input("Select a genre: "))
    if selected in range(0,len(genres)):
        editGenre(genres[selected])
    return

def editGenre(genre):
    quit = False
    while not quit:
        print("1.View Movies\n2.Add Movie\n3.Delete Movie\n4.Go Back")
        choice = int(input("Select an operation: "))
        if choice == 1:
            genre.printMovies()
        elif choice == 2:
            genre.addMovie(input("Enter Movie: "))
        elif choice == 3:
            genre.deleteMovie()
        elif choice == 4:
            quit = True
    return

def removeGenre(genres):
    printGenres(genres)
    selected = int(input("Select a genre: "))
    if selected in range(0,len(genres)):
        del genres[selected]
    writeGenres(genres)
    return

def printGenres(genres):
    i = 0
    for g in genres:
        print(""+str(i)+": "+g.name)
        i += 1
    return

if __name__ == "__main__":
    lastSelected = loadLastSelected()
    main()