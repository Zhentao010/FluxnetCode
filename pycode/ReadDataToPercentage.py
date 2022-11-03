import pandas as pd
import os
import numpy as np
import math
import xlwt
import xlrd

def dayValue(fileN):
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
                dayValue[i2+1][n] = eco['RECO_NT_VUT_REF'][i1];
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

def percentage(avermon):
    [avermonm, avermonn] = avermon.shape;
    perc = np.zeros((avermonm,avermonn),dtype=(float));
    for i in range(avermonn-1):
        sump = 0;
        if avermon[0][i+1] != 0:
            for j in range(avermonm-1):
                sump = sump + avermon[j+1][i+1];
                for j in range(avermonm-1):
                    perc[j+1][i+1] = avermon[j+1][i+1]/sump*100;
                perc[0,...] = avermon[0,...];
                perc[...,0] = avermon[...,0];
        else:
            continue;
    return perc

#写入文件函数
def save(data, path):
  f = xlwt.Workbook(); # 创建工作簿
  sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True) # 创建sheet
  [h, l] = data.shape # h为行数，l为列数
  for i in range(h):
    for j in range(l):
        if data[i, j] != 0:            
            sheet1.write(i, j, data[i, j])
            
    f.save(path)




#读取所需处理站点文件，返回需要读取的站点
def siteread(path):   # path为想要读取的excel文档
    file = xlrd.open_workbook(path); #打开想要读取的excel文档
    sheet = file.sheet_by_index(0);
    m = sheet.nrows;
    n = sheet.ncols;
    pathr = np.zeros((m-1,1));
    for i in range(n):
        if sheet.cell_values(0,i) == 'fluxnetid':
            for j in range(m):
                pathr[m][0] = sheet.cell_values(i,j);
        else:
            continue;
    return pathr
            
#第二版程序，不需要将输入文件分在不同的文件夹里，该程序可以根据输入excel信息进行自动的读取
#需要修改的数据仅有不同的path
path = 'F:/FLUXnet/OriginalData/FLUXNET/AllHourlyData/'  #储存原始数据的位置
pathsite = 'F:/FLUXnet/TreatedFluxNet/FluxnetInformation/fluxnet_site_info_all.xlsx'  #想要读取的站点信息excel文档，需经过筛选
path0 = ''  #储存计算得到的原始数据月平均值文件的位置
path1 = '' #储存百分比数据的位置
pathr = siteread(pathsite);
[m,n] = pathr.shape;
for csv_file in os.listdir(path):
    for i in range(m-1):
        if csv_file[4:10] == pathr[i][0]:
            print(csv_file);
            '''
            dayData = dayValue(path + csv_file);
            avermon = avermonth(dayData);
            perc = percentage(avermon);
            path2 = path0 + 'Avermon' + csv_file;
            path3 = path1 + 'Perc_' + csv_file;
            save(avermon,path2);
            save(perc,path3);
            '''



'''
#第一版程序，需要将原始文件手动剔出放到指定问价夹下读取
path = 'C:/Users/Lenovo/Desktop/fluxnetdata/TemperateOriginal/'
path1 = 'C:/Users/Lenovo/Desktop/fluxnetdata/temperatePercentageMonthly/'
for csv_file in os.listdir(path):
    dayData = dayValue(path + csv_file);
    avermon = avermonth(dayData);
    perc = percentage(avermon);
    path2 = path1 + 'Perc_' + csv_file;
    save(perc,path2);
'''

    
        
