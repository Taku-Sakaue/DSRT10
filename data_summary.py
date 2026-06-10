import openpyxl
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('参加者要約')

# 参加者情報の読み取り
indat = pd.read_excel(r'data/data.xlsx', skiprows=1, header=None)

# OSS参加者のみ
ossdat = indat[indat[3] == "製薬業界におけるR活用の可能性と課題"]


# 経験年数
# 各水準の件数
exyr = ossdat[2].value_counts()

plt.title('統計解析業務に携わった経験年数を以下からご選択ください。')


