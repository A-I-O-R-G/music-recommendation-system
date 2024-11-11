import random

class MusicRecommendationSystem:
    def __init__(self):
        """
        Inicializa o sistema de recomendaÃ§Ã£o com um dicionÃ¡rio de usuÃ¡rios e suas preferÃªncias.
        """
        self.user_preferences = {}

    def capture_preferences(self, user_id, genres, artists, playlists):
        """
        Captura as preferÃªncias musicais do usuÃ¡rio.
        :param user_id: Identificador Ãºnico do usuÃ¡rio.
        :param genres: Lista de gÃªneros preferidos.
        :param artists: Lista de artistas preferidos.
        :param playlists: Lista de playlists favoritas.
        """
        self.user_preferences[user_id] = {
            'genres': genres,
            'artists': artists,
            'playlists': playlists
        }
        print(f"PreferÃªncias do usuÃ¡rio {user_id} capturadas com sucesso.")

    def update_preferences(self, user_id, genres, artists, playlists):
        """
        Atualiza as preferÃªncias musicais do usuÃ¡rio.
        :param user_id: Identificador Ãºnico do usuÃ¡rio.
        :param genres: Lista de gÃªneros preferidos.
        :param artists: Lista de artistas preferidos.
        :param playlists: Lista de playlists favoritas.
        """
        if user_id in self.user_preferences:
            self.user_preferences[user_id] = {
                'genres': genres,
                'artists': artists,
                'playlists': playlists
            }
            print(f"PreferÃªncias do usuÃ¡rio {user_id} atualizadas com sucesso.")
        else:
            print("UsuÃ¡rio nÃ£o encontrado. As preferÃªncias nÃ£o foram atualizadas.")

    def recommend_music(self, user_id):
        """
        Gera recomendaÃ§Ãµes de mÃºsicas para o usuÃ¡rio baseado nas suas preferÃªncias.
        :param user_id: Identificador Ãºnico do usuÃ¡rio.
        :return: Lista de recomendaÃ§Ãµes.
        """
        if user_id not in self.user_preferences:
            print("UsuÃ¡rio nÃ£o encontrado. NÃ£o Ã© possÃ­vel gerar recomendaÃ§Ãµes.")
            return []

        preferences = self.user_preferences[user_id]
        recommendations = []

        for genre in preferences['genres']:
            recommendations.append(f"MÃºsica AleatÃ³ria no gÃªnero {genre}")
        for artist in preferences['artists']:
            recommendations.append(f"MÃºsica de {artist}")
        for playlist in preferences['playlists']:
            recommendations.append(f"MÃºsica da playlist {playlist}")

        random.shuffle(recommendations)  
        return recommendations[:5]  

    def display_recommendations(self, user_id):
        """
        Exibe as recomendaÃ§Ãµes de mÃºsicas para o usuÃ¡rio.
        :param user_id: Identificador Ãºnico do usuÃ¡rio.
        """
        recommendations = self.recommend_music(user_id)
        if recommendations:
            print(f"RecomendaÃ§Ãµes para o usuÃ¡rio {user_id}:")
            for music in recommendations:
                print(f"- {music}")

if __name__ == "__main__":
    music_system = MusicRecommendationSystem()
    music_system.capture_preferences(user_id="user1", genres=["Rock", "Pop"], artists=["Artist A", "Artist B"], playlists=["Playlist 1"])
    music_system.display_recommendations(user_id="user1")
    music_system.update_preferences(user_id="user1", genres=["Jazz"], artists=["Artist C"], playlists=["Playlist 2"])
    music_system.display_recommendations(user_id="user1")