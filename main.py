import numpy as np


def theta(state):
    pass


def sha3(input_bits):
    state = np.empty(3)
    for i in range(0,4):
        for j in range(0, 4):
            for k in range(0, 63):
                state[i][j][k] = input_bits[64*(5*j + i) + k]
    
