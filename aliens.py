import pygame
from pygame.sprite import Sprite
import game_functions as gf

class Alien(Sprite) :
    """a class that describes first alien """
    def __init__ (self,ai_settings,r1,points,level_type) :
        super().__init__()
        self.ai_settings = ai_settings
        self.points = points
        self.image = pygame.image.load('Images/alien.png')
        self.rect = self.image.get_rect()
        self.level_type = level_type


        #print("r1 = "+str(r1))

        if r1 == 1 : #row 1
            self.rect.x = 750
            self.rect.y = 60
        elif r1 == 2 : # row 2
            self.rect.x = 750
            self.rect.y = self.rect.y = ai_settings.screen_height / 3
        elif r1 == 3 : # row 3
            self.rect.x = 750
            self.rect.y = self.rect.y = ai_settings.screen_height / 2
        elif r1 == 4 : # row 4
            self.rect.x = 750
            self.rect.y = 400

    def update(self,  score, returned):
        """a method to update the first  ailen's position"""
        if returned :
            self.rect.x = 750
        else :
            self.speed = gf.return_speed(self.level_type , score)
            self.rect.x -= self.speed

        if self.level_type == 'easy' :
            return self.speed


    def check_collisions (self,airball,alien_group,airball_group):
        """a method to check collosions"""
        # if airball_group.colliderect(alien_group) :
        # 	self.points += 1
        # 	print(self.points)
        self.points = 0
        collisions_list = pygame.sprite.groupcollide(airball_group, alien_group, True, True)
        self.points += len(collisions_list)
        return self.points


class Alien1(Sprite):
    """a class that describes second ailen """

    def __init__(self, ai_settings, r2, points,level_type):
        super().__init__()
        self.ai_settings = ai_settings
        self.points = points
        self.level_type = level_type
        self.image = pygame.image.load('Images/alien.png')
        self.rect = self.image.get_rect()
        self.speed = 4
        # print("r2 = "+str(r2))
        if r2 == 1:  # row 1
            self.rect.x = 750
            self.rect.y = 60
        elif r2 == 2:  # row 2
            self.rect.x = 750
            self.rect.y = self.rect.y = ai_settings.screen_height / 3
        elif r2 == 3:  # row 3
            self.rect.x = 750
            self.rect.y = self.rect.y = ai_settings.screen_height / 2
        elif r2 == 4:  # row 4
            self.rect.x = 750
            self.rect.y = 400

    def update(self,score , returned):
        if returned:
            self.rect.x = 750
        else:
            self.speed = gf.return_speed(self.level_type, score)
            self.rect.x -= self.speed

        if self.level_type == 'easy':
            return self.speed

    def check_collisions(self, alien_group1, airball_group):
        """a method to check collosions"""
        # if airball_group.colliderect(alien_group1) :
        # 	self.points += 1
        # 	print(self.points)
        self.points = 0
        collisions_list = pygame.sprite.groupcollide(airball_group, alien_group1, True, True)
        self.points += len(collisions_list)
        return self.points
