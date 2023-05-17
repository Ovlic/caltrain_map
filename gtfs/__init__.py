
from .shape import Shape
from .stop import Stop
from .realtime_vehicles import VehicleActivity
    

def convert_shape_gtfs_to_shape(shape_gtfs: str) -> list(Shape):
    """Converts a string shape GTFS to a Shape object."""
    shape_gtfs = shape_gtfs.split("\n")[1:]
    l_shape_gtfs = [Shape(x.split(",")) for x in shape_gtfs]
    return l_shape_gtfs

def convert_stop_gtfs_to_stop(stop_gtfs) -> list(Stop):
    """Converts a string stop GTFS to a Stop object."""
    stop_gtfs = stop_gtfs.split("\n")[1:]
    for item in stop_gtfs:
        item = item.replace('"', '')
    l_stop_gtfs = [Stop(x.split(",")) for x in stop_gtfs]
    return l_stop_gtfs
