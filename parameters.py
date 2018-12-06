'''
Parameters of the simulation
'''

import numpy as np

def set_parameters():
    '''
    Parameters
    ----------

    S: int
        Number of servers
    U: int
        Number of users
    e1: float
        Error for user offloading convergence
    e2: float
        Error for server pricing convergence
    k: int
        parameter of the user's satisfaction function
    l: int
        parameter of the user's satisfaction function
    a: 1-D array
        parameter that reflects users' dynamic behavior to spen more money
        in order to buy computing support from the MEC servers
    b_min: int
        Minimum number of bits that the user is willing to offload
        Same for all users
    b_max: int
        Maximum number of bits that the user is willing to offload
        Same for all users
    c: 1-D array
        parameter that shows the server's computing cost
    fs: 1-D array
        parameter that shows the server's discount
    price_min: int
        Minimum vlaue that the server can set his price
    learning_rate: float
        parameter indicating the learning rate of the server selection learning
        mechanism
    '''

    S = 5
    U = 100
    e1 = 1e-02
    e2 = 1e-02

    k = 100
    l = 1000

    # User parameters
    a = 2.7*1e3 + np.random.random(U)*1e3
    b_min = 0
    b_max = 1000

    # Server parameters
    c = 0.2 + np.random.random(S)*0.1
    fs = 0.025 + np.random.random(S)*0.005
    price_min = 1e-1*5

    learning_rate = 0.7

    return locals()
