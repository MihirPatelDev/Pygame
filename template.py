# Pygame template - skeleton for a new pygame project
import pygame
import random

width = 360
hight = 480
fps = 30

# define colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# initialize pygame and crate window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Pygame Project")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(fps)
    # Process input (events)
    for event in pygame.event.get():
        #check for closing windown
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
