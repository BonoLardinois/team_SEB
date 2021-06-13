from copy import deepcopy
from shapely.geometry import Polygon

def rotation(coordinates, width, depth, placement, required_free_space): 
    if placement == 'vertical':
        # calculating new width and depth
        copy_width = deepcopy(width)
        copy_width_required_free_space = deepcopy(width + (2 * required_free_space))

        width = depth
        depth = copy_width
        width_with_required_free_space = depth + (2 * required_free_space)
        depth_with_required_free_space = copy_width_required_free_space
        

        # making polygons
        polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
        polygon_free_space = Polygon([coordinates, (coordinates[0] + width_with_required_free_space, coordinates[1]), (coordinates[0] + width_with_required_free_space, coordinates[1] + depth_with_required_free_space), (coordinates[0], coordinates[1] + depth_with_required_free_space)])

    if placement == 'horizontal':
        # making polygons
        width_with_required_free_space = width +(2 * required_free_space)
        depth_with_required_free_space = depth + (2 * required_free_space)
        polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
        polygon_free_space = Polygon([coordinates, (coordinates[0] + width_with_required_free_space, coordinates[1]), (coordinates[0] + width_with_required_free_space, coordinates[1] + depth_with_required_free_space), (coordinates[0], coordinates[1] + depth_with_required_free_space)])


    return (width, depth, polygon, polygon_free_space)