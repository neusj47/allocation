# 자산배분전략
# 0. 데이터 불러오기
# 1. 모멘텀 값 생성하기 : 최근 모멘텀 값에 대한 가중치 높음, annualized 개념
# 2. 타깃 자산 선택하기 : Risk Asset on 일 경우, Risk Asset 중 최고값, 아닐 경우 Safe Asset 중 최고값
# 3. 수익률 생성하기
#.4. 성과 분석

import pandas_datareader as pdr
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import quantstats as qs

pd.options.display.float_format = '{:.4f}'.format
pd.set_option('display.max_columns', None)

start_day = datetime(2019,6,30)
end_day = datetime.today()

RA = ['SPY','QQQ','VEA','EEM']
SA = ['AGG','LQD','SCHB','DGRO']

# 0. 데이터 불러오기
def get_price_data(RA, SA):
    df = pd.DataFrame(columns=RA+SA)
    for ticker in RA + SA:
        df[ticker] = pdr.get_data_yahoo(ticker, start_day - timedelta(days=365), end_day)['Adj Close']
    return df

df = get_price_data(RA,SA)

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

mom_col_list = [col+'_Mom' for col in df[RA+SA].columns]
df[mom_col_list] = df[RA+SA].apply(lambda x: calc_momentum(x, df), axis=1)

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

df = df[start_day:end_day].resample(rule='M').last()
df[['Signal','Price']] = df.apply(lambda x: select_asset(x, mom_col_list), axis=1)

# 3. 수익률 생성하기

rtn_col_list = [col + '_rtn' for col in df[RA + SA].columns]
df[rtn_col_list] = df[RA + SA].pct_change()

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

result = get_return(df,rtn_col_list)
signal = result['Signal']
profit = result['PROFIT']/100

#.4. 성과 분석
qs.reports.basic(profit)