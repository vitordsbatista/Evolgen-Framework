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

#Tournament selection
def tournament(pop, fitness, tour, pop_size):
    mating_pool = []
    while len(mating_pool) < pop_size:
        #Seleciona dois indivíduos aleatórios
        i1, i2 = rd.sample(range(pop_size), 2)
        r = rd.random()
        if fitness[i1] < fitness[i2]:
            if tour > r:
                mating_pool.append(pop[i1])
            else:
                mating_pool.append(pop[i2])
        else:
            if tour > r:
                mating_pool.append(pop[i2])
            else:
                mating_pool.append(pop[i1])
    if len(mating_pool) > pop_size:
        mating_pool = mating_pool[:pop_size]
    return mating_pool
