# Import necessary libraries
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the dataset
# Replace 'path_to_mall_customers.csv' with the actual path to the dataset you download from Kaggle
customers_df = pd.read_csv('Mall_Customers.csv')

# Select features for clustering
# Here we are using only the annual income and spending score for simplicity
X = customers_df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Hierarchical clustering
# We use the 'ward' linkage method to minimize the variance of clusters being merged
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
hc.fit(X)

# Plotting the resulting clusters
plt.figure(figsize=(10, 7))
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=hc.labels_, cmap='rainbow')
plt.title('Hierarchical Clustering of Mall Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

# Additionally, we can plot a dendrogram to visualize the hierarchical clustering process
# The dendrogram illustrates how each cluster is composed by drawing a U-shaped link between a non-singleton cluster and its children
Z = linkage(X, 'ward')
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distances')
plt.show()
