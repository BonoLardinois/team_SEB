import numpy as np
import matplotlib.pyplot as plt

def visualise(houses,):

    # Create data
    x_coordinates = []
    y_coordinates = []
    for house in houses:
        x_coordinates.append(house.bottom_left[0])
        y_coordinates.append(house.bottom_left[1])
    
    colors = (0,0,0)
    area = np.pi*3

    # Plot
    plt.scatter(x_coordinates, y_coordinates, s=area, c=colors, alpha=0.5)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()