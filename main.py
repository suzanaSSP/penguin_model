import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from agent import Penguin
import random
import numpy as np

plotRealTime = True
Nt = 1000
min_pos = 10
max_pos = 40
num_agents = 50
L = 50

def create_penguins():
    # Creating agents 
    penguins = [Penguin(random.randint(min_pos, max_pos), random.randint(min_pos, max_pos)) for _ in range(num_agents)]

    # Add neighbors to each penguin
    for penguin in penguins:
        penguin.neighbors = [other_penguin for other_penguin in penguins if other_penguin is not penguin]
        penguin.turn_on_switch()
        
    return penguins
        
def main():
    penguins = create_penguins()
    
    fig, ax = plt.subplots()
    
    for i in range(Nt):

        x = [agent.x for agent in penguins]
        y = [agent.y for agent in penguins]
        colors = [agent.color for agent in penguins]
    
        for agent in penguins:
            agent.check_state()

        if plotRealTime or (i == Nt-1):
            plt.cla()
            # Add penguins
            plt.scatter(x, y, s=60, c=colors)
            plt.scatter(L//2, L//2, s=60, c='tab:brown')
            ax.set(xlim=(0, L), ylim=(0, L))
            ax.set_aspect('equal')
            plt.pause(0.1)

        for agent in penguins:
            agent.move()
            agent.change_colors()

    plt.show()
    
if __name__ == '__main__':
    main()