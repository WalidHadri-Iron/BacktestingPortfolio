#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 10:03:25 2022

@author: juan
"""
import yfinance as yf  
import pandas as pd

def get_data(tics:list=None):
    '''
    

    Parameters
    ----------
    tics : list, list of tickers. If None, it takes some ETFs as default.

    Returns
    -------
    data : pandas.DataFrame
        Pandas dataframe contaning the time, and close value for each tick
        

    '''
    
    if tics is None:
        print('running with default list of tickers')
        
#         tics = ['DUST','NUGT',
#                 'LABD','LABU',
#                 'YINN','YANG',
#                 'EDZ','EDC']
#                 'ERY','ERX']

        tics=['FAZ','FAS',
                 'HIBL','HIBS',
                 'LABD','LABU',
                 'NUGT','DUST',
                 'SOXL','SOXS',
                 'YINN','YANG',
                 'EDZ','EDC',
                 'TNA','TZA',
                 'ERX','ERY',
                 'TMV','TMF',
                 'TYO','TYD']
        
    #'SPY'
#     dust/nugt/labd/labu/yinn/yang/ edz/edc/ery/erx
    
    spy = yf.download('SPY','2020-01-01','2022-07-01')
    data=pd.DataFrame(spy.index)
    data['SPY']=spy["Adj Close"].array
    
    for ticker in tics:
        
    
        print('querrying '+ticker+" ...")
        
        aux = yf.download(ticker,'2020-01-01','2022-07-01')
        data[ticker]=aux["Adj Close"].array
    return data,tics

# if __name__ =='__main__':
#     data,tics=get_data()
    