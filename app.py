import streamlit as st

# 1. 상태 관리 (State Management) 초기화: SPA의 핵심!
# 사용자가 새로고침을 누르지 않는 이상, 현재 몇 번 질문인지와 어떤 답변을 했는지 기억합니다.
if 'step' not in st.session_state:
    st.session_state.step = 0  # 현재 질문 번호 (0부터 시작)
if 'answers' not in st.session_state:
    st.session_state.answers = []  # 선택한 답변을 차곡차곡 모아둘 리스트

# 2. 질문 리스트 (나중에 15개로 쭉 늘려주시면 됩니다)
questions = [
    {"q": "오늘 저녁은 어떤 걸 드셨나요?", "options": ["든든한 찌개나 백반", "간단하게 빵이나 면", "입맛이 없어서 건너뜀"]},
    {"q": "오늘 하루, 누구와 가장 많이 대화하셨나요?", "options": ["가족이나 친구", "복지관이나 이웃 사람들", "거의 혼자 보냄"]},
    {"q": "지금 몸에서 가장 찌뿌둥한 곳은 어디신가요?", "options": ["어깨나 허리", "무릎이나 다리", "아픈 곳 없이 개운함"]}
]


# 버튼을 눌렀을 때 다음 질문으로 넘어가는 함수
def go_next(answer):
    st.session_state.answers.append(answer)  # 답변 저장
    st.session_state.step += 1  # 다음 질문으로 이동


# 3. 화면 표시 로직
st.title("🌱 내게 맞는 하루 루틴 찾기")

# 아직 질문이 남아있을 때 (질문 페이지)
if st.session_state.step < len(questions):
    current_q = questions[st.session_state.step]

    # 진행 상황을 알려주는 바 (예: 1 / 15)
    progress_ratio = (st.session_state.step + 1) / len(questions)
    st.progress(progress_ratio)
    st.write(f"**진행도: {st.session_state.step + 1} / {len(questions)}**")

    st.divider()  # 구분선

    # 현재 질문 출력
    st.subheader(current_q["q"])
    st.write("")  # 약간의 여백

    # 선택지 버튼 출력
    for option in current_q["options"]:
        # 버튼이 눌리면 go_next 함수가 실행되고 화면이 즉시 업데이트됩니다.
        if st.button(option, use_container_width=True):
            go_next(option)
            st.rerun()  # 화면 깜빡임 없이 다음 질문으로 부드럽게 전환

# 15개 질문이 모두 끝났을 때 (결과 페이지)
else:
    st.balloons()  # 축하 애니메이션 효과
    st.success("테스트가 모두 끝났습니다!")

    st.subheader("📊 어르신의 답변 결과 데이터")

    # 모인 답변 데이터를 보여줍니다.
    for i, ans in enumerate(st.session_state.answers):
        st.write(f"- {i + 1}번 문항: {ans}")

    st.info("💡 모인 이 데이터를 Pandas 등으로 분석해 맞춤형 루틴을 추천하는 로직을 붙이면 완성입니다!")

    # 다시 하기 버튼
    if st.button("처음부터 다시 하기"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
