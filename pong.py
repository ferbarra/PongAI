import pygame, time, uaio
from abc import ABC, abstractmethod

def main():
    window = create_window()
    
    menu_screen = MenuScreen(window)
    game_screen = GameScreen(window)
    game_over_screen = GameOverScreen(window)

    screens = [menu_screen, game_screen, game_over_screen]

    current_screen = menu_screen
    exit_program = False

    while not exit_program:
        # This assigns a the new screen when the old
        # one finished running.
        next_screen_name = current_screen.run()
        if next_screen_name == 'quit':
            exit_program = True
        for screen in screens:
            if screen.name == next_screen_name:
                current_screen = screen

    pygame.quit()
    
def create_window():
    pygame.init()
    title = 'Ping Pong'
    size = (700, 400)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    return surface

# User-definded classes:

"""
Every Screen class has a method called run which is tasked to perform
all the things that need to happen in each screen with the use of the
class's methods and attributes.
"""

class Screen(ABC):

    @abstractmethod
    def run(self):
        pass

class MenuScreen(Screen):

    def __init__(self, surface):
        self.name = 'menu'
        self.surface = surface

    def draw(self):
        # Renders its contents into the surface.
        uaio.draw_string("PONG", self.surface, location=(0, 50), center=True)
        self.start_game_button = uaio.create_button(
            "Start Game",
            self.surface,
            location=(0,150),
            center=True
        )
        pygame.display.update()

    def handleEvents(self):
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.start_game_button.collidepoint(mouse_pos):
                return "game"

    def run(self):
        print("Beginning screen running.")
        self.draw()
        choice = None
        while choice is None:
            choice = self.handleEvents()
        return choice

class GameOverScreen(Screen):
    
    def __init__(self, surface):
        self.name = 'game over'
        self.surface = surface

    def draw(self):
        uaio.draw_string("GAME OVER", self.surface, location=(0,100), center=True)
        self.play_again_btn = uaio.create_button(
            "Play Again",
            self.surface,
            location=(0,150),
            center=True
        )
        self.main_screen_btn = uaio.create_button(
            "Main Screen",
            self.surface,
            location=(0,200),
            center=True
        )

    def handleEvents(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.play_again_btn.collidepoint(mouse_pos):
                return "game"
            if self.main_screen_btn.collidepoint(mouse_pos):
                return "menu"

    def run(self):
        self.draw()
        choice = None
        while choice is None:
            choice = self.handleEvents()
        return choice

class GameScreen(Screen):
    def __init__(self, surface):
        self.name = 'game'
        self.surface = surface
        self.surface_size = surface.get_size()
        self.bg_color = pygame.Color('black')
        self.fg_color = pygame.Color('white')
        self.ball = Ball([int(self.surface_size[0]/2), int(self.surface_size[1]/2)], 10, [1,1], self.fg_color, surface)
        self.left_player = pygame.Rect(30,200, 15, 100)
        self.right_player = pygame.Rect(self.surface_size[0] - 45, 200, 15, 100)
        self.score = [0,0]
        self.close_clicked = False
        pygame.key.set_repeat(20, 20)
        
    def run(self):
        self.draw()
        while not self.close_clicked:
            self.handle_event()
            # wait some time so game doesn't go insanely fast
            time.sleep(0.00005)
            self.update()
            self.draw()
    
    def handle_event(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.close_clicked = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.move_player(self.left_player, -10)
            if event.key == pygame.K_a:
                self.move_player(self.left_player, 10)
            if event.key == pygame.K_p:
                self.move_player(self.right_player, -10)
            if event.key == pygame.K_l:
                self.move_player(self.right_player, 10)
                
                
    def move_player(self, player, scalar):
        if (scalar < 0 and player.top >= scalar):
            player.move_ip(0,scalar)
        elif (scalar > 0 and player.top + player.height <= self.surface_size[1] - scalar):
            player.move_ip(0, scalar)
        """
        Review this code later:
        if (player.y > scalar and player.y + player.height < self.surface_size[1]):
            player.move_ip(0, scalar)
        """           
            
    def update(self):
        if self.ball.score[0] < 11 and self.ball.score[1] < 11:
            self.ball.wall_collision()
            self.ball.paddle_collision(self.left_player, self.right_player)
            self.ball.move()
        
    def draw(self):
        self.surface.fill(self.bg_color)
        self.ball.draw()
        pygame.draw.rect(self.surface, self.fg_color, self.left_player)
        pygame.draw.rect(self.surface, self.fg_color, self.right_player)
        pygame.display.update()    
        

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
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.speed[index]
    
    def wall_collision(self):
        # if ball touches left side of the screen
        if (self.center[0] + self.radius >= self.surface_size[0]):
            # change x direction
            self.speed[0] *= -1
            # increase score in favor of left player
            self.score[0] += 1
        # if the ball touches the right side of the screen.
        elif (self.center[0] - self.radius <= 0):
            # change x direction
            self.speed[0] *= -1
            self.score[1] +=1
        # if the ball touches the up or down side of the screen
        if (self.center[1] + self.radius >= self.surface_size[1] or self.center[1] - self.radius <= 0):
            self.speed[1] *= -1           


    def paddle_collision(self, left_player, right_player):
        if left_player.collidepoint(self.center) and self.speed[0] < 0:
            self.speed[0] *= -1
        if right_player.collidepoint(self.center) and self.speed[0] > 0:
            self.speed[0] *= -1

if __name__ == '__main__':
    main()