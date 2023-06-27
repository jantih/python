import pygame
import textGUI
pygame.init()

WIDTH = 640
HEIGHT = 640
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Static FPS Test")
clock = pygame.time.Clock()
GUI = textGUI.TextGUI(screen, clock)

pygame.display.flip()

running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    GUI.updateGUI()
    clock.tick(FPS)
    pygame.display.update()