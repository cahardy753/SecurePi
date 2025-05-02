from signal import pause
import time
import pigpio
import paho.mqtt.client as mqtt #import MQTT library

#define constants for MQTT
TOPIC = 'iws3/servo'
PORT = 1883
QOS = 0
KEEPALIVE = 60

# Set hostname for MQTT broker
BROKER = 'iot.cs.calvin.edu'

# Indicates whether broker requires authentication.
# Set to True for authenticaion, set to False for anonymous brokers
BROKER_AUTHENTICATION = True

USERNAME = 'cs326'   # broker authentication username (if required)
PASSWORD = 'piot'   # broker authentication password (if required)

# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, flags, reason_code, properties):
  if reason_code == 0:
    print(f'Connected to {BROKER} successful.')
  else:
    print(f'Connection to {BROKER} failed. Return code={rc}')

# Callback when client receives a message from the broker
    #Not used?

# Setup MQTT client and callbacks
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

if BROKER_AUTHENTICATION:
  client.username_pw_set(USERNAME, password=PASSWORD)
client.on_connect = on_connect

# Connect to MQTT broker and subscribe to the iws3/servo topic
client.connect(BROKER, PORT, KEEPALIVE)
client.subscribe(TOPIC, qos=QOS)

client.loop_start()

PWM = 18

class State_Machine:
  def  __init__(self, pi):
    #copy pigpio object to self.pi
    self.pi = pi

        # Configure GPIO pins
    for pin in [16, 8, 7, 25]: 
      self.pi.set_pull_up_down(pin, pigpio.PUD_UP)  #set pullup resistor on GPIO pins
      self.pi.set_glitch_filter(pin, 1000)   # Set glitch filter  #set glitch filter

    self.states = {'SERVO_CLOSE', 'SERVO_OPEN'}
    self.state = 'SERVO_CLOSE'

    #pi.set_servo_pulsewidth(PWM,1100)

  def close_button_callback(self, gpio, level, tick):
    self.state = 'SERVO_CLOSE'
    print("sent message: servo close/0")
    #self.pi.set_servo_pulsewidth(PWM,1100)
    client.publish(TOPIC, 0)

  def open_button_callback(self, gpio, level, tick):
    self.state = 'SERVO_OPEN'
    print("sent message: servo open/1")
    client.publish(TOPIC, 1)
    
# connect to the pigpio service (which must be running)
pi = pigpio.pi()
if not pi.connected:
  exit(0)

pi.set_PWM_frequency(PWM,50); # Set PWM frequency to 50Hz

sm = State_Machine(pi) # Instantiate state machine


# Callbacks
cb1 = pi.callback(25, pigpio.FALLING_EDGE, sm.close_button_callback)
cb2 = pi.callback(7, pigpio.FALLING_EDGE, sm.open_button_callback)
#cb3 = pi.callback(8, pigpio.FALLING_EDGE, sm.right_button_callback)
#cb4 = pi.callback(16, pigpio.FALLING_EDGE, sm.stop_button_callback)

try:
  pause()
except KeyboardInterrupt:
  pi.stop()
  print("exiting")
