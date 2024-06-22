from IPython.display import display, HTML, IFrame
import base64
from IPython.core.display import Javascript
import random
import geopandas as gpd
from shapely.geometry import Point
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import Point, Polygon
from scipy.spatial import ConvexHull
import json
from scipy.interpolate import griddata
import cartopy.crs as ccrs
from shapely.geometry import Polygon
import requests

def plot_points(points):
    # Create a GeoDataFrame
    geometry = [Point(lon, lat) for lon, lat in points]
    gdf = gpd.GeoDataFrame(geometry=geometry, crs='EPSG:4326')
    # Convert GeoDataFrame to GeoJSON
    geojson_data = gdf.to_crs(epsg=4326).to_json()

    # Compute the map center based on the points
    min_lon, min_lat, max_lon, max_lat = gdf.total_bounds
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    # Create the HTML content with Leaflet map and dynamic markers
    map_html2 = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Map</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <style>
            #mapid {{ height: 600px; }}
        </style>
    </head>
    <body>
        <div id="mapid"></div>
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script>
            var map = L.map('mapid').setView([{center_lat}, {center_lon}], 13);

            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }}).addTo(map);

            // Add GeoJSON layer with markers
            var geojsonLayer = L.geoJSON({geojson_data}, {{
                onEachFeature: function (feature, layer) {{
                    if (feature.properties && feature.properties.popupContent) {{
                        layer.bindPopup(feature.properties.popupContent);
                    }}
                }}
            }}).addTo(map);

            // Fit map to the bounds of the GeoJSON layer
            map.fitBounds(geojsonLayer.getBounds());
        </script>
    </body>
    </html>
    """

    # Encode the HTML content in base64
    encoded_html2 = base64.b64encode(map_html2.encode()).decode()

    # Display the HTML content using an iframe
    return IFrame('data:text/html;base64,' + encoded_html2, width=800, height=600)

    
def plot_points_with_dot_markers(points, dot_size=5, dot_color="red", hue_column=None):
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(points, crs='EPSG:4326', geometry=gpd.points_from_xy([point['lon'] for point in points],
                                                                                [point['lat'] for point in points]))

    # Convert GeoDataFrame to GeoJSON
    geojson_data = gdf.to_crs(epsg=4326).to_json()

    # Compute the map center based on the points
    min_lon, min_lat, max_lon, max_lat = gdf.total_bounds
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    # Create the HTML content with Leaflet map and dynamic markers
    map_html4 = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Map</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <style>
            #mapid {{ height: 600px; }}
            .legend {{
                background-color: #fff;
                padding: 5px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
                position: absolute;
                bottom: 20px;
                left: 20px;
                z-index: 1000;
            }}
            .legend-title {{
                font-weight: bold;
                margin-bottom: 5px;
            }}
            .legend-item {{
                line-height: 18px;
                margin-bottom: 8px;
            }}
            .legend-item span {{
                display: inline-block;
                width: 15px;
                height: 15px;
                margin-right: 5px;
            }}
        </style>
    </head>
    <body>
        <div id="mapid"></div>
        <!-- Legend for color bar -->
        <div id="legend" class="legend">
            <div class="legend-title">Legend</div>
            <div class="legend-item"><span style="background-color: hsl(240, 100%, 50%);"></span> 0 - 20%</div>
            <div class="legend-item"><span style="background-color: hsl(180, 100%, 50%);"></span> 20 - 40%</div>
            <div class="legend-item"><span style="background-color: hsl(120, 100%, 50%);"></span> 40 - 60%</div>
            <div class="legend-item"><span style="background-color: hsl(60, 100%, 50%);"></span> 60 - 80%</div>
            <div class="legend-item"><span style="background-color: hsl(0, 100%, 50%);"></span> 80 - 100%</div>
        </div>
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script>
            var map = L.map('mapid').setView([{center_lat}, {center_lon}], 13);

            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }}).addTo(map);

            // Initialize min and max values for hue column
            var min = Infinity;
            var max = -Infinity;

            // Function to calculate color based on value
            function getColor(value, min, max) {{
                // Ensure value is within the range [min, max]
                value = Math.max(min, Math.min(max, value));
                
                // Scale value to a range between 0 and 1
                var scaledValue = (value - min) / (max - min);
                
                // Calculate hue based on the scaled value (0 to 240)
                var hue = (1 - scaledValue) * 240;
                
                // Construct HSL color string
                return `hsl(${{hue}}, 100%, 50%)`;
            }}

            // Define circle marker options
            var defaultDotMarkerOptions = {{
                radius: {dot_size},
                fillColor: "{dot_color}",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            }};

            // Add GeoJSON layer with dot markers
            var geojsonLayer = L.geoJSON({geojson_data}, {{
                pointToLayer: function (feature, latlng) {{
                    var dotMarkerOptions = defaultDotMarkerOptions;
                    if (feature.properties && feature.properties['{hue_column}'] !== undefined) {{
                        var hueValue = feature.properties['{hue_column}'];
                        min = Math.min(min, hueValue);
                        max = Math.max(max, hueValue);
                        dotMarkerOptions = {{
                            radius: {dot_size},
                            fillColor: getColor(hueValue, min, max),
                            color: "#000",
                            weight: 1,
                            opacity: 1,
                            fillOpacity: 0.8
                        }};
                    }}
                    return L.circleMarker(latlng, dotMarkerOptions);
                }},
                onEachFeature: function (feature, layer) {{
                    if (feature.properties && feature.properties.popupContent) {{
                        layer.bindPopup(feature.properties.popupContent);
                    }}
                }}
            }}).addTo(map);

            // Fit map to the bounds of the GeoJSON layer
            map.fitBounds(geojsonLayer.getBounds());

            // Add legend if hue_column is specified
            if ('{hue_column}' !== null) {{
                // Function to add legend
                var legend = L.control({{position: 'bottomleft'}});
                legend.onAdd = function (map) {{
                    var div = L.DomUtil.create('div', 'info legend');
                    div.innerHTML += '<div class="legend-title">Legend</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(240, 100%, 50%);"></span> 0 - 20%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(180, 100%, 50%);"></span> 20 - 40%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(120, 100%, 50%);"></span> 40 - 60%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(60, 100%, 50%);"></span> 60 - 80%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(0, 100%, 50%);"></span> 80 - 100%</div>';
                    return div;
                }};
                //legend.addTo(map);
            }}
        </script>
    </body>
    </html>
    """

    # Encode the HTML content in base64
    encoded_html4 = base64.b64encode(map_html4.encode()).decode()

    # Display the HTML content using an iframe
    return IFrame('data:text/html;base64,' + encoded_html4, width=800, height=600)
    
    
