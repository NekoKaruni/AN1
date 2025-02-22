import pandas as pd
import os

# data_j.csv からティッカーコードを読み込む
data_j = pd.read_csv('data_j.csv')
ticker_codes = data_j['ticker'].tolist()  # 'ticker' 列から4桁の数字を取得

# 結果を保存するためのリストを作成
results = []

# Dataフォルダ内のファイルを処理
for code in ticker_codes:
    # 対応するファイル名を作成
    file_name = f"Data/{code}_financial.csv"
    
    if os.path.exists(file_name):  # ファイルが存在するか確認
        # CSVファイルを読み込む
        df = pd.read_csv(file_name)
        
        # 'Unnamed: 0_bs' 列からデータを取得
        if 'Unnamed: 0_bs' in df.columns:
            for date in df['Unnamed: 0_bs']:
                results.append({'ticker': code, 'Kessan': date})  # 結果をリストに追加
        else:
            print(f"'Unnamed: 0_bs' 列が見つかりませんでした (ティッカーコード: {code})")
    else:
        print(f"ファイルが存在しません: {file_name}")

# DataFrameに変換
results_df = pd.DataFrame(results)

# 結果を data_k.csv ファイルに保存
results_df.to_csv('out/data_k.csv', index=False, encoding='utf-8-sig')

print("データを data_k.csv に保存しました。")


