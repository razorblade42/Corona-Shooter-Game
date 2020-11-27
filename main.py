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
        self.speed_x = 0
        self.speed = 8

    def boundary(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def movement(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speed_x = self.speed
        if keystate[pygame.K_LEFT]:
            self.speed_x = -self.speed
        self.rect.x += self.speed_x
    def update(self):
        self.movement()
        self.boundary()

class Corona(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH-self.rect.width)
        self.rect.y = random.randrange(-150,-100)
        self.speed_y = random.randrange(2,8)
        self.speed_x = random.randrange(-3,3)  #x direction motion
    def spawn_new_corona(self):
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2, 8)
        self.speed_x = random.randrange(-3, 3)  # x direction motion
    def boundary(self):
         if self.rect.left >  WIDTH + 5 or self.rect.right < -5 or self.rect.top > HEIGHT + 5:
            self.spawn_new_corona()
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.boundary()
#Game Functions


#Game sprites
all_sprites = pygame.sprite.Group()
all_corona = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(9):
    m = Corona()
    all_corona.add(m)
    all_sprites.add(m)
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