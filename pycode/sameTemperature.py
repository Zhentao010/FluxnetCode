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
from sklearn import linear_model 

def nightdata(fileN):
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    nightdata = np.zeros((10,3),dtype = float);
    a = np.zeros((1,3));
    n1 = 0;
    for i1 in range(ecom):
       hour = eco['TIMESTAMP_START'][i1]%10000;
       if hour <= 600 or hour>=1800:
           nightdata = np.row_stack((nightdata,a));
           nightdata[n1][0] = eco['TA_F_MDS'][i1];
           nightdata[n1][1] = eco['VPD_F_MDS'][i1];
           nightdata[n1][2] = eco['RECO_NT_VUT_REF'][i1];
           n1 = n1 +1;
       else:
           continue;
    return nightdata


def value(nightdata,T0,Tn,dt):  
    
    l = int((Tn - T0)/dt + 1);
    ecom = len(nightdata);

    dvalue = np.zeros((10,2*l),dtype = float);
    a = np.zeros((1,2*l));

    T = T0;
    for i0 in range(l):
        dvalue[0][i0*2] = T;
        T = T + dt;
    
    for i1 in range(ecom):
        for i2 in range(l):
            if nightdata[i1][0] >= dvalue[0][i2*2] - dt/2 and nightdata[i1][0] < dvalue[0][i2*2] + dt/2:
                if nightdata[i1][1] != -9999 and nightdata[i1][2] !=0 and nightdata[i1][2] != -9999:
                    dvalue[1][i2*2] = dvalue[1][i2*2] + 1;
                    b = list(dvalue[1,...]);
                    mm = max(b);
                    [m,n] = dvalue.shape;
                    if mm+2 > m:
                        dvalue = np.row_stack((dvalue,a));
                    dvalue[int(dvalue[1][i2*2])+ 1][i2*2] = nightdata[i1][1];
                    dvalue[int(dvalue[1][i2*2])+ 1][i2*2 + 1] = nightdata[i1][2];
    return dvalue


def regression(dvalue):
    [m,n] = dvalue.shape;
    slope = np.zeros((1,int(n/2)));
    for i in range(int(n/2)):
        a = [];
        b = [];
        for i1 in range(m):
            if dvalue[i1][2*i+1] != 0:
               a.append(dvalue[i1][2*i]);
               b.append(dvalue[i1][2*i+1]);
        regr = linear_model.LinearRegression();
        a = np.array(a);
        b = np.array(b);
        if len(a) != 0:
            regr.fit(a.reshape(-1,1),b);
            k = regr.coef_;
            slope[0][i] = k[0];
    return slope

path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #储存原始数据的位置
path0 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/夜间vpd和re/';  #储存计算得到的VPD月平均值文件的位置
path1 = 'C:/Users/Lenovo/Desktop/'
for csv_file in os.listdir(path):
    dnightdata = nightdata(path + csv_file);
    dvalue = value(dnightdata,-15,45,0.5); ####注意！ 1/dt要为整数
                                           #统计同一温度下的re和vpd
    #将统计的数据保存
    path00 = path0 + csv_file[4:10] +'.xlsx';
    dvalue_pd = pd.DataFrame(dvalue);
    writer1 = pd.ExcelWriter(path00);
    dvalue_pd.to_excel(writer1, sheet_name='VPD+RESP');
    writer1.save();
    
    #计算回归系数并汇总
    [m,n] = dvalue.shape;
    slope = np.zeros((1,int(n/2)));
    for i in range(int(n/2)):
        slope[0][i] = dvalue[0][2*i];        
    #求回归系数
    slopei = regression(dvalue);
    print(slopei);
    slope = np.row_stack((slope,slopei));


path11 = 'C:/Users/Lenovo/Desktop/slope.xlsx'
slope_pd = pd.DataFrame(slope);
writer2 = pd.ExcelWriter(path11);
slope_pd.to_excel(writer2, sheet_name='slope');
writer2.save();




