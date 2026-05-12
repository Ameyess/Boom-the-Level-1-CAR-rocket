"""
BoomBoom – RocketPy Simulation
Converted from BoomBoomL1.ork (OpenRocket 24.12)
Motor: AeroTech HP-H195NT (real thrust curve from .eng file)
Launch site: Launch Canada – Timmins, Ontario (Highway 144 / Mattagami First Nation lands)

Usage:
    pip install rocketpy
    python BoomBoom_rocketpy.py

Make sure AeroTech_HP-H195NT.eng is in the same folder as this script.
"""

import os
from rocketpy import Environment, SolidMotor, Rocket, Flight

# ---------------------------------------------------------------------------
# 1. Environment
#    Launch Canada launch field, Timmins, Ontario
#    ~15 km north of Timmins on Hwy 144 near Mattagami First Nation
#
#    ⚠️  Replace LAT/LON with the exact GPS waypoint from your event docs
#        if you have it — these are the best public approximation.
# ---------------------------------------------------------------------------
LAUNCH_LAT = 48.58          # ~15 km north of Timmins toward Mattagami
LAUNCH_LON = -81.37         # Hwy 144 corridor
LAUNCH_ELEVATION = 295      # metres above sea level (Timmins area average)

env = Environment(
    latitude=LAUNCH_LAT,
    longitude=LAUNCH_LON,
    elevation=LAUNCH_ELEVATION,
)
env.set_atmospheric_model(type="standard_atmosphere")

# ---------------------------------------------------------------------------
# 2. Motor – AeroTech HP-H195NT
#
#   From .eng header:  H195NBT  29mm  203.2mm  delay=10s
#                      propellant mass = 0.115 kg
#                      total mass      = 0.197 kg
#   Burn time: ~1.169 s (last non-zero thrust point)
# ---------------------------------------------------------------------------
ENG_FILE = os.path.join(os.path.dirname(__file__), "AeroTech_HP-H195NT.eng")

motor = SolidMotor(
    thrust_source=ENG_FILE,
    dry_mass=0.197 - 0.115,        # casing = 0.082 kg
    dry_inertia=(0.001, 0.001, 0.0001),
    nozzle_radius=0.010,
    grain_number=1,
    grain_density=1750,
    grain_outer_radius=0.0135,
    grain_initial_inner_radius=0.006,
    grain_initial_height=0.2032,
    grain_separation=0,
    grains_center_of_mass_position=0.1016,
    center_of_dry_mass_position=0.1016,
    nozzle_position=0.0,
    burn_time=1.169,
    throat_radius=0.007,
    interpolation_method="linear",
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

# ---------------------------------------------------------------------------
# 3. Rocket – BoomBoom
#
#   From .ork:
#     Body tube  : Estes BT-55, 0.4572 m, radius 0.0168275 m
#     Nose cone  : ogive, 0.10 m
#     Fins       : 3× trapezoidal, root 0.09 m, tip 0.06 m, sweep 0.04 m, span 0.03 m
#     Parachute  : 24-in Estes nylon, ejection at apogee
#     Total mass : 0.442 kg → airframe ≈ 0.245 kg
# ---------------------------------------------------------------------------
boomboom = Rocket(
    radius=0.0168275,
    mass=0.245,
    inertia=(0.08, 0.08, 0.001),
    power_off_drag=0.45,
    power_on_drag=0.45,
    center_of_mass_without_motor=0.224,
    coordinate_system_orientation="tail_to_nose",
)

boomboom.add_nose(
    length=0.100,
    kind="ogive",
    position=0.4572 + 0.100,
)

boomboom.add_trapezoidal_fins(
    n=3,
    root_chord=0.090,
    tip_chord=0.060,
    span=0.030,
    position=0.0,
    sweep_length=0.040,
    cant_angle=0,
)

boomboom.add_motor(
    motor=motor,
    position=0.0,
)

# 24-inch Estes nylon parachute — Cd_s = 1.5 × π × (0.3048)²
CHUTE_RADIUS = 0.6096 / 2
CD_S = 1.5 * 3.14159 * CHUTE_RADIUS**2

boomboom.add_parachute(
    name="MainChute_24in",
    cd_s=CD_S,
    trigger="apogee",
    sampling_rate=105,
    lag=0.0,
    noise=(0, 8.3, 0.5),
)

# ---------------------------------------------------------------------------
# 4. Flight
# ---------------------------------------------------------------------------
flight = Flight(
    rocket=boomboom,
    environment=env,
    rail_length=1.0,
    inclination=90,
    heading=0,
    max_time=400,
    terminate_on_apogee=False,
)

# ---------------------------------------------------------------------------
# 5. Results
# ---------------------------------------------------------------------------
print("\n========== BoomBoom Flight Summary ==========")
print(f"  Launch site      : Timmins, ON ({LAUNCH_LAT}°N, {LAUNCH_LON}°E, {LAUNCH_ELEVATION} m)")
print(f"  Apogee altitude  : {flight.apogee:.1f} m  ({flight.apogee * 3.281:.0f} ft)")
print(f"  Max velocity     : {flight.max_speed:.1f} m/s  (Mach {flight.max_speed / 340:.3f})")
print(f"  Max acceleration : {flight.max_acceleration:.1f} m/s²")
print(f"  Time to apogee   : {flight.apogee_time:.2f} s")
print(f"  Flight time      : {flight.t_final:.1f} s")
print(f"  Rail exit speed  : {flight.out_of_rail_velocity:.1f} m/s")
print("=============================================\n")

# ---------------------------------------------------------------------------
# 6. Google Earth KML export
# ---------------------------------------------------------------------------
flight.export_kml(
    file_name="BoomBoom_flight_Timmins.kml",
    time_step=0.1,          # one GPS point every 0.1 s → smooth arc
    extrude=True,           # draws vertical lines to ground — shows altitude clearly
    altitude_mode="absolute",
)
print("✅  Google Earth file saved → BoomBoom_flight_Timmins.kml")
print("    Open in Google Earth Pro to view the 3D trajectory over Timmins.")

# Uncomment for plots:
# flight.plots.trajectory_3d()
# flight.plots.linear_kinematics_data()
# flight.prints.flight_details()