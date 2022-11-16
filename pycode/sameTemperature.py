# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:42:25 2022

@author: Lenovo
"""

import pandas as pd
import os
import numpy as np


def value(fileN):  #variable 为想要统计的量
    eco = pd.read_csv(fileN);
    ecom = len(eco);

    dvalue = np.zeros((10,122),dtype = float);
    a = np.zeros((1,122));
    
    T = -20;
    for i0 in range(61):
        dvalue[0][i0*2] = T;
        T = T + 1;
    
    for i1 in range(ecom):
        for i2 in range(61):
            if eco['TA_F_MDS'][i1] >= dvalue[0][i2*2] - 0.5 and eco['TA_F_MDS'][i1] < dvalue[0][i2*2] + 0.5:
                dvalue[1][i2*2] = dvalue[1][i2*2] + 1;
                b = list(dvalue[1,...]);
                mm = max(b);
                if mm < dvalue[1][i2*2]:
                    dvalue = np.row_stack((dvalue,a));
               
                dvalue[int(dvalue[1][i2*2])+ 1][i2*2] = eco['VPD_F_MDS'][i1];
                dvalue[int(dvalue[1][i2*2])+ 1][i2*2 + 1] = eco['RECO_NT_VUT_REF'][i1];
                    
            else:
                continue;
            
    return dvalue


path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #储存原始数据的位置
path0 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/同温度下VPD和RE/';  #储存计算得到的VPD月平均值文件的位置

for csv_file in os.listdir(path):
    dvalue = value(path + csv_file);  ####
                                      #统计同一温度下的re和vpd
    path00 = path0 + csv_file[4:10] +'.xlsx';
    dvalue_pd = pd.DataFrame(dvalue);
    writer1 = pd.ExcelWriter(path00);
    dvalue_pd.to_excel(writer1, sheet_name='Respiration');
    writer1.save();


