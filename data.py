
import requests

base_url = "https://api.511.org/transit/"

class CaltrainData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.params["api_key"] = self.api_key
        self.session.params["agency"] = "CT"

    def get_vehicle_locations(self):
        url = base_url + "VehicleMonitoring"
        response = self.session.get(url)
        # print(response.text)
        return response

    
