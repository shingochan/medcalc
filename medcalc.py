import streamlit as st
import datetime
from datetime import date, timedelta, timezone


jst = timezone(timedelta(hours=9), 'JST')
dt_now = datetime.datetime.now(jst)
jst_today = datetime.date(dt_now.year, dt_now.month ,dt_now.day)
rxdate = st.sidebar.date_input("調剤日を入力してください",value=jst_today)
diff_day = st.sidebar.number_input("処方日数を入力してください",min_value=1,value=28)

rxday = timedelta(days= diff_day)
rxday2 = rxdate + rxday
rxday_min = rxday2 - timedelta(days = 7)
rxday_max = rxday2 + timedelta(days = 7)

print_layout = st.sidebar.checkbox('印刷レイアウト')


if print_layout:
    st.markdown(
    f"　次回来局予定日は**{rxday2.month}月{rxday2.day}日**です。  \nリフィル調剤可能な期間は**{rxday_min.month}月{rxday_min.day}**から**{rxday_max.month}月{rxday_max.day}日**までです。  \n"
    )
    st.sidebar.write('サイドバーを閉じてからラベルプリンタで印刷してください。')
else:
    st.write('リフィル計算機です。サイドバーに調剤日と処方日数を入力してください。')
    st.markdown(
        f"　次回調剤予定日　：**{rxday2}**  \nリフィル対応期間：**{rxday_min}**〜**{rxday_max}**  \n"
        )
