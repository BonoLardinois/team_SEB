import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.backends.backend_pdf

def visualise(land_objects, total,out_path="output/test.pdf"):

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
        
        else:
            rectangle = patches.Rectangle((land_object.bottom_left[0], land_object.bottom_left[1]), land_object.width, land_object.depth, linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(rectangle)   

    # Plot
    plt.plot(180 , 160)
    plt.title(f'Housing map, total: {total}')
    plt.xlabel('width')
    plt.ylabel('depth')
    plt.show()
    pdf = matplotlib.backends.backend_pdf.PdfPages(out_path)
    for fig in range(1, plt.gcf().number + 1):
        pdf.savefig(fig)
    pdf.close()
    
   