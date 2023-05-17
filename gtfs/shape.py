"""
Support for the GTFS shapes.txt file.
"""

class Shape(object):
    """
    shape_id,shape_pt_lon,shape_pt_lat,shape_pt_sequence,shape_dist_traveled
    p_1277284,-121.5661454201,37.003512298,1,0.00000000
"""
    def __init__(self, data):
        self.__data = data

    @property
    def shape_id(self):
        return self.__data[0]

    @property
    def shape_pt_lon(self):
        return self.__data[1]

    @property
    def shape_pt_lat(self):
        return self.__data[2]

    @property
    def shape_pt_sequence(self):
        return self.__data[3]

    @property
    def shape_dist_traveled(self):
        return self.__data[4]
