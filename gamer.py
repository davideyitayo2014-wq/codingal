import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Maze Runner")
clock = pygame.time.Clock()

player_x, player_y = 2.5, 2.5
player_angle = 0
FOV = math.pi /3
MAX_DEPTH = 20
SPEED = 0.05
MOUSE_SENS = 0.002

MAP = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,2,1],
    [1,0,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]

def cast_rays():
    for x in range(0, WIDTH, 2):
        ray_angle = player_angle - 0.52 + (x/WIDTH) * 1.04
        dist = 0
        while dist < 20:
            dist += 0.05
            tx = int(player_x + math.cos(ray_angle) * dist)
            ty = int(player_y + math.sin(ray_angle) * dist)
            if MAP[ty][tx] > 0:
                wall_h = int(3000 / dist)
                color = 255 - int(dist*10)
                pygame.draw.rect(screen, (color,color//2,color//2), (x, HEIGHT//2-wall_h//2, 2, wall_h))
                break

running = True
pygame.mouse.set_visible(False)
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.key ==pygame.K_ESCAPE: running = False

    keys = pygame.key.get_pressed()
    dx,dy = 0,0
    if keys[pygame.K_w]: dx,dy = math.cos(player_angle)*0.05