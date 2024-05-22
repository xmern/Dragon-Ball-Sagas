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
        self.frame = self.animations["punch1"][self.frame_no]
        self.attacking = True
    def punch2(self):
        self.animation = "punch2"
        self.frame_no = self.animations["punch2"]["frames"][0]
        self.frame = self.animations["punch2"][self.frame_no]
        self.attacking = True
    def punch3(self):
        self.animation = "punch3"
        self.frame_no = self.animations["punch3"]["frames"][0]
        self.frame = self.animations["punch3"][self.frame_no]
        self.attacking = True    
    def kick1(self):
        self.animation = "kick1"
        self.frame_no = self.animations["kick1"]["frames"][0]
        self.frame = self.animations["kick1"][self.frame_no]
        self.attacking = True             
    def handle_control_input(self,indices,human=True):
        if self.animation == "idle":
              if self.attacking == False:
                  if human:
                       if indices[0]: 
                          no = self.randint(0,1)
                          if no:
                            self.punch2()
                          else:
                              self.punch3()  
                       elif indices[1]:                   
                          no = self.randint(0,3)
                          if not no:
                            self.punch1()
                          elif no == 1:
                              self.kick1()                       

