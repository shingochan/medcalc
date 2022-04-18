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
    f"　次回調剤予定日　：**{rxday2}**  \nリフィル対応期間：**{rxday_min}**〜**{rxday_max}**  \n"
    )

st.markdown("# ")
# クレアチニンクリアランス
st.markdown("##### クレアチニンクリアランス計算機")
display = ("男性", "女性")
options = list(range(len(display)))
gender = st.selectbox("性別を選んでください。", options, format_func=lambda x: display[x])
age = st.number_input('年齢を入力してください。',value=75,min_value=0,max_value=120)
weight = st.number_input('体重を入力してください。',value=60,min_value=0,max_value=200)
if gender == 0:
    gender_coefficient=1
else:
    gender_coefficient=0.85

Cre = st.number_input('クレアチニン値を入力してください。',value=0.80,min_value=0.00,max_value=10.00,step=0.01)

CCr=round((140-age)*weight*gender_coefficient/(72*Cre),2)
st.markdown(f'クレアチニンクリアランス：{CCr}')
