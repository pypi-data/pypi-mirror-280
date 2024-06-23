import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt


def estimate_holes_ripser(X, threshold = 0.1, Persistence_diagrams = False):
    """
    Estimate holes in data manifold X using persistent homology with ripser.
    
    Args:
    X (numpy array): Data points on the manifold, shape (n_samples, n_features)
    The persistence threshold defaults to 0.1
    
    Returns:
    diagrams (list): Persistence diagrams for each dimension
    """
    # Compute persistent homology
    result = ripser(X)
    diagrams = result['dgms']

    persistence = diagrams[1]
    persistence = persistence[persistence[:, 1] - persistence[:, 0] > threshold]
    print("Number of holes is:", persistence.shape[0])

    total_size = np.sum(persistence[:,1]-persistence[:,0])
    mean_size = np.mean(persistence[:,1]-persistence[:,0])
    density_holes = total_size/np.max(persistence[:,1])-np.min(persistence[:,0])
    
    if Persistence_diagrams == True:
        plt.figure(figsize=(8, 6), dpi=700)
        plt.scatter(persistence[:, 0], persistence[:, 1], c=persistence[:, 1] - persistence[:, 0], cmap='cool', s=100)
        plt.colorbar(label='Persistence')
        plt.plot([0, persistence[:, 1].max()], [0, persistence[:, 1].max()], 'k--')
        plt.xlabel('Birth')
        plt.ylabel('Death')
        plt.title('Persistence Diagram')
        plt.axis('equal')
        plt.show()
    
    
    return persistence.shape[0], total_size, mean_size, density_holes


