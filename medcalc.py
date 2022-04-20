import streamlit as st
import datetime
from datetime import date, timedelta, timezone

st.set_page_config(page_title="リフィル計算機",page_icon=":calendar:",)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            section.main div.block-container {padding: 2.5rem !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


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
    f"　次回来局予定日は  \n**{rxday2.month}月{rxday2.day}日**です。  \nリフィル調剤可能な期間は  \n**{rxday_min.month}月{rxday_min.day}日**から**{rxday_max.month}月{rxday_max.day}日**です。  \n"
    )
    st.sidebar.write('サイドバーを閉じて、ラベルプリンタで印刷してください。')
else:
    st.markdown('リフィル計算機です。  \n**＞**を押してサイドバーに調剤日と処方日数を入力してください。')
    st.markdown(
        f"　次回調剤予定日：**{rxday2}**  \nリフィル対応期間：**{rxday_min}**〜**{rxday_max}**  \n"
        )
