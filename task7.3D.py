#The duty cycle for an LED (Light Emitting Diode) refers to the proportion of time it is on (lit) compared to the total time in a complete cycle. 
#It is typically expressed as a percentage and is a crucial parameter when using Pulse Width Modulation (PWM) to control the brightness of an LED.
""" The duty cycle determines how long the LED reLED_PULSEs on during each cycle. For example:
    0% duty cycle means the LED is off all the time.
    50% duty cycle means the LED is on for half the time and off for the other half, resulting in a 50% brightness level.
    100% duty cycle means the LED is on all the time (constant brightness).
""" 


### LIBRARIES INCLUDED ###
from time import sleep
from gpiozero import DistanceSensor, PWMOutputDevice

### LED PINS INITIALISATION ###
redLed = PWMOutputDevice(3)

### INSTANCE VARIABLE FOR ULTRASONIC SENSOR ###
ULTRASONIC = DistanceSensor(echo=5, trigger=7)
# Using GPIO 2,3 & 4 with pin no 3, 5 & 7 respectively

### Function for closing the window ###
def close():
    exit(1)

""" The "pulse" of an LED typically refers to the rapid on-off cycling of the LED's illumination using Pulse Width Modulation (PWM).
    It's the repeated switching of the LED between on and off states at a certain frequency and duty cycle to control its brightness.
    This pulsing is so fast that the human eye perceives it as a continuous level of brightness, allowing for dimming and control of the LED's output.
"""
# Function for controlling pulse of LED 
def LED_PULSE():
    running = True
    # Using try-catch block in the program
    try:
        redLed.on()
        
        while running:
            
            distance = ULTRASONIC.value # Variable for storing captured parameters
            print(f'Distance: {distance:1.2f} meters')
            
            # Duty cycle for redLed brightness
            brightness = round(1.0 - distance, 1)
            
            # Checking intensity level of LED
            if brightness < 0:
                brightness = 0.0
            
            # Set the redLed pulse
            redLed.value = brightness
            
            # Delay for 0.1 second
            sleep(0.1)
    
    except KeyboardInterrupt: # handling external errors
        pass
    
    finally:
        # Catching error and closing the data capturing process
        running = False
        ULTRASONIC.close()

if __name__ == '__LED_PULSE__':
    print("LED PULSE PWM")
    LED_PULSE()
    print("THANKS")
