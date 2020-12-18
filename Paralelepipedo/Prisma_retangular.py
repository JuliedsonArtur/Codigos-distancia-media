#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:26:13 2020

@author: juliedson
"""
import numpy as np
import time

# Define o tempo de início
start_time = time.time()

# O retângulo se encontra todo no 1° octante (x, y e z positivos).
# Dimensões do paralelepípedo:
x_max = 30
y_max = 10.34
z_max = 70

# Ponto de partida P = (1, 1, 1), logo x0 = 1
x0 = 1

# Definimos os passos em x0, y0 e z0 com valores próprios:
passo_x = 3
passo_y = 1
passo_z = 7

# Contadores da soma das distâncias (d) e da quantidade (n)
d = n = 0

# Let the game begin!
print('\033[1;32m\nBora então! \033[m', '\n')

while x0 < x_max:
    y0 = 1
    while y0 < y_max:
        z0 = 1
        while z0 < z_max:
            phi = 0
            for theta in range(0, 181, 18):
                if theta == 0:
                    d += z_max - z0
                    n += 1
                    #print(f'\033[0;35mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {z_max - z0}')
                elif theta == 180:
                    d += z0  
                    n += 1
                    #print(f'\033[35mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {z0}')
                else:
                    phi = 0
                    while True:
                        r = 0
                        while True:
                            r += 0.1
                            x = x0 + r*(np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180))
                            y = y0 + r*(np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180))
                            z = z0 + r*np.cos(theta*np.pi/180)
                            if (x <= 0 or x >= x_max or y <= 0 or
                            y >= y_max or z <= 0 or z >= z_max):
                                #print(f'\033[mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {r:.1f}')
                                d += r
                                n += 1
                                break
                        phi += 1/np.sin(theta*np.pi/180)
                        if phi >= 360:
                            break
            #print("...")
            z0 += passo_z
        y0 += passo_y
        print("\033[1;31m...\033[m")
    x0 += passo_x
    print('\033[1;34m...\033[m')

print(f'\033[1;32m\nTerminei todos os {n} pontos requeridos! :D\033[m\n')
print(f'No total, a soma das distância foi: \033[1;32m{d:.3f}\033[m')
print(f'A média foi de \033[1;32m{d/n:.3f} mm\033[m\n')

print()
delta_t = (time.time() - start_time)
if delta_t//60 > 0:
    sec = 60*(delta_t/60 - delta_t//60)
    print(f"\033[1;34m--- {delta_t//60} minutos e {sec:.3f} segundos ---\033[m")
else:
    print(f'\033[1;34m--- {delta_t:.3f} segundos ---\033[m')

################################################################################
#
# Note que:
#
#   --> Para Theta = 90, os passos em Phi são de 1°, como esperado!
#
#   --> Para 10 pontos em cada lado da peça, theta com passos de 18°
#       o programa demorou cerca de ~ 50 min para calcular
#       com r = 0.1, obteve n = 2280000 pontos, d = 22893761.0 
#       e uma média de d = 10.041 mm.
#
#   --> Com 10 pontos para cada lado, temos no total 1000 pontos no
#       interior da peça, com theta dando passos de 18°, temos um
#       total de 2280*1000 pontos, o que coincide com n calculado
#
#   --> Para um único ponto e theta com passos de 18°, temos n = 2280 (~ 14.171 s)
#
#   --> Para um único ponto e theta com passos de 1°, temos n = 41344 (~ 3 min s)
#          
#
################################################################################
