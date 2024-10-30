import yfinance as yf
import requests
import os
import pandas as pd
import time


daftar = os.path.join(os.path.dirname(__file__), 'DaftarSaham.xls')

def dl_stock(stock):
    kode = f"{stock}.JK"
    df = yf.download(kode)
    print(df.head())
    df.to_csv(f"./data/{stock}.csv")


df = pd.read_excel(daftar)
for i,j in df.iterrows():
    if (i < 5):
        dl_stock(j['Kode'])
        time.sleep(2)
    

            
    
    