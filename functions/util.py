from classes.Song import Song

def inicializarObjetosSong(song_titles, spotify_manager):
    songs = []

    for title in song_titles:
        song = Song(title=title, spotify_manager=spotify_manager)
        songs.append(song)
        print(songs)

    return songs


def getSongTitlesFromFile(filename):
    song_titles=[]

    with open(filename, "r") as arquivo:
        for linha in arquivo:
            song_titles.append(linha.strip())

    return song_titles
