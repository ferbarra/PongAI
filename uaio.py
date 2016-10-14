# This module uses Pygame to draw strings in a window,
# to input a string from the keyboard and to determine the
# pixel height and width of a string for any font size.

import pygame
from pygame.locals import *

def draw_string(string, surface, location=(0, 0), font_size=24, fg_color=pygame.Color('white'), bg_color=pygame.Color('black')):
    # Draw a string on the window surface
    # - string is the str object to draw
    # - surface is the window's pygame.Surface object
    # - location is a tuple containing the x and y int
    #   coordinates of the upper left corner of the string
    # - font_size is the int font size used to draw the string
    # - fg_color is the Pygame.Color used to draw the string
    # - bg_color is the Pygame.Color used for the background

    font = pygame.font.SysFont(None, font_size, True)
    text_image = font.render(string, True, fg_color, bg_color)
    surface.blit(text_image, location)
    pygame.display.update()

def input_string(prompt, surface, location=(0, 0), font_size=24, fg_color=pygame.Color('white'), bg_color=pygame.Color('black'), ):
    # Draw a prompt string on the window surface. Check keys
    # pressed by the user until an enter key is pressed and
    # return the sequence of key presses as a str object
    #
    # - prompt is the str to display
    # - surface is the window's pygame.Surface object
    # - location is a tuple containing the x and y int
    #   coordinates of the upper left corner of the string
    # - font_size is the int font size used to draw the string
    # - fg_color is the Pygame.Color used to draw the string
    # - bg_color is the Pygame.Color used for the background

    key = K_SPACE
    answer = ''
    while key != K_RETURN:
        draw_string(prompt + answer, surface, location, font_size, fg_color, bg_color)
        key = _get_key()
        key_state = pygame.key.get_pressed()
        if (K_SPACE <= key <= K_z):
            letter = pygame.key.name(key)
            if key_state[K_LSHIFT] or key_state[K_RSHIFT] or key_state[K_CAPSLOCK]:
                letter = letter.upper()
            answer = answer + letter
        if key == K_BACKSPACE:
            answer = answer[0:len(answer)-1]
            draw_string(prompt + answer + '    ', surface, location, font_size, fg_color, bg_color)
    return answer

def get_height(string, font_size=24):
    # Return the int pixel height of the string,
    # which will be smaller than the font size
    # - string is the str object
    # - font_size is the int font size for the string

    color = pygame.Color('black')
    font = pygame.font.SysFont(None, font_size, True)
    text_image = font.render(string, True, color)
    return text_image.get_height()
 
def get_width(string, font_size=24):
    # Return the int pixel width of the string 
    # - string is the str object
    # - font_size is the int font size for the string

    color = pygame.Color('black')
    font = pygame.font.SysFont(None, font_size, True)
    text_image = font.render(string, True, color)
    return text_image.get_width()
 
def _get_key():
    # Poll the events until the user presses a key and return it.
    # Discard all other events.
    # - self is the Poke object

    event = pygame.event.poll()
    while event.type != KEYUP:
        event = pygame.event.poll()
    return event.key

def _test():
    # To test the code in this module remove the # from
    # the #_test line below. Don't forget to put the #
    # back before saving the module for production use.
    # When testing try the backspace key.
    # Closing the window will not work for this simple test.

    pygame.init()
    surface_size = (500, 400)
    window_title = 'Window Title'
    surface = pygame.display.set_mode(surface_size, 0, 0)
    pygame.display.set_caption(window_title)
    bg_color = pygame.Color('black')
    string = input_string('enter text', surface)
    height = get_height(string)
    width = get_width(string)
    draw_string(string, surface, (0, height))
    draw_string(string, surface, (200 + width, 0))
    
#_test()