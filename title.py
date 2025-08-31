import pygame

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
    
    
def draw_button(screen, text, size, color, x, y, width, height):
    font = pygame.font.Font(None, size)
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)