from matplotlib import pyplot as plt
import math

y1 = []
y3 = []
od1 = []
od3 = []
dy1od = []
dy3od = []
hour1 = []
hour3 = []

with open("exp1_dev_od_t.txt","r") as inf1, open("exp3_dev_od_t.txt","r") as inf3:
	for line in inf1:
		hour1.append(float(line.split(' ')[0]))
		hour1 = hour1[0:175]
		od1.append(float(line.split(' ')[1]))
		od1 = od1[0:len(hour1)]

	for line in inf3:
		hour3.append(float(line.split(' ')[0]))
		hour3 = hour3[0:175]
		od3.append(float(line.split(' ')[1]))
		od3 = od3[0:len(hour3)]

for i in range(len(hour1)):
	x = i/12
	dy1od.append((5.17517069321637e-6*x**4-0.135450274605890e-3*x**3+0.179831680401571e-2*x**2+0.253433003932461e-3*x-0.175766165571670e-2)/od1[i])
	y1.append(1.03503413864327e-6*x**5-0.338625686514724e-4*x**4+0.599438934671904e-3*x**3+0.126716501966231e-3*x**2-0.175766165571670e-2*x+0.765012204504709e-1)
	
for i in range(len(hour3)):
	x = i/12
	dy3od.append((-0.196056692591518e-4*x**4+0.414762810297757e-3*x**3-0.293929262412322e-2*x**2+0.190963903929091e-1*x-0.138835920300355e-1)/od3[i])
	y3.append(-3.92113385183037e-6*x**5+0.103690702574439e-3*x**4-0.979764208041074e-3*x**3+0.954819519645455e-2*x**2-0.138835920300355e-1*x+.120028709683196)

reg_data = []
for i in range(2):
	reg_data.append(3.51358227885507*i+.220979790461345)

ax = [-math.log10(2027.76/2686.76), -math.log10(316.88/2686.76)]
ay = [0.5, 4.62]


fig = plt.figure(dpi=300)
fig.suptitle('Growth rate µ of both strains', fontsize=14, fontweight='bold')
p = fig.add_subplot(111)
p.grid()

p.set_xlabel("time (hours)")
p.set_ylabel("Growth rate (cell split per hour)")
# p.set_ylabel("Absorbance (OD)")
# p.set_xlabel("Device absorbsion (OD)")
# p.set_ylabel("Spectrophotometer absorbsion (OD)")


# p.plot(hour1, y1, 'r', label="Polynomial fit")
# p.plot(hour1, od1, 'c', label="Measured data")
# p.plot(hour3, y3, 'r', label="Polynomial fit")
# p.plot(hour3, od3, 'c', label="Measured data")
# p.plot(range(2), reg_data, label="Calibration regression line")
# p.plot(ax, ay, label="Two point approximation")
p.plot(hour1[0:175], dy1od[0:175], 'g', label="Mead yeast")
p.plot(hour3[0:150], dy3od[0:150], 'y', label="Empire Ale yeast")


y1max = max(dy1od)
y2max = max(dy3od)
p.plot([hour1[0], hour1[174]], [y1max, y1max], 'r', label="max μ for Mead yeast: {0:.2f}".format(y1max))
p.plot([hour1[0], hour1[174]], [y2max, y2max], 'b', label="max μ for Empire Ale yeast: {0:.2f}".format(y2max))

p.legend()
plt.savefig("gr.png")
# plt.show()