class Settings():
    
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 230)

        #ship move speed#
        self.ship_speed_factor = 2.5

        #bullet setting#
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 10