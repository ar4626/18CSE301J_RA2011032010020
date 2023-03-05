import matplotlib.pyplot as plt

# sample data
data = [1, 3, 3, 3, 5, 6, 8, 8, 9]

# set the number of bins
num_bins = 4

# create the histogram
plt.hist(data, bins=num_bins, edgecolor='black')

# set the title and labels
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# display the histogram
plt.show()
