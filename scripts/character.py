import time
class Character():
    def __init__(self):
        super().__init__()
        #physics related attributes
        self.vel = [0,0]
        self.acc = [0,0.35]
        #gameplay related atributes
        self.base_power = 5
        self.ki = 30
        self.health = 100
        self.full_health = 100
        self.multiplier = 0

        #animation related attributes
        self.frame = 0
        self.animations ={"idle":{},"test1": {"spritepack":"gokussj",
                "frames":[0, 2, 4, 5],
                0:{"duration":10,"action":"", "multiplier":0},
                2:{"duration":4,"action":"", "multiplier":0},
                4:{"duration":5,"action":"", "multiplier":0},
                5:{"duration":4,"action":"", "multiplier":0},
                }}
        self.animation = "intro"
        self.animation_dur = 0
        self.animation_counter = 0

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
            return

        if self.frame["duration"] == self.animation_dur:   
            if self.animation_counter == animation_last_index:
                self.animation = "idle"
                self.animation_counter = 0
                self.animation_dur = 0
                self.frame = self.animations["idle"]
                return                     
            self.animation_dur = 0
            self.animation_counter += 1
            frame_no = animation_["frames"][self.animation_counter]
            self.frame = animation_[frame_no]
            self.multiplier = self.frame["multiplier"]
    def update(self):
        if self.animation not in[ "","idle"]:
            self.play_animation()
        print(self.frame," ",self.animation," ",self.animation_counter)

cr = Character()
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
        