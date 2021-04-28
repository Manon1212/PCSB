

"""

import pygame

# Colors are triplets containint RGB values
# (see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  create the window
W, H = 500, 500  # Size of the graphic window
# Note that (0,0) is at the *upper* left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('square')

screen.fill(WHITE)  # fill it with white

# Draw a rectangle at the center of the screen (in the backbuffer)
width, height = 200, 200  # dimensions of the rectangle in pixels
left_x = center_x - width // 2  # x coordinate of topleft corner
top_y = center_y - height // 2  # y coordinate of topleft corner
pygame.draw.rect(screen, BLUE, (left_x, top_y, width, height))

pygame.display.flip()  # display the backbuffer on the screen

# save the image into a file
pygame.image.save(screen, "square-blue.png")


# Wait until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()

"""


#! /usr/bin/env python
# Time-stamp: <2021-03-25 13:26:23 christophe@pallier.org>
""" This is a simple reaction time experiment.

At each trial, a cross is displayed after some random time interval.
The user must click as quickly as possible on a key or a mouse button.

Reaction times are measured and saved in a file for further analyses.

"""
"""
import random
import pygame

N_TRIALS = 3  # total number of trials
MIN_WAIT_TIME = 2000
MAX_WAIT_TIME = 3000
MAX_RESPONSE_DELAY = 380
RESULT_FILE = 'reaction_times.csv'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def create_window():
	W, H = 1000, 1000 #Size of the graphic window
	center_x, center_y = W/2, H/2 
	screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
    return screen


def clear_screen(screen):
    screen.fill(BLACK)
    pygame.display.flip()


def display_instruction(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 32)
    line1 = myfont.render("A square patch of light will flash at irregular time intervals. Press a key as soon as possible when you see it !", 1, pygame.Color('white'))
    line2 = myfont.render("Press space bar to start.", 1, pygame.Color('white'))
    screen.blit(line1, (x, y))
    screen.blit(line2, (x, y + 60))
    pygame.display.flip()

left_x = (center_x - width  // 2) + d

def present_stimulus(angle)
	width, height = 35, 25 # dimensions of the rectangle in pixels
	left_x = center_x - width // 2  # x coordinate of topleft corner
	top_y = center_y - height // 2  # y coordinate of topleft corner
	pygame.draw.rect(screen, WHITE, left_x + angle, top_y, width, height)
	



def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True


def measure_reaction_time(max_response_delay=2000):
    button_pressed = False
    escape = False
    response_delay_elapsed = False
    reaction_time = 0
    pygame.event.clear()  # anticipations will be ignored
    t0 = pygame.time.get_ticks()

    while not button_pressed and not escape and not response_delay_elapsed:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                escape = True
                break
            if ev.type == pygame.QUIT:
                escape = True
                break
            if ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.KEYDOWN:
                reaction_time = pygame.time.get_ticks() - t0
                button_pressed = True

        if pygame.time.get_ticks() - t0 > MAX_RESPONSE_DELAY:
            response_delay_elapsed = True

    if escape:
        return None
    else:
        return reaction_time

def save_data(waiting_times, reaction_times, filename=RESULT_FILE):
    with open(filename, 'wt') as f:
        f.write('Wait,RT\n')
        for wt, rt in zip(waiting_times, reaction_times):
            f.write(f"{wt},{rt}\n")


##### main

pygame.init()
screen = create_window()
r = screen.get_rect()
W, H = r.width, r.height
center_x = W // 2
center_y = H // 2

waiting_times = []
reaction_times = []

display_instruction(screen, 20, center_y)
wait_for_keypress()
clear_screen(screen)

pygame.time.delay(2000)

for i_trial in range(N_TRIALS):
    clear_screen(screen)

    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    pygame.time.delay(waiting_time)

    present_cross(center_x, center_y, 20, pygame.Color('white'))

    reaction_time = measure_reaction_time()
    if reaction_time is None:  # escape pressed
        break

    waiting_times.append(waiting_time)
    reaction_times.append(reaction_time)
    print(i_trial, waiting_time, reaction_time)

save_data(waiting_times, reaction_times)
pygame.quit()



Les rectangles doivent être à x distance du centre :
0.43588989435
1.78
3.3166
"""
import random
import pygame

N_TRIALS = 3  # total number of trials
MIN_WAIT_TIME = 2000
MAX_WAIT_TIME = 3000
MAX_RESPONSE_DELAY = 380
RESULT_FILE = 'reaction_times.csv'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def create_window():
	W, H = 1000, 1000 #Size of the graphic window
	center_x, center_y = W/2, H/2 
	screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
    return screen


def clear_screen(screen):
    screen.fill(BLACK)
    pygame.display.flip()


def display_instruction(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 32)
    line1 = myfont.render("A square patch of light will flash at irregular time intervals. Press a key as soon as possible when you see it !", 1, pygame.Color('white'))
    line2 = myfont.render("Press space bar to start.", 1, pygame.Color('white'))
    screen.blit(line1, (x, y))
    screen.blit(line2, (x, y + 60))
    pygame.display.flip()

left_x = (center_x - width  // 2) + d

def present_stimulus(angle)
	width, height = 35, 25 # dimensions of the rectangle in pixels
	left_x = center_x - width // 2  # x coordinate of topleft corner
	top_y = center_y - height // 2  # y coordinate of topleft corner
	pygame.draw.rect(screen, WHITE, left_x + angle, top_y, width, height)
	



def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True


def measure_reaction_time(max_response_delay=2000):
    button_pressed = False
    escape = False
    response_delay_elapsed = False
    reaction_time = 0
    pygame.event.clear()  # anticipations will be ignored
    t0 = pygame.time.get_ticks()

    while not button_pressed and not escape and not response_delay_elapsed:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                escape = True
                break
            if ev.type == pygame.QUIT:
                escape = True
                break
            if ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.KEYDOWN:
                reaction_time = pygame.time.get_ticks() - t0
                button_pressed = True

        if pygame.time.get_ticks() - t0 > MAX_RESPONSE_DELAY:
            response_delay_elapsed = True

    if escape:
        return None
    else:
        return reaction_time

def save_data(waiting_times, reaction_times, filename=RESULT_FILE):
    with open(filename, 'wt') as f:
        f.write('Wait,RT\n')
        for wt, rt in zip(waiting_times, reaction_times):
            f.write(f"{wt},{rt}\n")


##### main

pygame.init()
screen = create_window()
r = screen.get_rect()
W, H = r.width, r.height
center_x = W // 2
center_y = H // 2

waiting_times = []
reaction_times = []

display_instruction(screen, 20, center_y)
wait_for_keypress()
clear_screen(screen)

pygame.time.delay(2000)

for i_trial in range(N_TRIALS):
    clear_screen(screen)

    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    pygame.time.delay(waiting_time)

    present_cross(center_x, center_y, 20, pygame.Color('white'))

    reaction_time = measure_reaction_time()
    if reaction_time is None:  # escape pressed
        break

    waiting_times.append(waiting_time)
    reaction_times.append(reaction_time)
    print(i_trial, waiting_time, reaction_time)

save_data(waiting_times, reaction_times)
pygame.quit()



Les rectangles doivent être à x distance du centre :
0.43588989435
1.78
3.3166
