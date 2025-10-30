import streamlit as st
import random

st.title("🎰 대한민국 로또 번호 생성기")
st.write("1부터 45 사이의 숫자 중 6개의 랜덤 번호를 뽑습니다!")

if st.button("🎲 로또 번호 생성하기"):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    st.success(f"당신의 로또 번호는: {numbers}")
