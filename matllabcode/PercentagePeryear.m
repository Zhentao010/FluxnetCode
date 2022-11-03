%将每年各月的数据求平均值
path = 'C:\Users\Lenovo\Desktop\MonthAverage\';
fileExt = '*.xlsx';
files = dir(fullfile(path,fileExt));
len = size(files,1);
for i=1:len
    fileName = strcat(path,files(i,1).name);
    fileName = string(fileName);
    perc = percentage(fileName);
    filename = char(fileName);
    writematrix(perc,'PERC_' + string(filename(42:47)) + '.xlsx')
end

function [perc] = percentage(fileName)
    avermon = xlsread(fileName);
    [m,n] = size(avermon);
    perc = zeros();
    for i = 2:n
        sump = 0;
        for j = 2:m
            sump = sump + avermon(j,i);
        end
        for j = 2:m
            perc(j,i) = avermon(j,i)/sump*100;
        end
    end
    perc(1,:) = avermon(1,:);
    perc(:,1) = avermon(:,1);
end