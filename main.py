# General imports
import pygame
import sys

# Window parameters
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Tic Tac Toe')

# Define colors
white = (255,255,255)
black = (0,0,0)
blue = (0,200,50)

# Define borders and sprites

# Set FPS rate
clock = pygame.time.Clock()

# Game Loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window if user clicks close
            pygame.quit()
            running == False
            sys.exit()


