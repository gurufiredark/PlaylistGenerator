import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

class Spotify:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env.local
        load_dotenv('.env.local')

        # Usa a variável de ambiente MY_VAR
        # Insira suas credenciais da API do Spotify
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_secret')
        
        # Configure a autenticação
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)


