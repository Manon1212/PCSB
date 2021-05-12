
import random
import pygame
import sys

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

W, H = 1000, 1000 #Size of the graphic window
center_x, center_y = W/2, H/2 

def create_window():
    screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
    return screen


def clear_screen(screen):
    screen.fill(BLACK)
    pygame.display.flip()


def display_instruction(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 32)
    line1 = myfont.render("A square patch of light will flash at irregular time intervals.", 1, pygame.Color('white'))
    if key == pygame.K_q:
        line2 = myfont.render("Press the key a as soon as possible when you see it !", 1, pygame.Color('white'))
    else:
        line2 =myfont.render("Press the key p as soon as possible when you see it !", 1, pygame.Color('white'))
    line3 = myfont.render("Press space bar to start.", 1, pygame.Color('white'))
    screen.blit(line1, (x, y))
    screen.blit(line2, (x, y + 60))
    screen.blit(line3, (x, y + 120))
    pygame.display.flip()



def present_stimulus(angle_choice, left_or_right):
    width, height = 35, 25 # dimensions of the rectangle in pixels
    left_x = center_x - width // 2  # x coordinate of topleft corner
    top_y = center_y - height // 2  # y coordinate of topleft corner
    Rect = (left_x + angle_choice * left_or_right, top_y, width, height)
    pygame.draw.rect(screen, WHITE, Rect)
    pygame.display.flip()



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
            if ev.key == pygame.K_q or ev.key == pygame.K_p:
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

#side = sys.argv[1]
#print(side)


pygame.init()
screen = create_window()
key = random.choice([pygame.K_q, pygame.K_p])


waiting_times = []
reaction_times = []

display_instruction(screen, 10, center_y)
wait_for_keypress()
clear_screen(screen)

pygame.time.delay(2000)


trial_number= 1 
left_or_right = random.choice([1, -1]) #stimulus lateralizatioon
angle = [4.3588989435, 100.8, 500.166] #distance from the center
for angle_choice in angle:
    clear_screen(screen)

    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    pygame.time.delay(waiting_time)

    present_stimulus(angle_choice, left_or_right)

    reaction_time = measure_reaction_time()
    if reaction_time is None: # escape pressed
        break

    waiting_times.append(waiting_time)
    reaction_times.append(reaction_time)
    print(trial_number, waiting_time, reaction_time)
    trial_number = trial_number+1


save_data(waiting_times, reaction_times)
pygame.quit()


