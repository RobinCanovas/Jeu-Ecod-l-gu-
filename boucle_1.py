import pygame
from pygame import *

from time import sleep
from random import randint

from projectile import Projectile

from player import Player

from monstre import Monstre

from game import Game

from meuble import Meuble

from coeur import Coeur

from game_play import Game_play
pygame.init()

## --- INITIALISATION ---

# *********************** #

# class game

game = Game()

##memory_niveau = game.niveau.retrouver_pos(1)

# changer le decords

print
pygame.display.set_caption("jeux")
taille_plan = 1
taille_plan_play = 10
surface = pygame.display.set_mode((736,700))

adresse_image = 'image/arrière plan/plan_obpti/plan_' + str(1) +'.jpg'

arrier_plan = pygame.image.load(adresse_image)
arrier_plan = pygame.transform.scale(arrier_plan, (int(taille_plan * arrier_plan.get_width()), (int(taille_plan * arrier_plan.get_height()))))


image_play_green = pygame.image.load('image/menu/play_green.png')
image_play_green = pygame.transform.scale(image_play_green, (int(taille_plan_play * image_play_green.get_width()), (int(taille_plan_play * image_play_green.get_height()))))
image_play_green_rect = image_play_green.get_rect()
image_play_green_rect.x = 245
image_play_green_rect.y = 82


image_nuage = pygame.image.load('image/menu/nuage.png')
image_nuage = pygame.transform.scale(image_nuage, (int(taille_plan_play * image_nuage.get_width()), (int(taille_plan_play * image_nuage.get_height()))))
image_nuage_rect = image_nuage.get_rect()
image_nuage_rect.x = -114
image_nuage_rect.y = 23


taille_pause = 0.7
image_pause = pygame.image.load('image/popup/pause.png')
image_pause = pygame.transform.scale(image_pause, (int(taille_pause * image_pause.get_width()), (int(taille_pause * image_pause.get_height()))))
image_pause_rect = image_pause.get_rect()
image_pause_rect.x = 186
image_pause_rect.y = 148


taille_fond = 100
image_fond = pygame.image.load('image/popup/fond.png')
image_fond = pygame.transform.scale(image_fond, (int(taille_fond * image_fond.get_width()), (int(taille_fond * image_fond.get_height()))))
image_fond_rect = image_fond.get_rect()
image_fond_rect.x = 0
image_fond_rect.y = 0



# --- initialisation des tic---

tic_bras = 0
tic_spam = 0
tic_spam_dash = 0
tic_sawn_monstre = 0
tic_edit = 0

# definir les limites de l'écrant


max_droite_ecrant = 708
max_gauche_ecrant = 0
game.player.proprtion_edcrant(max_droite_ecrant,max_gauche_ecrant)
max_droite_ecrant_charger = 600
condition_mouvement = 15
temps_avant_dash = 70
temps_de_dash = temps_avant_dash - 10




## --- debut de la boucle ---

runing = True

while runing == True:
    tic_fondu = 0

    if game.edit.is_playing == 1:


        game.game_play.uptade(surface,arrier_plan,temps_de_dash,max_droite_ecrant,max_gauche_ecrant,condition_mouvement,temps_avant_dash)

        if game.pressed.get(pygame.K_j) and game.pressed.get(pygame.K_k) and game.pressed.get(pygame.K_l):
            game.game_over()

    elif game.edit.is_playing == 0:
        surface.blit(arrier_plan,(0,0))
        surface.blit(image_nuage,(image_nuage_rect.x,image_nuage_rect.y))
        surface.blit(image_play_green,(image_play_green_rect.x,image_play_green_rect.y))

        if game.pressed.get(pygame.K_t) and game.pressed.get(pygame.K_y) and game.pressed.get(pygame.K_i):
            game.renit_game(-1)
            game.edit.is_playing = 2

    elif game.edit.is_playing == 2:

        game.edit.edit_game_player()

        surface.blit(arrier_plan,(0,0))

        for i in range(len(game.tab_groupe)):
            game.tab_groupe[i].draw(surface)

        for i in range(len(game.tab_groupe_print)):
            game.tab_groupe_print[i].draw(surface)

        game.edit.edit_game_player_affichage()

    elif game.edit.is_playing == 3:

##        if game.pressed.get(pygame.K_a):
##            image_pause_rect.x -= 1
##
##        if game.pressed.get(pygame.K_d):
##            image_pause_rect.x += 1
##
##        if game.pressed.get(pygame.K_s):
##            image_pause_rect.y += 1
##
##        if game.pressed.get(pygame.K_w):
##            image_pause_rect.y -= 1

        tic_fondu = tic_fondu + 1


        if tic_fondu < 50:
            surface.blit(image_fond,(image_fond_rect.x,image_fond_rect.y))

        surface.blit(image_pause,(image_pause_rect.x,image_pause_rect.y))

        if game.pressed.get(pygame.K_o):
            game.edit.is_playing = 1

    pygame.display.flip()

    for event in pygame.event.get():

        ## quiter le jeu

        if event.type == pygame.QUIT:
            runing = False
            pygame.display.quit()

        ## variable pour indiquer en permanance les boutons pressées

        elif event.type == pygame.KEYDOWN:

            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if image_play_green_rect.collidepoint(event.pos):
                if game.edit.is_playing == 0:
                    game.edit.is_playing = 1
                    game.renit_game(0)