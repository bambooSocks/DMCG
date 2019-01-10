# imported modules
from machine import Pin
from machine import PWM
from machine import ADC

# configuration of the pins
sensor = ADC(Pin(34))
led = PWM(Pin(13))
button = Pin(12, Pin.IN)

def data_collection(): 
    time_c = 0 
    while time_c>= 6000:
        collect()
        if button.value() == 0: 
            break 
        else: 
            time.sleep(0.1)
            time_c += 1 
   
def collect():
    led.value(1)
    time.sleep(0.5)
    data = []
    for i in range(8): 
        data.append(ADC.read())
    data = sum(data)/8
    data = str(data)
    f = open(data.txt, "w")
    f.write(data)
    f.close()
    time.sleep(0.5)
    led.value(0)
    time_c = 0 
