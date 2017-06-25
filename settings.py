class Settings():
    
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)    

        #bullet setting#
        
        self.bullet_width = 300
        self.bullet_height = 30
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 10

        #alien setting#        
        self.fleet_drop_speed = 10

        
        #ship setting#
        self.ship_limit = 3
        self.speedup_scale = 2.0
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
        
    def increase_speed(self):

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)  