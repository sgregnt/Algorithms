import sys
sys.path.append("/home/greg/.PyCharm2019.1/config/scratches/")
from scratch_3 import fftIndgen, gaussian_random_field, \
    gen_perturbations, perturb_mesh, get_trinagle_coordinates, get_tiangl_specs, \
    compute_energy, total_energy, energy_from_vertices, get_3_ring, get_triangles, plot_mesh, draw_change, check_angles, \
    plot_triangle_reshaped

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import copy
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as LA
import math
import matplotlib.pyplot as plt
import networkx as nx
from random import sample
import pickle

# file = '/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/dataset_500.pkl'
file = '/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/dataset_50.pkl'

with open(file, 'rb') as f:
    dataset = pickle.load(f)


import h5py

# h5file = "/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/experiments/train_graph_data.h5"
h5file = "/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/experiments/test_graph_data.h5"
# f = h5py.File("/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/experiments/ply_data_test1.h5")
print("here")

# first index should be the number of elements and the second row is the points

labels = [item[1] for item in dataset]
points = [item[0] for item in dataset]
points = [np.transpose(np.array(point)) for point in points]

n = points[0].shape[0]
q = np.zeros(shape = (50, n, 3))
for i, p in enumerate(points):
    q[i,:,:] = p

labels = np.array(labels)
labels.shape = (labels.shape[0], 1)
train_data_dic = {'data' : q, 'label' : labels}

with h5py.File(h5file, 'w') as f:
    dset = f.create_dataset("data", data=q)
    dset = f.create_dataset("label", data=labels)

f = h5py.File("/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/experiments/train_graph_data.h5")
data = f['data'][:]
label = f['label'][:]

print(f['data'].shape)
print("stop here")