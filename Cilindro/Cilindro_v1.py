#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:47:01 2020

Festa de Nossa Senhora de Guadalupe
Padroeira da América Latina

@author: juliedson
"""

import numpy as np

# Definindo as dimensões da peça cilíndrica de raio e altura:
z_max = 3
R = 5

# Ponto inicial em (0, 0, 1):
x0 = y0 = 0
z0 = 1

d = n = 0

for theta in range(0, 181, 90):
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
            phi += 45#/np.sin(theta*np.pi/180)
            if phi >= 360:
                break
                #print("...")
            
print(f'\033[1;32mTerminei todos os {n} pontos requeridos! :D\033[m\n')

print(d/n)

# Arrumar um jeito de varrer todo o disco inclusive com coordenadas negativas para x e y