# IMPORTS ---------------------------
import pygame
import textGUI
#------------------------------------

# CONSTANTS -------------------------
WIDTH = 640
HEIGHT = 640
FPS = 60
#------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("01")
clock = pygame.time.Clock()
GUI = textGUI.TextGUI(screen, clock)

pygame.display.flip()
running = True

while running:
    screen.fill((0,0,0))
    # Draw GUI
    GUI.updateGUI()

    # Draw BG
    # Draw FG
    # Draw Player
    # Draw other entities

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(FPS)
    pygame.display.update()