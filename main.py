import pygame
import title
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
    
    title.draw_text(screen, "Wpm test", 100, (91, 79, 79), screen_width - 350, screen_height // 8)# this is the title
    title.draw_button(screen, "Start", 50, (0, 128, 0), screen_width - 425, screen_height // 5, 200, 100)# this is the start button    
    
    
    pygame.display.flip()    
    clock.tick(60)