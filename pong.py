import pygame

def main():
    surface, size = create_window()
    pong_ball = Ball([200, 200], 20, (255,255,255), surface)
    pong_ball.draw()
    
def create_window():
    title = 'Ping Pong'
    size = (600, 500)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Ping Pong')
    return surface, size

# User-definded classes:

class Ball:
    def __init__(self, center, radius, color, surface):
        self.center = center
        self.radius = radius
        self.color = color
        self.surface = surface
    
    def draw(self):
        # Draw circle
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
    



class Player:
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.width = 15
        self.height = 100
        self.color = 0,0,0
        self.surface = surface

main()