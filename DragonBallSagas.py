from imports import *

#frameloader.load_frames("goku_base1")

WINDOW_SIZE = [700,600]
Screen = pygame.display.set_mode(WINDOW_SIZE)

class Game():
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.playerGroup1 = pygame.sprite.Group() 
        self.playerGroup2 = pygame.sprite.Group() 
        self.kiblasts1 = pygame.sprite.Group()
        self.kiblasts2 = pygame.sprite.Group()
        self.close = False

        self.clock = pygame.time.Clock()

        self.start_game()
    def start_game(self):
        self.player1 =  Goku_base1("l",animations=Animations["goku_base1"],frames=frameloader.load_frames("goku_base1"))  
        self.playerGroup1.add(self.player1)
    def human_controller(self):
        #z,x,a,s,q,w,left,right,up,down
        key_indices = [False,False,False,False,False,False,False,False,False,False]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            key_indices[0] = True
        if keys[pygame.K_x]:
            key_indices[1] = True
        if keys[pygame.K_a]:
            key_indices[2] = True     
        if keys[pygame.K_s]:
            key_indices[3] = True  
        if keys[pygame.K_q]:
            key_indices[4] = True  
        if keys[pygame.K_w]:
            key_indices[5] = True   
        if keys[pygame.K_LEFT]:
            key_indices[6] = True        
        if keys[pygame.K_RIGHT]:
            key_indices[7] = True 
        if keys[pygame.K_UP]:
            key_indices[8] = True    
        if keys[pygame.K_DOWN]:
            key_indices[9] = True   
        return key_indices                                                                               
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
            self.player1.handle_control_input(self.human_controller())
            self.playerGroup1.update()
            pygame.display.flip()
            self.clock.tick(30)
        self.close_game()

game = Game()

if __name__ == "__main__":
    game.update()
