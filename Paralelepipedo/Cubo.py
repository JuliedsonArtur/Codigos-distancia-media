#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:54:19 2020

@author: juliedson
"""
import numpy as np
import time

# Define o tempo de início
start_time = time.time()

# Dimensões da caixa:
x_max = y_max = z_max = 10

# Ponto de partida P = (1, 1, 1), logo x0 = 1
x0 = 1

# Definimos os passos em x0, y0 e z0 como 1 (de 1 em 1 u.m.):
passo_x = passo_y = passo_z = 1

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
            for theta in range(0, 181, 45):
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
                            r += 0.05
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
#            print("...")
            z0 += passo_z
        y0 += passo_y
        print("\033[1;31m...\033[m")
    x0 += passo_x
    print('\033[1;34m...\033[m')
#combinacoes = (8 + 2)*(x_max//5)*(y_max//3)*(z_max//2)

print(f'\033[1;32mTerminei todos os {n} pontos requeridos! :D\033[m\n')
print(f'No total, a soma das distância foi: \033[1;32m{d:.3f}\033[m')
print(f'A média foi de \033[1;32m{d/n:.3f} mm\033[m\n')

print()
delta_t = (time.time() - start_time)
if delta_t//60 > 0:
    print(f"\033[1;34m--- {delta_t//60} minutos e {60*(delta_t/60 - delta_t//60):.3f} segundos ---\033[m")
else:
    print(f'\033[1;34m--- {delta_t:.3f} segundos ---\033[m')
################################################################################
#
# Note que:
#
#   --> Para passos maiores (~5), o programa leva ~ 1 min para calcular;
#   --> Para Theta = 90, os passos em Phi são de 1°, como esperado!
#   --> Para passos iguais de 1, o programa demorou ~ 13.913 mins para calcular
#       com r = 0.05, obteve 635.688 pontos e uma média de d = 4.930 mm.
#
# O que falta:    
#   --> Fazer as dimensões corretas para a peça;
#
################################################################################
