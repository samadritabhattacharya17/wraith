import math

def offset_gps(lat, lon, distance_m, bearing_deg):
    R = 6378137.0
    bearing = math.radians(bearing_deg)
    lat1 = math.radians(lat)
    lon1 = math.radians(lon)
    ang_dist = distance_m / R
    lat2 = math.asin(
        math.sin(lat1) * math.cos(ang_dist)
        + math.cos(lat1) * math.sin(ang_dist) * math.cos(bearing)
    )
    lon2 = lon1 + math.atan2(
        math.sin(bearing) * math.sin(ang_dist) * math.cos(lat1),
        math.cos(ang_dist) - math.sin(lat1) * math.sin(lat2),
    )
    return math.degrees(lat2), math.degrees(lon2)

if __name__ == "__main__":
    HOME_LAT = 47.397971057728974
    HOME_LON = 8.546163739800146
    lat, lon = offset_gps(HOME_LAT, HOME_LON, 50.0, 0.0)
    print(f"Target: {lat:.7f}, {lon:.7f}")
