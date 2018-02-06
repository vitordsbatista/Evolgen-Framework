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
import matplotlib.pyplot as plt
import create_pop as cp
import fit_func as ff
import selection as sl
import crossover as cr
import mutation as mt
import functions as f
import copy
import inspect

class Evolgen:
    """Framework para a utilização e criação de algoritmos evolutivos
    Programa criado por: Vitor Batista

    pop     - list - população dos indivíduos (cada item é um indivíduo)
    fitness - list - aptidão dos indivíduos (cada item corresponde a um ind)
    """
    global best
    global mean
    best = []
    mean = []
    #Função de inicialização
    def __init__(self, has_pop=False, population=[100, 2, 'int', [-10, 10]], 
                 par=[], fun=[], fit=[], gen=100):
        if has_pop:
            self.pop = population
        else:
            self.create_pop(population)
        self.par = par
        self.gen = gen
        self.fit_func = fit
        #Tratamento dos parâmetros passados acima
        self.func_dict = dict(inspect.getmembers(f, inspect.isfunction))
        for i in fun:
            if not self.func_dict.has_key(i):
                raise ValueError("Does not exist any function called "+i)
        self.fun = fun

    def create_pop(self, parm):
        #Se não existir população inicial
        pop_size = parm[0]
        ind_size = parm[1]
        ind_range = parm[2]
        ind_type = parm[3]
        #O programa irá criar uma população...
        if ind_type == 'int':               #de inteiros
            self.pop = cp.pop_int(
                            pop_size,
                            ind_range,
                            ind_size)
        elif ind_type == 'float':           #de float 
            self.pop = cp.pop_float(
                            pop_size,
                            ind_range,
                            ind_size)
        elif ind_type == 'bin':             #binária
            self.pop = cp.pop_bin(
                            pop_size,
                            ind_range,
                            ind_size)

    def run(self):
        """Loop principal"""
        for i in range(self.gen):                   #Gerações
            for f, p in zip(self.fun, self.par):    #Laço com as funções
                self.func_dict[f](self, p)          #Excecuta as funções
            best.append(min(self.fit))
            mean.append(sum(self.fit)/len(self.fit))
            print 'Geração', i, 'best', best[-1]
    def plot(self):
        plt.plot(best)
        plt.plot(mean)
        plt.show()


pop_size = 100
par_sel = [0.8, pop_size]
par_cruz = [0.8, pop_size]
par_mut = [0.03, [-10, 10]]
parm = [par_sel, par_cruz, par_mut]
fun = ['sto', 'cop', 'mru']
def fit(pop):
    fit = []
    for i in pop:
        fit.append(i[0]**2 + i[1]**2)
    return fit

#egg = Evolgen(has_pop=True, population=pop, par=par, fun=fun, fit_func=fit)
egg = Evolgen(has_pop=False, population=[pop_size, 2, [-10, 10], 'float'], 
              par=parm, fun=fun, fit=fit)

egg.run()
egg.plot()
