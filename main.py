import pygame
import title
import game
pygame.init()


screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Wpm test")
clock = pygame.time.Clock()
delta = 0.1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))
    
    game.game_run(screen, screen_width, screen_height)
    pygame.display.flip()    
    clock.tick(60)