import os
import openpyxl
import pathlib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# フォント登録
font_path = os.path.join(os.path.dirname(__file__), "fonts", "ZenKakuGothicNew-Regular.ttf")

# フォントプロパティを作成
font_prop = font_manager.FontProperties(fname=font_path)

# matplotlib にフォントを登録・適用
plt.rcParams['font.family'] = font_prop.get_name()




st.title('参加者要約')

# 参加者情報の読み取り
indat = pd.read_excel(r'data/data.xlsx', skiprows=1, header=None)

# OSS参加者のみ
ossdat = indat[indat[3] == "製薬業界におけるR活用の可能性と課題"]


# 経験年数
# 各水準の件数
exyr = ossdat[2].value_counts()

plt.title('統計解析業務に携わった経験年数を以下からご選択ください。')

plt.pie(
    exyr, 
    labels=exyr.index, 
    autopct=lambda p: f'{p:.1f}% ({p * sum(exyr) / 100:.0f})',
    startangle=90
)

st.pyplot(plt)

