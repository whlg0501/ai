import pygame

class Cat():

    def __init__(self, screen):
        '''初始化飞船并设置其初始位置 不懂'''
        self.screen = screen


        self.image = pygame.image.load('images/cat.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centerx

    def blitme(self):

        self.screen.blit(self.image, self.rect)