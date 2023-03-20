from classes.Spotify import Spotify

spotifyManager = Spotify()

with open("songs.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
