import network as nx
from Functions.global_properties import *
from Functions.local_properties import *
from Functions.bool_functions import *
from test_graphs import *

def cost(G, e):
    retrun G[e[0][e[1]]]['weight']