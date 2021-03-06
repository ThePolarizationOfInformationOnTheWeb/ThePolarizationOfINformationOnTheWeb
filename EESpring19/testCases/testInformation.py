import numpy as np
from EESpring19.Information import *
#passed tests, log changed to base 2
print('Creating Test Distributions')
dist1 = np.array([0.5,0.25,0.125,0.125])
dist2 = np.array([0.25, 0.25, 0.25, 0.25])
print(dist1)
print(dist2)
print('Calculating Entropy of dist1')
distEnt = entropy(dist1)
print(distEnt)
print('Calculating KL Divergence of Distributions')
kl = kl_divergence(dist1, dist2)
print(kl)
kl2 = kl_divergence(dist2, dist1)
print('reverse entry')
print(kl2)
print('Creating Sample Joint Distribution')
joint = np.array([[0.125,0.0625,0.03125,0.03125],[0.0625, 0.125,0.03125,0.03125],[0.0625,0.0625,0.0625,0.0625],[0.25,0,0,0]])
#joint = np.matmul(np.matrix(dist1).T, np.matrix(dist2))#joint for when vars are independent of each other
print(joint)
print('Calculating Mutual Information')
mutual = mutual_information(joint)
print(mutual)