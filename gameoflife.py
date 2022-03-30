##!/usr/bin/env python3

"""

    Title :      gameoflife.py
    Notes :      Evolves a 2D data of cells from a user-given initial configuration, as per the rules of Game of Life (by John Conway) or similar
    Output :     Interactive, real-time evolving animation of 2D data
    Author :     Ayan Acharyya
    Started :    Mar 2022
    Example :    run gameoflife.py

"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.colors import LinearSegmentedColormap
import os, sys, argparse, time, datetime, random, copy

# -----------------------------------------------------
def evolve_conwayrule(data):
    '''
    Function to evolve an input data of cells based on the original criteria by John Conway (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):
    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    '''
    newdata = copy.deepcopy(data) # by default cells stay the same as the previous iteration
    map_live_nghbr = np.zeros(np.shape(data))

    for i in range(np.shape(data)[0]):
        for j in range(np.shape(data)[1]):
            map_live_nghbr[i, j] = np.sum(data[i-1: i+1, j-1: j+1]) - data[i, j]

    newdata[np.where((data == 1) & ((map_live_nghbr < 2) | (map_live_nghbr > 3)))] = 0 # any live cell with <2 or >3 live neighbour dies
    newdata[np.where((data == 0) & (map_live_nghbr == 3))] = 1 # any dead cell with 3 live neighbour becomes live
    # everything else stays live or stays dead

    return newdata

# -----------------------------------------------------
def evolve_myrule1(data):
    '''
    Function to evolve an input data of cells based on following criteria:

    '''
    newdata = copy.deepcopy(data)

    return newdata

# -----------------------------------------------------
def initialise_interactive_data(args):
    '''
    Function to initialise a figure for the interactive input 2D data
    '''
    data = np.zeros((args.size, args.size))
    data[int(args.size/2 - 2) : int(args.size/2 + 3), int(args.size/2 - 3) : int(args.size/2 + 3)] = 1 ##

    fig, ax = plt.subplots(1, figsize=(5, 5))
    image = plt.imshow(data, cmap=args.cmap, vmin=0, vmax=1)

    #ax.set_axis_off()
    ax.set_xticks(np.arange(-.5, args.size, 1), minor=True)
    ax.set_yticks(np.arange(-.5, args.size, 1), minor=True)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=0.2)
    ax.set_xticks([])
    ax.set_yticks([])

    #image.set_data(data)
    title = plt.title('After iteration 0', fontsize=15, va='bottom')

    return data, image, title, fig

# --------------------------------------------------------------------------------------------------------------
def init(data):
    image.set_data(data)

def animate(index, image, title, data):
    data = globals()[evolve_function_dict[args.rule]](data)  # call appropriate function to evolve the data, based on args.rule
    image.set_data(data)
    title.set_text('After iteration %d' % (index + 1))
    return image, data

# --------------------------------------------------------------------------------------------------------------
def parse_args():
    '''
    Function to parse keyword arguments
    '''

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='''Game of Life by Conway''')

    parser.add_argument('--rule', metavar='rule', type=str, action='store', default='conway', help='Which set of rules to evolve by? Default is conway')
    parser.add_argument('--niter', metavar='niter', type=int, action='store', default=10, help='How many interations to evolve for? Default is 10')
    parser.add_argument('--size', metavar='size', type=int, action='store', default=200, help='How many cells on each side to initialise with? Default is 200')
    args = parser.parse_args()

    return args

# -----main code-----------------
if __name__ == '__main__':
    args = parse_args()
    plt.close('all')
    evolve_function_dict = {'conway': 'evolve_conwayrule', 'myrule1': 'evolve_myrule1'}
    args.cmap = LinearSegmentedColormap.from_list('mycm', ['cornflowerblue', 'salmon'])

    data, image, title, fig = initialise_interactive_data(args)
    plt.show()
    print('Deb89:', data)  ##
    #sys.exit() #
    #anim = animation.FuncAnimation(fig, lambda x: animate(x, image, title, data), init_func=lambda x: init(data), frames=args.niter, interval=1)

    for index in range(args.niter):
        print('Doing', index+1, 'of', args.niter, 'iterations..')
        time.sleep(0.3)
        data = globals()[evolve_function_dict[args.rule]](data) # call appropriate function to evolve the data, based on args.rule
        print('Deb94:', data) ##

        #image.set_data(data)
        #title.set_text('After iteration %d' % (index + 1))

        #fig.canvas.flush_events()
        image = plt.imshow(data, cmap=args.cmap, vmin=0, vmax=1)
        title = plt.title('After iteration %d' % (index + 1), fontsize=15, va='bottom')

        plt.show()

    print('You have completed the Game of Life!')
