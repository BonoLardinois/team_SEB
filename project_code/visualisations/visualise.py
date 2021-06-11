import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualise(land_objects, total):

    # Create data
    fig, ax = plt.subplots()
    
    for land_object in land_objects:
        if land_object.name == "familyhome":
            rectangle = patches.Rectangle((land_object.bottom_left[0], land_object.bottom_left[1]), land_object.width, land_object.depth, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rectangle)   
            
        elif land_object.name == "bungalow":
            rectangle = patches.Rectangle((land_object.bottom_left[0], land_object.bottom_left[1]), land_object.width, land_object.depth, linewidth=1, edgecolor='y', facecolor='none')
            ax.add_patch(rectangle)   
        
        elif land_object.name == "maison":
            rectangle = patches.Rectangle((land_object.bottom_left[0], land_object.bottom_left[1]), land_object.width, land_object.depth, linewidth=1, edgecolor='g', facecolor='none')
            ax.add_patch(rectangle)    
        
        elif land_object.name == "water":
            rectangle = patches.Rectangle((land_object.bottom_left[0], land_object.bottom_left[1]), land_object.width, land_object.depth, linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(rectangle)   

    # for water in waters:
    #     top_right_x = water.top_right[0] - water.bottom_left[0]
    #     top_right_y = water.top_right[1] - water.bottom_left[1]
        
    #     water_rect = patches.Rectangle((water.bottom_left[0], water.bottom_left[1]), top_right_x, top_right_y, linewidth=1, edgecolor='b', facecolor='none')
    #     ax.add_patch(water_rect) 

    

    # Plot
    plt.plot(180 , 160)
    plt.title(f'Housing map, total: {total}')
    plt.xlabel('width')
    plt.ylabel('depth')
    plt.savefig('output/test.png')
    plt.show()
   