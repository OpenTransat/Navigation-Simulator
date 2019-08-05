SIMULATE_ON_BOAT = False #use serial port from the controller

SERIAL_PORT = "COM6"
SERIAL_BAUD = 115200
SERIAL_TIMEOUT = 5

SIM_MOVE_INTERVAL = 1
SIM_PRINT_INTERVAL = 10
SIM_MAX_SPEED = 2000000.0
#SIM_RUDDER_RESPONSE = 0.00005
SIM_RUDDER_RESPONSE = 0.0001

TACKMODE_DIRECTLY = 0
TACKMODE_ADJ_POS = 1
TACKMODE_ADJ_NEG = 2
TACKMODE_MAXDEV_POS = 3
TACKMODE_MAXDEV_NEG = 4

MENU = 40
W = 1500.0
H = 750.0
MAXW = 10*W
MAXH = 10*H

BOAT_LENGTH = 50
BOAT_BOW = 20
BOAT_WIDTH = 10
RUDDER_LENGTH = 20
SAIL_LENGTH = 40
FLAP_LENGTH = 20
DOT_RADIUS = 2
WIND_COMPASS = 100
HEADING_ARROW = 100

HEADING_OK_LIMIT = 10.0
RUDDER_RESPONSE = 0.00005
RUDDER_COEFF = 40.0
RUDDER_MIN_ANGLE = -30
RUDDER_MAX_ANGLE = 35

tackmode_str = ['TACKMODE_DIRECTLY', 'TACKMODE_ADJ_POS', 'TACKMODE_ADJ_NEG', 'TACKMODE_MAXDEV_POS', 'TACKMODE_MAXDEV_NEG']

FLAP_NORMAL = 10.0
FLAP_MAX = 15.0
TACK_SAIL_CRITICAL_ANGLE = FLAP_MAX/2
FLAP_ITERATION = 0.1

R_MEAN = 6371000.0

MAXDEV = 500000
MAXDEV_OK_FACTOR = 0.75
MAXDEV_OK = MAXDEV * MAXDEV_OK_FACTOR

WAYPOINT0 = 46.913520, -52.998886
WAYPOINT1 = 48.0, -13.0

tackmode = TACKMODE_DIRECTLY

gps_lat, gps_lng = WAYPOINT0
gps_lat_prev, gps_lng_prev = gps_lat, gps_lng

trueHeading = 45.0
MAX_SPEED = 2000000.0
GHOST_DISTANCE = 500000.0
trueWind = 0.0

dt = 0.001
dt_refresh = 4*dt

ghostPoint = 0.0, 0.0
closestPoint = 0.0, 0.0
ghostHeading = 0.0
ghostHeading_instant = 0.0
goHeading = 0.0
error = 0.0
sail_angle = 0.0

crossTrack = 0.0
pathAngle = 0.0

rudder = 0.0
flap = FLAP_NORMAL
flap_final = flap

x_prev = 0.0
y_prev = 0.0

speed = 0.0

paused = False

ghostHeading_initialized = False

sim_active = False;

adjAngle1 = 0.0 #global only for debugging
adjAngle2 = 0.0 #global only for debugging

c_boat, c_sail, c_rudder, c_flap = None, None, None, None
c_compass1, c_compass2, c_compass3, c_compass4, \
c_closestPoint, c_ghostPoint, c_ghostHeading, c_windDir, c_goHeading, c_adjHeading1, c_adjHeading2 \
    = None, None, None, None, None, None, None, None, None, None, None

ser = None

startchar = ''

sim_nextWaypoint = -1
mux = -1
isBehindPath = 0
magDec = 0.0

