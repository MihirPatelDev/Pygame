# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

width = 800
hight = 600
fps = 30

# define colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# set up assets folders
# Windows: "C:\Users\Mihir Coding\PycharmProjects\Pygame\Img\p1_jump.img"
# Mac: /Users/Mihir Coding/PycharmProjects/Pygame/Img/img"
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
    #Sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, hight / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > width:
            self.rect.right = 0

# initialize pygame and crate window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Pygame Project")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
    screen.fill(blue)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()