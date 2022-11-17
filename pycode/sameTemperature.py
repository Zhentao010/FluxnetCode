# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:42:25 2022

@author: Lenovo
"""

'''
统计夜间同一温度下的VPD和RESP数据
'''

import pandas as pd
import os
import numpy as np

def nightdata(fileN):
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    nightdata = np.zeros((ecom,3),dtype = float);
    n1 = 0;
    for i1 in range(ecom):
       hour = eco['TIMESTAMP_START'][i1]%10000;
       if hour <= 600 or hour>=1800:
           nightdata[n1][0] = eco['TA_F_MDS'][i1];
           nightdata[n1][1] = eco['VPD_F_MDS'][i1];
           nightdata[n1][2] = eco['RECO_NT_VUT_REF'][i1];
           n1 = n1 +1;
       else:
           continue;
    return nightdata


def value(nightdata):  
    
    ecom = len(nightdata);

    dvalue = np.zeros((10,102),dtype = float);
    a = np.zeros((1,102));

    T = -10;
    for i0 in range(51):
        dvalue[0][i0*2] = T;
        T = T + 1;
    
    for i1 in range(ecom):
        for i2 in range(51):
            if nightdata[i1][0] >= dvalue[0][i2*2] - 0.5 and nightdata[i1][0] < dvalue[0][i2*2] + 0.5:
                dvalue[1][i2*2] = dvalue[1][i2*2] + 1;
                b = list(dvalue[1,...]);
                mm = max(b);
                print(mm)
                [m,n] = dvalue.shape;
                print(m)
                if mm+2 > m:
                    dvalue = np.row_stack((dvalue,a));
               
                dvalue[int(dvalue[1][i2*2])+ 1][i2*2] = nightdata[i1][1];
                dvalue[int(dvalue[1][i2*2])+ 1][i2*2 + 1] = nightdata[i1][2];
            else:
                continue;
            
    return dvalue


path = 'D:/Data/FLUXnet/OriginalData/FLUXNET/AllHourlyData/';  #储存原始数据的位置
path0 = 'C:/Users/111/Desktop/处理后数据/夜间同一温度下的VPD和RESP/';  #储存计算得到的VPD月平均值文件的位置

for csv_file in os.listdir(path):
    dnightdata = nightdata(path + csv_file);
    dvalue = value(dnightdata);         ####
                                        #统计同一温度下的re和vpd
    path00 = path0 + csv_file[4:10] +'.xlsx';
    dvalue_pd = pd.DataFrame(dvalue);
    writer1 = pd.ExcelWriter(path00);
    dvalue_pd.to_excel(writer1, sheet_name='VPD+RESP');
    writer1.save();


