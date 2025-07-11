from settings import Settings
def move_char(ds_settings) :
    """ checking if character exeeded its limits (screen) """

    if ds_settings.down and  ds_settings.d_y <= ds_settings.screen_height - 115:
        ds_settings.d_y += ds_settings.speed
    elif ds_settings.down  and  ds_settings.d_y > ds_settings.screen_height - 115 :
        ds_settings.d_y -= 0

    if ds_settings.up and ds_settings.d_y >= -13 :
        ds_settings.d_y -= ds_settings.speed
    elif ds_settings.up :
        ds_settings.d_y += 0

def return_speed(level_type , score) :
    ai_settings = Settings()
    if level_type == 'easy':

        if score <=  10 :
            speed = 2.6
        if score > 10 and score <= 40:  # between 30 and 60 speed = 5
            speed = 3
        elif score > 40 and score <= 70:  # between 60 and 90 speed =6
            speed = 3.5
        elif score > 70 and score <= 90:  # between 60 and 90 speed =6
            speed = 4
        elif score > 90 and score <= 120:  # between 60 and 90 speed =6
            speed = 4.5
        elif score > 120 and score <= 160:  # between 60 and 90 speed =6
            speed = 5
        elif score > 160 and score <= 200:  # between 60 and 90 speed =6
            speed = 6.5
        elif score > 200:
            speed = 7.5

    elif level_type == 'medium':
        ai_settings.speed = 8

        if score > 30 and score <= 60:  # between 30 and 60 speed = 5
            speed = 3.8
        elif score > 60 and score <= 70:  # between 60 and 90 speed =6
            speed = 4.5
        elif score <= 30:
            speed = 3
        elif score > 70 and score <= 90:  # between 60 and 90 speed =6
            speed = 4.9
        elif score > 90 and score <= 120:  # between 60 and 90 speed =6
            speed = 5.5
        elif score > 120 and score <= 160:  # between 60 and 90 speed =6
            speed = 6
        elif score > 160 and score <= 200:  # between 60 and 90 speed =6
            speed = 7.5
        elif score > 200:
            speed = 9
    elif level_type == 'hard':
        ai_settings.speed = 100

        if score > 30 and score <= 60:  # between 30 and 60 speed = 5
            speed = 4.5
        elif score > 60 and score <= 70:  # between 60 and 90 speed =6
            speed = 5.3
        elif score <= 30:
            speed = 4
        elif score > 70 and score <= 90:  # between 60 and 90 speed =6
            speed = 5.9
        elif score > 90 and score <= 120:  # between 60 and 90 speed =6
            ai_settings.speed = 11
            speed = 6.7
        elif score > 120 and score <= 160:  # between 60 and 90 speed =6
            speed = 7.9
            ai_settings.speed = 12
        elif score > 160 and score <= 200:  # between 60 and 90 speed =6
            speed = 9
            ai_settings.speed = 13
        elif score > 200:
            ai_settings.speed = 10
            speed = 15

    return speed
