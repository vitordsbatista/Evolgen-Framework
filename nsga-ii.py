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
import functions as f

class NSGA_II:
    """Realiza a otimização multiobjetivo utilizando o algoritmo NSGA-II [1]
    Entrada: a

    Saida: a

    Programa criado por: Vitor Batista
    """
    def __init__(self, gen, cross, mut, fits, ini_pop, 
                 ind_type=None, ind_size=None,
                 ind_range=None, pop_size=None):
        """Inicializa os dados e a população inicial (caso nescessário)
        """
        self.gen = gen                    #Número de gerações
        self.cross = cross                #Taxa de cruzamento
        self.fits = fits                  #Lista de funções com as fitness
        self.ini_pop = ini_pop            #População inicial
        if not ini_pop:
            self.ind_type = ind_type      #Tipo dos inds ('int', 'float', 'bin')
            self.ind_size = ind_size      #Tamanho dos indivíduos
            self.ind_range = ind_range    #Intervalo dos indivíduos
            self.pop_size = pop_size      #Tamanho da população
            self.mut = 1/ind_size         #Taxa de mutação (pop criada)
        else:
            self.ind_type = 'Desconhecido'
            self.ind_size = len(ini_pop[0])     #Tamanho dos indivíduos
            self.ind_range = 'Desconhecido'     #Intervalo dos indivíduos
            self.pop_size = len(ini_pop)        #Tamanho da população
            self.mut = 1/len(ini_pop[0])        #Taxa de mutação (pop passada)

    def create_ini_pop(self):
        pass
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

    def plot(self):
        pass

ex_1 = NSGA_II(1000, None, None, [1, 2], [[4, 2], [2, 2]])
ex_1.res()
