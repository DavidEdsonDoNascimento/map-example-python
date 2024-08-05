import folium

from place import Place

places = [
    Place("Grande Pirâmide de Gizé", 29.978, 31.1344),
    Place("Farol de Alexandria", 31.2094, 29.913),
]

m = folium.Map(location=[28.978, 31.1344], zoom_start=5, control_scale=True)

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012",
    name="Esri.WorldStreetMap",
).add_to(m)

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
    name="Esri.WorldImagery",
).add_to(m)

folium.LayerControl().add_to(m)

for i in range(len(places)):
    place = places[i]
    folium.Marker(location=place.get_coord(), popup=place.get_name()).add_to(m)

m.save("place-in-map.html")
