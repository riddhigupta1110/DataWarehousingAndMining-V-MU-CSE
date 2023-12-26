import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

num_data_points = int(input("Enter the number of data points: "))
data_points = [list(map(float, input(f"Enter the coordinates for data point {i + 1} (xy): ").split())) for i in range(num_data_points)]

X = np.array(data_points)
Z = sch.linkage(X, 'complete')
merging_steps = []

for i in range(len(Z)):
    threshold = Z[i, 2]
    clusters = sch.fcluster(Z, threshold, criterion='distance')
    step = []

    for cluster_id in np.unique(clusters):
        data_point_indices = np.where(clusters == cluster_id)[0]
        data_point_cluster = [data_points[i] for i in data_point_indices]
        step.append(data_point_cluster)

    merging_steps.append((threshold, step))

    print(f"Step {i + 1}:")
    for merged_clusters in step:
        if len(merged_clusters) > 1:
            print(f"Merging {merged_clusters} at threshold {threshold:.2f}")

sch.dendrogram(Z, labels=[str(point) for point in X])
plt.xlabel('Data point')
plt.ylabel('Distance')
plt.show()
