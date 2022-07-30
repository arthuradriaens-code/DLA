import numpy as np
import random
from PIL import Image 
import colorsys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from alive_progress import alive_bar

#deze code is totaal ni efficient oeps haha
#setting the width of the output image as 128, can later be scaled
WIDTH = 512

def update(state):
    choises = [-1,1]
    for i in range(WIDTH):
        for j in range(WIDTH):
            if int(state[i][j]) == 1:
                if (i<WIDTH-1 and j < WIDTH-1 and -1<i and -1<j) and (state[i+1][j] == 2 or state[i-1][j] == 2 or state[i][j-1] == 2 or state[i][j+1] == 2):
                    state[i][j] = 2
                else:
                    if random.random() < 0.5:
                        i_ = 0
                        j_ = int(random.choice(choises))
                        if (j_ + j) > WIDTH - 1:
                            j_ = -j
                        elif (j_ + j) < 0:
                            j_ = WIDTH - 1 - j
                    else:
                        j_ = 0
                        i_ = int(random.choice(choises))
                        if (i_ + i) < 0:
                            i_ = WIDTH - 1 - i
                        elif (i_ + i) > WIDTH - 1:
                            i_ = -i
                    if int(state[i+i_][j+j_]) == 1:
                        state[i][j] = 1
                    else:
                        state[i][j] = 0 
                        state[i+i_][j+j_] = 1
            elif int(state[i][j]) == 2:
                state[i][j] = 2
    return state

#initialization
DLA = np.zeros((WIDTH,WIDTH)) #nothing
DLA[int(WIDTH/2)][int(WIDTH/2)] = 2 #DLA center

with alive_bar(WIDTH*10,title='Initializing',length=20,bar='filling',spinner='dots_waves2') as bar:
    for _ in range(int(WIDTH*10)): #amount of random sprites
        r = np.random.randint(10,WIDTH/2 - WIDTH/8)
        theta = np.random.uniform(0,2*np.pi)
        i = round(r*np.cos(theta) + WIDTH/2)
        j = round(r*np.sin(theta) + WIDTH/2)
        DLA[i][j] = 1
        bar()

fig, ax = plt.subplots()

calctime = 5000

dlas = np.zeros((calctime,WIDTH,WIDTH))

with alive_bar(calctime,title='Calculating',length=20,bar='filling',spinner='dots_waves2') as bar:
    for i in range(calctime):
        dlas[i] = DLA
        DLA = update(DLA)
        bar()
def animate(i):
    ax.clear()
    ax.imshow(dlas[i],origin='lower',interpolation='nearest')

anim = FuncAnimation(fig, animate,frames=calctime, interval=40)
anim.save('DLA.mp4')
ax.clear()
ax.imshow(DLA,origin='lower')
plt.savefig('final.pdf')
