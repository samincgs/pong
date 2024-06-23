from settings import *

class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            dt = self.clock.tick(60) / 1000
            
            pygame.display.update()
            
            
        pygame.quit()
        
        
if __name__ == '__main__':
    game = Game()
    game.run()