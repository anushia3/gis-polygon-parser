import geopandas as gpd
from shapely.geometry import LineString


def export_shapefile(
    vertices,
    output_path="survey_geometry.shp"
):

    line = LineString(vertices)

    gdf = gpd.GeoDataFrame(
        {"id": [1]},
        geometry=[line]
    )

    gdf.to_file(output_path)

    print(
        f"Shapefile saved to {output_path}"
    )