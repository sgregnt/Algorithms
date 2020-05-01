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
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#----------------------------------------
# generate random mesh deformations
#----------------------------------------

def fftIndgen(n):
    a = list(range(0, int(n/2)+1))
    b = list(range(1, int(n/2)))
    b.reverse()
    b = [-i for i in b]
    return a + b


def gaussian_random_field(Pk = lambda k : k**-2.0, size = 100):
    def Pk2(kx, ky):
        if kx == 0 and ky == 0:
            return 0.0
        return np.sqrt(Pk(np.sqrt(kx**2 + ky**2)))
    noise = np.fft.fft2(np.random.normal(size = (size, size)))
    amplitude = np.zeros((size,size))
    for i, kx in enumerate(fftIndgen(size)):
        for j, ky in enumerate(fftIndgen(size)):
            amplitude[i, j] = Pk2(kx, ky)
    return np.fft.ifft2(noise * amplitude)


def gen_perturbations(mesh_size, alpha, verbous=False):
    # generate random gaussian field

    out_x = gaussian_random_field(Pk = lambda k: k**alpha, size=mesh_size)
    out_y = gaussian_random_field(Pk = lambda k: k**alpha, size=mesh_size)
    out_z = gaussian_random_field(Pk = lambda k: k**alpha, size=mesh_size)


    if verbous:
        plt.figure()
        plt.imshow(out_x.real, interpolation='none')
        plt.figure()
        plt.imshow(out_y.real, interpolation='none')
        plt.figure()
        plt.imshow(out_z.real, interpolation='none')
        plt.show()

    return (out_x.real, out_y.real, out_z.real)

def perturb_mesh(mesh, perturbation):
    # add perturbation to the given mesh

    perturbed_mesh_x = mesh[0] + perturbation[0]
    perturbed_mesh_y = mesh[1] + perturbation[1]
    perturbed_mesh_z = mesh[2] + perturbation[2]

    return (perturbed_mesh_x, perturbed_mesh_y, perturbed_mesh_z)


#---------------------------------------------------------------------
# compute Dirichlet energy of the change from original to target mesh
#---------------------------------------------------------------------

def get_trinagle_coordinates(triangles, x, y, z):
    """convert triangles to actual coordinates
    the triangle is the indixes of the points that form the triangle
    """

    # [item for sublist in two_ring for item in sublist]
    # tri_cor = np.array([(x[i], y[i], z[i]) for triangle in triangles for i in triangle])


    tri_cor_reshape = np.array([((x[triangle[0]], y[triangle[0]], z[triangle[0]]),
                                 (x[triangle[1]], y[triangle[1]], z[triangle[1]]),
                                 (x[triangle[2]], y[triangle[2]], z[triangle[2]])) for triangle in triangles])
    # return tri_cor,tri_cor_reshape
    return tri_cor_reshape


def get_tiangl_specs(triangles_reshaped):
    """extract different parameters of the triangles to be used for calculations"""

    specs = []

    #        a1
    #    0--------1
    #     \      /
    #  a2  \    /  a3
    #       \  /
    #        2
    #

    for i, t in enumerate(triangles_reshaped):

        a1 = LA.norm(t[0]- t[1])
        a2 = LA.norm(t[0]- t[2])
        a3 = LA.norm(t[1]- t[2])



        alpha1 =  math.acos(np.abs(np.inner(t[1]-t[0], t[2] - t[0]))/ (a1 * a2))
        alpha1 =  math.acos((np.inner(t[1]-t[0], t[2] - t[0]))/ (a1 * a2))
        alpha1 =  math.acos(-(a3 ** 2 - a1 ** 2 - a2 ** 2)/(2.0* a1 * a2))



        alpha2 =  math.acos(np.abs(np.inner(t[2]-t[1], t[0] - t[1]))/ (a1 * a3))
        alpha2 =  math.acos((np.inner(t[2]-t[1], t[0] - t[1]))/ (a1 * a3))
        alpha2 =  math.acos(-(a2 ** 2 - a1 ** 2 - a3 ** 2)/(2.0* a1 * a3))


        alpha3 =  math.acos(np.abs(np.inner(t[1]-t[2], t[0] - t[2]))/ (a2 * a3))
        alpha3 =  math.acos((np.inner(t[1]-t[2], t[0] - t[2]))/ (a2 * a3))
        alpha3 = math.acos(-(a1 ** 2 - a2 ** 2 - a3 ** 2) / (2.0 * a2 * a3))

        cot1 = math.cos(alpha1)/math.sin(alpha1)
        # cot1 = np.abs(math.cos(alpha1)/math.sin(alpha1))
        cot2 = math.cos(alpha2)/math.sin(alpha2)
        # cot2 = np.abs(math.cos(alpha2)/math.sin(alpha2))
        cot3 = math.cos(alpha3)/math.sin(alpha3)
        # cot3 = np.abs(math.cos(alpha3)/math.sin(alpha3))

        specs.append([(a1, a2, a3), (alpha1, alpha2, alpha3), (cot1, cot2, cot3)])

    return specs

def compute_energy(cots_original, sides_target):
    """compute Dirichlet energy of the deformation of a single triangle"""

    cot1, cot2, cot3 = cots_original
    a1, a2, a3 =  sides_target
    s = 0.25

    return (s * (a1**2) * cot3  + s * (a2 ** 2) * cot2 + s * (a3 ** 2) * cot1)

