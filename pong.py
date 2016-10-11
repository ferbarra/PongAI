import pygame

def main():
    
    black = 0, 0, 0
    white = 255, 255, 255
    surface = create_window()
    
    
def create_window():
    title = 'Ping Pong'
    size = (600, 500)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Ping Pong')
    return surface

def start_match():
    class Player:
        width = 15
        height = 100
        color = 0,0,0
    
        

main()