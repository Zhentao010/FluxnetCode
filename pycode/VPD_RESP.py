# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:59:08 2022

@author: Lenovo
"""



import pandas as pd
import os
import numpy as np
from sklearn import linear_model 

def DTRSWC(filename):          #读取昼夜温差，VPD和土壤含水量
    dtrswc = pd.read_csv(filename);
    m = len(dtrswc);
    data = np.zeros((m,2),dtype = float);
    for i in range(m):
        if dtrswc['TA_F_MDS'][i] >= 20 and dtrswc['TA_F_MDS_DAY'][i] <= 21: 
            data[i][0] = dtrswc['VPD_F_MDS'][i]
            data[i][1] = dtrswc['RECO_NT_VUT_REF'][i];
        else:
            data[i][0] = -9999;
            data[i][1] = -9999;
    return data
        
def regression(a,b):
    k = 0;
    a = np.array(a);
    b = np.array(b);   
    regr = linear_model.LinearRegression();
    regr.fit(a.reshape(-1,1),b);
    k = regr.coef_;
    return k

path = 'D:/Data/fluxnet/OriginalData/AllDailyData/';  #储存原始数据的位置
path1 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/原始数据VPD_RESP/';    #储存读取的DTR_VPD_SWC数据的位置
path2 = 'C:/Users/Lenovo/Desktop/VPD_RESP_Slope.xlsx'    #储存计算的相关系数的位置
slope = np.zeros((1,1));
addslope = np.zeros((1,1));
nslope = 0;

for csv_file in os.listdir(path):
    print(csv_file);
    data = DTRSWC(path + csv_file);
    path11 = path1 + csv_file[4:10] +'.xlsx';
    data_pd = pd.DataFrame(data);
    writer1 = pd.ExcelWriter(path11);
    data_pd.to_excel(writer1, sheet_name='DTR_VPD_SWC');
    writer1.save();
    
    [m,n] = data.shape;
    for i in range(n-1):
        a = [];
        b = [];
        if max(list(data[...,i+1])) != 0:
            for j in range(m):
                    if data[j][0] != -9999 and data[j][i+1] != -9999:
                        a.append(data[j][0]);
                        b.append(data[j][i+1]);
            if len(b) != 0:
                slopei = regression(a, b);
                slope[nslope][i] = slopei;   
    print(slope[nslope,...]);
    nslope = nslope + 1;
    slope = np.row_stack((slope,addslope));
slopearray = np.array(slope);
slope_pd = pd.DataFrame(slopearray);
writer2 = pd.ExcelWriter(path2);
slope_pd.to_excel(writer2, sheet_name='slope');
writer2.save();