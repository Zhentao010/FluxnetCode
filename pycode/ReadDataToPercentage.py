import pandas as pd
import os
import numpy as np
import math


def dayValue(fileN,variable):  #variable 为想要统计的量
    eco = pd.read_csv(fileN);
    ecom = len(eco);
    days = math.ceil(ecom/48)+1;
    dayValue = np.zeros((49,days),dtype = float);
    
    t = 0;
    for i0 in range(48):
        dayValue[i0+1][0] = t;
        if (i0+1)%2 == 1:
            t = t + 30;
        else:
            t = t +70;
    n = 1;
    for i1 in range(ecom):
        hour = eco['TIMESTAMP_START'][i1]%10000;
        day = math.floor(eco['TIMESTAMP_START'][i1]/10000);
        dayValue[0][n] = day;
        for i2 in range(48):
            if hour == dayValue[i2+1][0]:
                dayValue[i2+1][n] = eco[variable][i1];
            else:
                continue;
        if hour == 2330:
            n = n + 1;
        else:
            continue;
    return dayValue

def avermonth(dayValue):
    daym = len(dayValue);
    dayn = int(dayValue.size/daym);
    adday = np.zeros((daym,1));
    dayValue = np.insert(dayValue, dayn, adday, axis = 1);
    avermon = np.zeros((49,math.ceil((dayn-1)/365)*12+1));
    
    i0 = 1;
    t = 0;
    for i in range(48):
        avermon[i+1][0] = t;
        if (i+1)%2 == 1:
            t = t +30;
        else:
            t = t +70;
    i1 = 0;
    for i in range(dayn-1):
        for j in range(12):
            if math.floor((dayValue[0][i+1]%10000)/100) == j+1:
                i1 = i1+1;
                avermon[0][(i0-1)*12+j+1] = math.floor(dayValue[0][i+1]/100);
                for k in range(daym-1):
                    avermon[k+1][(i0-1)*12+j+1] = avermon[k+1][(i0-1)*12+j+1] + dayValue[k+1][i+1];
            else:
                    continue;
            if math.floor((dayValue[0][i+2]%10000)/100) != math.floor((dayValue[0][i+1]%10000)/100):
                for j1 in range(daym-1):
                    avermon[j1+1][(i0-1)*12+j+1] = avermon[j1+1][(i0-1)*12+j+1]/i1;
                i1 = 0;
            else:
                continue;
        if dayValue[0][i+1]%10000 == 1231:
            i0 = i0 +1;
        else:
            continue;
    return avermon


path = 'D:/Data/fluxnet/OriginalData/AllHourlyData/';  #储存原始数据的位置
path0 = 'C:/Users/Lenovo/Desktop/未划分年份的初级数据/土壤水分月平均值/';  #储存计算得到的VPD月平均值文件的位置

for csv_file in os.listdir(path):
    eco = pd.read_csv(path + csv_file);
    if 'SWC_F_MDS_1' in eco.columns:
        dayDataSWC = dayValue(path + csv_file,'SWC_F_MDS_1');  ##
        avermonSWC = avermonth(dayDataSWC);                    #统计RESP的月平均值
                                                               #统计温度的月平均值
        path00 = path0 + csv_file[4:10] +'.xlsx';
        avermonSWC_pd = pd.DataFrame(avermonSWC);
                                                           
        writer1 = pd.ExcelWriter(path00);
        avermonSWC_pd.to_excel(writer1, sheet_name='SWC');
        writer1.save();

