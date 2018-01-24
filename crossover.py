#!/usr/bin/python
# -*- coding: utf-8 -*-
#===================================#
# File name: 						#
# Author: Vitor dos Santos Batista	#
# Date created: 					#
# Date last modified: 				#
# Python Version: 2.7				#
#===================================#

import numpy as np
import random as rd

#==============================================================================#
#Algoritmos Genéricos
#==============================================================================#
#Cruzamento de dois em dois indivíduos
def cross_two(mating_pool, pop_size, cross, cross_alg):
    pop_cross = []
    for i in range(0, pop_size, 2):
        i1 = mating_pool[i]             #Primeiro indivíduo
        i2 = mating_pool[i+1]           #Próximo indivíduo
        r = rd.random()
        if cross > r:                   #Taxa de cruzamento
            f1, f2 = cross_alg(i1, i2)
        else:
            f1, f2 = i1, i2
        pop_cross.append(i1)            #Adiciona eles na pop
        pop_cross.append(i2)            #Adiciona eles na pop
    if len(pop_cross) < pop_size:       #Caso o tamanho da população for ímpar
        pop_cross.append(mating_pool[-1])
    return pop_cross

#==============================================================================#
#Algoritmos específicos
#==============================================================================#
#Cruzamento com um ponto
def one_point(p1, p2):
    r = rd.randrange(1, len(p1))        #Ponto de conte
    f1 = p1[:r]+p2[r:]
    f2 = p2[:r]+p1[r:]
    return p1, p2

#Crossover uniforme
def crossBin(p1, p2):
    f1 = f2 = p2
    mask = np.random.random(indTam-1) > 0.5
    for i, gen in enumerate(mask):
        if gen is True:
            f1[i] = p1[i]
        else:
            f2[i] = p1[i]
    return f1, f2
