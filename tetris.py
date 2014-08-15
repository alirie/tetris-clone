from sys import exit
import pygame
from pygame.locals import *
from random import *


class Game:
	'''Tetris-Clone...'''

	def __init__(self):

		self.screen = pygame.display.set_mode([300, 600])  #
		self.x, self.y = 150, 0  #
		self.score = 0  #
		self.level = 1  #
		self.speed = 'speed'  #
		self.paused = False  # bool

		self.shape_i = Shape(self.screen, pygame.Color(0, 255, 0), ((100, 0), (200, 0), (200, 25), (100, 25)))  #
		self.shape_j = Shape(self.screen, pygame.Color(255, 255, 0), ((100, 0), (125, 0), (125, 25), (175, 25), (175, 50), (100, 50)))  #
		self.shape_l = Shape(self.screen, pygame.Color(0, 0, 255), ((100, 25), (150, 25), (150, 0), (175, 0), (175, 50), (100, 50)))  #
		self.shape_o = Shape(self.screen, pygame.Color(0, 255, 255), ((125, 0), (175, 0), (175, 50), (125, 50)))  #
		self.shape_s = Shape(self.screen, pygame.Color(120, 30, 60), ((100, 25), (125, 25), (125, 0), (175, 0), (175, 25), (150, 25), (150, 50), (100, 50)))  #
		self.shape_t = Shape(self.screen, pygame.Color(255, 0, 0), ((100, 0), (175, 0), (175, 25), (150, 25), (150, 50), (125, 50), (125, 25), (100, 25)))  #
		self.shape_z = Shape(self.screen, pygame.Color(60, 30, 120), ((100, 0), (150, 0), (150, 25), (175, 25), (175, 50), (125, 50), (125, 25), (100, 25)))  #
		
		self.shapes = [self.shape_i, self.shape_j, self.shape_l, self.shape_o, self.shape_s, self.shape_t, self.shape_z]
		self.foo = []  #

		self.current_Shape = New_Shape(self.shapes)


class Shape:
	'''Tetris Shape'''

	def __init__(self, Surface, color, pointlist, width=0):
		self.Surface = Surface
		self.color = color
		self.pointlist = pointlist
		self.width = width
		#pygame.draw.polygon(Surface, color, pointlist, width=0) -> Rect

def Move_Game(Game):
	new_pointlist = [list(coord) for coord in Game.current_Shape.pointlist]
	for coord in new_pointlist:
		coord[1] += 1
	Game.current_Shape.pointlist = tuple(new_pointlist)


def Move_Shape(Game, xy, direction):
	new_pointlist = [list(coord) for coord in Game.current_Shape.pointlist]
	for coord in new_pointlist:
		coord[xy] += direction
	Game.current_Shape.pointlist = tuple(new_pointlist.copy())


def Collision_Test():
	pass


def Pause_Game():
	pass


def Game_Over():
	pass


def Do_Stuff_With_Input(Game):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
			if event.key == K_p:
				Pause_Game()
			if event.key == K_UP:
				Game.current_Shape = New_Shape(Game.shapes)
				pass
			if event.key == K_LEFT:
				Move_Shape(Game, 0, -25)
			if event.key == K_RIGHT:
				Move_Shape(Game, 0, 25)
			if event.key == K_DOWN:
				Move_Shape(Game, 1, 25)


def Draw_Foo():
	for row in foo:
		for slot in row:
			pygame.draw.rect(screen, pygame.Color(r, g, b), (slot, row, 25, 25))
		pass
	pass


def New_Shape(shapes):
	ran = randint(0, 6)
	return shapes[ran]


def Run_Game():
	pygame.init()
	Tetris_Game = Game()
	Tetris_Game.current_Shape = Tetris_Game.shape_z
	while 1:
		#Draw Screen
		Tetris_Game.screen.fill(pygame.Color(0, 0, 0))
		#Draw Foo
		#Draw_Foo()
		#Draw current Shape
		pygame.draw.polygon(Tetris_Game.current_Shape.Surface, Tetris_Game.current_Shape.color, Tetris_Game.current_Shape.pointlist)

		Do_Stuff_With_Input(Tetris_Game)

		ticks = pygame.time.get_ticks()
		if ticks % 40 == 0:
			Move_Game(Tetris_Game)

		pygame.display.update()


if __name__ == "__main__":
	Run_Game()