import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Python\datadonut.csv')

# Extract the data
labels = df['Entity']
sizes = df['Percentage']

# Create the figure and the axes
fig, ax = plt.subplots(facecolor='black')

# Define the colors for the chart
colors = ['red', 'lightcoral']


# Plot the donut chart
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.5}, textprops={'color': 'white'})

# Add a circle in the middle to create a donut chart
centre_circle = plt.Circle((0,0),0.30,fc='black')
fig.gca().add_artist(centre_circle)

# Add a title
ax.set_title('Donut Chart for Two Entities', color='white')

# Show the plot
plt.show()
