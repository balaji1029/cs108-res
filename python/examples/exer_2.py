import numpy as np

def distance(arr):
    diff = arr.reshape(arr.shape[0], 1, arr.shape[1]) - arr
    dist = np.sqrt(np.sum(diff**2, axis=2))
    return dist

if __name__ == '__main__':
    arr = np.random.randint(0, 5, size=(5, 2))
    print(arr)
    print(distance(arr))