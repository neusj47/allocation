import pandas_datareader as pdr
import pandas as pd
from datetime import datetime, timedelta
import quantstats as qs

pd.options.display.float_format = '{:.4f}'.format
pd.set_option('display.max_columns', None)


# 0. 데이터 불러오기
def get_price_data(start_day, end_day, RA, SA):
    df = pd.DataFrame(columns=RA+SA)
    for ticker in RA + SA:
        df[ticker] = pdr.get_data_yahoo(ticker, start_day - timedelta(days=365), end_day)['Adj Close']
    return df

# 1. 모멘텀 값 생성하기
def calc_momentum(x, df):
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)
    try:
        before1 = df[x.name - timedelta(days=35):x.name - timedelta(days=30)].iloc[-1][0:8]
        before3 = df[x.name - timedelta(days=95):x.name - timedelta(days=90)].iloc[-1][0:8]
        before6 = df[x.name - timedelta(days=185):x.name - timedelta(days=180)].iloc[-1][0:8]
        before12 = df[x.name - timedelta(days=370):x.name - timedelta(days=365)].iloc[-1][0:8]

        momentum = 12 * (x / before1 - 1) + 4 * (x / before3 - 1) + 2 * (x / before6 - 1) + (x / before12 - 1)

    except Exception as e:
        # print("Error : ", str(e))
        pass
    return momentum

# 2. 타깃 자산 선택하기
def select_asset(x, mom_col_list):
    asset = pd.Series([0, 0], index=['Signal', 'Price'])
    if x[mom_col_list[0]] > 0 and x[mom_col_list[1]] > 0 and x[mom_col_list[2]] > 0 and x[mom_col_list[3]] > 0:
        max_momentum = max(x[mom_col_list[0]], x[mom_col_list[1]], x[mom_col_list[2]], x[mom_col_list[3]])
    else:
        max_momentum = max(x[mom_col_list[4]], x[mom_col_list[5]], x[mom_col_list[6]],x[mom_col_list[7]])

    asset['Signal'] = x[x == max_momentum].index[0].replace('_Mom', '')
    asset['Price'] = x[asset['Signal']]
    return asset

# 3. 수익률 생성하기 
def get_return(df,rtn_col_list):

    df['PROFIT'] = 0
    df['PROFIT_ACC'] = 0
    for i in range(len(df)):
        profit = 0
        if i != 0:
            profit = df[df.iloc[i - 1]['Signal'] + '_rtn'].iloc[i]
        df.loc[df.index[i], 'PROFIT'] = profit
        df.loc[df.index[i], 'PROFIT_ACC'] = (1 + df.loc[df.index[i - 1], 'PROFIT_ACC']) * (1 + profit) - 1
    df[['PROFIT', 'PROFIT_ACC']] = df[['PROFIT', 'PROFIT_ACC']] * 100
    df[rtn_col_list] = df[rtn_col_list] * 100
    return df

