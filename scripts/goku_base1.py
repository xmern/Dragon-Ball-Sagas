from scripts import character

class Goku_base1(character.Character):
    def __init__(self, side, animations ,frames):
        character.Character.__init__(self, side, animations ,frames)    
        self.actions = [self.punch1, self.punch2]
    def charge(self):
        pass
    def punch1(self):
        self.animation = "punch1"
        self.frame_no = self.animations["punch1"]["frames"][0]
    def punch2(self):
        pass
    def handle(self,indices,human=True):
        if self.animation == "idle":
              if self.attacking == False:
                  if human:
                       if indices[0]:
                      
                          self.punch1
                      

