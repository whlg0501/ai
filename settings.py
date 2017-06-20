class Settings():
    
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 230)    

        #bullet setting#
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 10

        #alien setting#
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction 1 move right -1 move left#
        self.fleet_direction = 1

        #ship setting#
        self.ship_speed_factor = 2.5
        self.ship_limit = 3