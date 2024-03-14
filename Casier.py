import pygame
import sys

class Skin:
    def __init__(self, name, image_path, price):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.price = price

class PagePrincipal:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("son/Jeu_Son.mp3")
        pygame.mixer.music.play(-1)

        # Définition des constantes
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1200, 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        pygame.display.set_caption("Trash Hunters - Skins écologiques")
        icon = pygame.image.load("image/icon.png")
        pygame.display.set_icon(icon)

        # Charger les skins
        self.skins = [
            Skin("Skin 1", "Image/skin1.png", 100),
            Skin("Skin 2", "Image/skin2.png", 150),
            Skin("Skin 3", "Image/skin3.png", 200)
        ]
        self.skin_index = 0

        # Police de caractères
        self.font = pygame.font.Font("Police/Roboto-Bold.ttf", 24)

        # Redimensionner le skin actif
        self.active_skin = pygame.transform.scale(self.skins[self.skin_index].image, (350, 350))

        # Position et taille du bouton de sélection de skin
        self.button_width = 150
        self.button_height = 50
        self.button_x = (self.SCREEN_WIDTH - self.button_width) // 2
        self.button_y = self.SCREEN_HEIGHT - 100

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RIGHT:
                        self.skin_index = (self.skin_index + 1) % len(self.skins)
                        self.active_skin = pygame.transform.scale(self.skins[self.skin_index].image, (350, 350))
                    elif event.key == pygame.K_LEFT:
                        self.skin_index = (self.skin_index - 1) % len(self.skins)
                        self.active_skin = pygame.transform.scale(self.skins[self.skin_index].image, (350, 350))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.skin_index = (self.skin_index + 1) % len(self.skins)
                        self.active_skin = pygame.transform.scale(self.skins[self.skin_index].image, (350, 350))

            self.screen.fill((43, 86, 59))  # Couleur de fond verte

            # Afficher le skin actif
            skin_rect = self.active_skin.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
            self.screen.blit(self.active_skin, skin_rect.topleft)

            # Afficher le nom et le prix du skin actif
            text_surface = self.font.render(f"{self.skins[self.skin_index].name}", True, (255, 255, 255))  # Texte blanc
            text_rect = text_surface.get_rect(center=(self.SCREEN_WIDTH // 2, skin_rect.bottom + 20))
            self.screen.blit(text_surface, text_rect)

            # Afficher le bouton de sélection de skin
            self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
            pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)  # Rectangle blanc
            button_text = self.font.render("Sélectionner", True, (0, 0, 0))  # Texte noir
            button_text_rect = button_text.get_rect(center=self.button_rect.center)
            self.screen.blit(button_text, button_text_rect)

            pygame.display.flip()

if __name__ == "__main__":
    from Page_Start import PagePrincipale
    page_principale = PagePrincipale()
    page_principale.run()
    pygame.quit()
    sys.exit()







