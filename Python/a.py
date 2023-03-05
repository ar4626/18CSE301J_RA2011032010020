import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y for the first data set
data1 = pd.read_csv('Python/data1.csv')
df1 = pd.DataFrame(data1)
X1 = list(df1.iloc[:, 0])
Y1 = list(df1.iloc[:, 1])

# Initialize the lists for X and Y for the second data set
data2 = pd.read_csv('Python\data.csv')
df2 = pd.DataFrame(data2)
X2 = [x + 0.4 for x in list(df2.iloc[:, 0])]
Y2 = list(df2.iloc[:, 1])

# Create the plot
fig, ax = plt.subplots()
ax.bar(X1, Y1, color='lightcoral', width=0.4)
ax.bar(X2, Y2, color='red', width=0.4, alpha=0.5)
ax.set_title("Students over 11 Years", color='white')
ax.set_xlabel("Years", color='white')
ax.set_ylabel("Number of Students", color='white')
ax.set_facecolor('black')
ax.tick_params(colors='white')

# Set the color of the text and the background
fig.patch.set_facecolor('black')
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

# Set the x-axis limits
ax.set_xlim([min(X1)-0.5, max(X2)+0.5])

# Show the plot
plt.show()
