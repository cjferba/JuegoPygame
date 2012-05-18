#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
import pygame
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

WIDTH = 700
HEIGHT = 525

def carga_fondo(name, colorkey=None):
	fullname = os.path.join('img', name)
	try:
		image = pygame.image.load(fullname) 
	except pygame.error, message: 
		print 'No se puede cargar la imagen:', name
		raise SystemExit, message
	image = image.convert()
	return image, image.get_rect()

def carga_imagen(name, colorkey=None):
	fullname = os.path.join('img', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'No se puede cargar la imagen:', name
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None: 
		if colorkey is -1: 
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()

def divide_imagen(image, rect):
	subimage = image.subsurface(rect)
	return subimage, rect
#GIRAR img = pygame.transform.flip(imagen[0], 1, 0)

# Definimos el color de fondo y el de las figuras
COLOR_FONDO = (50, 100, 50)
COLOR_CUADRADO = (255, 0, 0)
COLOR_CIRCULO = (0, 0, 255)
def main():

	window = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("¡Hola pyGame!")
	fondo=carga_fondo("circulo.jpg")
	window.blit(fondo[0],fondo[1])
	pygame.display.flip()
	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
			elif pygame.mouse.get_pressed()[0]:
				print "Has usado el botón izquierdo del ratón",pygame.mouse.get_pos()
				sp=carga_imagen("car.png")
				x=264
				y=400
				window.blit(sp[0],(x,y))
				pygame.display.flip()
			elif eventos.type == KEYDOWN and eventos.key == K_SPACE:
				print "Has pulsado espacio" 
				pygame.draw.rect(window, COLOR_CUADRADO, (50, 50, 100, 100))
				pygame.display.flip()
			elif eventos.type == KEYDOWN and eventos.key == K_RETURN:
				print "has pulsado X1"
				x=x+10
				window.blit(fondo[0],fondo[1])
				window.blit(sp[0],(x,y))
				pygame.display.flip()
			elif eventos.type == KEYDOWN and eventos.key == K_UP:
				y=y-10
				img = pygame.transform.rotate(sp[0],90 )
				window.blit(fondo[0],fondo[1])
				window.blit(img,(x,y))
				pygame.display.flip()
				

	return 0

if __name__ == '__main__':
	pygame.init()
	main()
