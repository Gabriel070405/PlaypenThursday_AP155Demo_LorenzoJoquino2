import numpy as np
import matplotlib.pyplot as plt
import sys


def createZerosArray(rowZeros, columnZeros):
    return np.zeros((rowZeros, columnZeros))

def sumOf1ToN(n):
    return sum(np.arange(n+1))


if __name__ == "__main__":
    name = sys.argv[1]
    number = int(sys.argv[2])
    print(f"Hello {name}")
    print(sumOf1ToN(number))
    print(sys.argv[0])