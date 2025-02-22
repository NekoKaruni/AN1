import os
import requests
import json
import pandas as pd 

# 環境変数から J-Quants のログイン情報を取得
mailaddress = os.getenv("JQ_MAIL_ADDRESS")
password = os.getenv("JQ_PASSWORD")

# API にログインして ID_TOKEN と REFRESH_TOKEN を取得
data = {"mailaddress": mailaddress, "password": password}
url = "https://api.jquants.com/v1/token/auth_user"
r_post = requests.post(url, data=json.dumps(data))

# API レスポンスを JSON 形式で取得
response_data = r_post.json()

# REFRESH_TOKEN を取得
refresh_token = response_data.get("refreshToken")
print("REFRESH_TOKEN:", refresh_token)  # REFRESH_TOKEN を表示

# REFRESH_TOKEN を使って新しい ID_TOKEN を取得
if refresh_token:
    refresh_url = f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={refresh_token}"
    r_refresh = requests.post(refresh_url)
    
    # 新しい ID_TOKEN のレスポンスを取得
    if r_refresh.status_code == 200:
        new_token_data = r_refresh.json()
        new_id_token = new_token_data.get("idToken")
        print("新しい ID_TOKEN:", new_id_token)  # 新しい ID_TOKEN を表示
    else:
        print("新しい ID_TOKEN の取得に失敗:", r_refresh.json())
else:
    print("REFRESH_TOKEN が取得できませんでした。")


ID_TOKEN = new_id_token

Standard_Itiran = pd.read_csv('data_j.csv')
