import numpy as np
import matplotlib.pyplot as plt

def toss(number_trials):
    return np.sum(np.random.randint(0, 2, (number_trials, 100)), axis=1)

def plot_hist(outcomes, index):
    plt.subplot(2, 2, index)
    plt.hist(outcomes, bins=100, color='c')
    plt.xlabel('Number of Heads')
    plt.ylabel('Frequency')
    plt.title(f'n = {outcomes.shape[0]}')
    plt.tight_layout()
    plt.savefig('exer_3.png')

if __name__ == '__main__':
    list_trials = np.array([10, 100, 1000, 10000])
    for i in range(list_trials.shape[0]):
        plot_hist(toss(list_trials[i]), i+1)
