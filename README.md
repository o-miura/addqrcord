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

## 参考にしたサイト
住所から緯度経度を取得するpythonスニペット
https://qiita.com/paulxll/items/7bc4a5b0529a8d784673?utm_source=stock_summary_mail&utm_medium=email&utm_term=adsystem-om&utm_content=%E4%BD%8F%E6%89%80%E3%81%8B%E3%82%89%E7%B7%AF%E5%BA%A6%E7%B5%8C%E5%BA%A6%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8Bpython%E3%82%B9%E3%83%8B%E3%83%9A%E3%83%83%E3%83%88&utm_campaign=stock_summary_mail_2021-10-16
