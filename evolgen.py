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
import copy

class Evolgen:
    """Framework para a utilização e criação de algoritmos evolutivos
    Programa criado por: Vitor Batista

    pop     - list - população dos indivíduos (cada item é um indivíduo)
    fitness - list - aptidão dos indivíduos (cada item corresponde a um ind)
    """

    #==========================================================================#
    #Switchers
    #==========================================================================#
    fit_switcher = {
        'fon': [ff.fon_f1, ff.fon_f2],
        'sch2': ff.sch2
    }
    sel_switcher = {
        'tour': sl.tournament
    }
    cross_switcher = {
        'two': cr.cross_two
    }
    cross_alg_switcher = {
        'op': cr.one_point
    }
    mut_switcher = {
        'ru': mt.random_uniform
    }

    best = []
    mean = []

    #Função de inicialização
    def __init__(self, 
                 pop=False, pop_size=100, ind_type='int', 
                 ind_func=[], ind_size=2, ind_range=[-10, 10],
                 fit='fon', sel='tour', cross='two',
                 cross_alg='op', tour=0.8, cross_ix=0.7,
                 mut='ru', mut_ind=0.03, gen=100):
        self.pop = pop              #População inicial
        self.pop_size = pop_size    #Tamanho da população
        self.ind_type = ind_type    #Tipo do ind('int', 'float', 'bin', 'other')
        self.ind_func = ind_func    #Função de criação dos indivíduos 
        self.ind_size = ind_size    #Tamanho dos indivíduos
        self.ind_range = ind_range  #Intervalo dos indivíduos
        #======================================================================#
        self.fit_par = fit          #Parâmetro da função de aptidão
        #TODO: encontrar uma forma de organizar os parâmetros não genérios
        self.tour = tour            #Taxa do torneio
        self.sel = sel              #Algoritmo de seleção
        self.cross = cross          #Método de cruzamento
        self.cross_alg = cross_alg  #Algoritmo de cruzamento
        self.cross_ix = cross_ix
        self.mut = mut
        self.mut_ind = mut_ind
        self.gen = gen

        #======================================================================#
        #Verifica se o fit é uma função ou um str
        self.fit = [] 
        if type(self.fit_par) == str:
            self.fit = self.fit_switcher.get(self.fit_par)
            if self.fit == None:
                raise ValueError("Não existe uma função com o nome",
                                 self.fit_par)
        elif callable(self.fit_par):                    #É uma função
            self.fit = self.fit_par

        #======================================================================#
        #Verifica o algoritmo de seleção
        if type(self.sel) == str:
            self.selection = self.sel_switcher.get(self.sel)
            if self.selection == None:
                raise ValueError("Não existe uma função com o nome", self.sel)
        elif callable(self.sel):                    #É uma função
            self.selection = self.sel

        #======================================================================#
        #verifica o método de cruzamento
        if type(self.cross) == str:
            self.crossover = self.cross_switcher.get(self.cross)
            if self.crossover == None:
                raise ValueError("não existe uma função com o nome",
                                 self.cross)
        elif callable(self.cross):                    #é uma função
            self.crossover = self.cross

        #======================================================================#
        #verifica o algoritmo de cruzamento
        if type(self.cross_alg) == str:
            self.ca = self.cross_alg_switcher.get(self.cross_alg)
            if self.ca == None:
                raise ValueError("não existe uma função com o nome",
                                 self.cross_alg)
        elif callable(self.cross_agl):                    #é uma função
            self.ca = self.cross_alg
        #======================================================================#
        #verifica o algoritmo de mutação
        if type(self.mut) == str:
            self.mutation = self.mut_switcher.get(self.mut)
            if self.mutation == None:
                raise ValueError("não existe uma função com o nome",
                                 self.mut)
        elif callable(self.mut):                    #é uma função
            self.mutation = self.mut

    def create_ini_pop(self):
        #Se não existir população inicial
        if not self.pop:
            #O programa irá criar uma população...
            if self.ind_type == 'int':               #de inteiros
                self.pop = cp.pop_int(
                                self.pop_size,
                                self.ind_range,
                                self.ind_size)
            elif self.ind_type == 'float':           #de float 
                self.pop = cp.pop_float(
                                self.pop_size,
                                self.ind_range,
                                self.ind_size)
            elif self.ind_type == 'bin':             #binária
                self.pop = cp.pop_bin(
                                self.pop_size,
                                self.ind_range,
                                self.ind_size)
            elif self.ind_type == 'other':           #com a função passada
                self.pop = self.ind_func(
                                self.pop_size,
                                self.ind_range,
                                self.ind_size)
        """
        #TODO: colocar mais argumentos na função passada
        TODO: criar um arquivo com todas as funções de criação da população
        inicial, e a medida que forem desenvolvidas novas funções, colcoar
        nela
        """
    def run_fit(self):
        #TODO: Verificar se a f executa tranquilamente na população e
        #retornar isso
        #Executa a fit na população
        if callable(self.fit):                      #Função única
            self.fitness = map(self.fit, self.pop)
        else:                                       #Multiobjetivo
            for i in f:
                self.fitness.append(map(self.fit, self.pop))

    def mut_pop(self, pop, mut):
        """Realiza a mutação em um indivíduo
        TODO: comentar direito
        """
        pop_out = copy.deepcopy(pop)
        for n, i in enumerate(pop_out):
            r = rd.random()
            if mut > r:
                i_mut = self.mutation(i, self.ind_range)
                pop_out[n] = i_mut
        return pop_out

    def run(self):
        """Loop principal"""
        self.create_ini_pop()                 #Criação da população inicial 
        self.run_fit()                        #Avaliação da população inicial
        for i in range(self.gen):
            self.pop = self.selection(self.pop,     #Seleção
                                  self.fitness, 
                                  self.tour, 
                                  self.pop_size)
            self.pop = self.crossover(self.pop,     #Cruzamento
                                  self.pop_size, 
                                  self.cross_ix, 
                                  self.ca)
            self.pop = self.mut_pop(self.pop,       #Mutação
                                self.mut_ind)
            self.run_fit()
            self.best.append(min(self.fitness))
            self.mean.append(sum(self.fitness)/self.pop_size)
            print 'Geração', i, 'best', min(self.fitness)

    def res(self):
        print 'Gerações:', self.gen
        print 'Taxa de cruzamento:', self.cross
        print 'Taxa de mutação:', self.mut
        print 'Tamanho da população:', self.pop_size
        print 'Tamanho do indivíduo:', self.ind_size
        print 'Intervalo do indivíduo:', self.ind_range
        print 'Número de funções:', len(self.fits)

    def out(self):
        """
        print 'População', self.pop
        print 'n de inds', self.ind_num
        print 'tipo do ind', self.ind_type
        print 'função do ind', self.ind_func
        print 'tamanho do ind', self.ind_size
        print 'range do ind', self.ind_range
        """
        print '======'
        print pop3[7]
        print pop4[7]

    def plot(self):
        plt.plot(self.best)
        plt.plot(self.mean)
        plt.show()

eg = Evolgen(ind_type='float', ind_range=[-100, 100], fit='sch2', tour=0.7, 
             mut_ind=0.1)
eg.run()
eg.plot()
