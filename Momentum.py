# -*- coding: utf-8 -*-
"""
Lecture 8
"""

import datetime as dt 
import pandas as pd
import numpy as np
import os
os.chdir("C:/Users/Raji/Desktop/Udemy/Udemy - Quant Finance")

nifty= pd.read_excel("QuantStrategy.xlsx",header=0,parse_cols="B:C",index_col=0)
nifty.index
nifty.sort_index(inplace=True)
nifty["Daily Returns"]=nifty["Price"].pct_change()
nifty.head()
nifty["Log Returns"]=np.log(nifty["Daily Returns"]+1)
nifty.tail()

#Find 75 past day sum
nifty["75 past day sum"]=nifty["Log Returns"].shift(periods=1).rolling(window=75).sum().tail()

#Find 75 past day sd
nifty["75 past day sd"]=nifty["Log Returns"].shift(periods=1).rolling(window=75).std().tail()

#Find momentum
nifty["momentum"]=nifty["75 past day sum"]/nifty["75 past day sd"]
nifty.tail()


# getting first day of each month.
nifty.groupby([nifty.index.year,nifty.index.month]).first()


nifty.drop("tday",axis=1,inplace=True)
def trading_days(x):
    s=1
    tday=[1]
    
    for i in range(1,x.shape[0]):
        if x[i].month==x[i-1].month:
            s+=1
            tday.append(s)
        elif i==x.shape[0]-1:
            if x[i].month==x[i-1].month:
                s+=1
                tday.append(s)
            else:
                s=1
                tday.append(s)
        else:
            s=1
            tday.append(s)
    return pd.DataFrame(tday)

a=trading_days(nifty.index)
a.index=nifty.index
a.column="tday"
nifty=pd.merge(nifty,a,left_index=True, right_index=True)     



"""
This is going to be an important one
"""

"""
Will need to add in monthly momentum calculations
"""








