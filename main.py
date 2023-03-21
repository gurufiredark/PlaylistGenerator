from classes.Spotify import Spotify
from functions.util import getSongTitlesFromFile, inicializarObjetosSong


spotify_manager = Spotify()

file_path="data/songs.txt"

song_titles=getSongTitlesFromFile(file_path)

songs = inicializarObjetosSong(song_titles, spotify_manager)

#representação cromossomica
#danceability, energy, speechiness, acousticness, instrumentalness, and valence.

representacoes_cromossomicas = []

representacoes_cromossomicas.append({'danceability': 0.65, 'energy': 0.75, 'acousticness': 0.5, 'instrumentalness': 0.5, 'valence': 1}) #Playlist Feliz
representacoes_cromossomicas.append({'danceability': 0.5, 'energy': 0.25, 'acousticness': 0.5, 'instrumentalness': 0.5, 'valence': 0}) #Playlist Triste
representacoes_cromossomicas.append({'danceability': 1, 'energy': 1, 'acousticness': 0.5, 'instrumentalness': 0.5, 'valence': 1}) #Playlist Festa