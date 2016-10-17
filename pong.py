import pygame, time, uaio

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
    def __init__(self, center, radius, speed, color, surface):
        self.center = center
        self.radius = radius
        self.speed = speed
        self.color = color
        self.surface = surface
        self.surface_size = surface.get_size()
        self.score = [0,0]
    
    def draw(self):
        # Draw circle
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
        # Draw left score
        uaio.draw_string(str(self.score[0]), self.surface, (20,10))
        # Draw right score
        uaio.draw_string(str(self.score[1]), self.surface, (self.surface_size[0] - 30, 10))
        
    def move(self):
        self.bounce()
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.speed[index]
    
    def bounce(self):
        # if ball touches left side of the screen
        if (self.center[0] + self.radius >= self.surface_size[0]):
            # return ball to the center of the screen.
            self.return_to_center()
            # increase score in favor of left player
            self.score[0] += 1
        # if the ball touches the right side of the screen.
        elif (self.center[0] - self.radius <= 0):
            # return ball to the center of the screen.
            self.return_to_center()
            self.score[1] +=1
        # if the ball touches the up or down side of the screen
        if (self.center[1] + self.radius >= self.surface_size[1] or self.center[1] - self.radius <= 0):
            #self.center[x] = self.center[0] * -1
            self.speed[1] *= -1           
            
    def return_to_center(self):
        self.center = [int(self.surface_size[0]/2),int(self.surface_size[1]/2)]
    
    
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
        self.ball = Ball([200, 200], 20, [1,1], self.fg_color, surface)
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