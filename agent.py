import numpy as np
import random

class Penguin:
    dt = 0.1
    radius = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = np.array([self.x, self.y])

        self.change_x = 0
        self.change_y = 0
        self.change_c = np.array([self.change_x, self.change_y])

        self.neighbors = None
        self.temperature = random.randint(0,50)
        self.switch = True


    def check_state(self, center):
        if self.switch:
            self.cold(center)
        elif not self.switch:
            self.warm(center)
        
    def penguin_in_front(self):
        for penguin in self.neighbors:        
            if np.linalg.norm(penguin.change_c - self.change_c) <= 1:
                return True
        return False
                
    def move(self): 
        if self.penguin_in_front():
            self.x = -1 * self.change_c[0]
            self.y = -1 * self.change_c[1]

        else:
            self.x = self.change_c[0]
            self.y = self.change_c[1]

        self.change_x = 0
        self.change_y = 0

    def cold(self, center): 
        # move to center
        self.change_x = center[0] - self.x
        self.change_y = center[1] - self.y

        new_x = self.x + (self.change_x * self.dt)   
        new_y = self.y + (self.change_y * self.dt)

        self.change_c = np.array([new_x, new_y])

        self.temperature += 1

        if self.temperature == 50:
            self.switch = False
    
    def warm(self, center): 
        # move away from center
        self.change_x = self.x - center[0]
        self.change_y = self.y - center[1]

        new_x = self.x + (self.change_x * self.dt)   
        new_y = self.y + (self.change_y * self.dt)

        self.change_c = np.array([new_x, new_y])

        self.temperature -= 1

        if self.temperature == 0:
            self.switch = True

    def repel(self):
        r = 0
        for agent in self.repulsion_penguins:
            dist_vect = agent.change_c - self.change_c

            r += dist_vect / (dist_vect @ dist_vect)

        self.c = -1 * r
        self.x = self.c[0]
        self.y = self.c[1]






