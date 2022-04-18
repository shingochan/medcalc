import streamlit as st
import datetime
from datetime import date, timedelta, timezone
import app1
import app2



PAGES = {
    "リフィル計算機": app1,
    "クレアチニンクリアランス計算機": app2
}
st.sidebar.title('アプリ選択')
selection = st.sidebar.radio("アプリを選んでください", list(PAGES.keys()))
page = PAGES[selection]
page.app()
