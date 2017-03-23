"""Utility functions."""

import matplotlib.pyplot as plt
import numpy as np


def get_dataset(num_samples, max_coord, function):
    x = np.random.random((num_samples, 2)) * max_coord
    y = function(x)
    return {"x": x, "y": y}


def compute_for_grid(X_0, X_1, function):
    X_0_X_1 = np.concatenate(
        (X_0.reshape((-1, 1)), X_1.reshape((-1, 1))), axis=1)
    Z = function(X_0_X_1)
    Z = np.reshape(Z, X_0.shape)
    return Z


def plot_function(ax, function, text):
    ax.cla()
    x_0 = np.linspace(0, 7, 100)
    x_1 = np.linspace(0, 7, 100)
    X_0, X_1 = np.meshgrid(x_0, x_1)
    Z = compute_for_grid(X_0, X_1, function)
    ax.plot_surface(X_0, X_1, Z, rstride=8, cstride=8, alpha=0.3)
    ax.contourf(X_0, X_1, Z, zdir='z', offset=-3, cmap=plt.cm.coolwarm)
    ax.contourf(X_0, X_1, Z, zdir='x', offset=-1, cmap=plt.cm.coolwarm)
    ax.contourf(X_0, X_1, Z, zdir='y', offset=-1, cmap=plt.cm.coolwarm)
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 8)
    ax.set_zlim(-3, 3)
    ax.view_init(45, 45)
    ax.set_title(text)
    return Z
