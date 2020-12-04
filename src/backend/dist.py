import numpy as np

def gamma_dist(gamma_shape, gamma_scale, size):
    np.random.gamma(gamma_shape, gamma_scale, size)

def normal_dist(normal_center, normal_std, size):
    np.random.normal(normal_center, normal_std, size)

