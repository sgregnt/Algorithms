import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

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

for alpha in [-4.0]:#, -4.0, -3.0, -2.0]:
    out = gaussian_random_field(Pk = lambda k: k**alpha, size=20)
    # plt.figure()
    # plt.imshow(out.real, interpolation='none')



import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')
xv, yv = np.meshgrid(range(out.real.shape[0]), range(out.real.shape[1]), sparse=False, indexing='ij')

scale = 2
xv = xv/scale
yv = yv/scale

# ax.plot(xv.reshape(-1), yv.reshape(-1), out.real.reshape(-1), label='parametric curve')
# ax.plot_surface(xv, yv, out.real, label='parametric curve')
tri=  matplotlib.tri.Triangulation(xv.reshape(-1), yv.reshape(-1))

import networkx as nx
G = nx.Graph()
G.add_edges_from(tri.edges)
L = nx.laplacian_matrix(G)


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

elem = 250
ring = get_3_ring(G, elem)
print(yv)
aa = ax.plot_trisurf(tri, out.real.reshape(-1), label='parametric curve', alpha=0.5)
ax.set_xlim3d(0, 20/scale)
ax.set_ylim3d(0, 20/scale)
ax.set_zlim3d(0, 1)

x = xv.reshape(-1)
y = yv.reshape(-1)
z = out.real.reshape(-1)

print(x[elem], y[elem], z[elem])
ax.scatter(x[elem], y[elem], z[elem], c='r' , s = 50)
print("ring size", len(ring))
for elem in ring:
    ax.scatter(x[elem], y[elem], z[elem], c='g', s=10)

# subsample point of the mesh
from random import sample
sample_size = 10
random_subsample = sample(set(ring), sample_size)

for elem in random_subsample:
    ax.scatter(x[elem], y[elem], z[elem], c='b', s=5)

# contruct mesh on the subsample
x_sub = [x[i] for i in random_subsample]
y_sub = [y[i] for i in random_subsample]
z_sub = [z[i] for i in random_subsample]

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = matplotlib.tri.Triangulation(x_sub, y_sub)
ax.plot_trisurf(triang, z_sub)


# plt.show()


def get_trinagle_coordinates(triangles, x, y, z):
    """conver triangles to actual coordinates"""

    # [item for sublist in two_ring for item in sublist]
    tri_cor = np.array([(x[i], y[i], z[i]) for triangle in triangles for i in triangle])
    tri_cor_reshape = np.array([((x[triangle[0]], y[triangle[0]], z[triangle[0]]),
                                 (x[triangle[1]], y[triangle[1]], z[triangle[1]]),
                                 (x[triangle[2]], y[triangle[2]], z[triangle[2]])) for triangle in triangles])
    return tri_cor,tri_cor_reshape


a,  triangles_reshaped = get_trinagle_coordinates(triang.triangles, x_sub, y_sub, z_sub)
b = triangles_reshaped
print(a[0], a[1], a[2])
print(b[0])
from numpy import linalg as LA
import math

def get_tiangl_specs(triangles_reshaped):

    results = []
    for t in triangles_reshaped:
        a1 = LA.norm(t[0]- t[1])
        a2 = LA.norm(t[0]- t[2])
        a3 = LA.norm(t[1]- t[2])

        alpha1 =  math.acos(np.abs(np.inner(t[1]-t[0], t[2] - t[0]))/ (a1 * a2))
        alpha1 =  math.acos((np.inner(t[1]-t[0], t[2] - t[0]))/ (a1 * a2))

        alpha2 =  math.acos(np.abs(np.inner(t[2]-t[1], t[0] - t[1]))/ (a1 * a3))
        alpha2 =  math.acos((np.inner(t[2]-t[1], t[0] - t[1]))/ (a1 * a3))

        alpha3 =  math.acos(np.abs(np.inner(t[1]-t[2], t[0] - t[2]))/ (a2 * a3))
        alpha3 =  math.acos((np.inner(t[1]-t[2], t[0] - t[2]))/ (a2 * a3))

        cot1 = math.cos(alpha1)/math.sin(alpha1)
        cot1 = np.abs(math.cos(alpha1)/math.sin(alpha1))
        cot2 = math.cos(alpha2)/math.sin(alpha2)
        cot2 = np.abs(math.cos(alpha2)/math.sin(alpha2))
        cot3 = math.cos(alpha3)/math.sin(alpha3)
        cot3 = np.abs(math.cos(alpha3)/math.sin(alpha3))

        results.append([(a1, a2, a3), (alpha1, alpha2, alpha3), (cot1, cot2, cot3)])

    return results

print(get_tiangl_specs(triangles_reshaped))
a = get_tiangl_specs(triangles_reshaped)
print(a[0][1])

# check that the sum adds up to 180 degrees.
b = [ np.sum(i[1]) for i in a ]
print(b)

def compute_energy(cots, sides):
    cot1, cot2, cot3 = cots
    a1, a2, a3 =  sides

    return (0.25 * (a1**2) * cot3  + 0.25 * (a2 ** 2) * cot2 + 0.25 * (a3 ** 2) * cot1)

def total_energy(triangles):
    energy = 0
    for triangle in triangles:
        energy +=  compute_energy(triangle)
    return energy

print(compute_energy(a[0]))
print(total_energy(a))

1/0

# from pymesh import obj
# m = obj.Obj("sample.obj")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

fig = plt.figure(figsize=plt.figaspect(0.5))

#============
# First plot
#============

# Make a mesh in the space of parameterisation variables u and v
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

# This is the Mobius mapping, taking a u, v pair and returning an x, y, z
# triple
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)

# Triangulate parameter space to determine the triangles
tri = mtri.Triangulation(u, v)

# Plot the surface.  The triangles in parameter space determine which x, y, z
# points are connected by an edge.
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)


#============
# Second plot
#============

# Make parameter spaces radii and angles.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles

# Map radius, angle pairs to x, y, z points.
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = mtri.Triangulation(x, y)

# Mask off unwanted triangles.
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)

# Plot the surface.
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)


plt.show()