# -*- coding: utf-8 -*-
"""merge csv and simplealgorthm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gR2xvZpCnocuBUNE4jjHBQO1Q_dRA4S_

The Ais data is collected and prepocessed in colab link:
https://colab.research.google.com/drive/16sxQvGoYLpPsBdd07Am-mu2tOBEdOMtK?usp=sharing

The CMEMS data about global ocean wave analysis and forecasting data collected and prepocessed in colab link:
https://colab.research.google.com/drive/19EvqDwiOGNMZszTKmYMB0AbEzXiTdzhh?usp=sharing

On this colab we combine two dataset and simple algorthm.
"""

import pandas as pd

ais=pd.read_csv("/content/drive/MyDrive/sih2024/2024_AIS.csv")
ais.head()

cmems=pd.read_csv("/content/drive/MyDrive/sih2024/cmemsdata.csv")
cmems.head()

print(ais.shape)
print(cmems.shape)

ais.dtypes

cmems.dtypes

ais.describe()

cmems.describe()

ais = ais.rename(columns={'LAT': 'latitude', 'LON': 'longitude'})
ais.head()

ais['BaseDateTime'] = pd.to_datetime(ais['BaseDateTime'])
cmems['time'] = pd.to_datetime(cmems['time'])

print(ais.dtypes)
print(cmems.dtypes)

ais.head()

cmems.head()

print(ais.shape)
print(cmems.shape)

ais_sorted = ais.sort_values('BaseDateTime')
cmems_sorted = cmems.sort_values('time')

merged_df = pd.merge_asof(ais_sorted, cmems_sorted, left_on='BaseDateTime', right_on='time', direction='nearest')
print(merged_df.shape)
merged_df.head()

merged_df.isnull().sum()

merged_df.to_csv('/content/drive/MyDrive/sih2024/mergeddata.csv', index=False)