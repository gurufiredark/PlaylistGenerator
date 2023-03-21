from classes.Song import Song

def inicializarObjetosSong(song_titles, spotify_manager):
    songs = []

    for title in song_titles:
        song = Song(title=title, spotify_manager=spotify_manager)
        songs.append(song)

    return songs


def getSongTitlesFromFile(filename):
    song_titles=[]

    with open(filename, "r") as arquivo:
        for linha in arquivo:
            song_titles.append(linha.strip())

    return song_titles

def printarMusicas(songs):
    for song in songs:
        print("x----------------------x")
        print(f'Title = {song.getTitle()} ')
        print(f'Danceability = {song.getDanceability()}')
        print(f'Energy = {song.getEnergy()}')
        print(f'Valence = {song.getValence()}')
        print("x----------------------x\n\n\n")

def printarMusicasPopulation(songs):
    print("{ ", end="")
    for song in songs:
        print(f' {song.getTitle()} ', end="")
        print(f' {song.getDanceability()} ', end="")
        print(f' {song.getEnergy()} ', end="")
        print(f' {song.getValence()} ', end="")
        print("||", end="")
    print(" }")