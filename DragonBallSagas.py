from imports import *

#frameloader.load_frames("goku_base1")

WINDOW_SIZE = [700,600]
Screen = pygame.display.set_mode(WINDOW_SIZE)

class Game():
    def __init__(self):
        self.playerGroup1 = pygame.sprite.Group() 
        self.playerGroup2 = pygame.sprite.Group() 
        self.kiblasts1 = pygame.sprite.Group()
        self.kiblasts2 = pygame.sprite.Group()
        self.close = False

        self.clock = pygame.time.Clock()

        self.start_game()
    def start_game(self):
        player =  Goku_base1("l",animations=Animations["goku_base1"],frames=frameloader.load_frames("goku_base1"))  
        self.playerGroup1.add(player)
    def human_controller(self):
        pass
        
    def draw_char(self):
        pass
    def check_hits(self):
        pass
    def close_game(self):
        exit()
    def update(self):
        while self.close == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close = True
                    pygame.quit()
            if self.close == True:
                break
            Screen.fill((255,255,255))
            self.playerGroup1.draw(Screen)
            self.playerGroup1.update()
            pygame.display.flip()
            self.clock.tick(30)
        self.close_game()

game = Game()

if __name__ == "__main__":
    game.update()
