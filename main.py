import pygame
import sys

pygame.init()



FPS = 60
SCREEN_WIDTH = 600
SCREEN_HIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))

background_img = pygame.image.load("pixel-art-landscapes-flower-field-background_52683-125359.jpg")
screen.blit(background_img,(0,0))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



while True:
    screen.blit(background_img, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.circle(screen, "red", player_pos, 15)
    dt = clock.tick(FPS) / 1000
    pygame.display.flip()

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        if player_pos.y >= 300 * dt: player_pos.y -= 300 * dt
    if key[pygame.K_s]:
        if player_pos.y <= screen.get_height() - 300 * dt: player_pos.y += 300 * dt
    if key[pygame.K_a]:
        if player_pos.x >= 300 * dt: player_pos.x -= 300 * dt
    if key[pygame.K_d]:
        if player_pos.x <= screen.get_width() - 300 * dt: player_pos.x += 300 * dt



