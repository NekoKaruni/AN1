library(tidyverse)
library(dplyr)

setwd("C:/Users/RY757/OneDrive/ドキュメント/AN1/data")

# ファイル一覧を取得
file_list <- list.files(pattern = "^[0-9]{4}_financial\\.csv$")

# 空のデータフレームを用意
final_df <- data.frame()

# 各ファイルに対してループ処理
for (file in file_list) {
  # ファイル名からティッカーコード（4桁の数字）を抽出
  ticker_code <- str_extract(file, "^[0-9]{4}")
  
  # CSVファイルを読み込む（すべて文字列として扱う）
  df <- read_csv(file, col_types = cols(.default = col_character()))
  
  # 必要な列を数値に変換
  fif_df <- df |> 
    mutate(across(c(`Share Issued_bs`, `Stock_Price`, `Net Income_is`, `Stockholders Equity_bs`), as.numeric)) |> 
    select(Year = `Unnamed: 0_bs`, 
           Share_Issued = `Share Issued_bs`, 
           Stock_Price = `Stock_Price`, 
           Net_income = `Net Income_is`, 
           Stock_Equity = `Stockholders Equity_bs`) |> 
    filter(!is.na(Year) & !is.na(Share_Issued)) |> 
    mutate(Ticker = ticker_code,
           PBR = Stock_Price / (Stock_Equity / Share_Issued),
           PER = Stock_Price / (Net_income / Share_Issued)) |> 
    select(Ticker, Year, PBR, PER)  # 必要な列のみ選択
  
  # データを統合
  final_df <- bind_rows(final_df, fif_df)
  
  # 処理が完了したことを知らせるメッセージ
  cat("Processing complete for:", ticker_code, "\n")
}

# 出力ファイル名を作成（全てのデータを1つのファイルに保存）
output_file <- "C:/Users/RY757/OneDrive/ドキュメント/AN1/out/Standard_PER_PBR.csv"

# 統合データをCSVファイルとして保存
write_csv(final_df, output_file)

cat("All processing complete! Output saved as:", output_file, "\n")
