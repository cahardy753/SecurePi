# Isaac Schaafsma (iws3), Cliff Hardy (cah43)
# This program controls a microservo using MQTT
# and inserts data into a SQL database

import paho.mqtt.client as mqtt
import pigpio
import sys
import urllib.parse as up
import time
import psycopg2

# Constants
TOPIC = 'iws3/servo'
PORT = 1883
QOS = 0
KEEPALIVE = 60
status = 0
TIMEZONE = "America/Detroit"
URI = '******' # Cloud database URI
TABLE = 'doorlog'

# setup servo and intialize position
PWM = 18
pi = pigpio.pi()
pi.set_PWM_frequency(PWM, 50)
pi.set_servo_pulsewidth(PWM, 1000)

# Set hostname for MQTT broker
BROKER = '*****'

# Indicates whether broker requires authentication.
# Set to True for authenticaion, set to False for anonymous brokers
BROKER_AUTHENTICATION = True

# Note: these constants must be set if broker requires authentication
USERNAME = '*******'   # broker authentication username (if required)
PASSWORD = '*******'   # broker authentication password (if required)

# log door event
def log_door_event(door_status):
    try:
      sqlcmd = f"INSERT INTO {TABLE} (status) VALUES ('{door_status}')"
      cursor.execute(sqlcmd)
      print(sqlcmd)
      sqlcmd = "delete from doorlog where datetime < NOW()-INTERVAL '7 days'"
      cursor.execute(sqlcmd)
      conn.commit()
    except Exception as e:
      print(f"Database error: {e}")
        

# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, flags, reason_code, properties):
  if reason_code == 0:
    print(f'Connected to {BROKER} successful.')
  else:
    print(f'Connection to {BROKER} failed. Return code={rc}')


# Callback when client receives a message from the broker
# Use messages to control position of servo
def on_message(client, data, msg):
  global status
  message = msg.payload.decode('utf-8')
  if msg.topic == TOPIC:
    if message == '1':
      if status == 1:
        print('Already Open')
      else:
        status = 1
        print('New state is: Open')
        log_door_event('Open')
        for pulse in range(1000, 2001, 50):  # Step by 50 for smooth motion
          pi.set_servo_pulsewidth(PWM, pulse)
          time.sleep(0.1)  # Small delay for gradual movement
    elif message == '0':
      if status == 0:
        print('Already Closed')
      else:
        status = 0
        print('New state is: Close')
        log_door_event('Close')
        for pulse in range(2000, 999, -50):  # Step by 50 for smooth motion
          pi.set_servo_pulsewidth(PWM, pulse)
          time.sleep(0.1)  # Small delay for gradual movement

# Setup MQTT client and callbacks
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

if BROKER_AUTHENTICATION:
  client.username_pw_set(USERNAME, password=PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker and subscribe to the servo topic
client.connect(BROKER, PORT, KEEPALIVE)
client.subscribe(TOPIC, qos=QOS)
# Connect to the SQL cloud database
up.uses_netloc.append("postgres")
uri = up.urlparse(URI)
conn = psycopg2.connect(database=uri.path[1:], user=uri.username, password=uri.password, host=uri.hostname, port=uri.port )

# Open a cursor to perform database operations
cursor = conn.cursor()

# Set the local timezone for this session
cursor.execute(f'SET TIME ZONE "{TIMEZONE}"')
conn.commit()

try:
  client.loop_forever()
except KeyboardInterrupt:
  client.disconnect()
  print('Done')
