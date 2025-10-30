import streamlit as st
import random
import pandas as pd

# -----------------------------
# 🎰 앱 기본 설정
# -----------------------------
st.set_page_config(page_title="대한민국 로또 번호 생성기", page_icon="🎲")
st.title("🎰 대한민국 로또 번호 생성기")
st.write("1부터 45까지의 숫자 중 6개의 번호를 무작위로 추첨합니다!")

# -----------------------------
# ⚙️ 옵션 선택
# -----------------------------
st.sidebar.header("🔧 옵션 설정")
num_sets = st.sidebar.slider("생성할 세트 수", 1, 10, 1)
include_bonus = st.sidebar.checkbox("보너스 번호 포함하기", value=True)

# -----------------------------
# 🎲 로또 번호 생성 함수
# -----------------------------
def generate_lotto_numbers(include_bonus=False):
    main_numbers = sorted(random.sample(range(1, 46), 6))
    bonus = random.choice([n for n in range(1, 46) if n not in main_numbers])
    if include_bonus:
        return main_numbers, bonus
    return main_numbers

# -----------------------------
# 🚀 버튼 클릭 시 실행
# -----------------------------
if st.button("🎯 로또 번호 생성하기"):
    results = []

    for i in range(num_sets):
        if include_bonus:
            nums, bonus = generate_lotto_numbers(include_bonus=True)
            results.append({
                "세트 번호": f"{i+1}번 세트",
                "번호": ", ".join(map(str, nums)),
                "보너스": bonus
            })
        else:
            nums = generate_lotto_numbers()
            results.append({
                "세트 번호": f"{i+1}번 세트",
                "번호": ", ".join(map(str, nums))
            })

    df = pd.DataFrame(results)
    st.subheader("🎉 생성된 로또 번호")
    st.dataframe(df, use_container_width=True)

    # CSV 다운로드 기능
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="💾 CSV로 저장하기",
        data=csv,
        file_name="lotto_numbers.csv",
        mime="text/csv"
    )

else:
    st.info("왼쪽 옵션을 설정하고, 버튼을 눌러 로또 번호를 생성하세요!")

# -----------------------------
# ✨ 하단 문구
# -----------------------------
st.markdown("---")
st.caption("© 2025 대한민국 로또 번호 생성기 | 제작: ChatGPT")
