# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:52:10 2022

@author: Lenovo
"""

import os
import pandas as pd
import numpy as np

path = 'C:/Users/Lenovo/Desktop/不同气候类型dt=0.1_cnt5/';

for csv_file in os.listdir(path):
    data = pd.read_csv(path + csv_file);
    [m,n] = data.shape;
    cal = np.zeros((1,n));
    for i in range(n):
        for j in range(m):
            if data[str(i+1.0)][j] != 0:
                cal[0][i] = cal[0][i] + 1;
    b = [];
    for i in range(n):
        b.append(cal[0][i]);
    mm = max(b);
    a0 = np.zeros((int(mm)+1,n));
    for i in range(n):
        a0[0][i] = i+1;
    for i in range(n):
        nn = 0;
        for j in range(m):
            if data[str(i+1.0)][j] != 0:
                nn = nn + 1;
                a0[nn][i] = data[str(i+1.0)][j];
    a = np.zeros((int(mm)+1,n));
    for i in range(n):
        a[0][i] = i+1;

    for i in range(n):
        for j in range(int(mm)):
            if a0[j+1][i] != 0:
                a[j+1][i] = a0[j+1][i];
            else:
                a[j+1][i] = 'nan';
    path00 = 'C:/Users/Lenovo/Desktop/'+ csv_file +'AverMinusNvpdt=0.1_0_to_nan.csv'
    a_np = pd.DataFrame(a);
    a_np.to_csv(path00, index= False, header= False)
