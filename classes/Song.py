
class Song:
    def __init__(self, title, spotify_manager):
        self.title= title
        
        result = spotify_manager.sp.search(self.title, type='track')
        track_id = result['tracks']['items'][0]['id']
        features = spotify_manager.sp.audio_features(track_id)

        atributos_desejados = ['danceability', 'energy',  'valence']

        novo_obj = {}
        obj_features=features[0]

        for atributo in atributos_desejados:
            # adiciona o atributo ao novo dicionário se ele existir no objeto original
            if atributo in obj_features:
                novo_obj[atributo] = obj_features[atributo]

        self.caracteristicas = novo_obj
    
    def getCaracteristicas(self):
        return self.caracteristicas
    
    def getTitle(self):
        return self.title
    
    def getDanceability(self):
        return self.caracteristicas['danceability']
    
    def getEnergy(self):
        return self.caracteristicas['energy']   
    
    def getValence(self):
        return self.caracteristicas['valence']

