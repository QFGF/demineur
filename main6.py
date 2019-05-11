import random
import time
import pygame
from pygame.locals import *
pygame.init()

window=pygame.display.init()
window2=pygame.display.init()
window_h=900 
window_w=1600
window=pygame.display.set_mode([window_w,window_h],FULLSCREEN)
fps_cap=3
fpsclock=pygame.time.Clock()
debug = False
pygame.key.set_repeat(1,1000/fps_cap-1)

playerx = 0
playery = 0
####
tmprandom = random.randint(1,12)
####







map=[]
finish=False
tx,x=0,0
ty,y=0,0



def CreateMap():
	n = 0
	for tmp0 in range(12):
		map.append([])
		for tmp1 in range(25):
			map[n].append(0)
		n += 1




def GenerateMineMap():
	n=0
	while n<3:
		minex= random.randint(0,4)
		miney= random.randint(0,4)
		if map[miney][minex]==0:
			map[miney][minex]=9
			n+=1



def GenerateMap():
	for tmpy in range(12):
		y=tmpy
		for tmpx in range(25):
			x=tmpx
			n=0
			for tmp0 in [-1,0,1]:
				y+=tmp0
				for tmp1 in [-1,0,1]:
					x+=tmp1
					if (y!=tmpy)or(x!=tmpx):
						if ((x>=0)and(x<=4))and((y>=0)and(y<=4)):
							if (map[y][x]==9): 
								n+=1
					x-=tmp1
				y-=tmp0
			if map[tmpy][tmpx]!=9:
				map[tmpy][tmpx]=n



def PrintMap():
	x=-1
	tmp1=[]
	for tmp0 in range(5):
		tmp1.append(tmp0)
	for tmp0 in map:
		n=[]
		y=-1
		x+=1
		for tmp1 in map[x]:
			y+=1
			if map[x][y]==9:
				n.append(0)
			elif tmp1<9:
				n.append(0)
			elif tmp1>9:
				n.append(int(str(tmp1)[1])) 
	Print_Line(9)


		
	
def SelectCase():
	entry=[playerx, playery]
	tmp0=1
	while tmp0:
		try :
			tx=int(entry[0])
			ty=int(entry[1])
			tmp0=0
		except:
			tx = 0
	return tx,ty



def case_gestion(x,y):
	if map[y][x]==9:
		print "\n\n\n   You Die\n\n\n" 
		return True
	elif map[y][x]==-1:
		print "\n\n\n   You Won\n\n\n"
		return True
	else:
		#print map[y][x]
		return False


def Print_Line(n):
	for tmp0 in range(n):
		print
Print_Line(5)

def draw_grille():
	for a in range(12):
		pygame.draw.line(window,(0,0,0),[0,a*(window_h/12)],[window_w,a*(window_h/12)])
	for b in range(25):
		pygame.draw.line(window,(0,0,0),[b*(window_w/25),0],[b*(window_w/25),window_h])

def __main__(finish,tx,ty,playery,playerx, tmprandom):
	CreateMap()
	GenerateMineMap()
	GenerateMap()
	while not(finish):
		tx,ty=SelectCase()
		finish=case_gestion(tx,ty)
		tx,ty=0,0
		pygame.Surface.fill(window,(255,255,255))
		draw_grille()
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_DOWN:
				if playery == (window_h - (window_h/12)):
					pass
				else:
					playery = playery + (window_h/12)
			elif event.type == KEYDOWN and event.key == K_UP:
				if playery == 0:
					pass
				else:
					playery = playery - (window_h/12)
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				if playerx == (window_w - (window_w/25)):
					pass
				else: 
					playerx = playerx + (window_w/25)
			elif event.type == KEYDOWN and event.key == K_LEFT:
				if playerx == 0:
					pass
				else:
					playerx = playerx - (window_w/25)
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				quit()
		####
		pygame.draw.rect(window, [0, 150, 255], (((window_w-(window_w/25), (tmprandom*(window_h/12))-(window_h/12), (window_w/25), (window_h/12)))))
		####
		pygame.draw.rect(window, [162, 162, 162], (playerx, playery,(window_w/25) , (window_h/12)))
		pygame.display.flip()
__main__(finish,tx,ty,playery, playerx, tmprandom)
