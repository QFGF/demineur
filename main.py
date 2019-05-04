import pygame
import random 
import time
from pygame.locals import *
pygame.init()
ecranx = 1000
ecrany = 1000
window = pygame.display.set_mode((ecranx, ecrany))
mainloop = True
class Map:
	def __init__(self, ecrany, ecranx):
		hauteur = 12
		largeur = 25
		blocy = ecrany / hauteur
		blocx = ecranx / largeur

	def grille(blocy, blocx) :
		pygame.gfxdraw.line(window,10,10,100,120,[255,0,0])
class Player:
	pass
gx = 0
gy = 0

while mainloop:
	Map.grille()
	pygame.display.flip()
	
