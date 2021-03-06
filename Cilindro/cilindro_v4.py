#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:48:26 2020

@author: juliedson
"""

# Essa versão varia x, y e z, também não toma pontos de nenhuma das faces

import time
import numpy as np

start_time = time.time()

# As dimensões da peça são:
#      R = 76.2 mm
#      H = 24.5 mm
# Definindo as dimensões da peça cilíndrica de raio e altura:
z_max = 24.5
R = 76.2

# Definindo os contadores:
d = n = 0

# Os valores de x e y vão de -R até R de modo que a combinação das coordenadas
# não ultrapasse o limite da circunferência de raio R
# Já a altura z varia de (0, z_max):
z0 = 1

# Vamos lá!

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
                    print(f'Para P = ({x0:.2f}, {y0:.2f}, {z0:.2f}):', end=' ')
                    if x0**2 + y0**2 < R**2:                    # Essa condição remove |x| > R
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
                                            #print(f'\033[mPara P = ({x0}, {y0}, {z0}), Theta = {theta}, phi = {phi:.2f} e r = {r:.1f}')
                                            d += r
                                            n += 1
                                            break
                                        r = round(r, 2) + 0.1   # Tive que usar o round por conta do problema de representação decimal
                                    phi += 1/np.sin(theta*np.pi/180)
                                    if phi >= 360:
                                        break
                    else:
                        print("\033[1;31mNão fiz nada.\033[m")
                else:
                    break
        else:
            break
    z0 += 5

print(f'\033[1;32m\nTerminei todos os {n} pontos requeridos! :D\n')
print(f'No total, a soma de todas as distâncias é {d:.2f} mm.')
print(f'\nA espessura média deu {d/n:.3f} mm.')

print()
delta_t = (time.time() - start_time)
if delta_t//60 > 0:
    sec = 60*(delta_t/60 - delta_t//60)
    print(f"\033[1;34m--- {delta_t//60} minutos e {sec:.3f} segundos ---\033[m")
else:
    print(f'\033[1;34m--- {delta_t:.3f} segundos ---\033[m')

###############################################################################
#
# Para R = 5, z_max = 3, theta dando passos de 9° e phi com passos corretos,
# levou 4.7 min para calcular tudo.
#
# Para R = 10, z_max = 3, theta dando passos de 36° e phi com passos corretos,
# demorou 5.4 min para ser feito o cálculo.
#
# Valores esperados:
#           
#           d = 1.2179e+10
#           n = 301397760
#           dmed = 40.4097 mm ou 4.04097 cm
###############################################################################