def plot_points_bubble(points, dot_size=5, dot_color="red", hue_column=None, weight = 0.3):
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(points, crs='EPSG:4326', geometry=gpd.points_from_xy([point['lon'] for point in points],
                                                                                [point['lat'] for point in points]))

    # Convert GeoDataFrame to GeoJSON
    geojson_data = gdf.to_crs(epsg=4326).to_json()

    # Compute the map center based on the points
    min_lon, min_lat, max_lon, max_lat = gdf.total_bounds
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    # Create the HTML content with Leaflet map and dynamic markers
    map_html4 = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Map</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <style>
            #mapid {{ height: 600px; }}
            .legend {{
                background-color: #fff;
                padding: 5px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
                position: absolute;
                bottom: 20px;
                left: 20px;
                z-index: 1000;
            }}
            .legend-title {{
                font-weight: bold;
                margin-bottom: 5px;
            }}
            .legend-item {{
                line-height: 18px;
                margin-bottom: 8px;
            }}
            .legend-item span {{
                display: inline-block;
                width: 15px;
                height: 15px;
                margin-right: 5px;
            }}
        </style>
    </head>
    <body>
        <div id="mapid"></div>
        <!-- Legend for color bar -->
        <div id="legend" class="legend">
            <div class="legend-title">Legend</div>
            <div class="legend-item"><span style="background-color: hsl(240, 100%, 50%);"></span> 0 - 20%</div>
            <div class="legend-item"><span style="background-color: hsl(180, 100%, 50%);"></span> 20 - 40%</div>
            <div class="legend-item"><span style="background-color: hsl(120, 100%, 50%);"></span> 40 - 60%</div>
            <div class="legend-item"><span style="background-color: hsl(60, 100%, 50%);"></span> 60 - 80%</div>
            <div class="legend-item"><span style="background-color: hsl(0, 100%, 50%);"></span> 80 - 100%</div>
        </div>
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script>
            var map = L.map('mapid').setView([{center_lat}, {center_lon}], 13);

            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }}).addTo(map);

            // Initialize min and max values for hue column
            var min = Infinity;
            var max = -Infinity;

            // Function to calculate color based on value
            function getColor(value, min, max) {{
                // Ensure value is within the range [min, max]
                value = Math.max(min, Math.min(max, value));
                
                // Scale value to a range between 0 and 1
                var scaledValue = (value - min) / (max - min);
                
                // Calculate hue based on the scaled value (0 to 240)
                var hue = (1 - scaledValue) * 240;
                
                // Construct HSL color string
                return `hsl(${{hue}}, 100%, 50%)`;
            }}
            
            // Function to calculate color based on value
            function getSize(value) {{
                // Ensure value is within the range [min, max]
                value = Math.max(min, Math.min(max, value));
                
                // Scale value to a range between 0 and 1
                var scaledValue = (value - min) / (max - min);
                
                // Calculate hue based on the scaled value (0 to 240)
                var hue = {weight}*scaledValue*100;
                return hue
            }}

            // Define circle marker options
            var defaultDotMarkerOptions = {{
                radius: {dot_size},
                fillColor: "{dot_color}",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            }};

            // Add GeoJSON layer with dot markers
            var geojsonLayer = L.geoJSON({geojson_data}, {{
                pointToLayer: function (feature, latlng) {{
                    var dotMarkerOptions = defaultDotMarkerOptions;
                    if (feature.properties && feature.properties['{hue_column}'] !== undefined) {{
                        var hueValue = feature.properties['{hue_column}'];
                        min = Math.min(min, hueValue);
                        max = Math.max(max, hueValue);
                        dotMarkerOptions = {{
                            radius: getSize(hueValue, min, max),
                            fillColor: getColor(hueValue, min, max),
                            color: "#000",
                            weight: 1,
                            opacity: 1,
                            fillOpacity: 0.8
                        }};
                    }}
                    return L.circleMarker(latlng, dotMarkerOptions);
                }},
                onEachFeature: function (feature, layer) {{
                    if (feature.properties && feature.properties.popupContent) {{
                        layer.bindPopup(feature.properties.popupContent);
                    }}
                }}
            }}).addTo(map);

            // Fit map to the bounds of the GeoJSON layer
            map.fitBounds(geojsonLayer.getBounds());

            // Add legend if hue_column is specified
            if ('{hue_column}' !== null) {{
                // Function to add legend
                var legend = L.control({{position: 'bottomleft'}});
                legend.onAdd = function (map) {{
                    var div = L.DomUtil.create('div', 'info legend');
                    div.innerHTML += '<div class="legend-title">Legend</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(240, 100%, 50%);"></span> 0 - 20%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(180, 100%, 50%);"></span> 20 - 40%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(120, 100%, 50%);"></span> 40 - 60%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(60, 100%, 50%);"></span> 60 - 80%</div>';
                    div.innerHTML += '<div class="legend-item"><span style="background-color: hsl(0, 100%, 50%);"></span> 80 - 100%</div>';
                    return div;
                }};
                //legend.addTo(map);
            }}
        </script>
    </body>
    </html>
    """

    # Encode the HTML content in base64
    encoded_html4 = base64.b64encode(map_html4.encode()).decode()

    # Display the HTML content using an iframe
    return IFrame('data:text/html;base64,' + encoded_html4, width=800, height=600)

def create_routing_map_html(start_latitude, start_longitude, end_latitude, end_longitude, min_lat, max_lat, min_lon, max_lon):
    # Construct the HTML content for the map
    map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>K-Means Clustering Map with Convex Hulls and Color Bar</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet-routing-machine/dist/leaflet-routing-machine.css" />
        <style>
            #mapid {{ height: 600px; }}
            .legend {{
                background-color: #fff;
                padding: 5px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
                position: absolute;
                bottom: 20px;
                left: 20px;
                z-index: 1000;
            }}
            .legend-title {{
                font-weight: bold;
                margin-bottom: 5px;
            }}
            .legend-item {{
                line-height: 18px;
                margin-bottom: 8px;
            }}
            .legend-item span {{
                display: inline-block;
                width: 15px;
                height: 15px;
                margin-right: 5px;
            }}
        </style>
    </head>
    <body>
        <div id="mapid"></div>

        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script src="https://unpkg.com/leaflet-routing-machine/dist/leaflet-routing-machine.js"></script>
        <script>
            var map = L.map('mapid').setView([{(min_lat + max_lat) / 2}, {(min_lon + max_lon) / 2}], 13);

            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }}).addTo(map);

            // Adding route between two points
            L.Routing.control({{
                waypoints: [
                    L.latLng({start_latitude}, {start_longitude}),
                    L.latLng({end_latitude}, {end_longitude})
                ],
                routeWhileDragging: true
            }}).addTo(map);
        </script>
    </body>
    </html>
    """
    
    # Encode HTML content in base64 for display in Jupyter Notebook
    encoded_html = base64.b64encode(map_html.encode()).decode()

    # Display the HTML content using an iframe
    return IFrame('data:text/html;base64,' + encoded_html, width=800, height=600)    