import sys

import pygame

from settings import Settings
from alien import Alien
from ship import Ship 
import game_functions as gf
from pygame.sprite import Group 




def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game. 
    while True: 
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        #Watch the keyboard and mouse events
  

run_game()



