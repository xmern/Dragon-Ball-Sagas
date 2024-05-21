from  pygame.sprite import Sprite
import time

class Character(Sprite):
    def __init__(self, side, animations ,frames=[]):
        super().__init__()
    
        #physics related attributes
        self.vel = [0,0]
        self.acc = [0,0.35]
        self.friction = 0.4
        #gameplay related atributes
        self.base_power = 5
        self.ki = 30
        self.health = 100
        self.full_health = 100
        self.multiplier = 0

        self.side = side
        self.actions = []

        #animation related attributes
        self.frame = 0
        self.animations = animations
        {"idle":{},"intro":{"frames":[0],0:{"duration":10,"action":"", "multiplier":0}},"test1": {"spritepack":"gokussj",
                "frames":[0, 2, 4, 5],
                0:{"duration":10,"action":"", "multiplier":0},
                2:{"duration":4,"action":"", "multiplier":0},
                4:{"duration":5,"action":"", "multiplier":0},
                5:{"duration":4,"action":"", "multiplier":0},
                }}
        self.animation = "intro"
        self.animation_dur = 0
        self.animation_counter = 0
        self.frames = frames
        self.frame_no = self.animations["intro"]["frames"][0]
        self.frame = self.animations["intro"][self.animations['intro']['frames'][0]]
        print(len(self.frames))
        self.image = self.frames[self.frame_no]
        self.rect = self.image.get_rect()
        self.attacking = False
        self.animation_actions = [self.instantTransmission,self.tele_forward,self.tele_backward]

    def play_animation(self):
        try:
            animation_ = self.animations[self.animation]
            animation_last_index = len(animation_["frames"])-1
            
        except KeyError:
            print(f"animation {self.animation} does not exist in animations dictionary")    
            return
        if self.animation_dur < self.frame["duration"]:
            self.animation_dur += 1 
        if self.animation_counter > animation_last_index:
            self.animation = "idle"
            self.animation_counter = 0
            self.animation_dur = 0
            self.frame = self.animation["idle"]
            self.frame_no = 0
            return

        if self.frame["duration"] == self.animation_dur:   
            if self.animation_counter == animation_last_index:
                self.animation = "idle"
                self.attacking = False
                self.animation_counter = 0
                self.animation_dur = 0
                self.frame = self.animations["idle"]
                self.frame_no = 0
                return                     
            self.animation_dur = 0
            self.animation_counter += 1
            self.frame_no = animation_["frames"][self.animation_counter]
            self.frame = animation_[self.frame_no]
            self.multiplier = self.frame["multiplier"]
    def instantTransmission(self,x,y):
        self.rect.center = x,y
    def tele_forward(self):
        self.rect.x += 200    
    def tele_backward(self):
        self.rect.x -= 200  
    def tele_upward(self):
        self.rect.y -= 200               
    def get_frame(self):
        pass
    def update(self):
        if self.animation not in[ "","idle"]:
            self.play_animation()
        if self.animation == "idle":
            self.frame_no = self.animations["idle"]["frames"][0]    
        self.image = self.frames[self.frame_no]
        #print(self.frame_no)
        #print(self.frame," ",self.animation," ",self.animation_counter)
'''
cr = Character()
cr.frame = {"duration":10,"action":"", "multiplier":0}
cr.animation_dur = 0
cr.animation = "test1"'''

if __name__ == "__main__":
    cr = Character('r',{})
    cr.frame = {"duration":10,"action":"", "multiplier":0}
    cr.animation_dur = 0
    cr.animation = "test1"
    while True:
        cr.update()
        time.sleep(0.5)




"""
the vel and acc lists store velocity and acceleration respectively acc_y is set to 0.35 i.e gravity 
self.ki is the character's ki energy it is full when at 100
self.health is the character health
frame keeps the current frame
animation keeps the current animation eg intro, attack_0 charge, etc
each frame is to play for a certain number of cycles this is tracked by animation_dur so 4 means the
animation is to play for 4 cycles, running at 30fps that's 4/30 of a second.
animation counter keeps track of the index of the current frame in the animation
"""        
        