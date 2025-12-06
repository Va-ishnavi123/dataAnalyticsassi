# import streamlit as st
# import folium
# from streamlit_folium import st_folium

# # Title
# st.title("Simple Folium Map in Streamlit")

# # Create a map centered on India
# m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)

# # --- Marker 1: Jaipur ---
# jaipur_lat, jaipur_lon = 26.9124, 75.7873
# folium.Marker(
#     location=[jaipur_lat, jaipur_lon],
#     popup=f"Place: Jaipur<br>Lat: {jaipur_lat}<br>Lon: {jaipur_lon}",
#     tooltip="Jaipur, Rajasthan"
# ).add_to(m)

# # --- Marker 2: Mumbai ---
# mumbai_lat, mumbai_lon = 19.0760, 72.8777
# folium.Marker(
#     location=[mumbai_lat, mumbai_lon],
#     popup=f"Place: Mumbai<br>Lat: {mumbai_lat}<br>Lon: {mumbai_lon}",
#     tooltip="Mumbai, Maharashtra"
# ).add_to(m)

# # Display map in Streamlit
# st_folium(m, width=700, height=500)
import streamlit as st
import folium
from streamlit_folium import st_folium

# Title
st.title("Simple Folium Map in Streamlit")

# Create a map centered on India with working tiles
m = folium.Map(
    location=[22.9734, 78.6569],
    zoom_start=5,
    tiles="CartoDB Positron"
)

# --- Marker 1: Jaipur ---
jaipur_lat, jaipur_lon = 26.9124, 75.7873
folium.Marker(
    location=[jaipur_lat, jaipur_lon],
    popup=f"Place: Jaipur<br>Latitude: {jaipur_lat}<br>Longitude: {jaipur_lon}",
    tooltip="Jaipur, Rajasthan"
).add_to(m)

# --- Marker 2: Mumbai ---
mumbai_lat, mumbai_lon = 19.0760, 72.8777
folium.Marker(
    location=[mumbai_lat, mumbai_lon],
    popup=f"Place: Mumbai<br>Latitude: {mumbai_lat}<br>Longitude: {mumbai_lon}",
    tooltip="Mumbai, Maharashtra"
).add_to(m)

# Display map in Streamlit
st_folium(m, width=700, height=500)
