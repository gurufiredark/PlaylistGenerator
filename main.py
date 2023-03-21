from classes.Spotify import Spotify
from functions.util import getSongTitlesFromFile, inicializarObjetosSong, printarMusicas


spotify_manager = Spotify()

file_path="data/songs.txt"

song_titles=getSongTitlesFromFile(file_path)

songs = inicializarObjetosSong(song_titles, spotify_manager)

printarMusicas(songs)

#representação cromossomica
#danceability, energy and valence.

representacoes_cromossomicas = []

representacoes_cromossomicas.append({'danceability': 0.65, 'energy': 0.75, 'valence': 1}) #Playlist Feliz
representacoes_cromossomicas.append({'danceability': 0.5, 'energy': 0.25, 'valence': 0}) #Playlist Triste
representacoes_cromossomicas.append({'danceability': 1, 'energy': 1, 'valence': 1}) #Playlist Festa