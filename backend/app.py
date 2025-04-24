from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import requests
import time
import json

stock_list_tse = ['0050', '0056', '2330', '2317', '1216']
stock_list_otc = ['6547', '6180']
app = Flask(__name__)
CORS(app)

# 組合API需要的股票清單字串
stock_list1 = '|'.join('tse_{}.tw'.format(stock) for stock in stock_list_tse)

# 6字頭的股票參數不一樣
stock_list2 = '|'.join('otc_{}.tw'.format(stock) for stock in stock_list_otc)
stock_list = stock_list1 + '|' + stock_list2
query_url = f'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_list}'
response = requests.get(query_url)
data = json.loads(response.text)
@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    return data

if __name__ == '__main__':
    app.run(debug=True,port=5001)