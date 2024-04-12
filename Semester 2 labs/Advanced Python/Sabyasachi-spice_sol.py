'''
Lab 7: ADVANCED PYTHON
Activity 1 : LISAN-AL-GAIB (Dune Reference)

Please ensure that you understand the algorithm for this activity before you start coding.

In this activity, your aim will be the following.
1) Implement the kmeans algorithm completely and correctly.
2) Implement all TODOs without using any loops
TA: Sabyasachi Samantaray
'''

### TODO 1: Importing the necessary libraries - numpy, matplotlib and time
### This TODO is already done for you
import time # for timing the execution
import numpy as np
import matplotlib.pyplot as plt
### TODO 1

### TODO 2a : Load data from data_path and store it in variable data
### Check the input file spice_locations.txt to understand the data format
def load_data(data_path):
    return np.loadtxt(data_path, delimiter=',')

### TODO 3.1 : Initialize the centers and labels
### If init_centers is None, initialize the centers by selecting K data points at random without replacement
### Else, use the centers provided in init_centers
def initialise_centers(data, K, init_centers=None):
    if init_centers is not None:
        centers = init_centers
    else:
        centers = data[np.random.choice(len(data), K, replace=False)]
    return centers

### TODO 3.2 : Initialize the labels to size (N,) where N is the number of data points
def initialise_labels(data):
    return np.zeros(len(data), dtype=int)

### TODO 4.1 : E step
### For each data point, find the distance to each center
def calculate_distances(data, centers):
    return np.linalg.norm(data[:, np.newaxis] - centers, axis=2)

### TODO 4.2 : E step
### For each data point, assign the label of the nearest center
def update_labels(distances):
    return np.argmin(distances, axis=1)

### TODO 5 : M step
### Update the centers to the mean of the data points assigned to it
def update_centers(data, labels, K):
    labels_one_hot = np.zeros((len(data), K))
    labels_one_hot[np.arange(len(data)), labels] = 1
    centers = np.dot(labels_one_hot.T, data)/np.sum(labels_one_hot, axis=0).reshape(K,1)
    return centers

### TODO 6 : Check for convergence
def check_termination(labels1, labels2):
    return np.all(labels1 == labels2)

### DON'T CHANGE ANYTHING IN THE FOLLOWING FUNCTION
def kmeans(data_path:str, K:int, init_centers):
    '''
    Input :
        data (type str): path to the file containing the data
        K (type int): number of clusters
        init_centers (type numpy.ndarray): initial centers. shape = (K, 2) or None
    Output :
        centers (type numpy.ndarray): final centers. shape = (K, 2)
        labels (type numpy.ndarray): labels for each data point. shape = (N,)
        time (type float): time taken for the algorithm to converge in seconds
    N is the number of data points each of shape (2,)
    '''
    data = load_data(data_path)    
    centers = initialise_centers(data, K, init_centers)
    labels = initialise_labels(data)

    start_time = time.time() # Time stamp before the algorithm starts

    while True:
        distances = calculate_distances(data, centers)
        labels_new = update_labels(distances)
        centers = update_centers(data, labels_new, K)
        if check_termination(labels, labels_new): break
        else: labels = labels_new
 
    end_time = time.time() # Time stamp after the algorithm ends
    return centers, labels, end_time - start_time 

### FILL THE LINES BELOW THE TODO COMMENTS
def visualise(data_path, labels, centers):
    data = load_data(data_path)

    # Scatter plot of the data points
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

    ### TODO 8 : In conclusion
    ### Set title as 'K-means clustering'
    plt.title('K-means clustering')
    ### Set xlabel as 'Longitude'
    plt.xlabel('Longitude')
    ### Set ylabel as 'Latitude'
    plt.ylabel('Latitude')
    ### Save the plot as 'kmeans.png'
    plt.savefig('kmeans.png')
    ### TODO 8

    return plt

if __name__ == '__main__':
    data_path = 'spice_locations2.txt'
    K, init_centers = 4, None
    centers, labels, time_taken = kmeans(data_path, K, init_centers)
    print('Time taken for the algorithm to converge:', time_taken)
    visualise(data_path, labels, centers)