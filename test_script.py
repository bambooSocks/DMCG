from machine import Pin
from machine import ADC
from machine import PWM
import time

led = PWM(Pin(13))
sen = ADC(Pin(34))

led.freq(1000)
sen.atten(3)

# f = open("data.txt", "w")
# f.write("Day is always the first!!!\n")
# f.write("PWM - ADC\n")
# f.close()


while 1:
	led.duty(650)
	data = []
	for _ in range(100):
		data.append(sen.read())
	data = sum(data)/100
	# f = open("data.txt", "a+")
	# f.write(str(data)+"\n")
	# f.close()
	print(data)
	time.sleep(0.1)


