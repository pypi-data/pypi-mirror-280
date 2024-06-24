import numpy as np
from skdim.id import TLE



def estimate_intrinsic_dimension(X, method='TLE'):
    if method == 'Covariance':
        intrinsic_dim = (np.trace(np.dot(X.T, X)))**2/np.trace(np.dot(X.T, X)**2)
    else:
        dim_estimator = TLE()
        intrinsic_dim = dim_estimator.fit(X).dimension_
    print("Intrinsic Dimensions:", intrinsic_dim)
    
    return intrinsic_dim
