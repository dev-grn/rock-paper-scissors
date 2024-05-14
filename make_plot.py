import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load data from a file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return [float(x) for x in data]

# Example usage with a hypothetical 'data.txt' file
data = load_data('/Users/devngj/Desktop/Projects/rps/1 1 1 200 2 1.txt')

# Step 2: Determine the range of the data
min_value = min(data)
max_value = max(data)

# Step 3: Create bins from min to max with a step of 5
bins = np.arange(min_value, max_value + 5, 5)  # Add 5 to include the max value in the range

# Step 4: Plot the histogram
plt.hist(data, bins=bins, edgecolor='black', rwidth=0.8)

# Set x-axis labels to show ranges
# plt.xticks([(a + b) / 2 for a, b in zip(bins[:-1], bins[1:])], [f'{int(a)}~{int(b-1)}' for a, b in zip(bins[:-1], bins[1:])])

# Adding labels and title
plt.xlabel('Rounds Needed for Win')
plt.ylabel('Frequency')
plt.title('1 1 1 200 2 1')

# Show plot
plt.show()

