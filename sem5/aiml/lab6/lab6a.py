# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load the dataset (after you have downloaded it from Kaggle)
iris_df = pd.read_csv(load_iris)

# Preprocess the data
# We will remove the species column and only use the features for clustering
X = iris_df.drop('Species', axis=1)

# Standardize the features (optional but recommended)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans clustering
# Assuming we want to cluster the data into 3 clusters (as there are 3 species of Iris in the dataset)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Assign the clusters to each row in the dataframe
iris_df['cluster'] = kmeans.labels_

# Plotting the clusters
# Here, for simplicity, we only plot two dimensions of the multi-dimensional data
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.title("K-Means Clustering of Iris Dataset")
plt.xlabel("Feature 1 after scaling")
plt.ylabel("Feature 2 after scaling")
plt.show()
