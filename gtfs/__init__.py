
from .shape import Shape
from .stop import Stop
from .realtime_vehicles import VehicleActivity
    

def convert_shape_gtfs_to_shape(shape_gtfs):
    shape_gtfs = shape_gtfs.split("\n")[1:]
    shape_gtfs = [Shape(x.split(",")) for x in shape_gtfs]
    return shape_gtfs

def convert_stop_gtfs_to_stop(stop_gtfs):
    stop_gtfs = stop_gtfs.split("\n")[1:]
    for item in stop_gtfs:
        item = item.replace('"', '')
    stop_gtfs = [Stop(x.split(",")) for x in stop_gtfs]
    return stop_gtfs
