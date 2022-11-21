# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:45:21 2022

@author: Lenovo
"""

#相对湿度和RE的关系
import pandas as pd
import os
import numpy as np
from sklearn import linear_model 

def SWCREdata(fileN):
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    data = np.zeros((1,3));
    a = np.zeros((1,3));
    n1 = 0;
    for i1 in range(ecom):
       if eco['RECO_NT_VUT_REF'][i1] !=-9999 and eco['RH'][i1] !=-9999 and eco['RECO_NT_VUT_REF'][i1] !=0 and eco['RH'][i1] !=0:
           data[n1][0] = eco['TIMESTAMP_START'][i1];
           data[n1][1] = eco['RH'][i1];
           data[n1][2] = eco['RECO_NT_VUT_REF'][i1];
           data = np.row_stack((data,a));
           n1 = n1 +1;
    return data

def regression(data):
    [m,n] = data.shape;
    k = 0;
    a = [];
    b = [];
    for i in range(m):
        a.append(data[i][1]);
        b.append(data[i][2]);
    a = np.array(a);
    b = np.array(b);
    regr = linear_model.LinearRegression();
    regr.fit(a.reshape(-1,1),b);
    k = regr.coef_;
    return k


path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #储存原始数据的位置
path0 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/Night方法/相对湿度和RE/';  #储存计算得到的VPD月平均值文件的位置
path1 = 'C:/Users/Lenovo/Desktop/'; #

slope = [];

for csv_file in os.listdir(path):
    eco = pd.read_csv(path + csv_file);
    if 'RH' in eco.columns:
        data = SWCREdata(path + csv_file);
        #将统计的数据保存
        path00 = path0 + csv_file[4:10] +'.xlsx';
        data_pd = pd.DataFrame(data);
        writer1 = pd.ExcelWriter(path00);
        data_pd.to_excel(writer1, sheet_name='TIME_SWM_RESP');
        writer1.save();
        #计算回归系数并汇总
        #求回归系数
        k= regression(data);
        print(k);
        slope.append(k);
    
slopearray = np.array(slope);
path11 = 'C:/Users/Lenovo/Desktop/RH_RESP_Slope.xlsx'
slope_pd = pd.DataFrame(slopearray);
writer2 = pd.ExcelWriter(path11);
slope_pd.to_excel(writer2, sheet_name='slope');
writer2.save();