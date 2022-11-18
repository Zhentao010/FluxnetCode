# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:34:21 2022

@author: Lenovo
"""

import numpy as np
import pandas as pd

path = 'C:/Users/Lenovo/Desktop/slope.xlsx';
xl = pd.read_excel(path);
data = xl.values;
[m,n] = data.shape;
sta = np.zeros((2,n-1));

for i in range(n-1):
    sta[0][i] = data[0][i+1];
    n1 = 0;
    n2 = 0;
    for j in range(m-1):
        if data[j+1][i+1] != 'nan':
            n1 = n1 + 1;
            if data[j+1][i+1] > 0:
                n2 = n2 + 1;
    per = n2/n1;
    sta[1][i] = per;
    
path1 = 'C:/Users/Lenovo/Desktop/percentage.xlsx'
sta_pd = pd.DataFrame(sta);
writer = pd.ExcelWriter(path1);
sta_pd.to_excel(writer, sheet_name='percentage');
writer.save();