def total_energy(original_triangles_specs, target_triangles_specs):
    """compute Dirichlet energy of the deformation of the whole mesh (expected to be a k-ring of a sort)"""

    energy = 0
    for i in range(len(original_triangles_specs)):
        energy +=  compute_energy(original_triangles_specs[i][2], target_triangles_specs[i][0])

    return energy

def energy_from_vertices(original_mesh, target_mesh, triangles = None, verbous=True):
    """Given original mesh and target mesh computes the Dirichlet energy of the function maping from
       original to target mesh

       each of the two meshes should be given in the form of tuple with 3 elements the first containing array of x
       cooridnates the second has y coordinates and the last has z cooridnates.

       triangulation will be constructed on the original mesh and used for the target mesh as well.
    """

    if triangles:
        tri_original = matplotlib.tri.Triangulation(original_mesh[0].reshape(-1), original_mesh[1].reshape(-1), triangles= triangles)
        tri_target = copy.deepcopy(tri_original)
    else:
        tri_original = matplotlib.tri.Triangulation(original_mesh[0].reshape(-1), original_mesh[1].reshape(-1))
        tri_target = copy.deepcopy(tri_original)

    tri_target.x = target_mesh[0].reshape(-1)
    tri_target.y = target_mesh[1].reshape(-1)

    if verbous:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(tri_original, original_mesh[2].reshape(-1), label='parametric curve', alpha=1)
        plt.show()

    # need to make it easier to work not on a grid
    #
    x_change = target_mesh[0] - original_mesh[0]
    y_change = target_mesh[1] - original_mesh[1]
    z_change = target_mesh[2] - original_mesh[2]


    if verbous:
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make the grid
        x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                              np.arange(-0.8, 1, 0.2),
                              np.arange(-0.8, 1, 0.8))

        ax.quiver(original_mesh[0], original_mesh[1], original_mesh[2], x_change, y_change, z_change, length=0.1, normalize=True)

        plt.show()

    x_o = original_mesh[0].reshape(-1)
    y_o = original_mesh[1].reshape(-1)
    z_o = original_mesh[2].reshape(-1)

    x_t = target_mesh[0].reshape(-1)
    y_t = target_mesh[1].reshape(-1)
    z_t = target_mesh[2].reshape(-1)

    original_triangles_reshaped = get_trinagle_coordinates(tri_original.triangles, x_o, y_o, z_o)
    target_triangles_reshaped = get_trinagle_coordinates(tri_target.triangles, x_t, y_t, z_t)

    original_specs = get_tiangl_specs(original_triangles_reshaped)
    target_specs = get_tiangl_specs(target_triangles_reshaped)

    return total_energy(original_specs, target_specs)


def get_3_ring(G, element):

    original_elem  = element
    one_ring = list(G.neighbors(element))

    two_ring = []
    for elem in one_ring:
          two_ring.append(list(G.neighbors(elem)))

    two_ring = [item for sublist in two_ring for item in sublist]
    three_ring = []
    for elem in two_ring:
          three_ring.append(list(G.neighbors(elem)))

    three_ring = [item for sublist in three_ring for item in sublist]
    all_elems =  [original_elem] + one_ring + two_ring + three_ring
    return np.unique(all_elems)


def get_triangles(ring, G):
    """Given the set of vertices return triangle entirely contained within the set"""

    cliques = nx.cliques_containing_node(G, list(ring))
    ring_set = set(ring)
    triangles = []
    triangles_sets = []
    # this finds same clique 3 times

    for key in cliques.keys():

        # all cliques where virtex "key" is present
        for triangle in cliques[key]:
            triangle_set = set(triangle)
            if triangle_set.issubset(ring_set):
                if triangle_set in triangles_sets:
                    pass
                else:
                    triangles_sets.append(set(triangle))
                    triangles.append(triangle)



    return triangles


def plot_mesh(mesh, z, verbous=False):
    if verbous:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(mesh, z, label='parametric curve', alpha=1)
        plt.show()


def draw_change(x, y, z, x_change, y_change, z_change, verbous=False):
    """draw vectors that show how each vertx has moved.
    """
    if verbous:
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.quiver(x, y, z, x_change, y_change, z_change, length=0.1, normalize=True)

        plt.show()


def check_angles(specs):
    """run check of what angles do I get in spec and if it makes sense"""

    total_bad = 0
    for i, spec in enumerate(specs):
        angles = spec[1]

        if (sum(angles) < np.pi * 0.99999) or (sum(angles) > np.pi * 1.000001):
            print("angles do not add up to pi in triangle", i, "angles", angles, "angles sum", sum(angles))

        for angle in angles:
            if angle > np.pi / 2:
                total_bad +=1
                print("one of the angles is larger than 90 degreesin triangle", i, "angle", angle, "sides",  spec[0])
    print("total bad", total_bad, "out of" , len(specs))

def plot_triangle_reshaped(triangles_reshaped, verbous=False):
    """plots triangles specified in triangle_reshape array"""
    if verbous:
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        for t in triangles_reshaped:
            # ax.scatter(t[:, 0], t[:, 1], t[:, 2], label='parametric curve', alpha=1)
            verts = [list(zip(t[:, 0], t[:, 1], t[:, 2]))]
            ax.add_collection3d(Poly3DCollection(verts))

        ax.set_xlim3d(0, 3.5)
        ax.set_ylim3d(0, 3.5)
        ax.set_zlim3d(-0.3, 0.3)

        plt.show()
