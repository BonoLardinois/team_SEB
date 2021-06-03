import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualise(houses, water):

    # Create data
    fig, ax = plt.subplots()
    
    for house in houses:
        if house.name == "familyhome":
            house_rect = patches.Rectangle((house.bottom_left[0], house.bottom_left[1]), 12, 12, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(house_rect)
            
        elif house.name == "bungalow":
            house_rect = patches.Rectangle((house.bottom_left[0], house.bottom_left[1]), 17, 13, linewidth=1, edgecolor='y', facecolor='none')
            ax.add_patch(house_rect)
        
        else:
            house_rect = patches.Rectangle((house.bottom_left[0], house.bottom_left[1]), 24, 22, linewidth=1, edgecolor='g', facecolor='none')
            ax.add_patch(house_rect)   

    print(water.top_right[0])
    print(water.top_right[1])

    water_rect = patches.Rectangle((water.left_bottom[0], water.left_bottom[1]), water.top_right[0], water.top_right[1], linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(water_rect) 

    

    # Plot
    plt.plot(180 , 160)
    plt.title('Housing map')
    plt.xlabel('width')
    plt.ylabel('depth')
    
    plt.show()