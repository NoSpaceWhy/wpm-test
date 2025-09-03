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

def keyboard():
    keyboard_layout = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
    ]
    
    key_width = 100
    key_height = 100
    key_spacing = 10
    start_x = 80
    start_y = 80
    text_size = 50
    
    keys = []
    # what the helll is this
    for row_index, row in enumerate(keyboard_layout):
        for col_index, letter in enumerate(row):
            x = start_x + col_index * (key_width + key_spacing) + (row_index * (key_width // 2))
            y = start_y + row_index * (key_height + key_spacing)
            keys.append((letter, x, y, key_width, key_height, text_size))
    
    return keys

   
def game_run(screen, screen_width, screen_height):
    screen.fill((255, 255, 255))
    return_to_title = True
    # print("game")
    keyboard_keys = keyboard()
    for key in keyboard_keys:
        letter, x, y, width, height, text_size = key
        key_box(screen, x, y, width, height, text_size, letter)
        