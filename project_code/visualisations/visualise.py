import matplotlib.pyplot as plt
import matplotlib.patches as patches
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def visualise(land_objects, total, number_land_objects, out_path="output/test.png"):

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

    # Plot
    # 3d plot
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # x = [0,1,1,0]
    # y = [0,0,1,1]
    # z = [0,1,0,1]
    # verts = [zip(x,y,z)]
    # ax.add_collection3d(Poly3DCollection(verts), zs=z)  

    #normal plot
    plt.plot(180 , 160)
    plt.title(f'Housing map, total: {total},  {number_land_objects}')
    plt.xlabel('width')
    plt.ylabel('depth')
    plt.margins(0,0)
    plt.savefig(out_path)
    
   