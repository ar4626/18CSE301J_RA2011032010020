import matplotlib.pyplot as plt

# Data
labels = ['Entity 1', 'Entity 2']
sizes = [60, 40]  # Percentage of each entity

# Create the figure and the axes
fig, ax = plt.subplots()

# Plot the donut chart
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.5})

# Add a circle in the middle to create a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Add a title
ax.set_title('Donut Chart for Two Entities')

# Show the plot
plt.show()
