# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:15:21 2022

@author: Lenovo
"""


import numpy as np
import pandas as pd
import math


Cov = np.zeros((8,8));
Covi0 = np.zeros((8,1));

distance = np.array([[0.00,4.47,3.61,8.06,9.49,6.71,8.94,13.45],
                     [4.47,0.00,2.24,10.04,13.04,10.05,12.17,17.80],
                     [3.61,2.24,0.00,11.05,13.00,8.00,10.05,16.97],
                     [8.06,10.04,11.05,0.00,4.12,13.04,15.00,11.05],
                     [9.49,13.04,13.00,4.12,0.00,12.37,.00,2.24,12.65],
                     [6.71,10.05,8.00,13.04,12.37,0.00,2.24,12.65],
                     [8.94,12.17,10.05,15.00,13.93,2.24,0.00,13.15],
                     [13.45,17.80,16.97,11.05,7.00,12.65,13.15,0.00]]);

V = np.array([477,696,227,646,606,791,783]);

for i in range(7):
    for j in range(7):
        Cov[j][i] = 10 * math.exp(-0.05*distance[j+1][i+1]*distance[j+1][i+1]);
        
for i in range(7):
    Cov[7][i] = 1;
    Cov[i][7] = 1;

for i in range(7):
    Covi0[i][0] = 10 * math.exp(-0.05*distance[0][i+1]*distance[0][i+1]);

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
