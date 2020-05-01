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

# ----------------------
# generate mesh
# ----------------------

mesh_size = 20
alpha = -6

# vanilla mesh
xv, yv = np.meshgrid(range(mesh_size), range(mesh_size), sparse=False, indexing='ij')

scale = 5
xv = xv/scale
yv = yv/scale
zv = 0 * xv # original mesh is in the plain

mesh = (xv, yv, zv)

dataset = []

for i in range(50):

    # ----------------------
    # generate two perturbation of the mesh, first is the original mesh and second is the target mesh
    # we want to compute Direchlet energy of moving from original to target mesh
    # ----------------------

    # first perturbation for original mesh
    tmp_out_x, tmp_out_y, tmp_out_z =  gen_perturbations(mesh_size, alpha, verbous=False)
    perturbation_original = (tmp_out_x, tmp_out_y, tmp_out_z)

    # first perturbation for target mesh
    tmp_out_x, tmp_out_y, tmp_out_z =  gen_perturbations(mesh_size, alpha, verbous=False)
    perturbation_target = (tmp_out_x, tmp_out_y, tmp_out_z)

    original_mesh = perturb_mesh(mesh, perturbation_original)
    target_mesh = perturb_mesh(mesh, perturbation_target)

    # ----------------------
    # generate two perturbation of the mesh, first is the original mesh and second is the target mesh
    # we want to compute Direchlet energy of moving from original to target mesh
    # ----------------------

    # x coordinate in index 0 of original_mesh, y is in index 1 and so on...
    tri_original = matplotlib.tri.Triangulation(original_mesh[0].reshape(-1), original_mesh[1].reshape(-1))
    tri_target = copy.deepcopy(tri_original)

    tri_target.x = target_mesh[0].reshape(-1)
    tri_target.y = target_mesh[1].reshape(-1)

    plot_mesh(tri_original, original_mesh[2].reshape(-1), verbous=False)

    # ----------------------
    # compute change (translation) of vertice between target and original location
    # ----------------------

    x_change = target_mesh[0] - original_mesh[0]
    y_change = target_mesh[1] - original_mesh[1]
    z_change = target_mesh[2] - original_mesh[2]

    draw_change(original_mesh[0], original_mesh[1], original_mesh[2], x_change, y_change, z_change, verbous=False)


    #----------------------------------------
    # extract triangle parameters for energy evaluation
    #----------------------------------------

    x_o = original_mesh[0].reshape(-1)
    y_o = original_mesh[1].reshape(-1)
    z_o = original_mesh[2].reshape(-1)

    x_t = target_mesh[0].reshape(-1)
    y_t = target_mesh[1].reshape(-1)
    z_t = target_mesh[2].reshape(-1)

    # for each triangle retrieve vertices, each vertex is 3-vector (and each triangle has 3 such vertices)
    original_triangles_reshaped = get_trinagle_coordinates(tri_original.triangles, x_o, y_o, z_o) # this is #t-by-3-by-3
    target_triangles_reshaped = get_trinagle_coordinates(tri_target.triangles, x_t, y_t, z_t)


    plot_triangle_reshaped(original_triangles_reshaped, verbous=True)
    plot_triangle_reshaped(target_triangles_reshaped, verbous=True)


    # extract tringle properties, cotangent, sides length and angles.
    original_specs = get_tiangl_specs(original_triangles_reshaped)
    target_specs = get_tiangl_specs(target_triangles_reshaped)

    # run some checks on the angles
    # NOTE: somehow there are many bad triangles (with angle above 90 degrees), but let's only look at the triangles
    # used for training

    # check_angles(original_specs)
    # check_angles(target_specs)

    #----------------------------------------
    # get k-ring
    #----------------------------------------

    G = nx.Graph()
    G.add_edges_from(tri_original.edges)

    element = 250


    ring = get_3_ring(G, element)
    # sample_size = int(len(ring)/2)
    sample_size = 18
    random_subsample = sample(set(ring), sample_size)

    # get the triangles entirely contained in the ring
    original_ring_triangles = get_triangles(ring, G)

    original_ring_triangles_reshaped = get_trinagle_coordinates(original_ring_triangles, x_o, y_o, z_o)
    target_ring_triangles_reshaped = get_trinagle_coordinates(original_ring_triangles, x_t, y_t, z_t)


    check_angles(get_tiangl_specs(original_ring_triangles_reshaped))
    check_angles(get_tiangl_specs(target_ring_triangles_reshaped))


    # for the subset ring we cannot extract the triangles (the triangles are broken since some of the points
    # are missing in the subsample) instead we buld a new mesh on the subsampled vertices. This is the simplest baseline
    # against which we compate neural network performance.
    #
    # contruct mesh on the subsample

    x_o_sub = [x_o[i] for i in random_subsample]
    y_o_sub = [y_o[i] for i in random_subsample]
    z_o_sub = [z_o[i] for i in random_subsample]

    # Create the Triangulation; no triangles so Delaunay triangulation created.
    triang = matplotlib.tri.Triangulation(x_o_sub, y_o_sub)

    x_t_sub = [x_t[i] for i in random_subsample]
    y_t_sub = [y_t[i] for i in random_subsample]
    z_t_sub = [z_t[i] for i in random_subsample]

    verbous = True
    if verbous:

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(tri_original, original_mesh[2].reshape(-1), label='parametric curve', alpha=0.5)


        ax.scatter(x_o[element], y_o[element], z_o[element], c='r', s=50)

        for elem in ring:
            ax.scatter(x_o[elem], y_o[elem], z_o[elem], c='g', s=15)

        for elem in random_subsample:
            ax.scatter(x_o[elem], y_o[elem], z_o[elem], c='k', s=10)

        ax.plot_trisurf(triang, z_o_sub)

        plt.show()

    print(total_energy(original_specs, target_specs))

    print("total energy", energy_from_vertices(original_mesh, target_mesh, verbous=True))


    print("ring number of triangles", len(original_ring_triangles), "ring size", len(ring))

    energy = energy_from_vertices(original_mesh, target_mesh, triangles=original_ring_triangles, verbous=True)
    print("energy of ring", energy)


    # subsampled triangles
    #
    G = nx.Graph()
    G.add_edges_from(triang.edges)
    original_ring_subsampled_triangles = get_triangles(G.nodes, G)

    original_ring_subsampled_triangles_reshaped = get_trinagle_coordinates(original_ring_subsampled_triangles, x_o_sub, y_o_sub, z_o_sub)
    target_ring_subsampled_triangles_reshaped = get_trinagle_coordinates(original_ring_subsampled_triangles, x_t_sub, y_t_sub, z_t_sub)

    original_ring_subsampled_specs = get_tiangl_specs(original_ring_subsampled_triangles_reshaped)
    target_sring_subsampled_specs = get_tiangl_specs(target_ring_subsampled_triangles_reshaped)

    print("subsampled ring number of triangles", len(triang.triangles), "subsample ring size", len(random_subsample))
    print("subsampledd ring energy (note, to compare one presumably need to adjust for area change)", total_energy(original_ring_subsampled_specs, target_sring_subsampled_specs))

    verbous = True
    if verbous:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(x_o_sub, y_o_sub, z_o_sub, c='g', s=5)
        ax.scatter(x_t_sub, y_t_sub, z_t_sub, c='b', s=15)
        plt.show()

    x_diff = np.array(x_t_sub) - np.array(x_o_sub)
    y_diff = np.array(y_t_sub) - np.array(y_o_sub)
    z_diff = np.array(z_t_sub) - np.array(z_o_sub)
    dataset.append([(x_diff, y_diff, z_diff), energy])


file = '/home/greg/pointnet/pointnet_graph_training/pointnet/graph_dataset/dataset.pkl'
def store_dataset(dataset, file):
    with open(file, 'wb') as f:
        pickle.dump(dataset, f)

store_dataset(dataset, file)
print("done" * 100)