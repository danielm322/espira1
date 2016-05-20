import numpy as np

mp = 3.205e-6
g = 9.8
L = 0.154
Ie = 1.02
le = 0.02
u0 = 4e-7*np.pi
Is = 1.995
dmp = 0.128e-6
dL = 0.001
dIe = 0.0212
dle = 0.001
dIs = 0.001

dn = np.sqrt((((g*L/(Ie*le*u0*Is))**2)*(dmp**2))+(((mp*g/(Ie*le*u0*Is))**2)*(dL**2))+((((mp*g*L)/(le*u0*Is*(Ie**2)))**2)*(dIe**2))+((((mp*g*L)/(Ie*u0*Is*(le**2)))**2)*(dle**2))+((((mp*g*L)/(le*u0*Ie*(Is**2)))**2)*(dIs**2)))
      
print dn
