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
import matplotlib.pyplot as plt
import create_pop as cp
import fit_func as ff
import selection as sl
import crossover as cr

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

    #Função de inicialização
    def __init__(self, 
                 pop=False, pop_size=100, ind_type='int', 
                 ind_func=[], ind_size=2, ind_range=[-10, 10],
                 fit='fon', sel='tour', cross='two',
                 cross_alg='op', tour=0.8, cross_ix=0.7):
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

        #======================================================================#
        #Verifica se o fit é uma função ou um str
        self.fit = [] 
        if type(self.fit_par) == str:
            self.fit = self.fit_switcher.get(self.fit_par)
            if self.fit == None:
                raise "Não existe uma função com o nome", self.fit_par
        elif callable(self.fit_par):                    #É uma função
            self.fit = self.fit_par

        #======================================================================#
        #Verifica o algoritmo de seleção
        if type(self.sel) == str:
            self.selection = self.sel_switcher.get(self.sel)
            if self.selection == None:
                raise "Não existe uma função com o nome", self.sel
        elif callable(self.sel):                    #É uma função
            self.selection = self.sel

        #======================================================================#
        #verifica o método de cruzamento
        if type(self.cross) == str:
            self.crossover = self.cross_switcher.get(self.cross)
            if self.crossover == None:
                raise "não existe uma função com o nome", self.cross
        elif callable(self.cross):                    #é uma função
            self.crossover = self.cross

        #======================================================================#
        #verifica o algoritmo de cruzamento
        if type(self.cross_alg) == str:
            self.ca = self.cross_alg_switcher.get(self.cross_alg)
            if self.ca == None:
                raise "não existe uma função com o nome", self.cross_alg
        elif callable(self.cross_agl):                    #é uma função
            self.ca = self.cross_alg

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

    def run(self):
        """Loop principal"""
        pass
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
        print 'pop', len(self.pop)
        print 'fit 1', len(self.fitness)
        pop2 = self.selection(self.pop, self.fitness, self.tour, self.pop_size)
        pop3 = self.crossover(pop2, self.pop_size, self.cross_ix, self.ca)
        print '======'
        print 'pop2', len(pop2)
        print 'pop3', len(pop3)


    def plot(self):
        pass

eg = Evolgen(ind_type='float', ind_range=[-100, 100], fit='sch2', tour=0.7)
eg.create_ini_pop()
eg.run_fit()
eg.out()
#Testes
