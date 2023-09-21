import pygame
from pygame.locals import *
import sys

pygame.init()

larg, altu = 800, 600
screen = pygame.display.set_mode((larg, altu), 0, 32)

white = (255, 255, 255)
black = (0, 0, 0)
tamanho = 30
retangulo = []
circulo = []
quadrado = []


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        keys = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if keys[pygame.K_r]:
                retangulo.append(event.pos)
            elif keys[pygame.K_c]:
                circulo.append(event.pos)
            else:
                quadrado.append(event.pos)

        screen.fill(white)

        for s in quadrado:
            pygame.draw.rect(screen, black, (s[0], s[1], tamanho, tamanho))
        for r in retangulo:
            pygame.draw.rect(screen, black, (r[0], r[1], tamanho * 2, tamanho))
        for c in circulo:
            pygame.draw.circle(screen, black, c, tamanho)
        pygame.display.update()