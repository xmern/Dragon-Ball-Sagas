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
    def kick2(self):
        self.animation = "kick2"
        self.frame_no = self.animations["kick2"]["frames"][0]
        self.frame = self.animations["kick2"][self.frame_no]
        self.attacking = True  
    def charge(self):
        self.animation = "charge"
        self.frame_no = self.animations["charge"]["frames"][0]
        self.frame = self.animations["charge"][self.frame_no]
                              
    def handle_control_input(self,indices,human=True):
        if self.animation in ["idle","left","right","up","down"]:
              if human:
                    if self.attacking == False:
                        
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
                                elif no == 2:
                                    self.kick2() 
                            elif indices[3]:
                                self.charge()     
                            elif indices[6] and indices[8]:
                                self.move_left()
                                self.move_up() 
                                if self.direction == "right":
                                    self.animation = "left"  
                                else:
                                    self.animation = "right"    
                            elif indices[7] and indices[8]:
                                self.move_right()
                                self.move_up() 
                                if self.direction == "right":
                                    self.animation = "right"  
                                else:
                                    self.animation = "left"                                  
                            elif indices[6]:
                                self.move_left()
                                if self.direction == "right":
                                    self.animation = "left"  
                                else:
                                    self.animation = "right" 
                            elif indices[7]:
                                self.move_right()
                                if self.direction == "right":
                                    self.animation = "right"  
                                else:
                                    self.animation = "left" 
                            elif indices[8]:
                                self.move_up()
                                self.animation = "up"                                
                            elif indices[9]:
                                self.move_down()
                                self.animation = "down"
                            else:
                                self.animation = "idle"    
    def update(self):
        super().update()
        if self.animation == "charge":
            self.rect.bottom += self.frame["offsety"] * self.scale
            if self.direction == "right":
                self.rect.x += self.frame["offsetx"] * self.scale
            if self.direction == "left":
                self.rect.x += self.frame["offsetxl"] * self.scale