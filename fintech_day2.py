import OpenDartReader
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import mplfinance as mf
import pandas as pd
import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
api_key = "ec1b08b1fc9b92bd337034391dbd11e6110262e0"

dart = OpenDartReader(api_key)
corp = '005930'
end = datetime.datetime.now().date() - datetime.timedelta(days=1)
start = end - relativedelta(months=4)


st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>4개월간 삼성 주가</h1>", unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)
df = fdr.DataReader(corp, start, end)
fig = mf.plot(df, type='candle', style='charles', title='Stock Price', ylabel='Price', volume=True)
st.pyplot(fig)

st.write(df)
