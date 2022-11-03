%将每天的数据汇总到一起
path = 'C:\Users\Lenovo\Desktop\TemperateOriginal\';
fileExt = '*.csv';
files = dir(fullfile(path,fileExt));
len = size(files,1);
for i=1:len
    fileName = strcat(path,files(i,1).name);
    fileName = string(fileName);
    dayValue = ecore(fileName);
    avermon = avermonth(dayValue);
    perc = percentage(avermon);
    filename = char(fileName);
    writematrix(avermon,'RECO_' + string(filename(47:53)) + '.xlsx')
end

%单个文件中生态系统呼吸数据读取函数
function [dayValue] = ecore(fileName)
    eco = readcell(fileName);
    [ecom, econ] = size(eco);
    dayValue = zeros();
   
    t = 0;
    for i = 1:48
        dayValue(i+1,1) = t;
        if mod(i,2) == 1
            t = t+30;
        else
            t = t+70;
        end
    end

    n = 2;
    for i = 1:econ
        if string(eco(1,i)) == 'RECO_NT_VUT_REF'
            for i0 = 2:ecom
                hour = mod(eco{i0,1},10000);
                day = (eco{i0,1} - hour)/10000;
                dayValue(1,n) = day;
                for i1 = 2:49
                    if hour == dayValue(i1,1)
                        dayValue(i1,n) = eco{i0,i};
                    else
                        continue;
                    end
                end
                if hour == 2330
                    n = n+1;
                else
                    continue;
                end
            end
        else
            continue;
        end
    end
end

%计算每个月的均值
function [avermon] = avermonth(dayValue)
    [m,n] =size(dayValue);
    dayValue = [dayValue zeros(m,1)];
    [m,n] =size(dayValue);
    dayValue = [dayValue,zeros(m,1)];
    avermon = zeros(49,ceil((n-1)/365)*12+1);

    i0 = 1;
    t = 0;
    for i = 1:48
        avermon(i+1,1) = t;
        if mod(i,2) == 1
            t = t+30;
        else
            t = t+70;
        end
    end

    i1 = 0;
    for i = 2:n-1
       for j = 1:12
           if floor(mod(dayValue(1,i),10000)/100) == j
               i1 = i1 +1;
               avermon(1,(i0-1)*12+j+1) = floor(dayValue(1,i)/100);
               for k = 2:m
                   avermon(k,(i0-1)*12+j+1) = avermon(k,(i0-1)*12+j+1) + dayValue(k,i);
               end
           else
               continue;
           end
           if floor(mod(dayValue(1,i+1),10000)/100) ~= floor(mod(dayValue(1,i),10000)/100)
               for j1 = 2:m
                   avermon(j1,(i0-1)*12+j+1) = avermon(j1,(i0-1)*12+j+1)/i1;
               end
               i1 = 0;
           else
               continue;
           end
       end
       if mod(dayValue(1,i),10000) == 1231
           i0 = i0 + 1;
       else
           continue;
       end
    end
end


%求百分比
function [perc] = percentage(avermon)
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
end