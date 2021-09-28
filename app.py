from stream_AA import *
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

st.title('ASSET_ALLOCATION Backtesting')

st.write('Backtest Asset-Allocation strategies using Quantstats packages')

start_date = st.date_input('Select start_date')
end_date = datetime.today()

TICKER_1 = {'MSCI WORLD' : 'URTH',
          'Developed Market' : 'VEA',
          'Asia' : 'VPL',
          'Asia w/o JPN' : 'EPP',
          'Europe' : 'VGK',
          'Emerging Market' : 'EMM',
          'Asia Emerging' : 'GMF',
          'S&P' : 'SPY',
          'NASDAQ' : 'QQQ',
          'Latin America' : 'ILF',
          'Brazil' : 'EWZ',
          'Mexico' : 'EWW',
          'Canada' : 'EWC',
          'Hongkong' : 'EWH',
          'China' : 'GXC',
          'Japan' : 'EWJ',
          'India' : 'INDY',
          'Vietnam' : 'VNM',
          'Austrailia' : 'EWA',
          'Germany' : 'EWG',
          'England' : 'EWU',
          'France' : 'EWQ'}
selected_stock_key_1 = st.selectbox('Select "RA1" you want to backtest', list(TICKER_1.keys()))
selected_stock_value_1 = TICKER_1[selected_stock_key_1]

TICKER_2 = {'MSCI WORLD' : 'URTH',
          'Developed Market' : 'VEA',
          'Asia' : 'VPL',
          'Asia w/o JPN' : 'EPP',
          'Europe' : 'VGK',
          'Emerging Market' : 'EMM',
          'Asia Emerging' : 'GMF',
          'S&P' : 'SPY',
          'NASDAQ' : 'QQQ',
          'Latin America' : 'ILF',
          'Brazil' : 'EWZ',
          'Mexico' : 'EWW',
          'Canada' : 'EWC',
          'Hongkong' : 'EWH',
          'China' : 'GXC',
          'Japan' : 'EWJ',
          'India' : 'INDY',
          'Vietnam' : 'VNM',
          'Austrailia' : 'EWA',
          'Germany' : 'EWG',
          'England' : 'EWU',
          'France' : 'EWQ'}
selected_stock_key_2 = st.selectbox('Select "RA2" you want to backtest', list(TICKER_2.keys()))
selected_stock_value_2 = TICKER_2[selected_stock_key_2]

TICKER_3 = {'MSCI WORLD' : 'URTH',
          'Developed Market' : 'VEA',
          'Asia' : 'VPL',
          'Asia w/o JPN' : 'EPP',
          'Europe' : 'VGK',
          'Emerging Market' : 'EMM',
          'Asia Emerging' : 'GMF',
          'S&P' : 'SPY',
          'NASDAQ' : 'QQQ',
          'Latin America' : 'ILF',
          'Brazil' : 'EWZ',
          'Mexico' : 'EWW',
          'Canada' : 'EWC',
          'Hongkong' : 'EWH',
          'China' : 'GXC',
          'Japan' : 'EWJ',
          'India' : 'INDY',
          'Vietnam' : 'VNM',
          'Austrailia' : 'EWA',
          'Germany' : 'EWG',
          'England' : 'EWU',
          'France' : 'EWQ'}
selected_stock_key_3 = st.selectbox('Select "RA3" you want to backtest', list(TICKER_3.keys()))
selected_stock_value_3 = TICKER_3[selected_stock_key_3]

TICKER_4 = {'MSCI WORLD' : 'URTH',
          'Developed Market' : 'VEA',
          'Asia' : 'VPL',
          'Asia w/o JPN' : 'EPP',
          'Europe' : 'VGK',
          'Emerging Market' : 'EMM',
          'Asia Emerging' : 'GMF',
          'S&P' : 'SPY',
          'NASDAQ' : 'QQQ',
          'Latin America' : 'ILF',
          'Brazil' : 'EWZ',
          'Mexico' : 'EWW',
          'Canada' : 'EWC',
          'Hongkong' : 'EWH',
          'China' : 'GXC',
          'Japan' : 'EWJ',
          'India' : 'INDY',
          'Vietnam' : 'VNM',
          'Austrailia' : 'EWA',
          'Germany' : 'EWG',
          'England' : 'EWU',
          'France' : 'EWQ'}
selected_stock_key_4 = st.selectbox('Select "RA4" you want to backtest', list(TICKER_4.keys()))
selected_stock_value_4 = TICKER_4[selected_stock_key_4]

TICKER_5 = {'AGG' : 'AGG',
          'LQD' : 'LQD',
          'SCHB' : 'SCHB',
          'DGRO' : 'DGRO'}
selected_stock_key_5 = st.selectbox('Select "SA1" you want to backtest', list(TICKER_5.keys()))
selected_stock_value_5 = TICKER_5[selected_stock_key_5]

TICKER_6 = {'AGG' : 'AGG',
          'LQD' : 'LQD',
          'SCHB' : 'SCHB',
          'DGRO' : 'DGRO'}
selected_stock_key_6 = st.selectbox('Select "SA2" you want to backtest', list(TICKER_6.keys()))
selected_stock_value_6 = TICKER_6[selected_stock_key_6]

TICKER_7 = {'AGG' : 'AGG',
          'LQD' : 'LQD',
          'SCHB' : 'SCHB',
          'DGRO' : 'DGRO'}
selected_stock_key_7 = st.selectbox('Select "SA3" you want to backtest', list(TICKER_7.keys()))
selected_stock_value_7 = TICKER_7[selected_stock_key_7]

TICKER_8 = {'AGG' : 'AGG',
          'LQD' : 'LQD',
          'SCHB' : 'SCHB',
          'DGRO' : 'DGRO'}
selected_stock_key_8 = st.selectbox('Select "SA4" you want to backtest', list(TICKER_8.keys()))
selected_stock_value_8 = TICKER_8[selected_stock_key_8]

RA = [selected_stock_value_1, selected_stock_value_2, selected_stock_value_3, selected_stock_value_4]
SA = [selected_stock_value_5, selected_stock_value_6, selected_stock_value_7, selected_stock_value_8]

df = get_price_data(start_date,end_date,RA,SA)
mom_col_list = [col+'_Mom' for col in df[RA+SA].columns]
df[mom_col_list] = df[RA+SA].apply(lambda x: calc_momentum(x, df), axis=1)
df = df[start_date:end_date].resample(rule='M').last()
df[['Signal','Price']] = df.apply(lambda x: select_asset(x, mom_col_list), axis=1)
rtn_col_list = [col + '_rtn' for col in df[RA + SA].columns]
df[rtn_col_list] = df[RA + SA].pct_change()
result = get_return(df,rtn_col_list)
signal = result['Signal']
profit = result['PROFIT']/100


# qs.reports.basic(profit)

signal

st.write('Cumulative Return')
fig = plt.figure(figsize=(17,7))
plt.title('Asset Allocation Strategy Return')
plt.plot((1 + profit).cumprod() - 1, label = 'AA_Momentum')
plt.legend()
plt.show()
st.pyplot(fig)

