import pygame
#import game.py
import game

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
    return screen.blit(text_surface, text_rect)
    
def title_run(screen, screen_width, screen_height):
    mos_pos = pygame.mouse.get_pos()
    
    game_start = False
    
    draw_text(screen, "Wpm test", 100, (91, 79, 79), 700, screen_height // 8)# this is the title
    start = draw_button(screen, "Start", 50, (0, 128, 0), screen_width - 450, screen_height // 5, 300, 100)# this is the start button
    game_mode = draw_button(screen, "Game mode", 50, (0, 0, 255), screen_width - 450, screen_height // 3, 300, 100)# this is the settings button
    Quit = draw_button(screen, "Quit", 50, (255, 0, 0), screen_width - 450, screen_height // 2.2, 300, 100)# this is the quit button
    
    if Quit.collidepoint(mos_pos):
        if pygame.mouse.get_pressed()[0]:
            print("real quit")
            pygame.quit()
            exit()
    
    if start.collidepoint(mos_pos):
        if pygame.mouse.get_pressed()[0]:
            game_start = True
            print("start")
        return 
    
    if game_mode.collidepoint(mos_pos):
        if pygame.mouse.get_pressed()[0]:
            print("game mode")
            # add game mode functionality here
