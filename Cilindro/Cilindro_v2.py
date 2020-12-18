#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:54:46 2020

@author: juliedson
"""
# Esse código varia o x

import numpy as np
import time

start_time = time.time()

# Definindo as dimensões da peça cilíndrica de raio e altura:
z_max = 3
R = 5

# Ponto inicial em (0, 0, 1):
x0 = -R
y0 = 0
z0 = 1

d = n = 0

while abs(x0) <= R:
    x0 += 1
    print(f'\033[1;31m\nPara x0 = {x0}\033[m')
    if x0**2 + y0**2 < R**2:
        for theta in range(0, 181, 45):
            phi = 0
            if theta == 0:
                d += z_max - z0
                n += 1
                print(f'\033[0;35mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {z_max - z0}')    
            elif theta == 180:
                d += z0
                n += 1
                print(f'\033[0;35mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {z0}')
            else:
                while True:
                    r = 0
                    while True:
                        #print(r)
                        x = x0 + r*(np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180))
                        y = y0 + r*(np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180))
                        z = z0 + r*np.cos(theta*np.pi/180)
                        raio = x**2 + y**2
                        if ( z <= 0 or z >= z_max or raio >= R**2 ):
                            print(f'\033[mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {r:.1f}')
                            d += r
                            n += 1
                            break
                        r = round(r, 2) + 0.1   # Tive que usar o round por conta do problema de representação decimal
                    phi += 36#/np.sin(theta*np.pi/180)
                    if phi >= 360:
                        break
                        #print("...")


print(f'\033[1;32m\nTerminei todos os {n} pontos requeridos! :D\n')
print(f'No total, a soma de todas as distâncias é {d:.2f} mm.')
print(f'\nA espessura média deu {d/n:.3f} mm.')

print()
delta_t = (time.time() - start_time)
if delta_t//60 > 0:
    print(f"\033[1;34m--- {delta_t//60} minutos e {60*(delta_t/60 - delta_t//60):.3f} segundos ---\033[m")
else:
    print(f'\033[1;34m--- {delta_t:.3f} segundos ---\033[m')