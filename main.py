import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위✌️ 바위✊ 보✋ 게임", page_icon="🎮", layout="centered")

# 타이틀 영역
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B;'>🎮 가위✌️ 바위✊ 보✋ 챌린지!</h1>
    <h3 style='text-align: center; color: #1E90FF;'>AI와 대결해서 이겨보세요 😎</h3>
""", unsafe_allow_html=True)

# 게임 옵션
options = ["✌️ 가위", "✊ 바위", "✋ 보"]
emoji_result = {
    "win": "🏆 이겼어요! 축하해요! 🎉",
    "lose": "😢 졌어요... 다음에 다시 도전해요!",
    "draw": "🤝 비겼어요! 다시 도전해봐요~"
}

st.markdown("---")

# 유저 선택
user_choice = st.radio("👇 당신의 선택을 고르세요!", options, horizontal=True)

# 게임 시작 버튼
if st.button("🎲 게임 시작!"):
    ai_choice = random.choice(options)
    
    # 결과 판정
    result = ""
    if user_choice == ai_choice:
        result = "draw"
    elif (
        (user_choice == "✌️ 가위" and ai_choice == "✋ 보") or
        (user_choice == "✊ 바위" and ai_choice == "✌️ 가위") or
        (user_choice == "✋ 보" and ai_choice == "✊ 바위")
    ):
        result = "win"
    else:
        result = "lose"

    # 결과 출력
    st.markdown(f"""
        <div style='text-align: center; font-size: 30px;'>
            🙋‍♂️ 당신: <strong>{user_choice}</strong><br>
            🤖 AI: <strong>{ai_choice}</strong><br><br>
            <span style='color: #FFD700;'>{emoji_result[result]}</span>
        </div>
    """, unsafe_allow_html=True)

    st.balloons() if result == "win" else None

# 하단
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)

