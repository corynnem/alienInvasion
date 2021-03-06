class Settings(): 
    # A class to store all settings for Alien Invasion

    def __init__(self): 
    # Initialize game settings
    # Screen settings
        self.screen_width = 900
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    # Ship settings
        self.ship_speed_factor = 1.5

    # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

    # Alien settings
        self.alien_speed_factor = float(0.1)
        self.fleet_drop_speed = 1
        self.fleet_direction = 1
