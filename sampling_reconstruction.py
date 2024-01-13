# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:13:16 2023

@author: Ansh
"""

# exp2 : study of sampling and reconstruction 
# aim : to study sampling theorem for various sampling rate and reconstruction of the sampled signal 

import numpy as np
import matplotlib.pyplot as plt

a = 4
fm = 1000
tm = 1/fm

t = np.linspace(0, tm, num=100)
x = a*np.cos(2 * np.pi * fm * t)
 
fig,ax = plt.subplots(1)
ax = plt.plot(t, x)
plt.title('Continuous Signal')
plt.xlabel('Time (Second)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


fs1 = 1.2*fm
ts1 = 1/fs1

t1 = np.arange(0, tm+ts1, ts1)
x1 = a*np.cos(2 * np.pi * fm * t1) 

fig1,ax1 = plt.subplots(1)
ax1 = plt.stem(t1, x1)
plt.title('fs = 1.2fm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fs2 = 2*fm
ts2 = 1/fs2

t2 = np.arange(0, tm+ts2, ts2)
x2 = a*np.cos(2 * np.pi * fm * t2) 

fig2,ax2 = plt.subplots(1)
ax2 = plt.stem(t2, x2)
plt.title('fs = 2fm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fs3 = 8*fm
ts3 = 1/fs3

t3 = np.arange(0, tm+ts3, ts3)
x3 = a*np.cos(2 * np.pi * fm * t3) 

fig3,ax3 = plt.subplots(1)
ax3 = plt.stem(t3, x3)
plt.title('fs = 8fm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


    
yt = len(t)
yx1 = len(x1)  # number of sample signal

xr1 = np.zeros(yt)
for i in np.arange(yx1):
    xr1 += x1[i]*2*fm*ts1*np.sinc(2*fm*(t-i*ts1))
    
fig6,ax6 = plt.subplots(1)
ax6 = plt.plot(t, xr1)
plt.title('reconstructed at fs = 1.2fm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
    


yt = len(t)
yx2 = len(x2)  # number of sample signal

xr2 = np.zeros(yt)
for i in np.arange(yx2):
    xr2 += x2[i]*2*fm*ts2*np.sinc(2*fm*(t-i*ts2))
    
fig5,ax5 = plt.subplots(1)
ax5 = plt.plot(t, xr2)
plt.title('reconstructed at fs = 2fm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

    


yt = len(t)
yx3 = len(x3)  # number of sample signal

xr3 = np.zeros(yt)
for i in np.arange(yx3):
    xr3 += x3[i]*2*fm*ts3*np.sinc(2*fm*(t-i*ts3))
    
fig4,ax4 = plt.subplots(1)
ax3 = plt.plot(t, xr3)
plt.title('reconstructed at fs = 8fm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()



