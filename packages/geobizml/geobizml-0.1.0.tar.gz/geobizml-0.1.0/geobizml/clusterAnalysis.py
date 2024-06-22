import base64
import json
import geopandas as gpd
import numpy as np
from sklearn.cluster import KMeans
from IPython.display import IFrame
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, davies_bouldin_score
import warnings
import os

def plot_elbow(X, max_clusters=10):
    # Suppress specific warnings
    warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")
    warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

    # Set environment variable to avoid the memory leak warning
    os.environ['OMP_NUM_THREADS'] = '1'
    sse = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        sse.append(kmeans.inertia_)
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_clusters + 1), sse, marker='o')
    plt.title('Elbow Plot')
    plt.xlabel('Number of clusters')
    plt.ylabel('SSE')
    plt.grid(True)
    plt.show()
    
def plot_scree(X, max_clusters=10):
    total_var = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        total_var.append(np.var(kmeans.cluster_centers_))
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_clusters + 1), total_var, marker='o')
    plt.title('Scree Plot')
    plt.xlabel('Number of clusters')
    plt.ylabel('Total Variance')
    plt.grid(True)
    plt.show()
    
def plot_silhouette(X, max_clusters=10):
    silhouette_avg = []
    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        cluster_labels = kmeans.fit_predict(X)
        silhouette_avg.append(silhouette_score(X, cluster_labels))
    plt.figure(figsize=(10, 6))
    plt.plot(range(2, max_clusters + 1), silhouette_avg, marker='o')
    plt.title('Silhouette Plot')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silhouette Score')
    plt.grid(True)
    plt.show()
    
def plot_davies_bouldin(X, max_clusters=10):
    db_score = []
    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        cluster_labels = kmeans.fit_predict(X)
        db_score.append(davies_bouldin_score(X, cluster_labels))
    plt.figure(figsize=(10, 6))
    plt.plot(range(2, max_clusters + 1), db_score, marker='o')
    plt.title('Davies-Bouldin Index Plot')
    plt.xlabel('Number of clusters')
    plt.ylabel('Davies-Bouldin Index')
    plt.grid(True)
    plt.show()

# Function to compute convex hulls and create GeoDataFrame with hulls
def create_convex_hulls(points_df):
    clusters = {}
    for cluster_id, cluster_points in points_df.groupby('cluster'):
        if len(cluster_points) > 2:  # Require at least 3 points for convex hull
            # Convert GeoSeries to list of Shapely Points
            points_list = [Point(xy) for xy in zip(cluster_points.geometry.x, cluster_points.geometry.y)]
            # Compute convex hull using scipy.spatial.ConvexHull
            hull = ConvexHull([(p.x, p.y) for p in points_list])
            hull_points = [points_list[vertice] for vertice in hull.vertices]
            cluster_polygon = Polygon([[p.x, p.y] for p in hull_points])
            clusters[cluster_id] = cluster_polygon
    hulls_df = gpd.GeoDataFrame(geometry=list(clusters.values()), index=list(clusters.keys()), crs='EPSG:4326')
    return hulls_df

def generate_clustering_map_html(points, n_clusters, radius=3, color='red'):
    # Perform clustering
    # Create a GeoDataFrame
    # Create a GeoDataFrame from points
    gdf = gpd.GeoDataFrame(points, crs='EPSG:4326', geometry=gpd.points_from_xy(points['lon'], points['lat']))

    # Convert GeoDataFrame to GeoJSON
    geojson_data = gdf.to_crs(epsg=4326).to_json()

    # Compute the map center based on the points
    min_lon, min_lat, max_lon, max_lat = gdf.total_bounds
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    # Perform clustering
    X = np.array(gdf.geometry.apply(lambda p: (p.x, p.y)).tolist())
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    gdf['cluster'] = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_

    # Prepare GeoJSON for centroids
    centroid_features = []
    for idx, centroid in enumerate(centroids):
        centroid_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [centroid[0], centroid[1]]
            },
            "properties": {
                "cluster": idx
            }
        }
        centroid_features.append(centroid_feature)

    centroid_geojson = {
        "type": "FeatureCollection",
        "features": centroid_features
    }

    # Create GeoDataFrame for convex hulls
    convex_hulls_df = gdf.groupby('cluster')['geometry'].apply(lambda x: x.unary_union.convex_hull).reset_index()
    gdf = gpd.GeoDataFrame(convex_hulls_df, geometry='geometry')
    convex_hulls_geojson = gdf.to_json()

    # Prepare HTML template for Leaflet map
    map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>K-Means Clustering Map with Convex Hulls</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <style>
            #mapid {{ height: 600px; }}
        </style>
    </head>
    <body>
        <div id="mapid"></div>
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script>
            var map = L.map('mapid').setView([{(min_lat + max_lat) / 2}, {(min_lon + max_lon) / 2}], 13);

            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }}).addTo(map);

            // Add GeoJSON layer for convex hulls
            var convexHullLayer = L.geoJSON({convex_hulls_geojson}, {{
                style: function (feature) {{
                    return {{
                        fillColor: '#ADD8E6',
                        weight: 1,
                        opacity: 1,
                        color: 'blue',
                        fillOpacity: 0.6
                    }};
                }},
                onEachFeature: function (feature, layer) {{
                    layer.bindPopup('Cluster ' + feature.properties.index);
                }}
            }}).addTo(map);

            // Add GeoJSON layer for centroids
            var centroidLayer = L.geoJSON({json.dumps(centroid_geojson)}, {{
                pointToLayer: function (feature, latlng) {{
                    return L.marker(latlng, {{
                        icon: L.divIcon({{
                            html: '<div style="background-color: #333; color: #fff; border-radius: 50%; width: 12px; height: 12px;"></div>',
                            className: 'centroid-marker',
                            iconSize: [12, 12],
                            iconAnchor: [6, 6]
                        }})
                    }});
                }},
                onEachFeature: function (feature, layer) {{
                    layer.bindPopup('Centroid for Cluster ' + feature.properties.cluster);
                }}
            }}).addTo(map);

            // Function to calculate color based on value
            function getColor(value) {{
                var hue = (1 - value / 100) * 240;
                return `hsl(${{hue}}, 100%, 50%)`;
            }}

            // Add GeoJSON layer with color-coded markers
            var geojsonLayer = L.geoJSON({geojson_data}, {{
                pointToLayer: function (feature, latlng) {{
                    var value = feature.properties.value;
                    var circleOptions = {{
                        radius: {radius},
                        fillColor: '{color}',
                        color: 'blue',
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.8
                    }};
                    return L.circleMarker(latlng, circleOptions);
                }},
                onEachFeature: function (feature, layer) {{
                    if (feature.properties && feature.properties.popupContent) {{
                        layer.bindPopup(feature.properties.popupContent);
                    }}
                }}
            }}).addTo(map);

            // Fit map to the bounds of the convex hulls layer
            map.fitBounds(convexHullLayer.getBounds());
        </script>
    </body>
    </html>
    """

    # Encode HTML content in base64 for display in Jupyter Notebook
    encoded_html = base64.b64encode(map_html.encode()).decode()

    # Return the HTML content as an IFrame
    return IFrame('data:text/html;base64,' + encoded_html, width=800, height=600)


