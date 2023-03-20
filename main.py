from classes.Spotify import Spotify
from functions.util import getSongTitlesFromFile, inicializarObjetosSong


spotify_manager = Spotify()

file_path="data/songs.txt"

song_titles=getSongTitlesFromFile(file_path)

songs = inicializarObjetosSong(song_titles, spotify_manager)

