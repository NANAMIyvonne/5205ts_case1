import pandas as pd
import numpy as np

# change here
my_dict = 'E:\\M-22-T2\\ECON5206 FIN econ\\case1\\'

# read data

df_JPM = pd.read_csv(my_dict + 'JPM_1206_2206.csv')
df_JPM.sort_values(by="Date",inplace=True, ascending=True)
df_JPM=df_JPM.loc[:,['Date','Adj Close']] 
df_JPM['log_Return'] = 100*np.log(df_JPM['Adj Close']/df_JPM['Adj Close'].shift(1))
df_JPM=df_JPM.dropna()
# df_JPM

Tbill = pd.read_csv(my_dict +'DGS3MO.csv') 
Tbill.sort_values(by="DATE",inplace=True, ascending=True)
Tbill.columns= ['Date','Rf']
Tbill['Rf'] = pd.to_numeric(Tbill['Rf'], errors='coerce')
Tbill['log_Rf'] = 100*np.log(Tbill['Rf']/Tbill['Rf'].shift(1))
Tbill=Tbill.dropna()
# Tbill

SP500 = pd.read_excel(my_dict + 'SP500.xlsx') 
SP500['Date'] = SP500['Date'].astype(str) 
SP500.sort_values(by="Date",inplace=True, ascending=True)
SP500['SP500'] = pd.to_numeric(SP500['SP500'], errors='coerce')
SP500['log_SP500'] = 100*np.log(SP500['SP500']/SP500['SP500'].shift(1))
SP500=SP500.dropna()
# SP500

# merge
new_df = pd.merge(df_JPM,Tbill, on='Date')
new_df = pd.merge(new_df,SP500, on='Date')
new_df['R_JPM']= new_df['log_Return']-new_df['log_Rf']
new_df['R_MARKET']= new_df['log_SP500']-new_df['log_Rf']
new_df

# clean inf
new_df = new_df.replace([np.inf, -np.inf], np.nan).dropna()
new_df
