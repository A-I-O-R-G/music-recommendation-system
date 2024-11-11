import random
import json

class MusicRecommendationSystem:
    def __init__(self):
        """
        Inicializa o sistema de recomendação com um dicionário de usuários e suas preferências.
        """
        self.user_preferences = {}

    def capture_preferences(self, user_id, genres, artists, playlists):
        """Captura as preferências musicais do usuário."""
        self.user_preferences[user_id] = {
            'genres': genres,
            'artists': artists,
            'playlists': playlists
        }
        print(f"Preferências do usuário '{user_id}' capturadas com sucesso.")

    def update_preferences(self, user_id, genres, artists, playlists):
        """Atualiza as preferências musicais do usuário."""
        if user_id in self.user_preferences:
            self.user_preferences[user_id] = {
                'genres': genres,
                'artists': artists,
                'playlists': playlists
            }
            print(f"Preferências do usuário '{user_id}' atualizadas com sucesso.")
        else:
            print(f"Usuário '{user_id}' não encontrado. As preferências não foram atualizadas.")

    def recommend_music(self, user_id, num_recommendations=5):
        """Gera recomendações de músicas para o usuário baseado nas suas preferências."""
        if user_id not in self.user_preferences:
            print(f"Usuário '{user_id}' não encontrado. Não é possível gerar recomendações.")
            return []

        preferences = self.user_preferences[user_id]
        recommendations = []

        # Gerar recomendações baseadas nos gêneros, artistas e playlists
        for genre in preferences['genres']:
            recommendations.append(f"Música Aleatória no gênero {genre}")
        for artist in preferences['artists']:
            recommendations.append(f"Música de {artist}")
        for playlist in preferences['playlists']:
            recommendations.append(f"Música da playlist {playlist}")

        random.shuffle(recommendations)
        return recommendations[:num_recommendations]

    def display_recommendations(self, user_id):
        """Exibe as recomendações de músicas para o usuário."""
        recommendations = self.recommend_music(user_id)
        if recommendations:
            print(f"Recomendações para o usuário '{user_id}':")
            for music in recommendations:
                print(f"- {music}")

    def save_preferences(self, filename):
        """Salva as preferências dos usuários em um arquivo JSON."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.user_preferences, f, indent=4)
            print(f"Preferências salvas em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar preferências: {e}")

    def load_preferences(self, filename):
        """Carrega as preferências dos usuários de um arquivo JSON."""
        try:
            with open(filename, 'r') as f:
                self.user_preferences = json.load(f)
            print(f"Preferências carregadas de '{filename}'.")
        except Exception as e:
            print(f"Erro ao carregar preferências: {e}")

if __name__ == "__main__":
    music_system = MusicRecommendationSystem()
    music_system.capture_preferences(user_id="user1", genres=["Rock", "Pop"], artists=["Artist A", "Artist B"], playlists=["Playlist 1"])
    music_system.display_recommendations(user_id="user1")
    music_system.update_preferences(user_id="user1", genres=["Jazz"], artists=["Artist C"], playlists=["Playlist 2"])
    music_system.display_recommendations(user_id="user1")
    music_system.save_preferences("preferencias.json")
    music_system.load_preferences("preferencias.json")