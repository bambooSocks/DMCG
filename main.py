# imported modules
from machine import Pin
from machine import PWM
from machine import ADC
import time

# configuration of the pins
sensor = ADC(Pin(34))
led = PWM(Pin(13), freq=1000)
red = PWM(Pin(14), freq=1000)
blue = PWM(Pin(32), freq=1000)
green = PWM(Pin(15), freq=1000)
mode_btn = Pin(22, Pin.IN, Pin.PULL_UP) # closer button
action_btn = Pin(23, Pin.IN, Pin.PULL_UP) # further button

time_c = 0

sensor.atten(3)     # ATTN_11DB
led.freq(1000)
f = open("data.txt", "w")
f.write("Day is always the first!!!\n")
f.close()

def collect():
    led.duty(500)
    time.sleep(0.01)
    data = []
    for i in range(100): 
        data.append(sensor.read())
    f = open("data.txt", "a+")
    f.write(str(sum(data)/100)+"\n")
    f.close()
    time.sleep(0.01)
    led.duty(0)
    time_c = 0
    
def reference(): 
    led.duty(500)
    time.sleep(0.01)
    data = []
    for i in range(8): # 100? 
        data.append(sensor.read())
    f = open("data.txt", "a+")
    f.write(" R- "+str(sum(data)/8)+"\n") #only part changed. --> "R-"
    f.close()
    time.sleep(0.01)
    led.duty(0)    
    
mode = 0 # 0 - disabled, 1 - reference, 2 - measurement
meas_enabled = False

while True:
    if mode == 0:
        if mode_btn.value() == 0:
            mode = 1
            continue
        if action_btn.value() == 0:
            pass
            #nothing
        # LED red solid

    # reference setup mode
    elif mode == 1:
        if mode_btn.value() == 0:
            mode = 2
            continue
        if action_btn.value() == 0:
            reference()
            # LED blue blinking
        # LED blue solid

    # measurement mode
    elif mode == 2:
        if mode_btn.value() == 0:
            mode = 0
            meas_enabled = False
            time_c = 0
            continue
        if action_btn.value() == 0:
            meas_enabled = True
        if meas_enabled:
            if time_c >= 1000: #TODO: was 60000
                collect()
            time_c += 1
            # LED green blinking
        # LED green solid

    else:
        mode = 0

    time.sleep(0.001)
