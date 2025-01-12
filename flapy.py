import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 400, 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption('Flappy Bird')


WHITE = (255, 255, 255)


clock = pygame.time.Clock()


bird_x = 50
bird_y = HEIGHT // 2
bird_width = 34
bird_height = 24
bird_velocity = 0
gravity = 0.5
jump_strength = -10


running = True

while running:
    screen.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    
    bird_velocity += gravity
    bird_y += bird_velocity

    
    pygame.draw.rect(screen, (255, 0, 0), (bird_x, bird_y, bird_width, bird_height))

    
    pygame.display.flip()

  
    clock.tick(30)

pygame.quit()
sys.exit()
