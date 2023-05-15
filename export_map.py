

import folium, json, os, io, time
from PIL import Image
from selenium import webdriver
from folium import plugins
import gtfs, data # local imports

from utils import makeBeautifyIcon
from mapparser import convert_to_png

vectorTileLayerStyles = {}

#import gtfs_testing.gtfs as gtfs, folium, gtfs_testing.color_list as color_list, random
file_name = "testmap_custom.html"
ct_data = data.CaltrainData("c5a00e4e-b8a4-40cd-b650-a89fc139d2f8")

m = folium.Map(
    location=[37.389951149, -121.98964476585], 
    # tiles=None,
    tiles='cartodbpositron',
    zoom_start=10,
    zoom_control=False,
    attributionControl=False,
    )

# Train colors (route_color, route_text_color):
# local: c5c5c5, 000000
# limited: ffcc4a, 000000
# bullet: E31837, ffffff




folium.map.CustomPane("labels").add_to(m)

#options = {
#    "vectorTileLayerStyles": vectorTileLayerStyles
#}

# vc = plugins.VectorGridProtobuf(url, "folium_layer_name", options)

# m.add_child(vc)



shapes_raw = open("shapes.txt").read()
shapes = gtfs.convert_shape_gtfs_to_shape(shapes_raw)
shape_ids = sorted([*set([x.shape_id for x in shapes])])
shape_ids.pop(shape_ids.index("p_1425796"))
shape_ids.pop(shape_ids.index("p_1425704"))

stops_raw = open("stops.txt").read()
stops = gtfs.convert_stop_gtfs_to_stop(stops_raw)

"""for stop in stops:
    tempstop = stop.stop_id.replace('"', '')
    print(f"'{tempstop}'")
    if tempstop.isnumeric():
        print(f"    {tempstop} is numeric")
        stops.pop(stops.index(stop))
    elif tempstop.isupper():
        print(f"    {tempstop} is upper")
        stops.pop(stops.index(stop))"""


shape_ids = ["p_1425699"]
for shape_id in shape_ids:
    line = [x for x in shapes if x.shape_id == shape_id]
    print(type(line))
    print(len(line))
    line_coords = [(float(x.shape_pt_lat), float(x.shape_pt_lon)) for x in line]
    folium.PolyLine(
        line_coords,
        color="#dd1f29",
        #tooltip=line[0].shape_id,
        ).add_to(m)

for stop in stops:
    # print(stop.stop_id)
    tempstop = stop.stop_id.replace('"', '')
    if tempstop.isnumeric():
        print(f"    {tempstop} is numeric")
        stops.pop(stops.index(stop))
        continue
    elif tempstop.isupper():
        print(f"    {tempstop} is upper")
        stops.pop(stops.index(stop))
        continue

    # folium.CircleMarker(
    #     location=[float(stop.stop_lat), float(stop.stop_lon)],
    #     radius=5,
    #     popup=stop.stop_name,
    #     color="#000000",
    #     fill=True,
    #     fillOpacity=1,
    #     fill_color="#ffffff",#"#dd1f29",
    #     tooltip=stop.stop_name
    # ).add_to(m)

    folium.Marker(
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


vehicles_json = ct_data.get_vehicle_locations().json()['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['VehicleActivity']
vehicles = []

for vehicle in vehicles_json:
    vehicles.append(gtfs.VehicleActivity(vehicle))

print(len(vehicles))
for vehicle in vehicles:
    folium.Marker(
        location=[vehicle.monitored_vehicle_journey.VehicleLocation.Latitude, vehicle.monitored_vehicle_journey.VehicleLocation.Longitude],
        popup=f"{vehicle.monitored_vehicle_journey.PublishedLineName} {vehicle.monitored_vehicle_journey.DirectionRef} ({vehicle.monitored_vehicle_journey.VehicleRef})",
        tooltip="Hi! Im a vehicle!eeee",
        #pane="labels",
        icon=plugins.BeautifyIcon(
            icon="fa-solid fa-train",
            border_color=vehicle.monitored_vehicle_journey.icon_color, #"#DD1F29",
            text_color=vehicle.monitored_vehicle_journey.text_color,  #"#b3334f",
            icon_shape="circle"
        )).add_to(m)


m.save(file_name)
# ones that are bad: 1425796, 1425704
# good but not 1277432
# 1277433


# await asyncio.sleep(1)
# parse_map(file_name)

delay=1

tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=file_name)
# m.save(file_name)


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1200,875")

browser = webdriver.Chrome(options=options)

browser.get(tmpurl)
print(browser.get_window_size())
#Give the map tiles some time to load
time.sleep(delay)
# browser.save_screenshot(png_name)

temp = io.BytesIO(browser.get_screenshot_as_png())
image = Image.open(temp)
image.show()

 
