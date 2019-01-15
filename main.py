# imported modules
from machine import Pin
from machine import PWM
from machine import ADC
import time

# configuration of the pins
sensor = ADC(Pin(34))
led = PWM(Pin(13), freq=78000)
red = Pin(14, Pin.OUT)
green = Pin(32, Pin.OUT)
blue = Pin(15, Pin.OUT)
mode_btn = Pin(22, Pin.IN, Pin.PULL_UP) # closer button
action_btn = Pin(23, Pin.IN, Pin.PULL_UP) # further button

# global variables
grState = 0
time_c = 0
mode = 0 # 0 - disabled, 1 - reference, 2 - measurement
meas_enabled = False

# initial settings of the ADC and LEDs
sensor.atten(3)     # ATTN_11DB
red.value(1)
blue.value(1)
green.value(1)
led.duty(0)

##
## @brief      Regression function
##
## @param      data  the data point to be evaluated
##
## @return     returns the evaluated value of the given datapoint
##
def reg(data):
    # monday data
    # A = -0.000884515926984929
    # B = 2.20532387481873
    # first tuesday data
    # A = -0.000829282657611729
    # B = 2.15723101966890
    # second tuesday data
    A = -0.000868473622808155
    B = 2.18445659325840
    return A*data+B

##
## @brief      A function used to collect data
##
def collect():
    led.duty(700)
    time.sleep(0.01)
    data = []
    for i in range(100):
        data.append(sensor.read())
    data = sum(data)/100
    f = open("data.txt", "a+")
    f.write(str(data)+" "+str(reg(data))+"\n")
    f.close()
    print("Raw:", data, "OD:", reg(data))
    led.duty(0)
    
##
## @brief      A function used to collect the reference data
##
def reference(): 
    led.duty(700)
    time.sleep(0.01)
    data = []
    for i in range(100):
        data.append(sensor.read())
    data = sum(data)/100
    f = open("data.txt", "a+")
    f.write("R- "+str(data)+" "+str(reg(data))+"\n")
    f.close()
    print("Raw:", data, "OD:", reg(data))
    led.duty(0)    

while True:
    # check for the current mode
    if mode == 0:
        # if the mode button was clicked debounce it, turn the red LED off and switch to reference setup (blanking) mode
        if mode_btn.value() == 0:
            time.sleep(0.01)
            while mode_btn.value() == 0:
                pass
            red.value(1)
            mode = 1
            continue
        # if the action button was clicked debounce it and do no other action
        if action_btn.value() == 0:
            time.sleep(0.01)
            while action_btn.value() == 0:
                pass
            #nothing
        red.value(0)
    # reference setup mode
    elif mode == 1:
        # if the mode button was clicked debounce it, turn the blue LED off, the green state on and switch to measurement mode
        if mode_btn.value() == 0:
            time.sleep(0.01)
            while mode_btn.value() == 0:
                pass
            mode = 2
            grState = 0
            blue.value(1)
            continue
        # if the action button was clicked debounce it and run the reference setup while blinking the LED
        if action_btn.value() == 0:
            time.sleep(0.01)
            while action_btn.value() == 0:
                pass
            print("saving reference")
            blue.value(1)
            reference()
        blue.value(0)
    # measurement mode
    elif mode == 2:
        # if the mode button was clicked debounce it, turn the green LED off, disable the measurement, clear the time counter and switch to disabled mode
        if mode_btn.value() == 0:
            time.sleep(0.01)
            while mode_btn.value() == 0:
                pass
            mode = 0
            green.value(1)
            meas_enabled = False
            time_c = 0
            continue
        # if the action button was clicked debounce it and enable the measurement
        if action_btn.value() == 0:
            time.sleep(0.01)
            while action_btn.value() == 0:
                pass
            print("starting measurement")
            meas_enabled = True

        # if enabled check for the value overpassing the 60000 counter and change the green state every second
        if meas_enabled:
            if time_c >= 300000:
                print("Collecting...")
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

    # delay in order to not overload the MCU
    time.sleep(0.001)
