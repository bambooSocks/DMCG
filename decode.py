import matplotlib.pyplot as plt
from math import log10
# from scipy import optimize
import numpy as np

# def reg (data):
# 	A = 3.51358227885507
# 	B = 0.220979790461345
	# return A*data+B

# def exponenial_func(x, a, b, c):
#     return a*np.exp(b*x)+c

# beg = 10
# rem = 85


# ref = [2688.01, 2686.05, 2686.69, 2686.67, 2686.63, 2687.16, 2686.79, 2686.55, 2685.49, 2686.26, 2686.31, 2686.1, 2689.78, 2685.6, 2686.7, 2687.89, 2687.36, 2686.43, 2686.61, 2686.0, 2687.3, 2687.69, 2686.91, 2686.71, 2685.32]
# ref = sum(ref)/len(ref)
od = []
# od_meas = []
# count = 0
# fitted = []
time = 0

with open("exp3_dev_od.txt","r") as inf, open("exp3_dev_od_tim.txt", "w") as outf:
	for line in inf:
		outf.write(str(round(time, 3))+" "+line)
		time += 1/12

		# print(-log10(float(line.split(" ")[0])/ref))
		# if count == 99:
		# 	count = 0
		# 	outf.write(str(reg(-log10(float(line.split(" ")[0])/ref)))+"\n")
		# od.append(float(line))

		# od_meas.append(float(line.split(" ")[1]))
		# outf.write(line.split(" ")[0]+"\n")
		# outf.write(str(-log10(float(line.split(" ")[0])/ref))+"\n")
		# outf.write(str(reg(-log10(float(line.split(" ")[0])/ref)))+"\n")
		# count += 1
	# outf.close()
	# print(od[beg:-rem])
	# params, params_covariance = optimize.curve_fit(exponenial_func, range(len(od)-rem-beg), od[beg:-rem], p0 = [0.243, 0.01, 0.2])

# for i in range(len(od)-rem-beg):
	# fitted.append(exponenial_func(i, params[0],params[1], params[2]))






# print(params)


# plt.plot(range(len(od)-rem-beg),od[beg:-rem], fitted)
# plt.show()