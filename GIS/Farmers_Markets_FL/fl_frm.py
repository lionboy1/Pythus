import folium
import pandas as pd

my_florida = folium.Map(location=[28.207003, -81.715364],
                        zoom_start = 7)
#Convert data to appropriate types                        
locations = pd.read_csv('fl_state_frm.csv')
locations['Lat'] = locations['Lat'].astype(float)
locations['Lon'] = locations['Lon'].astype(float)
locations['Result'] = locations['Result'].astype(str)

#Maybe over kill but when variables are set for map, force data type conversion again
long = pd.to_numeric(locations['Lon'], errors='coerce')
lat = pd.to_numeric(locations['Lat'], errors='coerce')
name = locations['Result'] = locations['Result'].astype(str)

#A quick check to see the array list starting from position 0 and showing everything after to the end
print(long.iloc[0:])

#Iterate over the csv and populate the map with the data

for index, (value1, value2, value3) in enumerate(zip(lat, long, name)):    
    folium.Marker([value1, value2],
                  popup=value3,
                  icon=folium.Icon(color='green')
                 ).add_to(my_florida)
                 
#Now load the map

my_florida
