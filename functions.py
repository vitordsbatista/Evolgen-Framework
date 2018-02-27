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
    calc_fit(self)
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

#Crowding Selection
def scd(self, parm):
    #TODO: Colocar na seleção o aux passando a população antes dela ser
    #modificada
    pop = self.pop
    front, crowd_dist = self.aux
    mating_pool = []
    #X01 - Colocar o tamanho da população no self
    pop_size = len(pop)
    for i in range(pop_size):
        id1 = rd.randrange(pop_size)                #Índice do ind 1
        id2 = rd.randrange(pop_size)                #Índice do ind 2
        i1 = pop[id1]                               #Gene do ind 1
        i2 = pop[id2]                               #Gene do ind 2
        fr1 = front[id1]                            #Front do ind 1
        fr2 = front[id2]                            #Front do ind 2
        cd1 = crowd_dist[id1]                       #Crowd_dist do ind 1
        cd2 = crowd_dist[id2]                       #Crowd_dist do ind 2
        chosen = nsga_ii_sel_cco(i1, i2, 
                         cd1, cd2, 
                         fr1, fr2)                  #Seleção
        mating_pool.append(chosen)
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
        p1 = mating_pool[i]                     #Primeiro indivíduo
        p2 = mating_pool[i+1]                   #Próximo indivíduo
        r = rd.random()
        if cross > r:                           #Taxa de cruzamento
            r = rd.randrange(1, len(p1))        #Ponto de conte
            f1 = p1[:r]+p2[r:]
            f2 = p2[:r]+p1[r:]
        else:
            f1, f2 = p1, p2
        pop_cross.append(f1)            #Adiciona eles na self.pop
        pop_cross.append(f2)            #Adiciona eles na self.pop
    if len(pop_cross) < self.pop_size:  #Caso o tamanho da pop for ímpar
        pop_cross.append(mating_pool[-1])
    self.pop = pop_cross

#Cruzamento binário
def cbn(self, parm):
    cross, pop_size = parm
    mating_pool = self.pop
    pop_cross = []
    for i in range(0, pop_size, 2):
        p1 = mating_pool[i]                         #Primeiro indivíduo
        p2 = mating_pool[i+1]                       #Próximo indivíduo
        r = rd.random()
        if cross > r:                               #Taxa de cruzamento
            mask = np.random.random(indTam-1) > 0.5 #Máscara
            for i, gen in enumerate(mask):
                if gen:
                    f1[i] = p1[i]
                else:
                    f2[i] = p1[i]
        else:
            f1, f2 = p1, p2
        pop_cross.append(f1)            #Adiciona eles na self.pop
        pop_cross.append(f2)            #Adiciona eles na self.pop
    if len(pop_cross) < self.pop_size:  #Caso o tamanho da pop for ímpar
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
            idx = rd.randrange(len(ind))     #Escolhe aleatoriamente um gen
            ind[idx] = rd.uniform(t1, t2)    #Modifica o indivíduo
    self.pop = pop



#==============================================================================#
#Others#
#==============================================================================#

#Calcula a fitness de uma população
def calc_fit(self, pop=False):
    """Calcula a fitness de uma população, ou de um conjunto de indivíduos"""
    if not pop:
        pop = self.pop
    fit = []
    for ind in pop:
        fit_tmp = []
        for f in self.fit_func:
            fit_tmp.append(f(self, ind))
        fit.append(fit_tmp)
    self.fit = fit
    if pop:
        return self.fit

#==============================================================================#
#NSGA-II#
#Seleção pelo operador de crowding distance
def nsga_ii_sel_cco(i1, i2, cd1, cd2, fr1, fr2):
    if fr1 < fr2:
        return i1
    elif fr2 < fr1:
        return i2
    elif cd1 > cd2:
        return i1
    elif cd2 > cd1:
        return i2
    else:
        return rd.choice([i1, i2])

