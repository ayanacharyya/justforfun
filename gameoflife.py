##!/usr/bin/env python3

"""

    Title :      gameoflife.py
    Notes :      Evolves a 2D map of cells from a user-given initial configuration, as per the rules of Game of Life (by John Conway) or similar
    Output :     Interactive, real-time evolving animation of 2D map
    Author :     Ayan Acharyya
    Started :    Mar 2022
    Example :    run gameoflife.py

"""
import numpy as np
from matplotlib import pyplot as plt
import os, sys, argparse, time, datetime, random

# -----------------------------------------------------
def evolve_conwayrule(map):
    '''
    Function to evolve an input map of cells based on the original criteria by John Conway
    '''

    return map

# -----------------------------------------------------
def evolve_myrule1(map):
    '''
    Function to evolve an input map of cells based on following criteria:

    '''

    return map

# -----------------------------------------------------
def initialise_interactive_map(args):
    '''
    Function to initialise a figure for the interactive input 2D map

    '''

    return map, ax

# -----------------------------------------------------
def update_figure(ax, map, counter, args):
    '''
    Function to update the figure given the current 2D map

    '''

    return ax

# --------------------------------------------------------------------------------------------------------------
def parse_args():
    '''
    Function to parse keyword arguments
    '''

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='''Game of Life by Conway''')

    parser.add_argument('--rule', metavar='rule', type=str, action='store', default='conway', help='Which set of rules to evolve by? Default is conway')
    parser.add_argument('--niter', metavar='niter', type=int, action='store', default=10, help='How many interations to evolve for? Default is 10')

    return args

# -----main code-----------------
if __name__ == '__main__':
    args = parse_args()
    evolve_function_dict = {'conway': 'evolve_conwayrule', 'myrule1': 'evolve_myrule1'}

    map, ax = initialise_interactive_map(args)

    for index in range(args.niter):
        map = globals()[evolve_function_dict[args.rule]](map) # call appropriate function to evolve the map, based on args.rule
        ax = update_figure(ax, map, index, args)

    print('You have completed the Game of Life!')
