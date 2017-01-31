# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *
#importation de la bibliothèque system
import sys
sys.path.append('Model/')
#importation de nos classes
from class_Hero import *
from class_Platform import *
from class_Atk import *
from class_Mob import *
#initialisation de pygame
pygame.init()

WIDTH = 1280
HEIGHT = 720
fenetre  = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)

fond_e = pygame.transform.scale(pygame.image.load("Images/background.png").convert(), (1280,720))

imagesBlanchon = {
                  "RidleLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()), True, False)
                    ],
                  "RidleRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "RmoveLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()), True, False)
                    ],
                  "RmoveRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha())
                    ],
                  "FfallRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_2.png").convert_alpha())
                    ],
                  "FfallLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_2.png").convert_alpha()), True, False)
                    ],
                  "FcrouchRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_2.png").convert_alpha())
                    ],
                  "FcrouchLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_2.png").convert_alpha()), True, False)
                    ],
                  "RslideRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_slide.png").convert_alpha())
                    ],
                  "RslideLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_slide.png").convert_alpha()), True, False)
                    ],
                  "FjumpRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha())
                    ],
                  "FjumpLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha()), True, False)
                    ],
                  "Oaa1Right":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha())
                    ],
                  "Oaa1Left":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()), True, False)
                    ]
                 }

imagesArcher = {
                  "RidleRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/archer/a_idle.png").convert_alpha())
                    ],
                  "RidleLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/archer/a_idle.png").convert_alpha()), True, False)
                    ],
                  "OdmgRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/archer/a_dmg_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/archer/a_dmg_2.png").convert_alpha())
                    ],
                  "OdmgLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/archer/a_dmg_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/archer/a_dmg_2.png").convert_alpha()), True, False)
                    ]
                }


blanchon_atkList = [Atk(1, 10, 10, {"idleRight":[pygame.image.load("Images/plateformtest.png").convert()],"idleLeft":[pygame.image.load("Images/plateformtest.png").convert()]}, 10 , 5, 0, 0, 0, 200)]
blanchon = Hero(200, 200, 64, 64, imagesBlanchon, 0.3, 0.7, 8, 6, WIDTH, 100.0, blanchon_atkList)
sol = Platform(0, HEIGHT-50, WIDTH, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 0.4)
#INIT PLATEFORMES
platforms = []
platforms.append(Platform(80, HEIGHT-150, 100, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 1))
platforms.append(Platform(250, HEIGHT-250, 100, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 1))

#INIT ENNEMIS
foes = []
foes.append(Mob(500, 500, 64, 64, imagesArcher, 0.3, 0.5, 5, 6, WIDTH, 50, []))

#INIT SYSTEM CLOCK
clock = pygame.time.Clock()
fps = 60
myfont = pygame.font.SysFont("monospace", 15)

while 1 :
    clock.tick(fps)
#GESTION EVENT------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == QUIT: 	#si l'utilisateur clique sur la croix
            sys.exit()          #on ferme la fenêtre
        if event.type == KEYDOWN:
            blanchon.key_down(event)
        if event.type == KEYUP:
            blanchon.key_up(event)

#GESTION DU DECORS--------------------------------------------------------------
    #Fond
    fenetre.blit(fond_e, (0,0))

    #Plateformes
    nbPlatf = len(platforms)
    for i in range (0, nbPlatf):
        fenetre.blit(platforms[i].get_img(), platforms[i].get_rect())

    #TEST: Affichage poll d'attEffect de blanchon
    for i in range (0, len(blanchon.get_AtkEffectList())):
        label = myfont.render(str(blanchon.get_AtkEffectList()[i].get_duration()), 1, (0,100,150))
        fenetre.blit(label, (100, i*100))
        label = myfont.render(str(blanchon.get_AtkEffectList()[i].get_x1())+" ; "+str(blanchon.get_AtkEffectList()[i].get_y1()), 1, (0,100,150))
        fenetre.blit(label, (200, i*100))


#GESTION DU HERO----------------------------------------------------------------

    #Affichage Hero
    blanchon.nextImg(fps)
    fenetre.blit(blanchon.get_img(), blanchon.get_rect())
    pygame.draw.rect(fenetre, (0,0,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10, 62, 6))
    pygame.draw.rect(fenetre, (0,255,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10,   int(max(min(blanchon.get_hp() / float(blanchon.get_hpMax()) * 60, 60), 0)),   6))

    #Teste Hero => Plateforme
    heroOnGround = blanchon.isOnGround()
    blanchon.setOnAir()
    blanchon.testPlatform(sol)
    for i in range (0, nbPlatf):
        blanchon.testPlatform(platforms[i])

    #Le hero est descendu d'une plateforme
    if(heroOnGround == True and blanchon.isOnGround() == False):
        blanchon.giveDoubleJump() #On lui donne un saut

    blanchon.update(fps)

#GESTION DES MOBS---------------------------------------------------------------

    #Teste Mob => Plateforme && Atk Hero => Mob
    nbFoes = len(foes)
    nbAtkHero = len(blanchon.get_AtkEffectList())
    for i in range (0, nbFoes):
        foes[i].nextImg(fps)
        fenetre.blit(foes[i].get_img(), foes[i].get_rect())
        pygame.draw.rect(fenetre, (0,0,0), (foes[i].get_rect().x, foes[i].get_rect().y - 10, 62, 6))
        pygame.draw.rect(fenetre, (255,0,0), (foes[i].get_rect().x, foes[i].get_rect().y - 10,   int(max(min(foes[i].get_hp() / float(foes[i].get_hpMax()) * 60, 60), 0)),   6))
        EnnemyOnGround = foes[i].isOnGround()
        foes[i].setOnAir()
        foes[i].testPlatform(sol)
        for j in range (0, nbPlatf):
            foes[i].testPlatform(platforms[j])
        for k in range (0, nbAtkHero):
            foes[i].testAtkEffect(blanchon.get_AtkEffectList()[k])
        foes[i].update(fps)

    pygame.display.flip()
