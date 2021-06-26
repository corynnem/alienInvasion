import pygame 

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen 
        self.ai_settings = ai_settings

        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right: 
            self.rect.centerx += 1
        if self.moving_left: 
            self.rect.centerx -= 1

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)