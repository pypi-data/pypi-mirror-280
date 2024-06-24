import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.linalg import svd
from sklearn.decomposition import PCA

def quantify_overall_concavity(data, k=20):
    # 使用 k 近邻方法计算每个点的局部邻域
    nn = NearestNeighbors(n_neighbors=k + 1)
    nn.fit(data)
    distances, indices = nn.kneighbors(data)
    
    # 计算局部曲率
    local_curvatures = []
    for i, point_neighbors in enumerate(indices):
        neighbor_points = data[point_neighbors]
        # 计算局部协方差矩阵
        local_cov_matrix = np.cov(neighbor_points[:, 1:].T)
        # 计算特征值
        eigenvalues = np.linalg.eigvals(local_cov_matrix)
        # 计算曲率
        curvature = np.mean(eigenvalues)
        local_curvatures.append(curvature)
    overall_concavity = np.mean(local_curvatures)
    
    return overall_concavity



def compute_hessian(coords):
    n = coords.shape[1]
    G = np.dot(coords.T, coords)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                H[i, j] = np.mean((G[:, i] - np.mean(G[:, i])) ** 2)
            else:
                H[i, j] = np.mean((G[:, i] - np.mean(G[:, i])) * (G[:, j] - np.mean(G[:, j])))
    return H

def estimate_curvatures(data, k=15, pca_components=8, curvature_type='both'):
    """
    Estimate Gaussian and mean curvature for high-dimensional data.

    Parameters:
    data (numpy array): The data points, shape (n_samples, n_features)
    k (int): Number of nearest neighbors for local neighborhood (default: 10)
    pca_components (int): Number of components for PCA (default: 3)
    curvature_type (str): Type of curvature to estimate ('gaussian', 'mean', or 'both')

    Returns:
    tuple: Mean Gaussian curvature and mean mean curvature if curvature_type is 'both',
           otherwise returns the respective curvature
    """
    
    nn = NearestNeighbors(n_neighbors=k + 1)
    nn.fit(data)
    distances, indices = nn.kneighbors(data)
    
    gaussian_curvatures = []
    mean_curvatures = []
    
    for i, point_neighbors in enumerate(indices):
        point = data[i]
        neighbors = data[point_neighbors[1:]]  # Exclude the point itself
        
        pca = PCA(n_components=min(pca_components, data.shape[1]))  # Reduce to specified dimensions
        pca.fit(neighbors - point)
        coords = pca.transform(neighbors - point)
        
        H = compute_hessian(coords)
        eigenvalues = np.linalg.eigvals(H)
        
        if len(eigenvalues) >= 2:
            k1, k2 = eigenvalues[:2]
            gaussian_curvature = k1 * k2  # Gaussian curvature is the product of the principal curvatures
            mean_curvature = (k1 + k2) / 2  # Mean curvature is the average of the principal curvatures
            
            gaussian_curvatures.append(gaussian_curvature)
            mean_curvatures.append(mean_curvature)
    
    if curvature_type == 'gaussian':
        return np.mean(gaussian_curvatures)
    elif curvature_type == 'mean':
        return np.mean(np.abs(mean_curvatures))
    elif curvature_type == 'both':
        return np.mean(gaussian_curvatures), np.mean(np.abs(mean_curvatures))
    else:
        raise ValueError("Invalid curvature_type. Choose 'gaussian', 'mean', or 'both'.")



def curvatures(data, k=15, pca_components=8, curvature_type='PCA'):
    if curvature_type == 'PCA':
        return quantify_overall_concavity(data, k=20)
    elif curvatures == 'gaussian':
        return estimate_curvatures(data, pca_components, curvature_type='gaussian')
    else:
        return estimate_curvatures(data, pca_components, curvature_type='mean')

