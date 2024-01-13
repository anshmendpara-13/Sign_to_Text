# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:10:19 2023

@author: Ansh
"""

import numpy as np
import matplotlib.pyplot as plt
a = 4
fm = 1000
tm = 1/fm
t = np.linspace(0, tm, num=1000)
x = a*np.cos(2 * np.pi * fm * t) 
fig1,ax1 = plt.subplots(1)
ax1 = plt.plot(t,x)
plt.title('Continuous Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

fs1 = 1.2*fm
ts1 = 1/fs1
t1 = np.arange(0,tm+ts1,ts1)
fig2,ax2 = plt.subplots(1)
ax2 = plt.stem(t1,x1)
plt.title('Sample Signal 1')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

fs2 = 2*fm
ts2 = 1/fs2
t2 = np.arange(0,tm+ts2,ts2)
x2 = a*np.cos(2 * np.pi * fm * t2) 
fig3,ax3 = plt.subplots(1)
ax3 = plt.stem(t2,x2)
plt.title('Sample Signal 2')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

fs3 = 8*fm
ts3 = 1/fs3
t3 = np.arange(0,tm+ts3,ts3)
x3 = a*np.cos(2 * np.pi * fm * t3) 
fig4,ax4 = plt.subplots(1)
ax4 = plt.stem(t3,x3)
plt.title('Sample Signal 3')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()


y = len(t)
z = len(x1)
xr = np.zeros(y)
for i in np.arange(z):    
    xr = x1[i]2*fm*ts1*np.sinc(2*fm(t-(i*ts1))) +xr
    
fig5,ax5 = plt.subplots(1)
ax5.plot(t,xr)
plt.grid()

z1 = len(x2)
xr = np.zeros(y)
for i in np.arange(z):
    xr = x2[i]2*fm*ts2*np.sinc(2*fm(t-(i*ts2))) +xr
    
fig6,ax6 = plt.subplots(1)
ax6.plot(t,xr)
plt.grid()

z = len(x3)
xr = np.zeros(y)
for i in np.arange(z):
    xr = x3[i]2*fm*ts3*np.sinc(2*fm(t-(i*ts3))) +xr
    
fig7,ax7 = plt.subplots(1)
ax7.plot(t,xr)
plt.grid()