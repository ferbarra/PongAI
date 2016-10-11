import pygame, time

def main():
    surface, size = create_window()
    game = Game(surface)
    game.play()
    pygame.quit()
    
def create_window():
    pygame.init()
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
        
    def move(self):
        surface_size = self.surface.get_size()
        for index in range(0, 2):
            self.center[index] = (self.center[index] + 1) % surface_size[index]  
            
          
        
class Game:
    def __init__(self, surface):
        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.ball = Ball([200, 200], 20, pygame.Color('white'), surface)
        self.close_clicked = False      
        
    def play(self):
        self.draw()
        while not self.close_clicked:
            self.handle_event()
            self.update()
            self.draw()
    
    def handle_event(self):
        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True 
            
    def update(self):
        self.ball.move()
        
    def draw(self):
        self.surface.fill(self.bg_color)
        self.ball.draw()
        pygame.draw.rect(self.surface, pygame.Color('white'), (10,200,20, 100))
        pygame.draw.rect(self.surface, pygame.Color('white'), (490,200,20, 100))
        pygame.display.update()    

main()