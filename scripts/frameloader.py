from scripts import frames
from pygame.image import load

def load_frames(sprite_name):
    frames_ = []
    for frame in frames.Frames[sprite_name]:
        img = load(frame)
        
        frames_.append(img)
    #print(frames_)    
    return frames_