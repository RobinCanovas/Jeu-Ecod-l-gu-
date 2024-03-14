import pygame
import sys

import pygame
from Page_Start import PagePrincipale
from Inventaire_Boutique import *
inventaire_joueur = Inventaire()
boutique = Boutique()

class PageBoutique2:
    def __init__(self):
        pygame.init()

        # Paramètres de la fenêtre
        self.window_width = 1200
        self.window_height = 800
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Boutique")
        icon = pygame.image.load("image\icon.png")
        pygame.display.set_icon(icon)
        # Couleurs
        self.blue = (0, 0, 255)
        self.white = (255, 255, 255)
        self.pink = (255, 182, 193)
        self.black = (0, 0, 0)

        # Police de texte
        self.font = pygame.font.Font(None, 36)

        # Liste des articles
        self.articles = [
            {"name": "Article 1", "price": "$10", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 2", "price": "$20", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 3", "price": "$15", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 4", "price": "$25", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 5", "price": "$30", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 1", "price": "$10", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 2", "price": "$20", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 3", "price": "$15", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 4", "price": "$25", "image": pygame.image.load("image/achat.png")},
            {"name": "Article 5", "price": "$30", "image": pygame.image.load("image/achat.png")},
        ]

        # Position des articles
        self.article_width = 300
        self.article_height = 300
        self.article_spacing = 20
        self.vertical_spacing = 200
        self.button_height = 40
        self.button_vertical = 100

        # Calcul position départ pour centrer articles
        self.num_rows = (len(self.articles) - 1) // 3 + 1
        self.start_x = (self.window_width - (3 * self.article_width + 2 * self.article_spacing)) // 2
        self.start_y = (self.window_height - (self.num_rows * (self.article_height + self.vertical_spacing + self.button_height) - self.vertical_spacing)) // 2

        # défilement proprieté
        self.scroll_y = -250
        self.scroll_speed = 5
        self.scrolling_up = False
        self.scrolling_down = False

        # inventaire
        self.purchased = [False] * len(self.articles)

        # argent
        self.argent = 100

    def is_mouse_over(self, x, y, width, height):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return x < mouse_x < x + width and y < mouse_y < y + height

    def can_buy_article(self, article_price):
        return self.argent >= article_price

    def quitter(self):
        page_principale = PagePrincipale()
        page_principale.run()
        pygame.quit()

    def display_boutique(self):
        self.window.fill(self.white)

        # Affichage des articles, bandeau bleu, bouton "acheter vie", bouton "retour", etc.
        for i, article in enumerate(self.articles):
            row = i // 3
            col = i % 3
            x = self.start_x + col * (self.article_width + self.article_spacing)
            y = self.start_y + row * (self.article_height + self.vertical_spacing) - self.scroll_y

            # Vérifiez si l'article est visible dans la fenêtre
            if y < self.window_height and y + self.article_height > 0:
                # Effacer texte précédent
                pygame.draw.rect(self.window, self.white, (x, y + self.article_height + self.button_vertical, self.article_width, self.button_height))

                # Affichage cadre autour de l'article
                pygame.draw.rect(self.window, self.blue, (x, y, self.article_width, self.article_height), 2)

                # Affichage du nom de l'article
                name_text = self.font.render(article["name"], True, self.blue)
                name_rect = name_text.get_rect(center=(x + self.article_width // 2, y + 30))
                self.window.blit(name_text, name_rect)

                # Affichage prix article
                price_text = self.font.render(article["price"], True, self.blue)
                price_rect = price_text.get_rect(center=(x + self.article_width // 2, y + 60))
                self.window.blit(price_text, price_rect)

                # Affichage de l'image article
                article_image = pygame.transform.scale(article["image"], (self.article_width, self.article_height))
                self.window.blit(article_image, (x, y + 90))

                # Affichage du bouton "Acheter"
                button_rect = pygame.Rect(x, y + self.article_height + self.button_vertical, self.article_width, self.button_height)
                pygame.draw.rect(self.window, self.blue, button_rect)

                # Vérifier si le bouton "Acheter" est cliqué
                if self.is_mouse_over(x, y + self.article_height + self.button_vertical, self.article_width, self.button_height) and pygame.mouse.get_pressed()[0]:
                    if not self.purchased[i]:  # Ajouter cette condition pour vérifier si l'article n'a pas déjà été acheté
                        if self.can_buy_article(int(article["price"][1:])):  # Convertir le prix en entier en excluant le signe dollar
                            self.purchased[i] = True
                            self.argent -= int(article["price"][1:])  # Déduire le montant du prix
                            print(f"Achete {article['name']}. Argent restant: ${self.argent}")
                        else:
                            print("Fonds insuffisants. Vous n'avez pas assez d'argent pour acheter cet article.")

                # Afficher "Achete" ou "Deja achete"
                if self.purchased[i]:
                    button_text = self.font.render("Deja achete", True, self.white)
                else:
                    button_text = self.font.render("Acheter", True, self.white)

                text_rect = button_text.get_rect(center=button_rect.center)
                self.window.blit(button_text, text_rect)

        # Affichage du bandeau bleu
        pygame.draw.rect(self.window, self.blue, (200, 0, 800, 150))

        # Affichage du texte "BOUTIQUE" au centre du bandeau
        boutique_text = self.font.render("BOUTIQUE", True, self.white)
        boutique_rect = boutique_text.get_rect(center=(self.window_width // 2, 75))
        self.window.blit(boutique_text, boutique_rect)

        # Affichage du bouton "acheter vie"
        bouton_vie = pygame.Rect(1000, 0, 200, 150)
        pygame.draw.rect(self.window, self.pink, bouton_vie)

        # Vérifier si le bouton "acheter vie" est cliqué
        if self.is_mouse_over(1000, 0, 200, 150) and pygame.mouse.get_pressed()[0]:
            PageAchatVie(self.window).run()

        # Affichage du texte "acheter vie"
        boutique_text = self.font.render("acheter vie", True, self.white)
        boutique_rect = boutique_text.get_rect(topleft=(1040, 60))
        self.window.blit(boutique_text, boutique_rect)

        # Affichage du bouton "retour"
        retour = pygame.Rect(0, 0, 200, 150)
        pygame.draw.rect(self.window, self.black, retour)

        # Vérifier si le bouton "retour" est cliqué
        if self.is_mouse_over(0, 0, 200, 150) and pygame.mouse.get_pressed()[0]:
            self.quitter()

        # Affichage du texte "retour"
        boutique_text = self.font.render("menu principale", True, self.white)
        boutique_rect = boutique_text.get_rect(topleft=(5, 60))
        self.window.blit(boutique_text, boutique_rect)

        pygame.display.flip()

    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.scrolling_down = True
                    elif event.key == pygame.K_DOWN:
                        self.scrolling_up = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.scrolling_down = False
                    elif event.key == pygame.K_DOWN:
                        self.scrolling_up = False

            if self.scrolling_up:
                self.scroll_y += self.scroll_speed
            elif self.scrolling_down and self.scroll_y > -200:
                self.scroll_y -= self.scroll_speed

            self.display_boutique()

        self.quitter()


from pygame.locals import QUIT

class PageAchatVie:
    def __init__(self, ecran):
        self.ecran = ecran
        self.couleur_fond = (0, 0, 0)
        self.bouton_achat = pygame.image.load("image/Coeur.png")
        self.bouton_achat = pygame.transform.scale(self.bouton_achat, (200, 200))
        self.bouton_rect_gauche = pygame.Rect(100, 300, 200, 200)
        self.bouton_rect_droite = pygame.Rect(900, 300, 200, 200)
        self.police = pygame.font.Font(None, 36)
        self.couleur_gauche = (255, 0, 0)
        self.couleur_droite = (0, 0, 255)
        self.clic_gauche = False
        self.clic_droite = False
        self.prix_vie = 50
        self.nombre_vies = 3
        self.bouton_image = pygame.image.load("image/annuler.png")
        self.bouton_image = pygame.transform.scale(self.bouton_image, (50, 50))
        self.bouton_rect_annuler = self.bouton_image.get_rect(topleft=(10, 10))

    def action_annuler(self):
        from Page_Start import PagePrincipale
        page_principale = PagePrincipale()
        page_principale.run()
        pygame.quit()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.bouton_rect_gauche.collidepoint(event.pos) and not self.clic_gauche:
                            self.clic_gauche = True
                            self.couleur_gauche = (0, 255, 0)
                            self.acheter_vie_1()
                        elif self.bouton_rect_droite.collidepoint(event.pos) and not self.clic_droite:
                            self.clic_droite = True
                            self.couleur_droite = (0, 255, 0)
                            self.acheter_vie()
                        elif self.bouton_rect_annuler.collidepoint(event.pos):
                            self.action_annuler()

            self.ecran.fill(self.couleur_fond)

            pygame.draw.rect(self.ecran, self.couleur_gauche, self.bouton_rect_gauche)
            pygame.draw.rect(self.ecran, self.couleur_droite, self.bouton_rect_droite)
            self.ecran.blit(self.bouton_achat, self.bouton_rect_gauche)
            self.ecran.blit(self.bouton_achat, self.bouton_rect_droite)
            self.ecran.blit(self.bouton_image, self.bouton_rect_annuler.topleft)

            texte_prix = self.police.render(f"Prix: 20 HP {self.prix_vie} coins", True, (255, 255, 255))
            texte_vies = self.police.render(f"Prix: Full HP 200", True, (255, 255, 255))
            self.ecran.blit(texte_prix, (100, 550))
            self.ecran.blit(texte_vies, (900, 550))

            pygame.display.flip()

    def acheter_vie(self):
        print("Vous gagnez 100hp(1vie)")

    def acheter_vie_1(self):
        print("Vous gagnez 20hp")