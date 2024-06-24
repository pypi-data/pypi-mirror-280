import numpy as np


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