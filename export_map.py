
# Imports
import folium, json, os, io, time, sys
from PIL import Image
from selenium import webdriver
from folium import plugins

# Check if os is windows (for webdriver)
if sys.platform == "win32": # Running windows
    from webdriver_manager.chrome import ChromeDriverManager # Webdriver manager for windows

# Local imports
import gtfs
from data import CaltrainData
from utils import makeBeautifyIcon

delay = 1 # Delay for loading the map
file_name = "testmap_custom.html" # Default filename to save the map to
ct_data = CaltrainData("c5a00e4e-b8a4-40cd-b650-a89fc139d2f8") # Create the CaltrainData object with the 511.org api key

# Create the map
m = folium.Map(
    location=[37.389951149, -121.98964476585], 
    # tiles=None,
    tiles='cartodbpositron',
    zoom_start=10,
    zoom_control=False,
    attributionControl=False,
    )

# Add labels so the train icons are on top
folium.map.CustomPane("labels").add_to(m)

# Train colors (route_color, route_text_color):
# local: c5c5c5, 000000
# limited: ffcc4a, 000000
# bullet: E31837, ffffff

shapes_raw = open("shapes.txt").read() # Get the train line shapes
shapes = gtfs.convert_shape_gtfs_to_shape(shapes_raw) # Convert csv to objects
shape_ids = sorted([*set([x.shape_id for x in shapes])]) # Sort in order
shape_ids.pop(shape_ids.index("p_1425796")) # Remove bad shapes
shape_ids.pop(shape_ids.index("p_1425704")) # Remove bad shapes

# Add line to map
shape_ids = ["p_1425699"] # Valid line shape
for shape_id in shape_ids:
    line = [x for x in shapes if x.shape_id == shape_id] # Get the line
    line_coords = [(float(x.shape_pt_lat), float(x.shape_pt_lon)) for x in line] # Convert to coords
    folium.PolyLine( # Add the line to the map
        line_coords,
        color="#dd1f29",
        #tooltip=line[0].shape_id,
        ).add_to(m)


stops_raw = open("stops.txt").read() # Get the train stops
stops = gtfs.convert_stop_gtfs_to_stop(stops_raw) # Convert csv to objects

# Add stops to map and remove duplicate and bad stops
for stop in stops: # Loop through stops
    tempstop = stop.stop_id.replace('"', '') # Remove quotes
    if tempstop.isnumeric(): # If the stop is numeric, remove it
        print(f"    {tempstop} is numeric")
        stops.pop(stops.index(stop))
        continue # Next stop
    elif tempstop.isupper(): # If the stop is upper, remove it
        print(f"    {tempstop} is upper")
        stops.pop(stops.index(stop))
        continue # Next stop

    folium.Marker( # Create the marker for the stop and give it css elements
        location=[float(stop.stop_lat), float(stop.stop_lon)],
        popup=stop.stop_name,
        icon=makeBeautifyIcon(
            icon=None,
            border_color="#000000",
            border_width=3,
            text_color="#b3334f",
            icon_shape="circle",
            inner_icon_style="opacity: 0;",
            icon_size=[13, 13],
        )
    ).add_to(m)

    print(f"    {tempstop} is good")

# Get the vehicle locations
vehicles_raw = ct_data.get_vehicle_locations()#.json()['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['VehicleActivity']

if sys.platform == "win32": # Running windows (json parsing issues?)
    vehicles_json = json.loads(vehicles_json.text.encode().decode("utf-8-sig"))['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['VehicleActivity']
else:
    vehicles_json = vehicles_raw.json()['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['VehicleActivity']
vehicles = []

for vehicle in vehicles_json: # Loop through vehicles
    vehicles.append(gtfs.VehicleActivity(vehicle)) # Convert to object

for vehicle in vehicles: # Loop through vehicles
    folium.Marker( # Create custom icon for vehicle
        location=[vehicle.monitored_vehicle_journey.VehicleLocation.latitude, vehicle.monitored_vehicle_journey.VehicleLocation.longitude],
        popup=f"{vehicle.monitored_vehicle_journey.PublishedLineName} {vehicle.monitored_vehicle_journey.DirectionRef} ({vehicle.monitored_vehicle_journey.VehicleRef})",
        tooltip="Hi! Im a vehicle!eeee",
        #pane="labels",
        icon=plugins.BeautifyIcon(
            icon="fa-solid fa-train",
            border_color=vehicle.monitored_vehicle_journey.icon_color, #"#DD1F29",
            text_color=vehicle.monitored_vehicle_journey.text_color,  #"#b3334f",
            icon_shape="circle"
        )).add_to(m)


m.save(file_name) # Save the map to a file

# Convert to png image

tmpurl = f"file://{os.getcwd()}/{file_name}" # Get the file path

# Set up the webdriver
options = webdriver.ChromeOptions() 
options.add_argument("--headless")
options.add_argument("--window-size=1200,875")

# Initialize the webdriver
if sys.platform == "win32": # Running windows
    # Windows requires you to preinstall the webdriver, this will automatically download it
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
else:
    browser = webdriver.Chrome(options=options)

browser.get(tmpurl) # Load the map
# print(browser.get_window_size())

#Give the map tiles some time to load
time.sleep(delay)

# Convert the map to an image

temp = io.BytesIO(browser.get_screenshot_as_png()) # Take a screenshot and save it as bytes
image = Image.open(temp) # Open the image from the bytes
image.show() # Show the image in the default image viewer
