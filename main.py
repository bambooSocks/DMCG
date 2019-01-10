# imported modules
from machine import Pin
from machine import PWM
from machine import ADC
import time

# configuration of the pins
sensor = ADC(Pin(34))
led = PWM(Pin(13))
button = Pin(12, Pin.IN, Pin.PULL_UP)
time_c = 0
itterator = 0

sensor.atten(3)     # ATTN_11DB
led.freq(1000)
f = open("data.txt", "w")
f.write("Day is always the first!!!\n")
f.close()

def collect():
    led.duty(1000)
    time.sleep(0.01)
    data = []
    for i in range(8): 
        data.append(sensor.read())
    data = str(sum(data)/8)
    f = open("data.txt", "a+")
    f.write(str(itterator)+" - "+str(data)+"\n")
    f.close()
    time.sleep(0.01)
    led.duty(0)
    time_c = 0

while True:
    if time_c >= 100: #TODO: was 6000
        collect()
        itterator += 1
    if button.value() == 0: 
        break 
    time.sleep(0.01)
    time_c += 1
    print("I am running")