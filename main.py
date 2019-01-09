# imported modules
from machine import Pin
from machine import PWM
from machine import ADC

# configuration of the pins
sensor = ADC(Pin(34))
led = PWM(Pin(13))
button = Pin(12, Pin.IN)



