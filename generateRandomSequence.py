import sys
import struct
import numpy as np



def generateRandomSequence():
    return np.random.randint(2**32 , size = 1000000)

holder = generateRandomSequence()
