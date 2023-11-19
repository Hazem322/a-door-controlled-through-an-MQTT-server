import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
GPIO.setwarnings(False)
# Configuration of GPIO broches
servo_pin = 24 # Use the GPIO pin number (BCM 24)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

# Configuration of PWM
pwm_frequency = 50 # PWM frequency in Hz
pwm = GPIO.PWM(servo_pin, pwm_frequency)

# Configuration MQTT
mqtt_broker = "test.mosquitto.org" # Address of broker MQTT
mqtt_topic = "servo/control" # Use MQTT to control the servo motor
mqtt_client = mqtt.Client()

#Function to define the angle of the servo motor
def set_angle(angle):
   duty_cycle = (angle / 18.0) + 2.5 # Calculation of rapport cycle for the angle donné
   pwm.ChangeDutyCycle(duty_cycle)
   time.sleep(1) # Attend 1 second to bring the servo motor into position

# Callback from MQTT connection
def on_connect(client, userdata, flags, rc):
   client.subscribe(mqtt_topic)

# Callback for receiving MQTT message
def on_message(client, userdata, msg):
   try:
     angle = float(msg.payload)
     if 0 <= angle <= 180:
       set_angle(angle)
     else:
       print("The angle should be closed at 0 and 180 degrees.")
   exceptValueError:
     print("MQTT Message invalid: angle non numérique")

# Configure MQTT callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

#Connexion with broker MQTT
mqtt_client.connect(mqtt_broker, 1883, 60)

try:
   pwm.start(0) # Delete the PWM from 0 (to the next position)
   mqtt_client.loop_start() # Delete the MQTT boucle
   while True:
     pass. pass
except KeyboardInterrupt:
   pass. pass
finally:
   pwm.stop()
   GPIO.cleanup()"
