# Import necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy.cluster import cmeans
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
# Replace 'path_to_iris_dataset.csv' with the actual path to the dataset you download from Kaggle
iris_df = pd.read_csv('Iris.csv')

# Select features for clustering
# Here we are using all the features for clustering, you can select which ones you want
X = iris_df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values.T

# Apply Fuzzy C-Means clustering
# 'cmeans' function returns a tuple, where the second element contains the membership values
# The parameters are:
# - data: N-dimensional array of data to cluster
# - c: Desired number of clusters or classes
# - m: Array exponentiation applied to the membership function u_old at each iteration
# - error: Stopping criterion; stop early if the norm of (u(p) - u(p-1)) < error
# - maxiter: Maximum number of iterations
# - init: Initial fuzzy c-partitioned matrix. If none provided, algorithm is randomly initialized
cntr, u, u0, d, jm, p, fpc = cmeans(X, c=3, m=2, error=0.005, maxiter=1000)

# Assign cluster membership
# Each data point has a membership for each cluster
cluster_membership = np.argmax(u, axis=0)

# Plotting the results
# For simplicity, we only plot the first two dimensions: SepalLengthCm vs SepalWidthCm
plt.figure(figsize=(8, 6))
for j in range(3):  # Assuming 3 clusters
    plt.scatter(X[0, cluster_membership == j],
                X[1, cluster_membership == j],
                label=f'Cluster {j}')

plt.scatter(cntr[:, 0], cntr[:, 1], s=300, marker='*', c='red', label='Centers')
plt.title('Fuzzy C-Means Clustering of Iris Dataset')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()
