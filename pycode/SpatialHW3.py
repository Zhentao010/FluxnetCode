# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:11:27 2022

@author: Lenovo
"""

import numpy as np
import pandas as pd
import math



variogram = np.zeros((4,4));
variogrami0 = np.zeros((4,1));

distance = np.array([[0,5.0,5.5,4.0,4.5],
                     [5.0,0,5.0,3.5,2.0],
                     [5.5,5.0,0,4.0,4.5],
                     [4.0,3.5,4.0,0,1.5],
                     [4.5,2.0,4.5,1.5,0]]);

V = np.array([477,696,227,646,606,791,783]);

for i in range(7):
    for j in range(7):
        variogram[j][i] = 10 *(1- math.exp(-0.3*distance[j+1][i+1]));
        
for i in range(7):
    variogram[7][i] = 1;
    variogram[i][7] = 1;

for i in range(7):
    variogrami0[i][0] = 10 *(1- math.exp(-0.3*distance[0][i+1]));

Covi0[7][0] = 1;

Covinv = np.linalg.inv(Cov);

lamda = C = np.dot(Covinv, Covi0);

V0 = 0;
 
for i in range(7):
    V0 += lamda[i] * V[i];

Var = 0;

for i in range(7):
    Var = -lamda[i]*Covi0[i] + Var;

Var = 10 + Var - lamda[7];


