"""
Support for GTFS stops.txt
"""

class Stop(object):
    """
    stop_id,stop_code,stop_name,stop_lat,stop_lon,zone_id,stop_desc,stop_url,location_type,parent_station,stop_timezone,wheelchair_boarding,platform_code
    "22nd_street","22nd_street",22nd Street,37.756972,-122.392492,"69669","","","1","","America/Los_Angeles","0",""
    """
    def __init__(self, data):
        self.__data = data

    @property
    def stop_id(self):
        return self.__data[0]

    @property
    def data(self):
        return self.__data

    @property
    def stop_code(self):
        return self.__data[1]

    @property
    def stop_name(self):
        return self.__data[2]

    @property
    def stop_lat(self):
        return self.__data[3]

    @property
    def stop_lon(self):
        return self.__data[4]

    @property
    def zone_id(self):
        return self.__data[5]

    @property
    def stop_desc(self):
        return self.__data[6]

    @property
    def stop_url(self):
        return self.__data[7]

    @property
    def location_type(self):
        return self.__data[8]

    @property
    def parent_station(self):
        return self.__data[9]

    @property
    def stop_timezone(self):
        return self.__data[10]

    @property
    def wheelchair_boarding(self):
        return self.__data[11]

    @property
    def platform_code(self):
        return self.__data[12]

