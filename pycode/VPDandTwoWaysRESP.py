# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:22:06 2022

@author: Lenovo
"""
#此般的目的在于读取night和day两种方法的数据到同一列中，用于看VPD对RESP的影响

#第一列时间、第二列温度、第三列呼吸作用、第四列温度转换、第五列VPD转换

import pandas as pd
import os
import numpy as np

def dataTransfer(fileN):
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    Data = np.zeros((ecom,6),dtype = float);

    n1 = 0;
    for i1 in range(ecom):
       hour = eco['TIMESTAMP_START'][i1]%10000;
       if hour>=600 and hour<=1800:
           Data[n1][0] = eco['TIMESTAMP_START'][i1];
           Data[n1][1] = eco['TA_F_MDS'][i1];
           Data[n1][2] = eco['RECO_DT_VUT_REF'][i1];
           Data[n1][3] = eco['VPD_F_MDS'][i1];
           Data[n1][4] = 1000/(eco['TA_F_MDS'][i1]+273);
           Data[n1][5] = np.log(eco['RECO_DT_VUT_REF'][i1]);
           n1 = n1 +1;
       else:
           Data[n1][0] = eco['TIMESTAMP_START'][i1];
           Data[n1][1] = eco['TA_F_MDS'][i1];
           Data[n1][2] = eco['RECO_NT_VUT_REF'][i1];
           Data[n1][3] = eco['VPD_F_MDS'][i1];
           Data[n1][4] = 1000/(eco['TA_F_MDS'][i1]+273);
           Data[n1][5] = np.log(eco['RECO_NT_VUT_REF'][i1]);
           n1 = n1 + 1;
    return Data


path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #储存原始数据的位置
for csv_file in os.listdir(path):
    a = csv_file[4:10];
    path1 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/Day方法/VPD和两种方法的RESP/' + a + '.xlsx';
    Data = dataTransfer(path + csv_file);
    
    Data_pd = pd.DataFrame(Data);
    writer = pd.ExcelWriter(path1);
    Data_pd.to_excel(writer, sheet_name='sheet1');
    writer.save();