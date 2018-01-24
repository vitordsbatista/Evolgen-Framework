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

class Evolgen:
    """Framework para a utilização e criação de algoritmos evolutivos
    Programa criado por: Vitor Batista
    """
    pop = []

    def __init__(self, 
                 ind_pop=False, ind_num=100, ind_type='int', 
                 ind_func=[], ind_size=2, ind_range=[-10, 10]):
        self.ind_pop = ind_pop      #População inicial
        self.ind_num = ind_num      #Número de ind numa pop
        self.ind_type = ind_type    #Tipo do ind ('int', 'float', 'bin', 'other')
        self.ind_func = ind_func    #Função de criação dos indivíduos 
        self.ind_size = ind_size    #Tamanho dos indivíduos
        self.ind_range = ind_range  #Intervalo dos indivíduos


    def create_ini_pop(self):
        #Se existir população inicial
        if self.ind_pop:
            self.pop = self.ind_pop
        #Caso contrário, o programa irá criar a pop
        else:
            if self.ind_type == 'int':               #de inteiros
                self.pop = cp.pop_int(
                                self.ind_num,
                                self.ind_range,
                                self.ind_size)
            elif self.ind_type == 'float':           #de float 
                self.pop = cp.pop_float(
                                self.ind_num,
                                self.ind_range,
                                self.ind_size)
            elif self.ind_type == 'bin':             #binária
                self.pop = cp.pop_bin(
                                self.ind_num,
                                self.ind_range,
                                self.ind_size)
            elif self.ind_type == 'other':           #com a função passada
                self.pop = self.ind_func(
                                self.ind_num,
                                self.ind_range,
                                self.ind_size)
        """
        #TODO: colocar mais argumentos na função passada
        TODO: criar um arquivo com todas as funções de criação da população
        inicial, e a medida que forem desenvolvidas novas funções, colcoar
        nela
        """

    def run(self):
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
        print 'População', self.pop
        print 'n de inds', self.ind_num
        print 'tipo do ind', self.ind_type
        print 'função do ind', self.ind_func
        print 'tamanho do ind', self.ind_size
        print 'range do ind', self.ind_range
    def plot(self):
        pass

ex = Evolgen(ind_type='float')
ex.out()
ex.create_ini_pop()
print '========='
ex.out()
