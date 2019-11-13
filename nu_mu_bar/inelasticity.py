import ROOT as r
import numpy as np

y_mu_bar = np.loadtxt("inel_nu_mu_bar.txt", usecols=[0], dtype=float)
En_mu_bar = np.loadtxt("inel_nu_mu_bar.txt", usecols=[1], dtype=int)

mu_bar_b1 = []
mu_bar_b2 = []
mu_bar_b3 = []

nu_bar_b1 = []      #Event id's in first bin
nu_bar_b2 = []      #Event id's in second bin
nu_bar_b3 = []      #Event id's in third bin

for j in range (len(y_mu_bar)):
    if (0. < y_mu_bar[j] < .55):
        mu_bar_b1.append(y_mu_bar[j])
        nu_bar_b1.append(En_mu_bar[j])
    if (.55 < y_mu_bar[j] < .77):
        mu_bar_b2.append(y_mu_bar[j])
        nu_bar_b2.append(En_mu_bar[j])
    if (.77 < y_mu_bar[j] < 1.):
        mu_bar_b3.append(y_mu_bar[j])
        nu_bar_b3.append(En_mu_bar[j])

mean_bar_b1 = np.mean(mu_bar_b1)
mean_bar_b2 = np.mean(mu_bar_b2)
mean_bar_b3 = np.mean(mu_bar_b3)

xi_bar_b1 = []
xi_bar_b2 = []
xi_bar_b3 = []

for bin in (mu_bar_b1):
    xi_bar_b1.append(mean_bar_b1)
for bin in (mu_bar_b2):
    xi_bar_b2.append(mean_bar_b2)
for bin in (mu_bar_b3):
    xi_bar_b3.append(mean_bar_b3)

file=open('inelasticity_nu_mu_bar_output.txt', 'w')
file.write('Event ID' + '       ' + 'Inelasticity y' + '     ' + '<y> of the bin' + '\n')
for event in range(len(xi_bar_b1)):
    file.write('{:5}    {:15}   {:15}'.format(nu_bar_b1[event], mu_bar_b1[event], xi_bar_b1[event]))
    file.write('\n')
for event in range(len(xi_bar_b2)):
    file.write('{:5}    {:15}   {:15}'.format(nu_bar_b2[event], mu_bar_b2[event], xi_bar_b2[event]))
    file.write('\n')
for event in range(len(xi_bar_b3)):
    file.write('{:5}    {:15}   {:15}'.format(nu_bar_b3[event], mu_bar_b3[event], xi_bar_b3[event]))
    file.write('\n')
file.close()

#end of the script
