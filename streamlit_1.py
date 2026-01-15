# 파이썬에서 제공하는 모듈 (대쉬보드를 만들어줌, 웹사이트 아님 - 웹사이트는 flask 로 제작)
# 가상환경 이름 venv 로 만들기 (암묵적인 룰)

# pip install streamlit  # streamlit 모듈 설치
# pip install --upgrade streamlit  # streamlit 모듈 업그레이드

import streamlit as st  # streamlit 모듈 불러오기
import numpy as np   # 숫자계산 numpy 모듈 불러오기
import pandas as pd  # 그래프 그리는 pandas 모듈 불러오기 (엑셀자료 연산에 최고봉!)
from datetime import datetime as dt  # 날짜/시간 모듈 불러오기
import datetime

st.title("이것이 타이틀이다")  # 웹사이트 제목

# python streamlit_1.py  # 이걸론 실행 불가. 아래가 실행 명령어
# streamlit run streamlit_1.py

st.header("이것이 헤더이다")  # 웹사이트 헤더
st.subheader("이것이 서브헤더이다")  # 웹사이트 서브헤더
st.text("이것이 텍스트이다")  # 웹사이트 텍스트
st.markdown("- 이것이 마크다운이다")  # 웹사이트 마크다운
st.write("123,[1,2,3]")  # 웹사이트 라이트

st.title("스마일 : 😊")  # 이모지 사용 가능 
st.caption("캡션은 그림에 대한 설명")  # 그림에 대한 설명
st.markdown("**마크다운 굵게**")
st.markdown("*마크다운 기울임*")
st.markdown("~~마크다운 취소선~~")

st.markdown("**김효정**,*김효정*,~~김효정~~")  # 마크다운 여러개 조합 가능

# 코드 표시
sample_code = """
def hello():
    print("hello world")"""

st.code(sample_code, language="python")  # 코드 블록 표시

# 마크다운 문법 지원
st.markdown("텍스트의 색상을 ':green[초록색]'으로, 그리고 **:blue[파란색]** 볼드체를 설정할 수 있다")   # :color[text] 형태로 색상 지정 가능
# st.markdown("배경색은 `:bg-yellow[노란색]`, `:bg-pink[분홍색]`, `:bg-lightblue[하늘색]` 등으로 설정할 수 있다")  # :bg-color[text] 형태로 배경색 지정 가능 

st.markdown(":green[$\sqrt{x^2 + y^2}=1$]")  #:green 수학기호 초록색으로  #$\ 앞뒤로 넣으면 달러표시 넣어줌  #[sqrt{x^2 + y^2] 수학기호가 아예 수학문제처럼 보임
st.latex(r"\sqrt{x^2 + y^2}=1")  # 수학기호만 화면 가운데에 표시



st.title("데이터프레임 그래프 그리기")

# 데이터프레임 으로 그래프 그리기
# dataframe 생성
dataframe = pd.DataFrame(           #class의 method(기능) 호출
    {"first column": [1,2,3,4],
    "second column": [10,20,30,40]})   

# dataframe 출력
st.dataframe(dataframe)     #엑셀처럼 수정가능. (너비 조절, 정렬(오름차순, 내림차순), 다운로드, ctrl+f 등등)

# 테이블 출력
st.table(dataframe)         #고칠 수 없음. 테이블 완전 고정! like 이미지

# 통계치 출력
st.metric(label="온도", value="25℃", delta="1.2℃")  #delta는 변화량
st.metric(label="삼성", value="143,800원", delta="3500원")

# 콜럼을 나눠서 달러환율 / 유로환율 / 엔화환율 출력
st.header("26.01.15 주요국 환율")  # 웹사이트 헤더
col1, col2, col3 = st.columns(3)  #3등분
col1.metric(label="달러USD", value="1,470.60원", delta="4.10원")
col2.metric(label="유로EUR", value="1,711.36원", delta="3.55원")
col3.metric(label="엔JPY", value="927.67원", delta="1.06원")

# 버튼 만들기
button = st.button("버튼을 눌러주세요")  # 버튼 생성
if button :
    st.write(":blue[버튼이 눌렸습니다✅]")

