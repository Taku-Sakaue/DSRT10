import openpyxl
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# フォント登録
_font_path = pathlib.Path(__file__).parent.parent / "fonts" / "NotoSansJP-Regular.ttf"
if _font_path.exists():
    font_manager.fontManager.addfont(str(_font_path))
    matplotlib.rcParams["font.family"] = (
        font_manager.FontProperties(fname=str(_font_path)).get_name()
    )
matplotlib.rcParams["axes.unicode_minus"] = False





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

