#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:52:10 2020

@author: juliedson
"""
###########################################################
#
# Comecei com um cubo de lado 10 (u.m.)
#
# Peguei um ponto bem no meio, x0 = y0 = z0 = 5
#
# Theta e Phi variavam a cada 45° de início
#
# Assim ficou fácil de conferir as contas feitas para x, y
# e z com o incremento dado pelo r.
#
# Depois, fui adicionando as demais variações de coordena-
# das e conferindo algumas delas.
#
###########################################################

import time
import numpy as np

start_time = time.time()

# Dimensões da caixa:
x_max = y_max = z_max = 10

# Ponto de partida P = (1, 1, 1), logo x0 = 1
x0 = 1

# Contadores da soma das distâncias (d) e da quantidade (n)
d = n = 0

# Let the game begin!

print('\033[1;32mBora então! \033[m', '\n')
while x0 < x_max:
    print(f'\033[1;32mComeçando para x0 = {x0}...\033[m')
    y0 = 1
    while y0 < y_max:
        print(f'\033[1;32mE para y0 = {y0}\033[m')
        z0 = 1
        while z0 < z_max:
            print(f'\033[1;32mCom z0 = {z0}\033[m')
            phi = 0
            for theta in range(0, 181, 90):
                if theta == 0:
                    print('\033[1;34mtheta = 0 aqui\033[m')
                elif theta == 180:
                    print('\033[1;34mtheta = 180 aqui\033[m')
                else:
                    while True:
                        r = 0
                        while True:
                            r += 0.01
                            x = x0 + r*(np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180))
                            y = y0 + r*(np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180))
                            z = z0 + r*np.cos(theta*np.pi/180)
                            if (x <= 0 or x >= x_max or y <= 0 or
                            y >= y_max or z <= 0 or z >= z_max):
                                print(f'Para P = ({x0}, {y0}, {z0}), Theta = {theta} com r = {r:.1f} e phi = {phi}')
                                break
                        phi += 45#/np.sin(theta*np.pi/180)
                        if phi >= 360:
                            break
            print(f'\033[1;31mTerminei tudo para z0 = {z0}\033[m')
            z0 += 2            
#        print('Cheguei até aqui')
        print(f'\033[1;31mTerminei tudo para y0 = {y0}\033[m')
        y0 += 3
#    if y0 > y_max:             Se fosse usar loop infinito para y
#        break                  Mas mudei de ideia...
    print(f'\033[1;31mTerminei tudo para x0 = {x0}\033[m','\n')    
    x0 += 5
#    if x0 > x_max:             Idem para x
#        break

print('\033[1;32mTerminei todos os pontos requeridos! :D\033[1m')
print()
delta_t = (time.time() - start_time)
if delta_t//60 > 0:
    seg = 60*(delta_t/60 - delta_t//60)
    print(f"\033[1;34m--- {delta_t//60} minutos e {seg:.2f} segundos ---\033[m")
else:
    print(f'\033[1;34m--- {delta_t:.3f} segundos ---\033[m')

##################################################################
# Note que:
#
# Para P = (1, 1, z), Theta = 90 com r = 12.7 e phi = 45
#
# E r verdadeiro é r = 9*(2)^(1/2) = 12.72792
#
# O que falta:    
#   --> Colocar os contadores no meio do código;
#   --> Colocar a contagem correta para os thetas == 0 e 180;
#   --> Fazer as dimensões corretas para a peça;
#   --> Colocar os passos corretos para phi.
#
##################################################################
