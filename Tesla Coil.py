import pygame
import random


#Tva e na python 3.5 zaradi pygame nz tup sum

#Init makes things work i dunno ...
pygame.init()

#Making the color variables
black = (0,0,0)
purplish_blue = (204, 153, 255)
purple = (178, 102, 255)

#Window size
screen_width = 1000
screen_height = 800

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tesla Coil')

#Function for drawing the coil and the lightnings
def draw_a_tree(mouse_position):

    #Placing the Coil on the damn screen
    coil = pygame.image.load('tesla_coil.png')
    coil = pygame.transform.scale(coil, (500, 450))
    rect = coil.get_rect()
    rect = rect.move((250, 330))
    game_display.blit(coil, rect)

    pygame.display.update()

    first_point = (screen_width/2, screen_height/2)
    for i in range(0,2):
        color = random.choice([purple, purplish_blue])
        random_width = random.randint(0,800)
        random_height = random.randint(0,600)
        second_point = (random_width, random_height)
        pygame.draw.line(game_display, color, first_point, second_point, 2)
        pygame.draw.line(game_display, color, second_point, position, 2)

        first_point = second_point
        pygame.display.update()

game_exit = False
#This makes the window not close immediately

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    # Mouse position
    position = pygame.mouse.get_pos()

    game_display.fill(black)
    draw_a_tree(position)
    pygame.display.update()

pygame.quit()
quit()