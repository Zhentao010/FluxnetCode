# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:45:03 2022

@author: Lenovo
"""

import pandas as pd
import os
import numpy as np

path = 'C:/Users/Lenovo/Desktop/Regression/Original/';

for filename in os.listdir(path):
    data = pd.read_csv(path+filename);
    [m,n] = data.shape;
    a = [];
    for i in range(n):
        for j in range(m):
            if i == 0:
                if data['0.' + str(i)][j] != 0:
                    a.append(data[str('0.'+str(i))][j]);    
            else:
                if data['0.0.'+str(i)][j] != 0:
                    a.append(data['0.0.'+str(i)][j]);
    
    a = np.array(a);
    path2 = 'C:/Users/Lenovo/Desktop/Regression/total/' + filename + '.csv';
    a_pd = pd.DataFrame(a);
    a_pd.to_csv(path2, index= False, header= False);
            