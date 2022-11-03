# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:12:25 2022

@author: Zhentao Liu
"""

#将所有年份相同月的数据汇总到一起
path = 'C:\Users\Lenovo\Desktop\Percentage\';
fileExt = '*.xlsx';
files = dir(fullfile(path,fileExt));
len = size(files,1);
year96 = zeros(49,1);
year97 = zeros(49,1);
year98 = zeros(49,1);
year99 = zeros(49,1);
year00 = zeros(49,1);
year01 = zeros(49,1);
year02 = zeros(49,1);
year03 = zeros(49,1);
year04 = zeros(49,1);
year05 = zeros(49,1);
year06 = zeros(49,1);
year07 = zeros(49,1);
year08 = zeros(49,1);
year09 = zeros(49,1);
year10 = zeros(49,1);
year11 = zeros(49,1);
year12 = zeros(49,1);
year13 = zeros(49,1);
year14 = zeros(49,1);

a = [199601,199701,199801,199901,200001,200101,200201,200301,200401,200501,200601,200701,200801,200901,201001,201101,201201,201301,201401];

k = 0;

for i=1:len
    fileName = strcat(path,files(i,1).name);
    fileName = string(fileName);
    perc = xlsread(fileName);
    [m,n] = size(perc);
    for i0 = 2:n
        for j = 1:19
            if perc(1,i0) == a(1,j)
                k = j;
            else
                continue;
            end
            switch k
                case 1
                    year96 = [year96 perc(:,i0)];
                case 2
                    year97 = [year97 perc(:,i0)];
                case 3
                    year98 = [year98 perc(:,i0)];
                case 4
                    year99 = [year99 perc(:,i0)];
                case 5
                    year00 = [year00 perc(:,i0)];
                case 6
                    year01 = [year01 perc(:,i0)];
                case 7
                    year02 = [year02 perc(:,i0)];
                case 8
                    year03 = [year03 perc(:,i0)];
                case 9
                    year04 = [year04 perc(:,i0)];
                case 10
                    year05 = [year05 perc(:,i0)];
                case 11
                    year06 = [year06 perc(:,i0)];
                case 12
                    year07 = [year07 perc(:,i0)];
                case 13
                    year08 = [year08 perc(:,i0)];
                case 14
                    year09 = [year09 perc(:,i0)];
                case 15
                    year10 = [year10 perc(:,i0)];
                case 16
                    year11 = [year11 perc(:,i0)];
                case 17
                    year12 = [year12 perc(:,i0)];
                case 18
                    year13 = [year13 perc(:,i0)];
                case 19
                    year14 = [year14 perc(:,i0)];
            end
        end
    end
end
writematrix(year96,  '96'+ string('_Mon_') + '.xlsx');
writematrix(year97,  '97'+ string('_Mon_') + '.xlsx');
writematrix(year98,  '98'+ string('_Mon_') + '.xlsx');
writematrix(year99,  '99'+ string('_Mon_') + '.xlsx');
writematrix(year00,  '00'+ string('_Mon_') + '.xlsx');
writematrix(year01,  '01'+ string('_Mon_') + '.xlsx');
writematrix(year02,  '02'+ string('_Mon_') + '.xlsx');
writematrix(year03,  '03'+ string('_Mon_') + '.xlsx');
writematrix(year04,  '04'+ string('_Mon_') + '.xlsx');
writematrix(year05,  '05'+ string('_Mon_') + '.xlsx');
writematrix(year06,  '06'+ string('_Mon_') + '.xlsx');
writematrix(year07,  '07'+ string('_Mon_') + '.xlsx');
writematrix(year08,  '08'+ string('_Mon_') + '.xlsx');
writematrix(year09,  '09'+ string('_Mon_') + '.xlsx');
writematrix(year10,  '10'+ string('_Mon_') + '.xlsx');
writematrix(year11,  '11'+ string('_Mon_') + '.xlsx');
writematrix(year12,  '12'+ string('_Mon_') + '.xlsx');
writematrix(year13,  '13'+ string('_Mon_') + '.xlsx');
writematrix(year14,  '14'+ string('_Mon_') + '.xlsx');