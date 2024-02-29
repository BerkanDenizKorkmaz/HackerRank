import pygame
import os

WIDTH, HEIGTH = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
FPS = 60
VEL = 5

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10 , HEIGTH)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
def draw_window(red, yellow):
    win.fill(WHITE)
    pygame.draw.rect(win, (0,0,0), BORDER)
    win.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    win.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL

    if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x:  # RIGHT
        yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL

    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGTH: # DOWN
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        red.x -= VEL

    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        red.x += VEL

    if keys_pressed[pygame.K_UP]: # UP
        red.y -= VEL

    if keys_pressed[pygame.K_DOWN]: # DOWN
        red.y += VEL

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        draw_window(red,yellow)





    pygame.quit()

if __name__ == "__main__":
    main()