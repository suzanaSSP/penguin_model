import numpy as np
import random
import math

class Penguin:
    dt = 0.1
    L = 50
    midway_radius = L//2
    center = [L//2, L//2]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = np.array([self.x, self.y])

        self.change_x = 0
        self.change_y = 0
        self.change_c = np.array([self.change_x, self.change_y])

        self.neighbors = None
        self.temperature = 20 - math.dist(self.center, self.c)
        self.switch = True

        self.color = 'k'
    def turn_on_switch(self):
        # This only runs on the first time to see where to start
        # if 19 < self.temperature < 21::
        if self.temperature < 10:
            self.switch = True
        elif self.temperature >= 10:
            self.switch = False
            
    def check_state(self):
        if self.switch:
            self.im_cold()
        elif not self.switch:
            self.im_warm()
        
    def penguin_in_front(self):
        for penguin in self.neighbors:        
            if np.linalg.norm(penguin.change_c - self.change_c) <= 1:
                return True
        return False
                
    def move(self): 
        # if self.penguin_in_front():
        #     self.x = -1 * self.change_c[0]
        #     self.y = -1 * self.change_c[1]
        #     self.c = np.array([self.x, self.y])
        #     self.temperature =  self.temperature = 20 - math.dist(self.center, self.c)
            
        # else:
        self.x = self.change_c[0]
        self.y = self.change_c[1]
        self.c = np.array([self.x, self.y])
        self.temperature = 20 - math.dist(self.center, self.c)
        
        self.change_x = 0
        self.change_y = 0

    def im_cold(self): 
        # move to center
        self.change_x = self.center[0] - self.x
        self.change_y = self.center[1] - self.y

        new_x = self.x + (self.change_x * self.dt)   
        new_y = self.y + (self.change_y * self.dt)

        self.change_c = np.array([new_x, new_y])
    
        if 19 < self.temperature < 21:
            self.switch = False
    
    def im_warm(self): 
        # move away from center
        self.change_x = self.x - self.center[0]
        self.change_y = self.y - self.center[1]

        new_x = self.x + (self.change_x * self.dt)   
        new_y = self.y + (self.change_y * self.dt)

        self.change_c = np.array([new_x, new_y])

        if self.temperature < 1:
            self.switch = True
            
    def change_colors(self):
        if math.dist(self.c, self.center) <= 5:
            self.color = 'tab:red'
        elif 5 < math.dist(self.c , self.center) <= 10:
            self.color = 'tab:orange'
        elif 10 < math.dist(self.c, self.center) <= 20:
            self.color = 'tab:blue'
        else:
            self.color = 'tab:cyan'

    def repel(self):
        r = 0
        for agent in self.repulsion_penguins:
            dist_vect = agent.change_c - self.change_c

            r += dist_vect / (dist_vect @ dist_vect)

        self.c = -1 * r
        self.x = self.c[0]
        self.y = self.c[1]






