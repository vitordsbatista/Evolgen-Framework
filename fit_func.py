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
def sch2(x):
    x, y = x
    n = m.sin(x**2+y**2)**2 - 0.5
    d = (1.+0.001*(x**2 + y**2))**2
    res = 0.5 + n/d
    return res

