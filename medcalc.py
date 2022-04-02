import streamlit as st
import datetime
from datetime import date
from datetime import timedelta

st.title("リフィル計算機")


rxdate = st.date_input("調剤日を入力してください")
diff_day = st.number_input("処方日数を入力してください",min_value=1,value=28)
rxday = timedelta(days= diff_day)

rxday2 = rxdate + rxday

rxday_min = rxday2 - timedelta(days = 7)
rxday_max = rxday2 + timedelta(days = 7)

st.write(
    f"次回調剤予定日は{rxday2}です。リフィル可能な期間は{rxday_min}から{rxday_max}までです。"
    )
