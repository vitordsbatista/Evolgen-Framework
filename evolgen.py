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
import copy
import inspect
import fit_func as fit
import functions as f

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
                 par=[], fun=[], fit=[], gen=100, aux_func=[], **kwargs):
        if has_pop:
            self.pop = population
        else:
            self.create_pop(population)
        self.par = par
        self.gen = gen
        self.fit_func = fit
        self.aux_func = aux_func
        self.aux = [[], []]
        #Tratamento dos parâmetros passados acima
        self.func_dict = dict(inspect.getmembers(f, inspect.isfunction))
        for i in fun:
            if not self.func_dict.has_key(i):
                raise ValueError("Does not exist any function called "+i)
        self.fun = fun
        self.kwargs = kwargs

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
        mo = True
        for i in range(self.gen):                   #Gerações
            for fu, p in zip(self.fun, self.par):    #Laço com as funções
                self.func_dict[fu](self, p)          #Excecuta as funções
            #Alterar para caso o problema seja multiobjetivo
            if mo:
                print 'Geração', i
            else:
                best.append(min(self.fit))
                mean.append(sum(self.fit)/len(self.fit))
                print 'Geração', i, 'best', best[-1]
        if mo:
            #Colocar as fitness e não os indivíduos do front
            tmp = f.non_dom_sort(self, self.pop) 
            self.best_front = f.calc_fit(self, tmp)
            print self.best_front
    def plot(self):
        #Alterar para caso o problema seja multiobjetivo
        mo = True
        if mo:
            """
            for i in self.best_front:
                plt.plot(i[0], i[1], 'o', color='r')
            """
            fronts = dict()
            pop = self.pop
            i=0
            while any(pop):                      #Enquanto existir algo na pop
                tmp = f.non_dom_sort(self, pop)    #Front não dominado
                for j in tmp:                    
                    if j in pop:
                        pop.remove(j)            #Remove o front da população
                fronts[i] = tmp                  #Adiciona ele no dicionario
                i += 1                           #Incrementa o contador
            for i in range(1,len(fronts)):
                for j in fronts[i]:
                    k = []
                    for fu in self.fit_func:
                        k.append(fu(self, j))
                    plt.plot(k[0], k[1], 'o', color='b')
                plt.plot(k[0], k[1], 'o', color='b')
            #Plot do fornt f0, fiz isso pq existem alguns ind que ficam em 
            #dois fronts, e assim o f0 sempre fica em destaque
            for i in fronts[0]:
                k = []
                for fu in self.fit_func:
                    k.append(fu(self, i))
                plt.plot(k[0], k[1], 'o', color='r')
            plt.plot(k[0], k[1], 'o', color='r', label='f0')
            plt.legend(loc='best')                          #Legenda do plot
        else:
            plt.plot(best)
            plt.plot(mean)
        plt.show()



"""
pop_size = 100
ind_size = 100
ind_range = [0, 1]
par_sel = [0.8, pop_size]
par_cruz = [0.7, pop_size]
par_mut = [0.1, ind_range]
parm = [par_sel, par_cruz, par_mut]
fun = ['sto', 'cop', 'mru']
fit_func = [fit.fem]

train = np.load('train_10x10.npy')
test = np.load('test_10x10.npy')

l_train = np.load('train_label.npy')
l_test = np.load('test_label.npy')

top = [100, 10, 1]
egg = Evolgen(has_pop=False, population=[pop_size, ind_size, 
                                         ind_range, 'float'], 
              par=parm, fun=fun, fit=fit_func, gen=100, 
              ann = [top, train, l_train])
egg.run()
"""
#=================#
pop_size = 100
ind_size = 2
ind_range = [-100, 100]
ind_range = [-np.pi, np.pi]
par_sel = [0.8, pop_size]
par_cruz = [0.8, pop_size]
par_mut = [0.03, [-100, 100]]
parm = [par_sel, par_cruz, par_mut]
#fun = ['sto', 'cop', 'mru']
fun = ['fcd', 'cop', 'mru']
fit_func = [fit.f1, fit.f2]
fit_func = [fit.pol_f1, fit.pol_f2]
egg = Evolgen(has_pop=False, population=[pop_size, ind_size, 
                                         ind_range, 'float'], 
              par=parm, fun=fun, fit=fit_func, gen=1000)
egg.run()
egg.plot()
