import requests
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


def conv_to_list(obj):
    '''
    將物件轉換為list
    '''
    if not isinstance(obj, list):
        results = [obj]
    else:
        results = obj
    return results


def df_conv_col_type(df, cols, to, ignore=False):
    cols = conv_to_list(cols)
    for col in cols:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce').astype(to)
        except Exception as e:
            print(f"df_conv_col_type - 欄位 {col} 轉換失敗: {e}")
    return df


def date_get_today(with_time=False):
    '''
    取得今日日期，並指定為台北時區
    '''
    import pytz
    central = pytz.timezone('Asia/Taipei')

    if with_time == True:
        now = datetime.datetime.now(central)
    else:
        now = datetime.datetime.now(central).date()
    return now


# 下載證交所資料 ------
link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
data = pd.read_csv(link)
# ['證券代號', '證券名稱', '成交股數', '成交金額', '開盤價',
#  '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data.columns = ['STOCK_SYMBOL', 'NAME', 'TRADE_VOLUME', 'TRADE_VALUE',
                'OPEN', 'HIGH', 'LOW', 'CLOSE', 'PRICE_CHANGE', 'TRANSACTION', 'EXTRA_COLUMN']
# 標註今日日期
data['WORK_DATE'] = date_get_today()
cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]
# 除了證券代號外，其他欄位都是str，且部份資料中有''
data = data.replace('', np.nan, regex=True)
# 將data type轉為float
data = df_conv_col_type(df=data,
                        cols=['TRADE_VOLUME', 'TRADE_VALUE', 'OPEN', 'HIGH', 'LOW',
                              'CLOSE', 'PRICE_CHANGE', 'TRANSACTION'],
                        to='float')

