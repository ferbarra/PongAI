import pygame

def main():
    surface, size = create_window()
    
    
def create_window():
    title = 'Ping Pong'
    size = (600, 500)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Ping Pong')
    return surface, size

#def start_match():
    

class Player:
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.width = 15
        self.height = 100
        self.color = 0,0,0
    
        

main()