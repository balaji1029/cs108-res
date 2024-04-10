'''
THEME : LISAN - AL - GAIB
—----------------------------------------------------------------------------------------
Some helpful References:
1. Array creation routines
https://numpy.org/doc/stable/reference/routines.array-creation.html
2. Logic Functions
https://numpy.org/doc/stable/reference/routines.logic.html
3. Broadcasting
https://numpy.org/doc/stable/user/basics.broadcasting.html
4. Linear Algebra
https://numpy.org/doc/stable/reference/routines.linalg.html
5. Random Generation
https://numpy.org/doc/stable/reference/random/legacy.html
—------------------------------------------------------------------------------------------------------------------------
The House of Harkonnens, the great spice miners of Arrakis faced a grave dilemma. The
extraction of the precious spice, Melange, was fraught with uncertainty. The spice blooms in
remote regions, hidden beneath the endless dunes, and its distribution was irregular and
unpredictable.
Legend has it that an old wise woman, inspired by the prophecy of the Lisan-al-Gaib, devised a
method to unveil the spice's secret locations. She believed that the spice's distribution held
patterns, invisible to the naked eye but decipherable through the whispers of data.
Her method, known as the Lisan-al-Gaib Algorithm, became a beacon of hope for the spice
miners. This algorithm takes as input the available locations where traces of spice were
found(called spice points), and finds out potential locations of spice nodes(or spice centers).
Every spice center has a cluster of spice points. Or conversely, every spice point belongs to a
cluster of a spice center. The algorithm is explained in the next page.
Fill in the TODOs of the spice.py
When done with all TODOs, to visualise the final results of clustering of spice nodes. Run the
run.py script. You can change the data_path and value of K(number of clusters) and observe the
output clustering. You are given with kmeans_1.png (data_path = 'spice_locations.txt', K = 2)
and kmeans_2.png (data_path = 'spice_locations2.txt', K = 4)
-----------------------------------------------------------------------------------
NOTE:
1. Do not change anything other than where asked for filling the TODOs.
2. You need to achieve the required output without using loops. To check no usage of loops, we
shall run a naive approach of parsing of file to search. Each additional for/while => incurs a
penalty of -2. So do not use them even within comments!Following is the Lisan-al-Gaib Algorithm.
—---------------------------------------------------------
Input:
1. Dataset containing 2D coordinates of locations where traces of spice were found,
2. K (guess of number of spice nodes)
Output: Potential locations of K spice centers/nodes
Algorithm:
1. For each of the spice point, maintain a label (0 to K-1, corresponding to the cluster of the
spice center it belongs to)
2. Initialise with a random guess for the coordinates of K spice centers, choose them to be
randomly K of the spice locations themselves.
3. Loop:
a. E Step: (Keeping the coordinates of the K spice centers fixed, update the labels)
i.
For each spice point, find the nearest spice center, and assign the spice
point to the cluster of that spice center.
ii.
To do this, for each spice point, we first compute distance(here,
euclidean) to all the spice centers and assign the label corresponding to
that spice node which has the shortest of all distances.\
b. M Step: (Keeping the labels of spice points fixed, update the coordinates of the
spice centers)
i.
The new coordinate of the i^{th} spice center is the mean of coordinates
of all spice points belonging to the cluster wiith label = i
c. Repeat Loop until the labels don’t change.
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
'''
'''
Lab 7: ADVANCED PYTHON
Activity 1 : LISAN-AL-GAIB (Dune Reference)
Author : Sabyasachi Samantaray

Here we will be dealing only with 2D data to aid visualisation

In this activity, your aim will be the following.
1) Implement the kmeans algorithm completely and correctly.
2) Implement all TODOs without using any loops
'''

### TODO 1: Importing the necessary libraries - numpy, matplotlib and time
### This TODO is already done
import time # to time the execution
import numpy as np
import matplotlib.pyplot as plt
### TODO 1

### TODO 2
### Load data from data_path
### Check the input file spice_locations.txt to understand the Data Format
### Return : np array of size Nx2
def load_data(data_path):
    return np.loadtxt(data_path, delimiter=',')

### TODO 3.1
### If init_centers is None, initialize the centers by selecting K data points at random without replacement
### Else, use the centers provided in init_centers
### Return : np array of size Kx2
def initialise_centers(data, K, init_centers=None):
    if init_centers is None:
        return data[np.random.choice(range(data.shape[0]), K, replace=False)]
    else:
        return init_centers

### TODO 3.2
### Initialize the labels to all ones to size (N,) where N is the number of data points
### Return : np array of size N
def initialise_labels(data):
    return np.zeros(data.shape[0])

def distance(a, b):
    return a**2 + b**2
    

### TODO 4.1 : E step
### For Each data point, find the distance to each center
### Return : np array of size NxK
def calculate_distances(data, centers):
    centers_x = centers[:,0]
    centers_y = centers[:,1]
    data_x = data[:,0]
    data_y = data[:,1]
    dist_x_square = (data_x[:,None]-centers_x)**2
    dist_x_square += (data_y[:,None]-centers_y)**2
    dist_x_square = np.sqrt(dist_x_square)
    return dist_x_square

### TODO 4.2 : E step
### For Each data point, assign the label of the nearest center
### Return : np array of size N
def update_labels(distances):
    return np.argmin(distances, axis=1)

### TODO 5 : M step
### Update the centers to the mean of the data points assigned to it
### Return : np array of size Kx2
def update_centers(data, labels, K):
    def find_mean(i):
        result = np.mean(data[np.where(labels==i)], axis=0)
        return result
    
    here_func = np.vectorize(find_mean, signature='()->(n)')
    return here_func(np.arange(K))

### TODO 6 : Check convergence
### Check if the labels have changed from the previous iteration
### Return : True / False
def check_termination(labels1, labels2):
    return np.array_equal(labels1, labels2)

### DON'T CHANGE ANYTHING IN THE FOLLOWING FUNCTION
def kmeans(data_path:str, K:int, init_centers):
    '''
    Input :
        data (type str): path to the file containing the data
        K (type int): number of clusters
        init_centers (type numpy.ndarray): initial centers. shape = (K, 2) or None
    Output :
        centers (type numpy.ndarray): final centers. shape = (K, 2)
        labels (type numpy.ndarray): label of each data point. shape = (N,)
        time (type float): time taken by the algorithm to converge in seconds
    N is the number of data points each of shape (2,)
    '''
    data = load_data(data_path)    
    centers = initialise_centers(data, K, init_centers)
    labels = initialise_labels(data)

    start_time = time.time() # Time stamp 

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
    plt.title('K-means clustering')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.savefig('kmeans.png')

    ### TODO 7 : In conclusion
    ### Set title as 'K-means clustering'

    ### Set xlabel as 'Longitude'

    ### Set ylabel as 'Latitude'

    ### Save the plot as 'kmeans.png'


    ## DO NOT CHANGE THE FOLLOWING LINE
    return plt

# data = load_data("spice_locations.txt")
# centers = initialise_centers(data, 3)
# labels = initialise_labels(data)
# result = calculate_distances(data, centers)
# labels = update_labels(result)
# new_centers = update_centers(data, labels, 3)
# print(result)
