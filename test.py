#!/usr/bin/python
# -*- coding: utf-8 -*-
#===================================#
# File name: 						#
# Author: Vitor dos Santos Batista	#
# Date created: 					#
# Date last modified: 				#
# Python Version: 2.7				#
#===================================#

import evolgen as egg

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
egg = egg.evolgen(has_pop=False, population=[pop_size, ind_size, 
                                         ind_range, 'float'], 
              par=parm, fun=fun, fit=fit_func, gen=1000)
egg.run()
egg.plot()
