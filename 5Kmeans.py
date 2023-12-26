#pip install scikit-learn
import numpy as np
from sklearn.cluster import KMeans

k = int(input("Enter the number of clusters (k): "))

# Sample one-dimensional data
data = np.array([2,4,6,8,10])
# Reshape the data to a two-dimensional array
data = data.reshape(-1, 1)

# Initialize the KMeans model
kmeans = KMeans(n_clusters=k)
# Fit the model to the data
kmeans.fit(data)

# Get cluster labels and cluster centers
labels = kmeans.labels_

# Display cluster labels and centroids
for cluster in range(k):
    cluster_data = data[labels == cluster]
    print(f"Cluster {cluster + 1}:")
    print("Data points:", cluster_data)
    print()

