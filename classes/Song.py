
class Song:
    def __init__(self, title, spotifyManager):
        self.title= title
        
        result = spotifyManager.sp.search(self.title, type='track')
        track_id = result['tracks']['items'][0]['id']
        features = spotifyManager.sp.audio_features(track_id)

        atributos_desejados = ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'valence']
        objeto_filtrado = {atributo: features[atributo] for atributo in atributos_desejados if atributo in features}

        self.caracteristicas = objeto_filtrado
    
    def getCaracteristicas(self):
        return self.caracteristicas
    
    def getTitle(self):
        return self.title
    
    def getDanceability(self):
        return self.caracteristicas['danceability']
    
    def getEnergy(self):
        return self.caracteristicas['energy']   
    
    def getSpeechiness(self):
        return self.caracteristicas['speechiness']
    
    def getAcousticness(self):
        return self.caracteristicas['acousticness']
    
    def getInstrumentalness(self):
        return self.caracteristicas['instrumentalness']
    
    def getValence(self):
        return self.caracteristicas['valence']

