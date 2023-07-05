import matplotlib.pyplot as plt
from agent import Penguin
import random

plotRealTime = True
Nt = 1000
min_pos = 5
max_pos = 15
num_agents = 20
L = 20


# Creating agents 
penguins = [Penguin(random.randint(min_pos, max_pos), random.randint(min_pos, max_pos)) for i in range(num_agents)]

# Add neighbors to each penguin
for penguin in penguins:
    penguin.neighbors = [other_penguin for other_penguin in penguins if other_penguin is not penguin]
    
center = [L//2, L//2]

fig, ax = plt.subplots()
for i in range(Nt):

    x = [agent.x for agent in penguins]
    y = [agent.y for agent in penguins]

    for agent in penguins:
        agent.check_state(center)

    if plotRealTime or (i == Nt-1):
        plt.cla()
        # Add penguins
        plt.scatter(x, y, s=10, c='k')
        # Add center
        ax.scatter(center[0], center[1], s=10, c='y')
        ax.set(xlim=(0, L), ylim=(0, L))
        ax.set_aspect('equal')
        plt.pause(0.01)

    for agent in penguins:
        agent.move()


plt.show()