import asyncio
import subprocess
from mavsdk import System

TARGET_LAT = 47.3982050
TARGET_LON = 8.5461637
REL_ALT_M = 5.0
DROP_ALT_M = 2        # descend to this AGL before dropping
ARRIVAL_TOL_M = 1.0
DETACH_TOPIC = "/payload/detach"

def haversine_flat_m(lat1, lon1, lat2, lon2):
    d_lat = (lat2 - lat1) * 111320
    d_lon = (lon2 - lon1) * 111320 * 0.6763
    return (d_lat ** 2 + d_lon ** 2) ** 0.5

async def wait_until_armed_and_home_set(drone):
    print("Waiting for global position + home lock...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("Position lock OK.")
            return

async def get_home_absolute_altitude(drone):
    async for pos in drone.telemetry.position():
        return pos.absolute_altitude_m

async def wait_reached(drone, target_lat, target_lon, tol=ARRIVAL_TOL_M):
    async for pos in drone.telemetry.position():
        dist = haversine_flat_m(pos.latitude_deg, pos.longitude_deg, target_lat, target_lon)
        if dist < tol:
            return
async def wait_altitude(drone, target_rel_alt, tol=0.1):
    async for pos in drone.telemetry.position():
        if abs(pos.relative_altitude_m - target_rel_alt) < tol:
            return

def release_payload():
    print(f"Publishing detach on {DETACH_TOPIC} ...")
    subprocess.run(["gz", "topic", "-t", DETACH_TOPIC, "-m", "gz.msgs.Empty", "-p", ""], check=False)

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")
    print("Waiting for drone connection...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected to drone.")
            break
    await wait_until_armed_and_home_set(drone)
    home_abs_alt = await get_home_absolute_altitude(drone)
    target_abs_alt = home_abs_alt + REL_ALT_M
    print("Arming...")
    await drone.action.arm()
    print(f"Taking off to {REL_ALT_M} m AGL...")
    await drone.action.set_takeoff_altitude(REL_ALT_M)
    await drone.action.takeoff()
    await asyncio.sleep(10)
    print(f"Flying to target {TARGET_LAT}, {TARGET_LON} @ {target_abs_alt:.1f} m AMSL...")
    await drone.action.goto_location(TARGET_LAT, TARGET_LON, target_abs_alt, 0)
    await wait_reached(drone, TARGET_LAT, TARGET_LON)
    print("Target reached. Descending to drop altitude...")
    drop_abs_alt = home_abs_alt + DROP_ALT_M
    await drone.action.goto_location(TARGET_LAT, TARGET_LON, drop_abs_alt, 0)
    await wait_altitude(drone, DROP_ALT_M)
    await asyncio.sleep(3)

    print("Releasing payload...")
    release_payload()          # <-- Add this line

    await asyncio.sleep(1)     # Optional but recommended

    print("Returning to launch...")
    await drone.action.return_to_launch()
    
if __name__ == "__main__":
    asyncio.run(run())
