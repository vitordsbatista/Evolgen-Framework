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

def pop_int(ind_num, ind_range, ind_size):
    """ Cria uma população inteira
    Parâmetros: ind_num(int) - Tamanho da população
                ind_range([min, max]) - Intervalo dos gens do indivíduo
                ind_size(int) - Tamanho do indivíduo

    Retorno:   pop(list) - Lista com a população inicial
    """
    pop = list()                            #Inicia a população
    for i in range(ind_num):
        x = rd.sample(range(ind_range[0], ind_range[1]), ind_size)
        pop.append(x)
    return pop

def pop_float(ind_num, ind_range, ind_size):
    """ Cria uma população float
    Parâmetros: ind_num(int) - Tamanho da população
                ind_range([min, max]) - Intervalo dos gens do indivíduo
                ind_size(int) - Tamanho do indivíduo

    Retorno:   pop(list) - Lista com a população inicial
    """
    pop = list()                            #Inicia a população
    #TODO: encontrar uma forma mais rápida e elegante pra fazer isso
    for i in range(ind_num):
        t1, t2 = ind_range
        ind = [rd.uniform(t1, t2) for i in range(ind_size)]
        pop.append(ind)
    return pop

#TODO
def pop_bin(ind_num, ind_range, ind_size):
    pass

