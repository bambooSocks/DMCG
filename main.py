# imported modules
from machine import Pin
from machine import PWM
from machine import ADC
import time

# configuration of the pins
sensor = ADC(Pin(34))
led = PWM(Pin(13), freq=1000)
red = Pin(14, Pin.OUT)
green = Pin(32, Pin.OUT)
blue = Pin(15, Pin.OUT)
mode_btn = Pin(22, Pin.IN, Pin.PULL_UP) # closer button
action_btn = Pin(23, Pin.IN, Pin.PULL_UP) # further button

grState = 0
time_c = 0

sensor.atten(3)     # ATTN_11DB
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
red.value(1)
blue.value(1)
green.value(1)
led.duty(0)

while True:
    if mode == 0:
        print("mode0")
        if mode_btn.value() == 0:
            time.sleep(0.01)
            while mode_btn.value() == 0:
                pass
            red.value(1)
            mode = 1
            continue
        if action_btn.value() == 0:
            time.sleep(0.01)
            while action_btn.value() == 0:
                pass
            #nothing
        red.value(0)
    # reference setup mode
    elif mode == 1:
        print("mode1")
        if mode_btn.value() == 0:
            time.sleep(0.01)
            while mode_btn.value() == 0:
                pass
            mode = 2
            grState = 0
            blue.value(1)
            continue
        if action_btn.value() == 0:
            time.sleep(0.01)
            while action_btn.value() == 0:
                pass
            blue.value(1)
            reference()
        blue.value(0)
    # measurement mode
    elif mode == 2:
        print("mode2")
        if mode_btn.value() == 0:
            time.sleep(0.01)
            while mode_btn.value() == 0:
                pass
            mode = 0
            green.value(1)
            meas_enabled = False
            time_c = 0
            continue
        if action_btn.value() == 0:
            time.sleep(0.01)
            while action_btn.value() == 0:
                pass
            meas_enabled = True

        if meas_enabled:
            if time_c >= 60000: #TODO: was 60000
                collect()
                time_c = 0
            if time_c % 1000 == 0:
                if grState == 1:
                    grState = 0
                else:
                    grState = 1
            time_c += 1
        green.value(grState)
    else:
        mode = 0

    time.sleep(0.001)
