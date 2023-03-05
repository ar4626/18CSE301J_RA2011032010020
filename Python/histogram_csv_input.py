import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
data = pd.read_csv('Python\data.csv')
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Create the plot
fig, ax = plt.subplots()
ax.bar(X, Y, color='red')
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

# Show the plot
plt.show()