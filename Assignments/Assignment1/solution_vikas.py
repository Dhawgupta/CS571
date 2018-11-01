m = int(input("picks: "))
n = int(input("flips: "))
theta = float(input("p: "))
theta_1 = float(input("p1: "))
theta_2 = float(input("p2: "))
# theta_1_init =
iterations = int(input("iterations: "))
import random
import math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

tol = 1e-6
iteration = 0
tot_c1_H = 0
tot_c1_T = 0
tot_c2_H = 0
tot_c2_T = 0
a = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    if random.random() < theta:
        for j in range(n):
            if random.random() < theta_1:
                a[i][j] = 1
            else:
                a[i][j] = 0
    else:
        for j in range(n):
            if random.random() < theta_2:
                a[i][j] = 1
            else:
                a[i][j] = 0
print("observations=", a)
thetas = [] # list of theta
theta1s = [] # list of theta1
theta2s = [] # list of theta2

while iteration < iterations:
    thetas.append(theta)
    theta1s.append(theta_1)
    theta2s.append(theta_2)
    # E step
    temp_p = 0
    for k in a:
        len_k = len(k)
        H = np.sum(k)
        T = len_k - H
        lik_c1 = stats.binom.pmf(H, len_k, theta_1)
        lik_c2 = stats.binom.pmf(H, len_k, theta_2)
        wt_c1 = lik_c1 / (lik_c1 + lik_c2)
        temp_p += wt_c1
        wt_c2 = lik_c2 / (lik_c1 + lik_c2)
        # increment counts
        tot_c1_H += wt_c1 * H
        tot_c1_T += wt_c1 * T
        tot_c2_H += wt_c2 * H

        tot_c2_T += wt_c2 * T
    new_theta = temp_p / len(a)

    # M step
    new_theta_1 = tot_c1_H / (tot_c1_H + tot_c2_T)
    new_theta_2 = tot_c2_H / (tot_c2_H + tot_c2_T)
    delta_change1 = new_theta_1 - theta_1
    delta_change2 = new_theta_2 - theta_2
    if delta_change1 < tol and delta_change2 < tol:
        break
    else:
        theta = new_theta
        theta_1 = new_theta_1
        theta_2 = new_theta_2
        iteration += 1
        print(theta_1)
        print(theta_2)
print("opt_theta_1=", theta_1)
print("opt_theta_2=", theta_2)
plt.subplot(3,1,1)
plt.plot(range(len(theta1s)), theta1s)
# plt.plot(range(len(theta1s)), )
plt.subplot(3,1,2)
plt.plot(range(len(theta2s)), theta2s)

plt.subplot(3,1,3)
plt.plot(range(len(thetas)), thetas)
plt.title("Plot for p : {}, p1 : {}, p2 : {} ".format(thetas[0],theta1s[0], theta2s[0]))
plt.show()
plt.savefig("plot.png")







