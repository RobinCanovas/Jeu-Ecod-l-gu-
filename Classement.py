# Créé par Alicia Canovas-Andri, le 14/03/2024 en Python 3.7
import pygame
import sys

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Leaderboard:
    def __init__(self):
        pygame.init()

        # Définition des constantes
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Top 5 des meilleurs joueurs")

        # Liste des joueurs
        self.players = [
            Player("Joueur 1", '100%'),
            Player("Joueur 2", '90%'),
            Player("Joueur 3", '80%'),
            Player("Joueur 4", '70%'),
            Player("Joueur 5", '60%')
        ]

        # Police de caractères
        self.font = pygame.font.Font(None, 30)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # Couleur de fond blanc

            # Dessiner le carré
            square_size = 200
            square_x = (self.SCREEN_WIDTH - square_size) // 2
            square_y = (self.SCREEN_HEIGHT - square_size) // 2
            pygame.draw.rect(self.screen, (0, 0, 0), (square_x, square_y, square_size, square_size), 2)  # Carré noir

            # Afficher la liste des joueurs dans le carré
            text_spacing = 40
            text_x = square_x + 20
            text_y = square_y + 20
            for index, player in enumerate(self.players):
                player_text = f"{player.name}: {player.score}"
                text_surface = self.font.render(player_text, True, (0, 0, 0))  # Texte noir
                text_rect = text_surface.get_rect(topleft=(text_x, text_y + index * text_spacing))
                self.screen.blit(text_surface, text_rect)

            pygame.display.flip()

if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.run()
    pygame.quit()
    sys.exit()

