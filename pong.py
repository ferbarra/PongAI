import pygame, time

def main():
    surface = create_window()
    game = Game(surface)
    game.play()
    pygame.quit()
    
def create_window():
    pygame.init()
    title = 'Ping Pong'
    size = (600, 500)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Ping Pong')
    return surface

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
            
class Player:
    def __init__(self, coordinates, width, height, color, surface):
        self.coordinates = coordinates
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
        
    def draw(self):
        # Draw rectangle
        pygame.draw.rect(self.surface, self.color, (self.coordinates[0],self.coordinates[1], self.width, self.height))
        
class Game:
    def __init__(self, surface):
        self.surface = surface
        self.surface_size = surface.get_size()
        self.bg_color = pygame.Color('black')
        self.fg_color = pygame.Color('white')
        self.ball = Ball([200, 200], 20, self.fg_color, surface)
        self.player_1 = Player([10,200], 20, 100, self.fg_color, surface)
        self.player_2 = Player([self.surface_size[0] - 30, 200], 20, 100, self.fg_color, surface)
        self.close_clicked = False      
        
    def play(self):
        self.draw()
        while not self.close_clicked:
            self.handle_event()
            # wait some time so game doesn't go insanely fast
            time.sleep(0.005)
            self.update()
            self.draw()
    
    def handle_event(self):
        event = pygame.event.poll()
        if event.type == 'QUIT':
            self.close_clicked = True 
            
    def update(self):
        self.ball.move()
        
    def draw(self):
        self.surface.fill(self.bg_color)
        self.ball.draw()
        self.player_1.draw()
        self.player_2.draw()
        pygame.display.update()    
        

main()