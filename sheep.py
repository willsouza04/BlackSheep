import pygame, random

from pygame.sprite import Sprite

class Sheep(Sprite):

    # Inicia a ovelha e configura a posição, velocidade e direção.
    def __init__(self, screen, settings, color_sheep):
        super(Sheep, self).__init__()

        self.screen = screen
        self.color_sheep = color_sheep
        self.settings = settings

        if self.color_sheep == "black":
            self.image = pygame.image.load('images/black sheep.png')
        else:
            self.image = pygame.image.load('images/white sheep.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.centerx = float(random.randint(1, settings.screen_width))
        self.centery = float(random.randint(1, settings.screen_height))

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.direction = [random.choice([1, -1]), random.choice([1, -1])]

        if self.direction[0] == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        self.speed_x = random.random() + settings.sheep_speed
        self.speed_y = random.random() + settings.sheep_speed


    # Atualiza a posição e velocidade da ovelha.
    def update(self, settings):
        if self.direction[0] == 1:
            if self.rect.right > self.screen_rect.right:
                self.direction[0] = -1
                self.speed_x = random.random() + settings.sheep_speed
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            if self.rect.left < self.screen_rect.left:
                self.direction[0] = 1
                self.speed_x = random.random() + settings.sheep_speed
                self.image = pygame.transform.flip(self.image, True, False)
        if self.direction[1] == 1:
            if self.rect.bottom > self.screen_rect.bottom:
                self.direction[1] = -1
                self.speed_y = random.random() + settings.sheep_speed
        else:
            if self.rect.top < self.screen_rect.top:
                self.direction[1] = 1
                self.speed_y = random.random() + settings.sheep_speed

        self.centerx += (self.speed_x * self.direction[0])
        self.centery += (self.speed_y * self.direction[1])

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    # Altera a cor da ovelha.
    def loadColorSheep(self, color):
        if color == "black":
            self.image = pygame.image.load('images/black sheep.png')
        else:
            self.image = pygame.image.load('images/white sheep.png')

        if self.direction[0] == -1:
            self.image = pygame.transform.flip(self.image, True, False)


    # Desenha a ovelha em seu local devido.
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    
