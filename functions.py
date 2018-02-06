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
#Selection#
#==============================================================================#
#Tournament selection
def sto(self, parm):
    self.fit = self.fit_func(self.pop)
    tour, self.pop_size = parm
    mating_pool = []
    while len(mating_pool) < self.pop_size:
        #Seleciona dois indivíduos aleatórios
        i1, i2 = rd.sample(range(self.pop_size), 2)
        r = rd.random()
        if self.fit[i1] < self.fit[i2]:
            if tour > r:
                mating_pool.append(self.pop[i1])
            else:
                mating_pool.append(self.pop[i2])
        else:
            if tour > r:
                mating_pool.append(self.pop[i2])
            else:
                mating_pool.append(self.pop[i1])
    if len(mating_pool) > self.pop_size:
        mating_pool = mating_pool[:self.pop_size]
    self.pop = mating_pool

#==============================================================================#
#Crossover#
#==============================================================================#
#Cruzamento de um ponto
def cop(self, parm):
    cross, self.pop_size = parm
    mating_pool = self.pop
    pop_cross = []
    for i in range(0, self.pop_size, 2):
        p1 = mating_pool[i]             #Primeiro indivíduo
        p2 = mating_pool[i+1]           #Próximo indivíduo
        r = rd.random()
        if cross > r:                   #Taxa de cruzamento
            r = rd.randrange(1, len(p1))        #Ponto de conte
            f1 = p1[:r]+p2[r:]
            f2 = p2[:r]+p1[r:]
        else:
            f1, f2 = p1, p2
        pop_cross.append(f1)            #Adiciona eles na self.pop
        pop_cross.append(f2)            #Adiciona eles na self.pop
    if len(pop_cross) < self.pop_size:       #Caso o tamanho da self.população for ímpar
        pop_cross.append(mating_pool[-1])
    self.pop = pop_cross

#Cruzamento binário
def cbn(self, parm):
    cross, pop_size = parm
    mating_pool = self.pop
    pop_cross = []
    for i in range(0, pop_size, 2):
        p1 = mating_pool[i]             #Primeiro indivíduo
        p2 = mating_pool[i+1]           #Próximo indivíduo
        r = rd.random()
        if cross > r:                   #Taxa de cruzamento
            mask = np.random.random(indTam-1) > 0.5     #Máscara
            for i, gen in enumerate(mask):
                if gen:
                    f1[i] = p1[i]
                else:
                    f2[i] = p1[i]
        else:
            f1, f2 = p1, p2
        pop_cross.append(f1)            #Adiciona eles na self.pop
        pop_cross.append(f2)            #Adiciona eles na self.pop
    if len(pop_cross) < self.pop_size:       #Caso o tamanho da self.população for ímpar
        pop_cross.append(mating_pool[-1])
    self.pop = pop_cross

#========================================================================#
#Mutation#
#========================================================================#
def mru(self, parm):
    mut, ind_range = parm
    t1, t2 = ind_range                       #Range
    pop = self.pop
    for ind in pop:
        if mut > rd.random():
            idx = rd.randrange(len(ind))             #Escolhe aleatoriamente um gen
            ind[idx] = rd.uniform(t1, t2)            #Modifica o indivíduo
    self.pop = pop
