import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('D.xlsx')

# Extract data from the DataFrame
names = df['Name']
ages = df['Age']
scores = df['Score']

# Bar Chart
plt.bar(names, scores)
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Bar Chart of Scores')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Scatter Plot
plt.scatter(ages, scores, label='Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Scatter Plot of Age vs. Score')
plt.grid(True)
plt.show()

# Histogram
plt.hist(ages, bins=5, color='yellow', edgecolor='red')  # 'bins' represent the number of bins in the histogram
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Ages')
plt.show()
