# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:15:00 2022

@author: Lenovo
"""

import pandas as pd
import os
import numpy as np
import xlwt
import math

def dataTransfer(fileN):
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    upData = np.zeros((ecom,5),dtype = float);
    downData = np.zeros((ecom,5),dtype = float);

    n1 = 0;
    n2 = 0;
    for i1 in range(ecom):
       hour = eco['TIMESTAMP_START'][i1]%10000;
       if hour>=530 and hour<=1430:
           upData[n1][0] = eco['TIMESTAMP_START'][i1];
           upData[n1][1] = eco['TA_F_MDS'][i1];
           upData[n1][2] = eco['RECO_NT_VUT_REF'][i1];
           upData[n1][3] = 1000/(eco['TA_F_MDS'][i1]+273);
           upData[n1][4] = np.log(eco['RECO_NT_VUT_REF'][i1]);
           n1 = n1 +1;
       else:
           downData[n2][0] = eco['TIMESTAMP_START'][i1];
           downData[n2][1] = eco['TA_F_MDS'][i1];
           downData[n2][2] = eco['RECO_NT_VUT_REF'][i1];
           downData[n2][3] = 1000/(eco['TA_F_MDS'][i1]+273);
           downData[n2][4] = np.log(eco['RECO_NT_VUT_REF'][i1]);
           n2 = n2 + 1;
    return upData, downData


#写入文件函数
def save(data, path):
    f = xlwt.Workbook(); # 创建工作簿
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True) # 创建sheet
    [h, l] = data.shape # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i, j]);
    f.save(path);


path = 'C:/Users/Lenovo/Desktop/china/';  #储存原始数据的位置
for csv_file in os.listdir(path):
    a = csv_file[4:10];
    path1 = 'C:/Users/Lenovo/Desktop/dayValue/' + a + '.xlsx';
    upData, downData = dataTransfer(path + csv_file);
    
    upData_pd = pd.DataFrame(upData);
    downData_pd = pd.DataFrame(downData);
    writer = pd.ExcelWriter(path1);
    upData_pd.to_excel(writer, sheet_name='up');
    downData_pd.to_excel(writer, sheet_name='down');
    writer.save();

    