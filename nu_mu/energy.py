import ROOT as r
import numpy as np

energy_mu = np.loadtxt("ener_nu_mu.txt", usecols=[0], dtype=float)
En_mu = np.loadtxt("ener_nu_mu.txt", usecols=[1], dtype=int)

mu_b1 = []
mu_b2 = []
mu_b3 = []

nu_b1 = []      #Event id's in first bin
nu_b2 = []      #Event id's in second bin
nu_b3 = []      #Event id's in third bin

for i in range (len(energy_mu)):
    if (10. <  energy_mu[i] < 37.5):
        mu_b1.append(energy_mu[i])
        nu_b1.append(En_mu[i])
    if (37.5 < energy_mu[i] < 65.):
        mu_b2.append(energy_mu[i])
        nu_b2.append(En_mu[i])
    if (65. < energy_mu[i] < 150.):
        mu_b3.append(energy_mu[i])
        nu_b3.append(En_mu[i])

mean_b1 = np.mean(mu_b1)
mean_b2 = np.mean(mu_b2)
mean_b3 = np.mean(mu_b3)

xi_b1 = []
xi_b2 = []
xi_b3 = []

for bin in (mu_b1):
    xi_b1.append(mean_b1)
for bin in (mu_b2):
    xi_b2.append(mean_b2)
for bin in (mu_b3):
    xi_b3.append(mean_b3)

file=open('energy_nu_mu_output.txt', 'w')
file.write('Event ID' + '       ' + 'Energy' + '        ' + '<E> of the bin' + '\n')
for event in range(len(xi_b1)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b1[event], mu_b1[event], xi_b1[event]))
    file.write('\n')
for event in range(len(xi_b2)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b2[event], mu_b2[event], xi_b2[event]))
    file.write('\n')
for event in range(len(xi_b3)):
    file.write('{:5}    {:15}   {:15}'.format(nu_b3[event], mu_b3[event], xi_b3[event]))
    file.write('\n')
file.close()

#end of the script
