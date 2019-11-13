import ROOT as r
import numpy as np

y_mu = np.loadtxt("inel_nu_mu.txt", usecols=[0], dtype=float)
En_mu = np.loadtxt("inel_nu_mu.txt", usecols=[1], dtype=int)

mu_b1 = []
mu_b2 = []
mu_b3 = []

nu_b1 = []      #Event id's in first bin
nu_b2 = []      #Event id's in second bin
nu_b3 = []      #Event id's in third bin

for i in range (len(y_mu)):
    if (0. <  y_mu[i] < .53):
        mu_b1.append(y_mu[i])
        nu_b1.append(En_mu[i])
    if (.53 < y_mu[i] < .75):
        mu_b2.append(y_mu[i])
        nu_b2.append(En_mu[i])
    if (.75 < y_mu[i] < 1.):
        mu_b3.append(y_mu[i])
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

file=open('inelasticity_nu_mu_output.txt', 'w')
file.write('Event ID' + '       ' + 'Inelasticity y' + '     ' + '<y> of the bin' + '\n')
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
