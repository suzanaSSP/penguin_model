import numpy as np
import random

class Penguin:
    dt = 0.1
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = np.array([self.x, self.y])

        self.change_x = 0
        self.change_y = 0
        
        self.neighbors = None
        self.temperature = random.randint(0, 200)
        
    def check_state(self, center):
        if self.temperature < 200:
           self.move_to_center(center)
        elif self.temperature > 200:
            self.move_away(center)
        
    def penguin_in_front(self, new_c):
        for penguin in self.neighbors:
            if all(penguin.c == new_c):
                return True
        return False
                
    def move(self):
        new_x = self.x + (self.change_x * self.dt)   
        new_y = self.y + (self.change_y * self.dt)
        new_c = np.array([new_x, new_y])
        
        if self.penguin_in_front(new_c):
            pass
        else:
            self.x = new_x
            self.y = new_y
             
        self.change_x = 0
        self.change_y = 0  

    def move_to_center(self, center): 
        self.change_x = center[0] - self.x
        self.change_y = center[1] - self.y
        self.temperature += 1

    def move_away(self, center): 
        self.change_x = self.x - center[0]
        self.change_y = self.y - center[1]
        self.temperature -= 1
