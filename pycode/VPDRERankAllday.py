# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:46:15 2022

@author: Lenovo
"""


import pandas as pd
import os
import numpy as np
from sklearn import linear_model 
from scipy.stats import spearmanr

def VPDREdata(fileN):
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
           nightdata = np.row_stack((nightdata,a));
           nightdata[n1][0] = eco['TA_F_MDS'][i1];
           nightdata[n1][1] = eco['VPD_F_MDS'][i1];
           nightdata[n1][2] = eco['RECO_DT_VUT_REF'][i1];
           n1 = n1 +1;
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


def rank(dvalue):
    [m,n] = dvalue.shape;
    slope = np.zeros((1,int(n/2)));
    for i in range(int(n/2)):
        a = [];
        b = [];
        for i1 in range(m):
            if dvalue[i1][2*i+1] != 0:
               a.append(dvalue[i1][2*i]);
               b.append(dvalue[i1][2*i+1]);
        a = np.array(a);
        b = np.array(b);
        if len(a) != 0:
            coef, p= spearmanr(a, b);
            slope[0][i] = coef;
    return slope


path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #???????????????????????????
path0 = 'C:/Users/Lenovo/Desktop/??????????????????????????????/Vpd???RE_Allday_Rank/';  #?????????????????????VPD???????????????????????????
path1 = 'C:/Users/Lenovo/Desktop/';

T0 = -20;
Tn = 45;
dt = 0.5;
n = 2*int((Tn - T0)/dt + 1);

T = T0;
slope = np.zeros((1,int(n/2)));

for i in range(int(n/2)):
    slope[0][i] = T;
    T = T + dt;
        
for csv_file in os.listdir(path):
    dnightdata = VPDREdata(path + csv_file);
    dvalue = value(dnightdata,T0,Tn,dt);   ####????????? 1/dt????????????
                                           #????????????????????????re???vpd
    #????????????????????????
    path00 = path0 + csv_file[4:10] +'.xlsx';
    dvalue_pd = pd.DataFrame(dvalue);
    writer1 = pd.ExcelWriter(path00);
    dvalue_pd.to_excel(writer1, sheet_name='VPD+RESP');
    writer1.save();

    #???????????????????????????
    #???????????????
    slopei = rank(dvalue);
    print(slopei);
    slope = np.row_stack((slope,slopei));

path11 = 'C:/Users/Lenovo/Desktop/Rank0.5.xlsx'
slope_pd = pd.DataFrame(slope);
writer2 = pd.ExcelWriter(path11);
slope_pd.to_excel(writer2, sheet_name='Rank');
writer2.save();