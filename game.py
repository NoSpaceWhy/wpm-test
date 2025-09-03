import pygame
import title

def key_box(screen, x, y, width, height, text_size,letter):
    key_font = pygame.font.Font(None, text_size)
    key_text = key_font.render(letter, True, (0, 0, 0))
    key_rect = pygame.Rect(x, y, width, height)
    key_rect = key_text.get_rect(center=key_rect.center)
    textBox_colour = (112, 146, 125)
    pygame.draw.rect(screen, textBox_colour, key_rect)
    return screen.blit(key_text, key_rect)
    
def game_run(screen, screen_width, screen_height):
    screen.fill((255, 255, 255))
    return_to_title = True
    # print("game")
          