from machine import Pin
from machine import ADC
from machine import PWM
import time

led = PWM(Pin(13), freq=78000)
sen = ADC(Pin(34))

sen.atten(3)

def reg(data)
	A = -0.000884515926984929
	B = 2.20532387481873
	return A*data+B

while 1:
	led.duty(800)
	data = []
	for _ in range(100):
		data.append(sen.read())
	data = sum(data)/100
	print(data, "OD -", reg(data))


	# for i in range(100):
	# 	led.duty(i*10)
	# 	data = []
	# 	for _ in range(100):
	# 		data.append(sen.read())
	# 	data = sum(data)/100
	# 	print(i, str(data)+', ')
	# 	time.sleep(0.1)
	# led.duty(0)
	# time.sleep(0.01)