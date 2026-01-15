import streamlit as st  # streamlit 모듈 불러오기
import random  # 랜덤 모듈 불러오기
import datetime  # 날짜/시간 모듈 불러오기

st.title("로또 번호 생성기")  # 웹사이트 제목  

st.header("로또 번호를 생성해드립니다!")  # 웹사이트 헤더
st.subheader("아래 버튼을 눌러 로또 번호를 생성하세요.")  # 웹사이트 서브헤더

def generate_lotto():
    lotto = set()   # set()으로 중복 없는 번호를 6개까지만 담는 그릇 lotto 생성
    while len(lotto) < 6:
        number = random.randint(1, 45)  # 1~45 사이의 숫자 랜덤 추출
        lotto.add(number)  # set에 번호 추가. set은 append가 아닌 add 사용(b/c 순서없음)
    return lotto

button = st.button("로또 번호 생성해주세요!")  # 버튼 생성
if button:  # 버튼이 눌리면
    for i in range(1,6):  # 5세트 생성
        st.subheader(f"{i}번째 추천 로또 번호: {generate_lotto()}")  # 번호 출력

    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  # 생성 시각 출력