from copy import deepcopy
from shapely.geometry import Polygon

def rotation(coordinates, width, depth, width2, depth2, placement, required_free_space): 
    if placement == 'vertical':
        copy_width = deepcopy(width)
        copy_width2 = deepcopy(width2)
        width = depth
        depth = copy_width
        width2 = depth2
        depth2 = copy_width2
        polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
        polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
    if placement == 'horizontal':
        polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
        polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])


    return (width, depth, depth2, width2, polygon, polygon_free_space)

