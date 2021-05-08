# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:53:19 2021

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import datasets

df=datasets.load_iris()
X=df.data[:, :2]
y=df.target


fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(df.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("three Classes")
ax.set_xlabel(" Sepal Length")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Sepal Width")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Petal Length")
ax.w_zaxis.set_ticklabels([])

plt.show()