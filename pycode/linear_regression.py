# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:13:38 2022

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from scipy.stats import chi2_contingency

xlsx = pd.ExcelFile(r'C:/Users/Lenovo/Desktop/test/test9.xlsx');

updata = pd.read_excel(xlsx,'Sheet1');
downdata = pd.read_excel(xlsx,'Sheet2');
#升温数据的拟合
sns.lmplot(x='t', y='r', data = updata, legend_out=False, truncate=True);
plt.show;
fit1 = sm.formula.ols('t~r',data=updata).fit();
print(fit1.params);
#降温数据的拟合
sns.lmplot(x='t', y='r', data = downdata, legend_out=False, truncate=True);
plt.show;
fit2 = sm.formula.ols('t~r',data = downdata).fit();
print(fit2.params);