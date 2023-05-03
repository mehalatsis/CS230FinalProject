import streamlit as st
import pandas as pd
import folium                           # learned how to use folium to create an interactive map with the on click pop-ups of the names of the roller coasters
from streamlit_folium import st_folium

data = pd.read_csv('RollerCoasters-Geo.csv')
df = pd.DataFrame(data)
df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

st.title(':blue[Map of The Roller Coasters]:earth_americas:')
st.write('Below is a map of the locations of the roller coasters. Click on one of the points to see the name of the roller coaster!')
st.write('https://towardsdatascience.com/3-easy-ways-to-include-interactive-maps-in-a-streamlit-app-b49f6a22a636')

m = folium.Map(location=[df.lat.mean(), df.lon.mean()],
               zoom_start=3, control_scale=True)


for i, row in df.iterrows():
    iframe = folium.IFrame('Roller Coaster: ' + str(row["Coaster"]))
    popup = folium.Popup(iframe, min_width=125, max_width=200)
    folium.Marker(location=[row['lat'], row['lon']],
                  popup=popup, c=row['Coaster']).add_to(m)

st_data = st_folium(m, width=700)

