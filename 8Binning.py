import numpy as np

dataset = input("Enter numbers separated by ',': ").split(',')
dataset = [int(i) for i in dataset]
dataset = np.array(dataset)

bin_size = int(input("Enter bin size: "))

dataset.sort()

# Calculate the number of bins
no_bins = len(dataset) // bin_size + (len(dataset) % bin_size > 0)

# Create bins
bins = np.array_split(dataset, no_bins)

# Calculate mean, median, and boundaries
bin_mean = [np.mean(bin) for bin in bins]
bin_median = [np.median(bin) for bin in bins]
bin_boundary = [bin[[0, -1]] for bin in bins]

print("Bins:", bins)
print("Bin Mean:", bin_mean)
print("Bin Median:", bin_median)
print("Bin Boundary:", bin_boundary)