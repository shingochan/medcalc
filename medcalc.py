import streamlit as st
import datetime
from datetime import date, timedelta, timezone

jst = timezone(timedelta(hours=9), 'JST')
dt_now = datetime.datetime.now(jst)
jst_today = datetime.date(dt_now.year, dt_now.month ,dt_now.day)

st.markdown("##### リフィル計算機")
rxdate = st.date_input("調剤日を入力してください",value=jst_today)
diff_day = st.number_input("処方日数を入力してください",min_value=1,value=28)

rxday = timedelta(days= diff_day)
rxday2 = rxdate + rxday
rxday_min = rxday2 - timedelta(days = 7)
rxday_max = rxday2 + timedelta(days = 7)

st.markdown(
    f"次回調剤予定日：**{rxday2}**  \nリフィル対応期間：**{rxday_min}**〜**{rxday_max}**  \n"
    )
