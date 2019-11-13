import ROOT as r
import numpy as np

x_mu_bar = np.loadtxt("bjor_nu_mu_bar.txt", usecols=[0], dtype=float)
En_mu_bar = np.loadtxt("bjor_nu_mu_bar.txt", usecols=[1], dtype=int)

mu_bar_b1 = []
mu_bar_b2 = []
mu_bar_b3 = []
mu_bar_b4 = []
mu_bar_b5 = []
mu_bar_b6 = []
mu_bar_b7 = []

nu_bar_b1 = []      #Event id's in first bin
nu_bar_b2 = []      #Event id's in second bin
nu_bar_b3 = []      #Event id's in third bin
nu_bar_b4 = []      #Event id's in fourth bin
nu_bar_b5 = []      #Event id's in fifth bin
nu_bar_b6 = []      #Event id's in sixth bin
nu_bar_b7 = []      #Event id's in seventh bin

ne_bar_b1 = 0
ne_bar_b2 = 0
ne_bar_b3 = 0
ne_bar_b4 = 0
ne_bar_b5 = 0
ne_bar_b6 = 0
ne_bar_b7 = 0

for j in range (len(x_mu_bar)):
    if (0. < x_mu_bar[j] < 5e-3):
        mu_bar_b1.append(x_mu_bar[j])
        nu_bar_b1.append(En_mu_bar[j])
        ne_bar_b1 += 1
    if (5e-3 < x_mu_bar[j] < 3.8e-2):
        mu_bar_b2.append(x_mu_bar[j])
        nu_bar_b2.append(En_mu_bar[j])
        ne_bar_b2 += 1
    if (3.8e-2 < x_mu_bar[j] < 7e-2):
        mu_bar_b3.append(x_mu_bar[j])
        nu_bar_b3.append(En_mu_bar[j])
        ne_bar_b3 += 1
    if (7e-2 < x_mu_bar[j] < .113):
        mu_bar_b4.append(x_mu_bar[j])
        nu_bar_b4.append(En_mu_bar[j])
        ne_bar_b4 += 1
    if (.113 < x_mu_bar[j] < .18):
        mu_bar_b5.append(x_mu_bar[j])
        nu_bar_b5.append(En_mu_bar[j])
        ne_bar_b5 += 1
    if (.18 < x_mu_bar[j] < .6):
        mu_bar_b6.append(x_mu_bar[j])
        nu_bar_b6.append(En_mu_bar[j])
        ne_bar_b6 += 1
    if (.6 < x_mu_bar[j] < 1.):
        mu_bar_b7.append(x_mu_bar[j])
        nu_bar_b7.append(En_mu_bar[j])
        ne_bar_b7 += 1

mean_bar_b1 = np.mean(mu_bar_b1)
mean_bar_b2 = np.mean(mu_bar_b2)
mean_bar_b3 = np.mean(mu_bar_b3)
mean_bar_b4 = np.mean(mu_bar_b4)
mean_bar_b5 = np.mean(mu_bar_b5)
mean_bar_b6 = np.mean(mu_bar_b6)
mean_bar_b7 = np.mean(mu_bar_b7)

xi_bar_b1 = []
xi_bar_b2 = []
xi_bar_b3 = []
xi_bar_b4 = []
xi_bar_b5 = []
xi_bar_b6 = []
xi_bar_b7 = []

for bin in (mu_bar_b1):
    xi_bar_b1.append(mean_bar_b1)
for bin in (mu_bar_b2):
    xi_bar_b2.append(mean_bar_b2)
for bin in (mu_bar_b3):
    xi_bar_b3.append(mean_bar_b3)
for bin in (mu_bar_b4):
    xi_bar_b4.append(mean_bar_b4)
for bin in (mu_bar_b5):
    xi_bar_b5.append(mean_bar_b5)
for bin in (mu_bar_b6):
    xi_bar_b6.append(mean_bar_b6)
for bin in (mu_bar_b7):
    xi_bar_b7.append(mean_bar_b7)

file=open('bjorken_nu_mu_bar_output.txt', 'w')
file.write('Event ID' + '       ' + 'Bjorken x' + '     ' + '<x> of the bin' + '    ' + '# of events in that bin' + '\n')
for event in range(len(xi_bar_b1)):
	file.write('{:5}    {:15}   {:15}	{:10}'.format(nu_bar_b1[event], mu_bar_b1[event], xi_bar_b1[event], ne_bar_b1))
    file.write('\n')
for event in range(len(xi_bar_b2)):
    file.write('{:5}    {:15}   {:15}	{:10}'.format(nu_bar_b2[event], mu_bar_b2[event], xi_bar_b2[event], ne_bar_b2))
    file.write('\n')
for event in range(len(xi_bar_b3)):
    file.write('{:5}    {:15}   {:15}	{:10}'.format(nu_bar_b3[event], mu_bar_b3[event], xi_bar_b3[event], ne_bar_b3))
    file.write('\n')
for event in range(len(xi_bar_b4)):
    file.write('{:5}	{:15}	{:15}	{:10}'.format(nu_bar_b4[event], mu_bar_b4[event], xi_bar_b4[event], ne_bar_b4))
    file.write('\n')
for event in range(len(xi_bar_b5)):
    file.write('{:5}	{:15}	{:15}	{:10}'.format(nu_bar_b5[event], mu_bar_b5[event], xi_bar_b5[event], ne_bar_b5))
    file.write('\n')
for event in range(len(xi_bar_b6)):
    file.write('{:5}	{:15}	{:15}	{:10}'.format(nu_bar_b6[event], mu_bar_b6[event], xi_bar_b6[event], ne_bar_b6))
    file.write('\n')
for event in range(len(xi_bar_b7)):
    file.write('{:5}	{:15}	{:15}	{:10}'.format(nu_bar_b7[event], mu_bar_b7[event], xi_bar_b7[event], ne_bar_b7))
    file.write('\n')
file.close()

#end of the script
