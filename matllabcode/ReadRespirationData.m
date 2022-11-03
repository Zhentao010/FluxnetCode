
path = 'C:\Users\Lenovo\Desktop\FLX_GL-ZaH_FLUXNET2015_FULLSET_HH_2000-2014_2-4.xlsx';
% ecoreValue = ecore(path);

%单个文件中生态系统呼吸数据读取函数
% function [ecoValue] = ecore(fileName)
    eco = readcell(path);
    [ecom, econ] = size(eco);
    DAYValue = zeros();
    n = 0;

    %--------------按时间顺序提取到ecoValue中--------------------------------
    for i0 = 1:econ
        if string(eco(1,i0)) == 'RECO_NT_VUT_REF'
            for i1 = 2:ecom
                DAYValue(i1-1,1) = round(eco{i1,1});
                DAYValue(i1-1,2) = eco{i1,i0};
            end
        else
            continue;
        end
    end
    %--------------按照每天提取到dayValue中----------------------------------
    [valuem,valuen] = size(DAYValue);
    
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
    for i0 = 1:valuem
        hour = mod(DAYValue(i0,1),10000);
        day = (DAYValue(i0,1) - hour)/10000;
        dayValue(1,n) = day;
        for i1 = 2:49
            if hour == dayValue(i1,1)
                dayValue(i1,n) = DAYValue(i0,2);
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



% end

%图形测试
