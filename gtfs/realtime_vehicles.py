
from utils import toDateTime

class VehicleActivity(object):
    """
    {
        "RecordedAtTime": "2023-04-18T15:55:26Z",
        "ValidUntilTime": "",
        "MonitoredVehicleJourney": {
            "LineRef": "L1",
            "DirectionRef": "S",
            "FramedVehicleJourneyRef": {
                "DataFrameRef": "2023-04-18",
                "DatedVehicleJourneyRef": "154"
            },
            "PublishedLineName": "Local",
            "OperatorRef": "CT",
            "OriginRef": "70012",
            "OriginName": "San Francisco Caltrain Station",
            "DestinationRef": "70272",
            "DestinationName": "Tamien Caltrain Station",
            "Monitored": true,
            "InCongestion": null,
            "VehicleLocation": {
                "Longitude": "-122.396133",
                "Latitude": "37.775589"
            },
            "Bearing": null,
            "Occupancy": null,
            "VehicleRef": "154",
            "MonitoredCall": {
                "StopPointRef": "70022",
                "StopPointName": "22nd Street Caltrain Station",
                "DestinationDisplay": "Tamien",
                "VehicleLocationAtStop": "",
                "VehicleAtStop": "",
                "AimedArrivalTime": "2023-04-18T17:13:00Z",
                "ExpectedArrivalTime": "2023-04-18T15:55:48Z",
                "AimedDepartureTime": "2023-04-18T17:13:00Z",
                "ExpectedDepartureTime": "2023-04-18T17:13:00Z"
            },
            "OnwardCalls": {
                "OnwardCall": [

                ]
            }
        }
    }
    """
    def __init__(self, data):
        self.__data = data
        self.monitored_vehicle_journey = MonitoredVehicleJourney(data['MonitoredVehicleJourney'])

    @property
    def RecordedAtTime(self):
        return toDateTime(self.__data['RecordedAtTime'])

    @property
    def ValidUntilTime(self):
        return self.__data['ValidUntilTime']


class VehicleLocation(object):
    """
    {
        "Longitude": "-122.396133",
        "Latitude": "37.775589"
    }
    """
    def __init__(self, data):
        self.__data = data

    @property
    def Longitude(self) -> float:
        return float(self.__data['Longitude'])

    @property
    def Latitude(self) -> float:
        return float(self.__data['Latitude'])


class MonitoredCall(object):
    """
    {
        "StopPointRef": "70022",
        "StopPointName": "22nd Street Caltrain Station",
        "DestinationDisplay": "Tamien",
        "VehicleLocationAtStop": "",
        "VehicleAtStop": "",
        "AimedArrivalTime": "2023-04-18T17:13:00Z",
        "ExpectedArrivalTime": "2023-04-18T15:55:48Z",
        "AimedDepartureTime": "2023-04-18T17:13:00Z",
        "ExpectedDepartureTime": "2023-04-18T17:13:00Z"
    }
    """
    def __init__(self, data):
        self.__data = data

    @property
    def StopPointRef(self):
        return self.__data['StopPointRef']

    @property
    def StopPointName(self):
        return self.__data['StopPointName']

    @property
    def DestinationDisplay(self):
        return self.__data['DestinationDisplay']

    @property
    def VehicleLocationAtStop(self):
        return self.__data['VehicleLocationAtStop']

    @property
    def VehicleAtStop(self):
        return self.__data['VehicleAtStop']

    @property
    def AimedArrivalTime(self):
        return self.__data['AimedArrivalTime']

    @property
    def ExpectedArrivalTime(self):
        return self.__data['ExpectedArrivalTime']

    @property
    def AimedDepartureTime(self):
        return self.__data['AimedDepartureTime']

    @property
    def ExpectedDepartureTime(self):
        return self.__data['ExpectedDepartureTime']

class MonitoredVehicleJourney(object):
    """
    {
        "LineRef": "L1",
        "DirectionRef": "S",
        "FramedVehicleJourneyRef": {
            "DataFrameRef": "2023-04-18",
            "DatedVehicleJourneyRef": "154"
        },
        "PublishedLineName": "Local",
        "OperatorRef": "CT",
        "OriginRef": "70012",
        "OriginName": "San Francisco Caltrain Station",
        "DestinationRef": "70272",
        "DestinationName": "Tamien Caltrain Station",
        "Monitored": true,
        "InCongestion": null,
        "VehicleLocation": {
            "Longitude": "-122.396133",
            "Latitude": "37.775589"
        },
        "Bearing": null,
        "Occupancy": null,
        "VehicleRef": "154",
        "MonitoredCall": {
            "StopPointRef": "70022",
            "StopPointName": "22nd Street Caltrain Station",
            "DestinationDisplay": "Tamien",
            "VehicleLocationAtStop": "",
            "VehicleAtStop": "",
            "AimedArrivalTime": "2023-04-18T17:13:00Z",
            "ExpectedArrivalTime": "2023-04-18T15:55:48Z",
            "AimedDepartureTime": "2023-04-18T17:13:00Z",
            "ExpectedDepartureTime": "2023-04-18T17:13:00Z"
        },
        "OnwardCalls": {
            "OnwardCall": [

            ]
        }
    }
    """
    def __init__(self, data):
        self.__data = data
        self.__vehicle_location = VehicleLocation(data['VehicleLocation'])
        self.__monitored_call = MonitoredCall(data['MonitoredCall'])

    @property
    def LineRef(self):
        return self.__data['LineRef']

    @property
    def DirectionRef(self):
        return self.__data['DirectionRef']

    @property
    def FramedVehicleJourneyRef(self):
        return self.__data['FramedVehicleJourneyRef']

    @property
    def PublishedLineName(self):
        return self.__data['PublishedLineName']

# local: c5c5c5, 000000
# limited: ffcc4a, 000000
# bullet: E31837, ffffff

    @property
    def icon_color(self):
        colors = {
            "Local": "#9e9e9e",
            "Limited": "#ffcc4a",
            "Bullet": "#E31837"
        }
        if "LTD" in self.PublishedLineName:
            return colors['Limited']
        return colors[self.PublishedLineName]


    @property
    def text_color(self):
        colors = {
            "Local": "#000000",
            "Limited": "#000000",
            "Bullet": "#000000"#"#ffffff"
        }
        if "LTD" in self.PublishedLineName:
            return colors['Limited']
        return colors[self.PublishedLineName]


    @property
    def OperatorRef(self):
        return self.__data['OperatorRef']

    @property
    def OriginRef(self):
        return self.__data['OriginRef']

    @property
    def OriginName(self):
        return self.__data['OriginName']

    @property
    def DestinationRef(self):
        return self.__data['DestinationRef']

    @property
    def DestinationName(self):
        return self.__data['DestinationName']

    @property
    def Monitored(self):
        return self.__data['Monitored']

    @property
    def InCongestion(self):
        return self.__data['InCongestion']

    @property
    def VehicleLocation(self):
        return self.__vehicle_location

    @property
    def Bearing(self):
        return self.__data['Bearing']

    @property
    def Occupancy(self):
        return self.__data['Occupancy']

    @property
    def VehicleRef(self):
        return self.__data['VehicleRef']

    @property
    def MonitoredCall(self):
        return self.__monitored_call