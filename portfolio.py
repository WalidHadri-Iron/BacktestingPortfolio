#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:57:03 2022

@author: juan
"""
import pandas as pd
import numpy as np
import get_data as gd
import matplotlib.pyplot as plt
def MonteCarlo(N:int,
               pi:pd.DataFrame,
               allShort:bool=True):
    
    if allShort:
        sign=-1
    else:
        sign=1
    
    sharpe=np.zeros(N)
    rp=np.zeros(N)
    cov=np.zeros(N)

    weights=np.zeros((N,pi.shape[1]))
    
    
    for i in range(N):
        weights[i,:]=sign*np.random.random(pi.shape[1])
        weights[i,:]=weights[i,:]/np.sum(np.abs(weights[i,:]))
        sharpe[i],rp[i],cov[i],_=getSharpe(pi, weights[i,:])
        
    
    return weights,sharpe,rp,cov


def getSharpe(df:pd.DataFrame,
               weights:np.array,
               rf:float=0.0):
    DAYS=252
    returns= df.diff()/df
    returns=returns.to_numpy()[1:]
    cov = np.cov(returns.T)
    rp = (returns.mean(0)*DAYS)@weights 
    rets = (returns)@weights 

    port_var = weights@(cov*DAYS)@weights 
    sharpe = (rp-rf)/np.sqrt(port_var)
    
    return sharpe,rp,port_var,rets


 


#%%

# data,ticks=gd.get_data()
# pi=data.drop(columns='SPY')
# pi=pi.drop(columns='Date') 
# #%%    
# weights,sharpes,rp,cov=MonteCarlo(10000,pi)    
# #%%
# plt.scatter(cov,rp,c=sharpes)


# ind=np.argmax(sharpes)
# indm=np.argmin(cov)
# plt.plot(cov[ind],rp[ind],'*r',label='max sharpe')
# plt.plot(cov[indm],rp[indm],'*m',label='min vol')
# plt.legend()
# plt.colorbar(label='Sharpe Ratio')
# plt.xlabel('Volatility')
# plt.ylabel('Return')
# plt.title('Sharpe Ratio')
# plt.show()

# #%%
#     #%%
# opt_weights=weights[np.argmax(sharpes)]
# _,_,_,ret=getSharpe(pi, opt_weights)
# spy=data['SPY']
# spy=spy.diff()/spy[1:]
 
# INITIAL_CAPITAL=1e6
# plt.plot(np.cumsum(ret)*INITIAL_CAPITAL,label='Portfolio')
# plt.plot(np.cumsum(spy)*INITIAL_CAPITAL,label='SPY')
# plt.legend()
# plt.title('')    
    
    
    
    