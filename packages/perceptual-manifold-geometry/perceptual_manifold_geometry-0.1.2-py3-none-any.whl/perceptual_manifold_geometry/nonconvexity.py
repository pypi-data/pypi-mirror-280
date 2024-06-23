import numpy as np
from scipy.spatial import ConvexHull
from sklearn.random_projection import GaussianRandomProjection


def approximate_convex_hull_volume(X, n_projections=10, n_components=3):
    """
    Approximate the convex hull volume of high-dimensional data using random projections.
    
    Args:
    X (numpy array): Data points on the manifold, shape (n_samples, n_features)
    n_projections (int): Number of random projections to use
    n_components (int): Number of dimensions to reduce to in each projection
    
    Returns:
    approx_hull_volumes (list): List of approximate convex hull volumes for each projection
    """
    n_samples, n_features = X.shape
    approx_hull_volumes = []
    
    for _ in range(n_projections):
        # Apply random projection
        projector = GaussianRandomProjection(n_components=n_components)
        X_projected = projector.fit_transform(X)
        
        # Compute convex hull in the reduced space
        hull = ConvexHull(X_projected)
        hull_volume = hull.volume
        approx_hull_volumes.append(hull_volume)
    
    return approx_hull_volumes


def calculate_volume(Z, d=1.0):
    Z_mean = np.mean(Z, axis=0)
    # Calculate (Z - Z_mean)
    diff = Z - Z_mean

    # Calculate (Z - Z_mean)(Z - Z_mean)^T
    outer_product = np.dot(diff.T, diff)

    # Calculate \frac{d}{m}(Z - Z_mean)(Z - Z_mean)^T
    scaled_outer_product = (d / Z.shape[0]) * outer_product

    # Calculate I + \frac{d}{m}(Z - Z_mean)(Z - Z_mean)^T
    matrix_sum = np.eye(Z.shape[1]) + scaled_outer_product

    # Calculate \frac{1}{2} \log_2(I + \frac{d}{m}(Z - Z_mean)(Z - Z_mean)^T)
    volume = 0.5 * np.log2(np.linalg.det(matrix_sum))
    density = volume/len(Z)

    return volume, density


def estimate_nonconvexity(X, n_projections=10, n_components=5, alpha = 10000):
    """
    Estimate the nonconvexity of high-dimensional data manifold using random projections.
    
    Args:
    X (numpy array): Data points on the manifold, shape (n_samples, n_features)
    n_projections (int): Number of random projections to use
    n_components (int): Number of dimensions to reduce to in each projection
    
    Returns:
    nonconvexity (float): Nonconvexity measure based on convex hull approximations
    """
    # Compute original data bounding box volume
    data_bounding_volume, density = calculate_volume(X)
    print(f"Data bounding volume: {data_bounding_volume}")
    
    # Approximate convex hull volumes using random projections
    approx_hull_volumes = approximate_convex_hull_volume(X, n_projections, n_components)
    
    print(f"Approximate hull volumes: {approx_hull_volumes}")
    
    # Estimate nonconvexity
    mean_approx_hull_volume = np.mean(approx_hull_volumes)
    nonconvexity = (mean_approx_hull_volume - data_bounding_volume*alpha) / mean_approx_hull_volume
    
    return nonconvexity



