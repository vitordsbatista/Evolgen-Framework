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
import math as m

#POL - Poloni's two objective function
def pol_f1(self, ind):
    x, y = ind
    return (1
            + (pol_a1() - pol_b1(x, y))**2
            + (pol_a2() - pol_b2(x, y))**2)
def pol_f2(self, ind):
    x, y = ind
    return (x+3)**2 + (y+1)**2
def pol_a1():
    return (.5*m.sin(1)
            - 2*m.cos(1)
            + m.sin(2)
            - 1.5*m.cos(2))
def pol_a2():
    return (1.5*m.sin(1)
            - m.cos(1)
            + 2*m.sin(2)
            - .5*m.cos(2))

def pol_b1(x, y):
    return (.5*m.sin(x)
            - 2*m.cos(x)
            + m.sin(y)
            - 1.5*m.cos(y))

def pol_b2(x, y):
    return (1.5*m.sin(x)
            - m.cos(x)
            + 2*m.sin(y)
            - .5*m.cos(y))
#FON - Fonseca and Fleming's study[1]
#len(x) = 3
#Best - x1 = x2 = x3  | [-1/sqrt(3), 1/sqrt(3)]
def fon_f1(x):
    x = np.array(x)
    res = 1 - m.exp( -sum((x - 1/m.sqrt(3))**2))
    return res

def fon_f2(x):
    x = np.array(x)
    res = 1 - m.exp( -sum((x + 1/m.sqrt(3))**2))
    return res

#Scaffer function nº2
#len(x) = 2
#Best - f(x) = 0
def sch2(pop):
    fit = []
    for i in pop:
        x, y = i
        n = m.sin(x**2+y**2)**2 - 0.5
        d = (1.+0.001*(x**2 + y**2))**2
        res = 0.5 + n/d
        fit.append(res)
    return fit

def f1(self, ind):
    x, y = ind
    a = 4*pow(x,2)+4*pow(y,2)
    if g1(x, y):
        a = a+2
    if g2(x, y):
        a = a+2
    return a
def f2(self, ind):
    x, y = ind
    a = pow((x-5),2) + pow((y-5),2)
    if g1(x, y):
        a = a+2
    if g2(x, y):
        a = a+2
    return a
def g1(x, y):    
    s = pow((x-5),2) + y**2
    if s <= 25:
        return True
    return False
def g2(x, y):
    s = x - 3*y + 10
    if s <= 0:
        return True
    return False

def nonlin(x, deriv = False):
    if deriv == True:
        return x*(1-x)
    return 1/(1+np.exp(-x))

#Fitness Err Mean
def fem(self, ind):
    top, inputs, outputs = self.kwargs['ann']
    weights = []
    ind = np.array(ind)
    #Extrai os pesos do indivíduo
    for i, j in zip(top[:-1], top[1:]):
        print ind
        w_tmp, ind = np.split(ind, [i*j])
        print i, j
        print i*j
        print w_tmp.shape
        w_tmp = w_tmp.reshape(i, j)
        weights.append(w_tmp)
    err = []
    #Calcula o erro
    out_ann = []
    for inp, out in zip(inputs, outputs):
        layers = [inp]
        for w in weights:
            a = np.dot(layers[-1], w)
            layers.append(nonlin(np.dot(layers[-1], w)))
        err.append((out - layers[-1])**2)
        out_ann.append(layers[-1])
    return sum(err)/len(err)
