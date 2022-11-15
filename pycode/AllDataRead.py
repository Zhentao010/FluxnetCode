# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:42:32 2022

@author: Lenovo
"""


import pandas as pd
import os
import numpy as np
import xlwt


def dataTransfer(fileN):
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    Data = np.zeros((ecom,6),dtype = float);
    n=0;
    for i1 in range(ecom):
        if eco['RECO_NT_VUT_REF'][i1] != -9999:
            Data[n][0] = eco['TIMESTAMP_START'][i1];
            Data[n][1] = eco['TA_F_MDS'][i1];
            Data[n][2] = eco['VPD_F_MDS'][i1];
            Data[n][3] = eco['RECO_NT_VUT_REF'][i1];
            Data[n][4] = 1000/(eco['TA_F_MDS'][i1]+273);
            Data[n][5] = np.log(eco['RECO_NT_VUT_REF'][i1]);
            n = n+1;
        else:
            continue;
    return Data


#写入文件函数
def save(data, path):
    f = xlwt.Workbook(); # 创建工作簿
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True) # 创建sheet
    [h, l] = data.shape # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i, j]);
    f.save(path);


path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #储存原始数据的位置
for csv_file in os.listdir(path):
    a = csv_file[4:10];
    path1 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/RespTempVpd/' + a + '.xlsx';
    Data = dataTransfer(path + csv_file);
    Data_pd = pd.DataFrame(Data);
    writer = pd.ExcelWriter(path1);
    Data_pd.to_excel(writer, sheet_name='Sheet1');
    writer.save();