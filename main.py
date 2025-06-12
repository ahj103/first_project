import streamlit as st
import random
import string

# 단어 리스트 (예시)
WORDS = ["PYTHON", "STREAMLIT", "HANGMAN", "DEVELOPER", "COMPUTER", "PROGRAMMING", "ARTIFICIAL", "INTELLIGENCE"]

# 행맨 이모지 그림 단계 (총 6단계)
HANGMAN_PICS = [
    "😀🙂😐",  # 처음 (아무도 없음)
    "😵",      # 머리
    "😵👕",   # 몸통
    "😵👕👖", # 몸통 + 다리
    "😵👕👖✋", # 한 팔
    "😵👕👖✋✋"  # 두 팔 완성 (끝)
]

MAX_WRONG = len(HANGMAN_PICS) - 1

# 페이지 설정
st.set_page_config(page_title="🎉 단어 맞추기 게임 (Hangman) 🎉", page_icon="🕹️", layout="centered")

st.markdown("""
    <h1 style="text-align: center; color: #FF6F61;">🕹️ 단어 맞추기 게임 (Hangman) 🕹️</h1>
    <h3 style="text-align: center; color: #1E90FF;">알파벳을 맞춰 단어를 완성하세요! 🔤</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# 세션 상태 초기화
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = set()
    st.session_state.wrong = 0
    st.session_state.finished = False
    st.session_state.message = ""

def display_word():
    displayed = " ".join([letter if letter in st.session_state.guessed else "⬜" for letter in st.session_state.word])
    return displayed

def check_win():
    return all([l in st.session_state.guessed for l in st.session_state.word])

# 게임 진행
if not st.session_state.finished:
    st.markdown(f"<p style='font-size: 40px; text-align:center;'>단어: <strong>{display_word()}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 30px; text-align:center;'>남은 기회: <strong>{MAX_WRONG - st.session_state.wrong}</strong> ❌</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 50px; text-align:center;'>{HANGMAN_PICS[st.session_state.wrong]}</p>", unsafe_allow_html=True)
    
    guess = st.text_input("한 글자 입력 (영어 대문자만)", max_chars=1).upper()

    if guess and guess in string.ascii_uppercase:
        if guess in st.session_state.guessed:
            st.warning(f"❗ 이미 '{guess}'를 입력했어요!")
        else:
            st.session_state.guessed.add(guess)
            if guess not in st.session_state.word:
                st.session_state.wrong += 1

            if check_win():
                st.session_state.finished = True
                st.session_state.message = "🏆 축하합니다! 단어를 맞췄어요! 🎉"
            elif st.session_state.wrong >= MAX_WRONG:
                st.session_state.finished = True
                st.session_state.message = f"💀 실패! 정답은 '{st.session_state.word}' 였어요! 다시 도전하세요! 🔄"

        st.experimental_rerun()

else:
    # 게임 종료 메시지
    color = "#28a745" if check_win() else "#dc3545"
    st.markdown(f"""
        <h2 style='text-align:center; color: {color};'>{st.session_state.message}</h2>
        <p style='font-size: 40px; text-align:center;'>단어: <strong>{st.session_state.word}</strong></p>
        <p style='font-size: 60px; text-align:center;'>{HANGMAN_PICS[st.session_state.wrong]}</p>
    """, unsafe_allow_html=True)

    if st.button("🔄 다시 시작하기"):
        st.session_state.word = random.choice(WORDS)
        st.session_state.guessed = set()
        st.session_state.wrong = 0
        st.session_state.finished = False
        st.session_state.message = ""
        st.experimental_rerun()

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by ChatGPT & Streamlit</p>", unsafe_allow_html=True)
