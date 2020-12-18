#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:42:15 2020
Memória de São Davi, Rei e Profeta
@author: juliedson
"""
# Esse tenta uma expressão analítica para d'. 
#
# Code for a cylinder with a mirrored upper face.

import time
import numpy as np
from math import degrees, sqrt

start_time = time.time()

# Dimensions:
#      R = 76.2 mm
#      H = 24.5 mm
# Setting the dimension for radius and height:
z_max = 24.5
R = 76.2

# Setting the counters for summed distance (d) and the number of points (n):
d = n = 0

# The x and y values goes from -R to R and it's needed that x² + y² < R²,
# i. e., the point (x, y) must belong to R radius disk.
# However the  height coordinate is restrained in (0, z_max):
z0 = 1

#Soma incremento delta para theta<theta limite por conta da refleão na fac sup
# 行きましょうか？

while z0 < z_max:
    y0 = -R
    while True:
        y0+= 20
        print()
        if y0 < R:
            x0 = -R
            while True:
                x0 += 20
                if x0 < R:
                    print(f'For P = ({x0:.2f}, {y0:.2f}, {z0:.2f}):', end=' ')
                    if x0**2 + y0**2 < R**2:               # To remove |x| > R
                        for theta in range(0, 181, 18):
                            phi = 0
                            if theta == 0:
                                d += z_max - z0
                                n += 1
                                print("\033[1;36mOk!\033[m")
                                #print(f'\033[0;35mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {z_max - z0}')    
                            elif theta == 180:
                                d += z0
                                n += 1
                                #print(f'\033[0;35mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {z0}')
                            else:
                                while True:
                                    r = 0
                                    while True:
                                        #print(r)
                                        x = x0 + r*(np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180))
                                        y = y0 + r*(np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180))
                                        z = z0 + r*np.cos(theta*np.pi/180)
                                        raio = x**2 + y**2
                                        if (z <= 0 or z >= z_max or raio >= R**2):
                                            delta_z = z_max - z0
                                            theta_limit = np.arctan((R - sqrt(x0**2 + y0**2))/delta_z)                                            
                                            if theta < degrees(theta_limit):
                                                d += (R - sqrt(x0**2 + y0**2))/np.sin(theta*np.pi/180)
                                                n += 1
                                                break
                                            else:
                                                d += r
                                                n +=1
                                                break
                                        r = round(r, 2) + 0.1   # Tive que usar o round por conta do problema de representação decimal
                                    phi += 1/np.sin(theta*np.pi/180)
                                    if phi >= 360:
                                        break
                    else:
                        print("\033[1;31mNothing\033[m")
                else:
                    break
        else:
            break
    z0 += 5
    print()

print(f'\033[1;32m\nI finished all {n} points! :D\n\033[m')
print(f'The sum of all distances is \033[1;32m{d:.2f} mm.\033[m')
print(f'\nThe mean thickness is \033[1;32m{d/n:.3f} mm.\033[m')

print()
delta_t = (time.time() - start_time)
if delta_t//60 > 0:
    sec = 60*(delta_t/60 - delta_t//60)
    print(f"\033[1;34m--- {delta_t//60} minutes e {sec:.3f} seconds ---\033[m")
else:
    print(f'\033[1;34m--- {delta_t:.3f} seconds ---\033[m')

# Método "analítico"
# passos x, y = 20, passo z = 5, theta 18 e phi correto
# 490200 pontos, d = 18816865.99 mm e resultado 38.386 mm em 
# 33.15 minutos. São 215 pontos dentro da peça, 215*2280 = 490200 = n

