from flask_cors import CORS
import requests
import pandas as pd
from io import StringIO
from flask import Flask, jsonify
import json

app = Flask(__name__)
CORS(app)

query_url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
response = requests.get(query_url)

# 判斷 API 呼叫是否成功
if response.status_code != 200:
    raise Exception('取得股票資訊失敗。')
else:
    print(response.text)

# 解析 CSV 資料
csv_data = StringIO(response.text)
data = pd.read_csv(csv_data)

# 將 DataFrame 轉為字典列表以便 JSON 回應
data = data.to_dict(orient='records')

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    return app.response_class(
        response=json.dumps(data, ensure_ascii=False),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)