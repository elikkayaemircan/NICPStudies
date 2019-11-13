import ROOT as r
import numpy as np

x_mu = np.loadtxt("bjor_nu_mu.txt", usecols=[0], dtype=float)
En_mu = np.loadtxt("bjor_nu_mu.txt", usecols=[1], dtype=int)

mu_b1 = []
mu_b2 = []
mu_b3 = []
mu_b4 = []
mu_b5 = []
mu_b6 = []
mu_b7 = []

nu_b1 = []      #Event id's in first bin
nu_b2 = []      #Event id's in second bin
nu_b3 = []      #Event id's in third bin
nu_b4 = []      #Event id's in fourth bin
nu_b5 = []      #Event id's in fifth bin
nu_b6 = []      #Event id's in sixth bin
nu_b7 = []      #Event id's in seventh bin

for i in range (len(x_mu)):
    if (0. <  x_mu[i] < 5e-3):
        mu_b1.append(x_mu[i])
        nu_b1.append(En_mu[i])
    if (5e-3 < x_mu[i] < 5e-2):
        mu_b2.append(x_mu[i])
        nu_b2.append(En_mu[i])
    if (5e-2 < x_mu[i] < .1):
        mu_b3.append(x_mu[i])
        nu_b3.append(En_mu[i])
    if (.1 < x_mu[i] < 0.16):
        mu_b4.append(x_mu[i])
        nu_b4.append(En_mu[i])
    if (.16 < x_mu[i] < .26):
        mu_b5.append(x_mu[i])
        nu_b5.append(En_mu[i])
    if (.26 < x_mu[i] < .65):
        mu_b6.append(x_mu[i])
        nu_b6.append(En_mu[i])
    if (.65 < x_mu[i] < 1.):
        mu_b7.append(x_mu[i])
        nu_b7.append(En_mu[i])

mean_b1 = np.mean(mu_b1)
mean_b2 = np.mean(mu_b2)
mean_b3 = np.mean(mu_b3)
mean_b4 = np.mean(mu_b4)
mean_b5 = np.mean(mu_b5)
mean_b6 = np.mean(mu_b6)
mean_b7 = np.mean(mu_b7)

xi_b1 = []
xi_b2 = []
xi_b3 = []
xi_b4 = []
xi_b5 = []
xi_b6 = []
xi_b7 = []

for bin in (mu_b1):
    xi_b1.append(mean_b1)
for bin in (mu_b2):
    xi_b2.append(mean_b2)
for bin in (mu_b3):
    xi_b3.append(mean_b3)
for bin in (mu_b4):
    xi_b4.append(mean_b4)
for bin in (mu_b5):
    xi_b5.append(mean_b5)
for bin in (mu_b6):
    xi_b6.append(mean_b6)
for bin in (mu_b7):
    xi_b7.append(mean_b7)

file=open('bjorken_nu_mu_output.txt', 'w')
file.write('Event ID' + '       ' + 'Bjorken x' + '     ' + '<x> of the bin' + '\n')
for event in range(len(xi_b1)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b1[event], mu_b1[event], xi_b1[event]))
    file.write('\n')
for event in range(len(xi_b2)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b2[event], mu_b2[event], xi_b2[event]))
    file.write('\n')
for event in range(len(xi_b3)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b3[event], mu_b3[event], xi_b3[event]))
    file.write('\n')
for event in range(len(xi_b4)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b4[event], mu_b4[event], xi_b4[event]))
    file.write('\n')
for event in range(len(xi_b5)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b5[event], mu_b5[event], xi_b5[event]))
    file.write('\n')
for event in range(len(xi_b6)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b6[event], mu_b6[event], xi_b6[event]))
    file.write('\n')
for event in range(len(xi_b7)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b7[event], mu_b7[event], xi_b7[event]))
    file.write('\n')
file.close()

#end of the script
