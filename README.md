# addqrcord.py
pythonでCSVリストからGoogleMapへのリンクQRコードを生成する

CSVファイルは、「ファイル名, 住所」の形式で作成する
CSVファイルの文字コードはUTF-8

実行するとファイル名+”.png”でQRコード画像を生成する
このQRコードはGoogle Mapへのリンクが記録されている

QRコードの生成場所は、addqrcord.pyの場所に「qrcode」フォルダを作成し、そこに保存される
ターミナルに生成過程とプログレスバーが表示される


## 動作環境

python 3.8.10にて作成　仮想環境Venvを使用

import sys　の行は不要かも