def fcd(self, parm):
    parents = self.aux[0]
    offspring = self.pop
    pop = parents + offspring
    pop_size = parm[1]                          #TODO: 1 - global
    calc_fit(self)
    #Criação dos fronts
    fronts = dict()                             #Inicialização dos fronts
    i = 0                                       #Contador
    while any(pop):                             #Enquanto existir algo na pop
        tmp = non_dom_sort(self, pop)           #Front não dominado
        for j in tmp:                           
            if j in pop:
                pop.remove(j)                   #Remove o front da população
        fronts[i] = tmp                         #Adiciona ele no dicionario
        i += 1                                  #Incrementa o contador

    pop = []                                        #Reinicializa a pop
    crowd_dist = []                                 #Reinicializa o crowd_dist
    j = 0                                           #Contador
    while True:
        pop += fronts[j]                            #Adiciona o fron na pop
        crowd_dist += nsga_ii_cd_front(             #Calcula o cd do front j
                        self, fronts[j])
        j = j + 1                                   #Incrementa o contador
        if fronts.has_key(j):
            if len(pop) + len(fronts[j]) > pop_size:
                break
        else:
            break

    if len(pop) < pop_size:                 #Verifica se pop não está completa
        rest = pop_size - len(pop)
        last_front = fronts[j]                      #Último front
        last_front = nsga_ii_crowding_sort(         #Crows_sort no último front
                        self, fronts[j])          
        crowd_dist += nsga_ii_cd_front(             #Calcula o cd do last_front
                        self, last_front[0:rest])
        pop += last_front[0:rest]                   #Adiciona ele na pop
    self.pop = pop
    self.aux = [pop, crowd_dist]                    #Armazena os fronts e o cd

#Calcula a crowd distance de todos os indivíduos de um determinado front
def nsga_ii_cd_front(self, front):
    l = len(front)              #Tamalho do front
    cd = [0] * l                #Inicializa o cd dos fronts
    ix = range(l)               #Índices
    fit = self.fit_func
    for f in fit:
        f_tmp = [f(self, x) for x in front]   #Calcula a fit para o front
        fit_ix = zip(ix, f_tmp) #Tupla com o ix e a fitness de cada indivíduo
        #Ordena pela fitness
        fit_ix = sorted(fit_ix, key=lambda fit_ix: fit_ix[1])
        cd[fit_ix[0][0]] = float('inf')         #O primeiro recebe inf
        cd[fit_ix[l-1][0]] = float('inf')       #O último recebe inf
        for i in range(1, l-2):                 #Restante dos indivíduos
            fit_ant = fit_ix[i - 1][1]          #Fitness do posterior
            fit_pos = fit_ix[i + 1][1]          #Fitness do anterior
            cd[fit_ix[i][0]] += fit_pos-fit_ant #Calcula o crowdind distance
    return cd                                   #Retorna o cd

#Ordenação dos fronts pelo cd
def nsga_ii_crowding_sort(self, front):
    cd = nsga_ii_cd_front(self, front)              #CD para o front
    cd = zip(front, cd)                             #Junta o cd e o front
    cd = sorted(cd, key=lambda cd: cd[1])           #Ordena pelo cd
    front_sort = [x[0] for x in cd]                 #Pega só o front do cd
    return front_sort                               #Retorna o front ordenado
#Dominância de uma população
def non_dom_sort(self, pop):
    """ Realiza o processo de não dominância de uma população
    Parâmetros: pop(list) - lista com os indivíduos nela
                fit(list) - lista com as fits do algoritmo
    Retorno:    pop_out   - lista com os indivíduos não domidados de pop
    """
    pop_out = [pop[0]]                          #Inicia a pop_out 
    for n, i in enumerate(pop):
        if not (i in pop_out):                  #Se o i não está no pop_out
            pop_out.append(i)                   #Adiciona o i na pop_out
            pop_out_tmp = pop_out[:]            #Copia a pop_out
            for m, j in enumerate(pop_out_tmp):
                if i != j:                      #Não compara dois iguais
                    if dom(self, i, j):         #Se o i (n) domina o j (m)
                        if j in pop_out :
                            pop_out.remove(j)   #Remove o j do pop_out
                    elif dom(self, j, i):       #Se o j (m) domina o i (n)
                        if i in pop_out:
                            pop_out.remove(i)   #Remove o i do pop_out
    return pop_out

#Dominação (verifica se o a domina o b)
def dom(self, ind1, ind2):
    """  Verifica se um indivíduo domina o outro. A verificação é se o ind 1 
        domina o ind 2, se verdadeiro, retorna True, caso contrário, 
        retorna False
    Parâmetros: ind1(list) - indivíduo 1
                ind2(list) - indivíduo 2
    Retorno:    boolean
    """
    fit = self.fit_func
    for f in fit:
        #Caso uma fit do ind1 for pior que a do ind2
        if f(self, ind1) > f(self, ind2):            
            return False        #Retorna False
    for f in fit:               #Caso uma fit do ind1 for melhor que a do ind2
        if f(self, ind1) < f(self, ind2):
            return True         #Retorna True
    return False                #Se nada acontecer, retorna False
#NSGA-II-end#
#==============================================================================#
