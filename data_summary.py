import openpyxl
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

st.title('参加者要約')

# 参加者情報の読み取り
indat = pd.read_excel(r'data/data.xlsx', skiprows=1, header=None)

# OSS
ossdat = indat[indat[6] == "製薬業界におけるR活用の可能性と課題"]
