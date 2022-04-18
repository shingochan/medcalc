import streamlit as st

def app():
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
