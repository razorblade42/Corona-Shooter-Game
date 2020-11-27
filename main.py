import pygame
import random

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,0)

#settings:
pygame.init()
pygame.mixer.init()
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shoot-Karona!")
clock = pygame.time.Clock()
FPS = 60

#Game Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10  #sepration between bottom and ship

    def update(self):
        pass


#Game Functions


#Game sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Main Game
running = True
while running:
    clock.tick(FPS)

    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update (for our sprites)
    all_sprites.update()
    #Draw/Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #Update the display
    pygame.display.update()
pygame.quit()