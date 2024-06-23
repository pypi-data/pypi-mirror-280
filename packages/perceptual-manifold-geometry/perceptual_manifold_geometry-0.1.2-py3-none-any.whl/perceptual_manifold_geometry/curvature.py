import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.linalg import svd

def quantify_overall_concavity(data, k=20):

    nn = NearestNeighbors(n_neighbors=k + 1)
    nn.fit(data)
    distances, indices = nn.kneighbors(data)
    

    local_curvatures = []
    for i, point_neighbors in enumerate(indices):
        neighbor_points = data[point_neighbors]

        local_cov_matrix = np.cov(neighbor_points[:, 1:].T)

        eigenvalues = np.linalg.eigvals(local_cov_matrix)

        curvature = np.mean(eigenvalues)
        local_curvatures.append(curvature)
        overall_concavity = np.mean(local_curvatures)
    
    return overall_concavity

