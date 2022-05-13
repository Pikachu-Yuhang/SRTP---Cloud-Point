from splay import SplayTree
import numpy as np
from sklearn.decomposition import PCA

# Some constants
multiplier = 100    # multiplier is to magnify the value of points
divide = 200        # divide the size of bounding box
threshold = 0       # threshold of resterization

splaytree: SplayTree = SplayTree()

# Input and process the points
# original points
origin_point_set = \
    [[1.08948, 0.0324, 0.00000], \
    [1, 0, 0], \
    [1.0895, 0.032411, 0.00001], \
    [0.4728, 0.983362, 0.29372], \
    [0.0089372, 0.836, 0.47392], \
    [1.18222, 0.322, 0.0], \
    [0.0244, 0.0032, 0.0007]]   
mag_point_set = []          # points after magnifying
rasterized_point_set = []   # points after rasterization
for point in origin_point_set:
    mag_point_set.append([int(i * multiplier) for i in point])

# Insert the points into the splay tree
for mag_point in mag_point_set:
    splaytree.insert(mag_point)

# Size of bounding box
a = 1.0
b = 1.0
c = 1.0

# Decide which voxels to be rasterized
splaytree.traverse(splaytree.root, threshold, rasterized_point_set)

splaytree.inorder(splaytree.root)
print(rasterized_point_set)

# Using PCA to reduce dimension
point_data = np.array(rasterized_point_set)
pca = PCA(n_components = 'mle', copy = False)
point_data = pca.fit_transform(point_data)
print(point_data)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)