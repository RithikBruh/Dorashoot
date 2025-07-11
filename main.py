import pygame
import sys
from pygame.locals import *
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint
from aliens import Alien
from aliens import Alien1
import time

# this is asshole code

class Ball(Sprite):
    """a class that describes air ball (bullet)"""

    def __init__(self, ai_settings):
        super().__init__()
        self.ai_settings = ai_settings
        self.image = pygame.image.load('Images/rock.png')  # loading bullet png
        self.rect = self.image.get_rect()  # making it as a rect
        self.rect.x = ai_settings.d_x + 93  # placing it 93 more than the doaramon x axis
        self.rect.y = ai_settings.d_y + 75  # placing it 75 more than the doaramon y axis

    def update(self):
        """ a  method to update the ball (bullet) position """
        self.rect.x += self.ai_settings.ball_speed


class Mouse(Sprite):
    """a class to change mouse icon and replace with new one"""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/doraemon_mouse.png')  # loading cursor image
        self.rect = self.image.get_rect()  # making it as a rectangle

    def update(self):
        """a method to update its position """
        self.rect.center = pygame.mouse.get_pos()  # getting the position of mouse


def main():
    """main function go run the game"""

    ai_settings = Settings()  # creating settings istance
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('DoraShoot  by Rithik')
    # add images
    doraemon_image = pygame.image.load('Images/d_shooting_copy.png')
    doraemon_image_rect = doraemon_image.get_rect()
    background_image = pygame.image.load('Images/background.png')
    bg_1 = pygame.image.load('Images/bg_1.png')  # image for choose level window
    medium_image = pygame.image.load('Images/medium.png')
    bg_2 = pygame.image.load('Images/game_over.png')
    hard_image = pygame.image.load('Images/hard.png')
    mute_image = pygame.image.load('Images/mute.png')
    unmute_image = pygame.image.load('Images/unmute.png')
    restart_image = pygame.image.load('Images/restart.png')
    menu = pygame.image.load('Images/menu.png')
    instructions = pygame.image.load('Images/instructions.png')
    # making mouse invisible
    pygame.mouse.set_visible(True)  # Todo : just kept for test , change again to False
    # setting background image x and y coordinates
    b_x = 1
    b_y = 1
    b1_x = 0
    b1_y = 0
    easy_x = 250
    easy_y = 120
    med_x = 250
    med_y = 200
    hard_x = 250
    hard_y = 280
    m_x = 745
    m_y = 460
    um_x = 745
    um_y = 460
    r_x = 250
    r_y = 50
    p_x = 290
    p_y = 250
    ma_x = 0
    ma_y = 0
    # mouse
    mouse = Mouse()
    mouse_group = Group()
    mouse_group.add(mouse)

    # air  ball
    airball_group = Group()
    airball = Ball(ai_settings)
    shoot_sound = pygame.mixer.Sound('SoundEffects/pop.wav')

    # bg musics
    gameover_music = pygame.mixer.Sound('SoundEffects/gameover.wav')

    # alien group
    alien_group = Group()
    # alien1 group
    alien_group1 = Group()

	# initailly score will be 0
    score = 0
    #initaillt returned will be false 
    returned = False
    # initally lives will be 3
    lives = 3
    life_image = pygame.image.load('Images/doracake.png')

    # windows
    win_chooselevel = True #todo : make it as false
    win_game = False
    win_gameover = False
    game_active = True
    win_menu = True
    win_ins = False

    # clock
    fps = 60
    clock = pygame.time.Clock()

    if game_active : 
        while game_active :

            if win_menu :
                bg_choose = pygame.mixer.Sound('SoundEffects/choose.wav')
                bg_choose.play(-1)

                # it is in window menu
                while True:
                    screen.blit(menu , (ma_x , ma_y))
                    play_image = pygame.image.load('Images/play.png')
                    screen.blit(play_image , (p_x , p_y))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()          
                            game_active = False

                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_p :
                                print('play')
                                win_menu = False
                                win_ins = True
                                bg_choose.stop()
                                pygame.time.wait(1000)
                                break

                        elif event.type == pygame.MOUSEBUTTONDOWN :
                            p = pygame.mouse.get_pos()
                            #print(p)
                            for x in range(290, 490):
                                for y in range(249, 352):
                                    if p == (x, y):
                                        print('play')
                                        win_menu = False
                                        win_ins = True
                                        bg_choose.stop()
                                        pygame.time.wait(1000)
                                        break


                    mouse_group.draw(screen)  # draws mouse on screen
                    mouse_group.update()  # updates mouse position
                    pygame.display.update()
                    if win_menu == False :
                        break

            if win_ins :
                bg_choose = pygame.mixer.Sound('SoundEffects/choose.wav')
                bg_choose.play(-1)

                # it is in window menu
                while True:
                    screen.blit(instructions , (ma_x , ma_y))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                            game_active = False

                        if event.type == pygame.KEYDOWN :
                            print('choose level ')
                            win_ins = False
                            win_chooselevel = True
                            bg_choose.stop()
                            pygame.time.wait(1000)
                            break


                    mouse_group.draw(screen)  # draws mouse on screen
                    mouse_group.update()  # updates mouse position
                    pygame.display.update()
                    if win_ins == False :
                        break

            if win_chooselevel:
                bg_choose = pygame.mixer.Sound('SoundEffects/choose.wav')
                bg_choose.play(-1)
                sound = 'unmute'
                # it is in window choose level
                while True:
                    screen.blit(bg_1, (b1_x, b1_y))  # adding background image
                    easy_image = pygame.image.load('Images/easy_1.png')
                    screen.blit(easy_image, (easy_x, easy_y))
                    screen.blit(medium_image, (med_x, med_y))
                    screen.blit(hard_image, (hard_x, hard_y))
                    if sound == 'unmute':  # if unmute we should print mute image
                        screen.blit(mute_image, (m_x, m_y))
                        bg_choose.set_volume(1)
                    if sound == 'mute':  # if mute we should print unmute image
                        screen.blit(unmute_image, (um_x, um_y))
                        bg_choose.set_volume(0)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                            game_active = False
                        if event.type == KEYDOWN:
                            if event.key == pygame.K_m:
                                print(sound)
                                if sound == 'mute':
                                    sound = 'unmute'
                                elif sound == 'unmute':
                                    sound = 'mute'
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print(pygame.mouse.get_pos())
                        # elif event.type == MOUSEBUTTONDOWN :
                        p = pygame.mouse.get_pos()

                    if event.type == MOUSEBUTTONDOWN:
                        for x in range(266, 468):
                            for y in range(210, 260):
                                if p == (x, y):
                                    print('Easy')
                                    pygame.time.wait(1000)
                                    win_game = True
                                    level_type = 'easy'

                        for x in range(270, 459):
                            for y in range(295, 343):
                                if p == (x, y):
                                    print('Medium')
                                    pygame.time.wait(1000)
                                    win_game = True
                                    level_type = 'medium'

                        for x in range(744, 785):
                            for y in range(465, 492):
                                if p == (x, y):
                                    print(sound)
                                    if sound == 'mute':
                                        sound = 'unmute'
                                        break
                                    elif sound == 'unmute':
                                        sound = 'mute'
                                        break

                        for x in range(266, 468):
                            for y in range(376, 423):
                                if p == (x, y):
                                    print('hard')
                                    pygame.time.wait(1000)
                                    win_game = True
                                    level_type = 'hard'

                    if win_game:
                        bg_choose.stop()
                        break

                    mouse_group.draw(screen)  # draws mouse on screen
                    mouse_group.update()  # updates mouse position
                    pygame.display.update()

            if win_game:

                if returned :
                    lives = 3
                score = 0
                bg_music = pygame.mixer.Sound('SoundEffects/game.wav')
                bg_music.set_volume(0.4)
                bg_music.play(-1)
                sound = 'unmute'
                while True:  # main loop of the game
                    # score text
                    font = pygame.font.Font('freesansbold.ttf', 22)
                    score_message = font.render(('Score :' + str(score)), True, (233, 0, 0), False)
                    score_message_rect = score_message.get_rect()
                    score_message_rect.center = (730, 20)

                    lives_message = font.render('Lives :', True, (255, 0, 0), False)
                    lives_message_rect = lives_message.get_rect()
                    lives_message_rect.center = (40, 25)

                    screen.blit(background_image, (b_x, b_y))  # adding background image
                    screen.blit(doraemon_image, (ai_settings.d_x, ai_settings.d_y))  # adding Character
                    screen.blit(score_message, score_message_rect)
                    screen.blit(lives_message, lives_message_rect)

                    if sound == 'unmute':  # if unmute we should print mute image
                        screen.blit(mute_image, (m_x, m_y))
                        bg_music.set_volume(0.4)
                    if sound == 'mute':  # if mute we should print unmute image
                        screen.blit(unmute_image, (um_x, um_y))
                        bg_music.set_volume(0)

                    life_image_x = 80
                    life_image_y = 5

                    life_image_x1 = 120
                    life_image_y1 = 5

                    life_image_x2 = 160
                    life_image_y2 = 5
                    if lives == 1:
                        screen.blit(life_image, (life_image_x, life_image_y))
                    elif lives == 2:
                        screen.blit(life_image, (life_image_x, life_image_y))
                        screen.blit(life_image, (life_image_x1, life_image_y1))

                    elif lives == 3:
                        screen.blit(life_image, (life_image_x, life_image_y))
                        screen.blit(life_image, (life_image_x1, life_image_y1))
                        screen.blit(life_image, (life_image_x2, life_image_y2))

                    elif score == 0:
                        pass

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                            game_active = False

                        if event.type == KEYDOWN:  # checks if player pressed key

                            if event.key == K_DOWN:
                                ai_settings.down = True
                            elif event.key == K_UP:
                                ai_settings.up = True
                            elif event.key == K_q:
                                pygame.quit()
                                sys.exit()
                            elif event.key == K_p:
                                print(score)
                            elif event.key == K_l:
                                print(lives)
                            elif event.key == K_SPACE:
                                if len(airball_group) <= 0:
                                    shoot_sound.play()
                                    airball = Ball(ai_settings)
                                    airball_group.add(airball)

                            if event.key == pygame.K_m:
                                print(sound)
                                if sound == 'mute':
                                    sound = 'unmute'
                                elif sound == 'unmute':
                                    sound = 'mute'

                        elif event.type == KEYUP:  # checks if player  released  key
                            if event.key == K_DOWN:
                                ai_settings.down = False
                            elif event.key == K_UP:
                                ai_settings.up = False

                        elif event.type == MOUSEBUTTONDOWN :
                            p = pygame.mouse.get_pos()
                            for x in range(744, 785):
                                for y in range(465, 492):
                                    if p == (x, y):
                                        print(sound)
                                        if sound == 'mute':
                                            sound = 'unmute'
                                            break
                                        elif sound == 'unmute':
                                            sound = 'mute'
                                            break

                    # randomly generating rows or alien 1 and alien 2
                    if len(alien_group) == 0:
                        r1 = randint(1, 4)
                    if len(alien_group1) == 0:
                        r2 = randint(1, 4)
                    # making both rows not equal
                    while True:
                        if r1 == r2:
                            r2 = randint(1, 4)
                        elif r1 != r2:
                            break

                    gf.move_char(ai_settings)  # moving doraemon character

                    airball_group.draw(screen)  # drawing the elements in air ball group
                    airball_group.update()  # updating the position of air ball

                    # getting rid of extra bullets
                    for air_ball in airball_group.copy():
                        if air_ball.rect.x > 770:
                            airball_group.remove(airball)

                    # creating alien and alien 1 instances
                    alien = Alien(ai_settings, r1, score, level_type)
                    alien1 = Alien1(ai_settings, r2, score, level_type)

                    if len(alien_group) == 0:  # adding alien if no of aliens are 0
                        alien_group.add(alien)

                    elif len(alien_group) > 0:  # removing aliens if no of aliens are greater than 0
                        for i in range(len(alien_group.copy())):
                            alien_group.remove(i)

                    for alien_g in alien_group.copy():  # removing aliens which are going out of screen
                        if alien_g.rect.x < 0:
                            if lives > 0:
                                lives -= 1
                            alien_group.remove(alien_g)

                    if len(alien_group1) == 0:  # adding alien if no of aliens are 0
                        alien_group1.add(alien1)


                    elif len(alien_group1) > 0:  # removing aliens if no of aliens are greater than 0
                        for i in range(len(alien_group1.copy())):
                            alien_group1.remove(i)

                    for alien_g1 in alien_group1.copy():  # removing aliens which are going out of screen
                        if alien_g1.rect.x < 0:
                            if lives > 0:
                                lives -= 1

                            alien_group1.remove(alien_g1)

                    alien_group.draw(screen)  # drawing aliens in group
                    alien_group.update(score,returned)  # updating its position
                    alien_group1.draw(screen)
                    alien_group1.update(score,returned)

                    #MAKE returned false
                    returned = False

                    # checking collisions
                    points1 = alien.check_collisions(airball, alien_group, airball_group)
                    points2 = alien1.check_collisions(alien_group1, airball_group)
                    score = score + points1 + points2

                    mouse_group.draw(screen)  # draws mouse on screen
                    mouse_group.update()  # updates mouse position
                    pygame.display.update()
                    if lives == 0:
                        win_gameover = True
                        pygame.time.wait(500)
                        break
                    clock.tick(fps)

            if win_gameover:
                win_game = False
                bg_music.stop()
                while True:
                    # adding background image
                    screen.blit(bg_2, (0, -4))
                    #adding restart image
                    screen.blit(restart_image , (r_x , r_y))
                    # adding score text
                    font = pygame.font.Font('freesansbold.ttf', 35)
                    score_message1 = font.render(('Score : ' + str(score)), True, (0, 30, 255), False)
                    score_message1_rect = score_message.get_rect()
                    score_message1_rect.center = (100, 150)
                    screen.blit(score_message1, score_message1_rect)

                    gameover_music.set_volume(0.3)
                    gameover_music.play()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                            game_active = False

                        if event.type == MOUSEBUTTONDOWN :
                            p = pygame.mouse.get_pos()
                            #print(p)
                            for x in range(149, 199):
                                for y in range(53, 95):
                                    if p == (x, y):
                                        print('restart')
                                        pygame.time.wait(1000)
                                        win_gameover = False
                                        win_game = True
                                        win_chooselevel = False
                                        gameover_music.stop()
                                        break


                    if event.type == KEYDOWN :
                            if event.key == pygame.K_r :
                                win_gameover = False
                                win_game  = True
                                win_chooselevel = False
                                gameover_music.stop()
                                pygame.time.wait(1000)
                                break 
                    if win_game :
                        returned = True
                        break 

                    mouse_group.draw(screen)  # draws mouse on screen
                    mouse_group.update()  # updates mouse position
                    pygame.display.update()

                # if win_game :
                #     break 

main()