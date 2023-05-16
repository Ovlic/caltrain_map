
import requests

base_url = "https://api.511.org/transit/"

class CaltrainData:
    """
    Caltrain Data class for getting data from the 511 transit api.
    # Parameters:
    api_key (str): The api key for the 511 transit api.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.params["api_key"] = self.api_key
        self.session.params["agency"] = "CT"

    def get_vehicle_locations(self):
        """Get live vehicle locations for Caltrain.
        # Returns:
        requests.Response: The response from the api.
        """
        url = base_url + "VehicleMonitoring"
        response = self.session.get(url)
        # print(response.text)
        return response
