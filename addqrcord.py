# coding=utf-8
#
# [タイトル：住所]のCSVリストから、タイトル名のGoogleMap QRコード画像(png)を作成する
# pip install lxml が必要
# 制作：2021.10.11
# ver.1.0.2
#
import sys
import requests
import qrcode
import pandas as pd
import time
from bs4 import BeautifulSoup
from tqdm import tqdm


# CSVデータの読み込み
dict_from_csv = pd.read_csv('address_list.csv', header=None, index_col=0, squeeze=True).to_dict()

url = 'http://www.geocoding.jp/api/'
gmap = 'https://www.google.com/maps/search/?api=1&query='

for title, address in tqdm(dict_from_csv.items()):
  payload = {"v": 1.1, 'q': address}
  r = requests.get(url, params=payload)
  ret = BeautifulSoup(r.content,'lxml')
  if ret.find('error'):
      raise ValueError(f"Invalid address submitted. {address}")
  else:
      file_name = title + ".png"
      lat = ret.find('lat').string
      lon = ret.find('lng').string
      lat_s = str(lat)
      lon_s = str(lon)
      qr = gmap + lat_s + "," + lon_s
      img =qrcode.make(qr)
      img.save("qrcode" + '/' + file_name)
      tqdm.write("Add: {}".format(file_name)) # 作成したファイル名を表示
      time.sleep(5)