# 체크박스 만들기
agree = st.checkbox("체크박스를 눌러주세요")  # 체크박스 생성
if agree :
    st.write(":green[체크박스가 선택되었습니다✅]")

# 라디오 버튼 만들기
select = st.radio("당신의 MBTI 버튼을 선택해주세요", ("INFJ", "ESTP", "INTJ"), index=1)  # 라디오 버튼 생성   #index=1 은 기본값 설정(ESTP 에 눌러져있음)
if select == "INFJ" :
    st.write("옹호자(INFJ)는 매우 희귀한 성격임에도 불구하고 세상에 큰 영향력을 발휘하곤 합니다")
elif select == "ESTP" :
    st.write("설득력이 좋고, 인맥 스펙트럼이 넓으며, 의사 표현이 정직하고 명확합니다.")
else :
    st.write("전략가는 모든 것에 의문을 제기합니다. 다른 많은 성격은 현재 상태를 유지하고 일반적인 통념과 다른 사람의 전문 지식에 의존해 살아가곤 합니다.")

# 셀렉트박스 만들기
favorite_color = st.selectbox("당신이 가장 좋아하는 색깔은 무엇인가요?", 
                              ("빨강", "파랑", "초록", "노랑", "보라"))  # 셀렉트박스 생성
st.write(f"당신이 가장 좋아하는 색깔은 :red[{favorite_color}] 입니다.")   #:red{ }  #변수 색깔 지정   #텍스트는 [], 변수는 {} 안에 넣어야함

# 멀티셀렉트박스 만들기
hobbies = st.multiselect("당신의 취미는 무엇인가요?", 
                         ['독서', '운동', '영화', '음악', '여행'])  # 멀티셀렉트박스 생성
st.write("당신의 취미는 ", hobbies, "입니다.")

# 슬라이더 만들기
age = st.slider("당신의 나이는 몇 살인가요?", 0, 120, 25)  # 슬라이더 생성   #0~120사이, 기본값 25
st.write("당신의 나이는 ", age, "살 입니다.")   

value = st.slider("범위의 값을 다음과 같은 범위로 설정하세요", 0.0,100.0,(25.0,75.0))
st.write(f"설정된 범위는 :green[{value}] 입니다.")

# 날짜 입력 만들기
start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2026,1,1,0,0),  #최소값 2026년1월1일 0시0분
    max_value=dt(2026,12,31,0,0),  #최대값 2026년12월31일 0시0분
    value = dt(2026,1,15,0,0),  #기본값 2026년6월15일 12시30분
    step = datetime.timedelta(days=1),  #슬라이더가 1일 단위로 움직임
    # step = datetime.timedelta(hours=1),  #슬라이더를 1시간 단위로 움직임
    format = "YYYY년 MM월 DD일"    #표시형식
  ) 

st.write(f"약속 날짜는 :blue[{start_time}] 입니다.")

# 시간 입력 만들기
appointment = st.time_input(
    "약속 시간을 선택하세요",
    value = dt.strptime("13:30", "%H:%M").time(),  #기본값 13시30분
    )
st.write(f"약속 시간은 :blue[{appointment}] 입니다.")


# 텍스트 입력 만들기
title = st.text_input(
    label = "가고싶은 여행지가 있나요?", 
    placeholder = "예: 파리, 뉴욕, 도쿄") 
st.write(f"당신이 가고싶은 여행지는 :green[{title}]입니다.")


# 숫자 입력 버튼 만들기
number = st.number_input(
    label = "당신이 좋아하는 숫자는 무엇인가요?",
    min_value = 0,
    max_value = 100,
    value = 50,  #초기 설정값
    step = 1    #한칸씩 움직일게요
)
st.write(f"당신이 좋아하는 숫자는 :green[{number}]입니다.")


# 파일 다운로드 버튼
st.download_button(
    label="CSV 파일 다운로드",
    data=dataframe.to_csv().encode('utf-8'),  #line 52 의 dataframe 데이터를 csv파일로 다운로드할 수 있는 버튼생성
    file_name="sample.csv",
    mime="text/csv"   # mime 타입 지정 (파일형식 지정)
)

