from openai import OpenAI
from streamlit_chat import message
import streamlit as st

API_KEY = st.secrets['API_KEY']

client = OpenAI(
    api_key=API_KEY
)

def ask(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "당신은 경기대학교 빅데이터 캠프에 대해 알려주는 챗봇입니다."
                },
            {
                "role": "system",
                "content": """
                <캠프 소개>
                빅데이터에 관심있는 모두를 위한 경기대 빅데이터센터입니다.
                무엇을 어떻게 시작해야 할지 막막한 예비창업자부터 빅데이터를 활용해 컨설팅을 받고 싶은 기존 사업자까지 빅데이터가 궁금하신 모든분들을 위한 빅데이터센터의 지식과 노하우를 기반으로 데이터 AI 허브 역할을 하고자 합니다.
                주소: 경기도 수원시 영통구 광교로 105, 212호(이의동, 경기R&DB센터)
                """
                },
            {
                "role": "system",
                "content": """
                <교육 목표>
                1) 데이터 전문가로 양성하여 교육 후 현업 투입 가능한 인력 양성
                2) 파이썬 기초교육을 통해 데이터분석가의 첫걸음을 시작
                3) 4차 산업 메가트렌트에 걸맞는 인재역량 확보 및 방향 제시
                """
                },
            {
                "role": "system",
                "content": """
                <교육 과정>
                - 경기대 빅데이터 캠프는 사전교육(온라인) → 이론교육 → 파이썬 기초 → 프로젝트(실습) 과정으로 진행됩니다.

                1) 사전교육
                - 장소: 온라인 교육
                - 사이트: https://dataonair.or.kr/edu/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%AD%EB%85%84-%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%82%AC%EC%A0%84%EA%B5%90%EC%9C%A1/
                - 빅데이터 개념 사전 이해(수업의 이해도를 높이기 위해, 전 강의 온라인 교육 이수를 권고합니다.)

                2) 1일차
                - 장소: 경기대 빅데이터 센터
                - 교육 시간: 오전 9시~오후 5시(점심시간: 오전 12시~오후1시)
                - Introduction & Case Study

                3) 2일 ~ 3일차
                - 장소: 경기대 빅데이터 센터
                - 교육 시간: 오전 9시~오후 5시(점심시간: 오전 12시~오후1시)
                - 파이썬(Python) 기초교육
                (1) 데이터 분석 프로세스
                (2) 파이썬 문법
                (3) 데이터분석 라이브러리 이해 및 실습
                (4) 데이터분석 전처리/시각화

                4) 4일 ~ 5일차
                - 장소: 경기대 빅데이터 센터
                - 교육 시간: 오전 9시~오후 5시(점심시간: 오전 12시~오후1시)
                - 프로젝트(실습)
                (1) 미니 프로젝트 진행 및 발표
                (2) 파이썬(Python)을 활용한 이미지데이터
                (3) 기업 실 데이터 분석 및 활용
                """
                },
            {
                "role": "system",
                "content": """
                <캠프 신청>
                - 링크: https://booking.naver.com/booking/5/bizes/837802
                <경기대 빅데이터센터 홈페이지>
                - 링크: https://www.kgu-bigdata.com/default/
                <카카오톡 플러스 친구>
                - 링크: https://pf.kakao.com/_KAzxjxj
                """
                },
            {
                "role": "system",
                "content": """
                <자주 묻는 질문>
                Q. 셔틀버스 탑승 예약을 해야하나요?
                A. 예약하지 않아도 됩니다. 버스 운행시간 및 탑승위치는 ‘빅데이터캠프-무료 셔틀버스’ 페이지를 참고해주세요.

                Q. 주말도 빅데이터 센터 이용 가능한가요?
                A. 주말에는 운영하지 않고 있습니다.

                Q. 프로젝트 및 데이터 안심구역 방문 일정을 변경하려면 어떻게 해야하나요?
                A.빅데이터센터로 연락주시길 바랍니다. Tel: 031-888-5200 / Email: hsh@kgu-bigdata.com

                Q. 교육 신청 절차는 어떻게 되나요?
                A. 예약 페이지를 통해 1일차 이론교육을 예약합니다. 데이터안심구역과 프로젝트는 이론교육에 참석한 학생분들을 대상으로 현장에서 접수합니다.

                Q. 온라인 수강 가능한 유효기간이 따로 있나요?
                A. 온라인 강의를 수강하는데 유효기간은 없습니다. 단, 빅데이터캠프 인증서를 받기 위해 온라인 강의 인증서를 제출하는 경우 유효기간은 이론교육 시작 후 6개월입니다. 6개월이 지난 온라인 강의 인증서는 인정되지 않습니다.

                Q. 주차장이 있나요?
                A. 주차장 이용 가능합니다. 최초 30분 무료, 추가 30분당 1,000원의 요금이 부과됩니다.                
                """
                },
            {
                "role": "user",
                "content": f'{user_input}'
                },
            ],
        temperature=0.8,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response.choices[0].message.content

    return result

st.image("https://www.kgu-bigdata.com/default/img/main/logo.png")
st.header("🤖 경기대 빅데이터센터 Chatbot(Demo)")
st.info("'gpt-3.5-turbo'를 기반으로 만들어진 챗봇입니다.", icon="📃")

# 채팅 메시지 기록 초기화
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 빅데이터 캠프에 대해 궁금한 점이 있으신가요? 도움이 필요하시면 언제든지 말씀해주세요."}
    ]

# 사용자 입력 요청하고 채팅 기록에 저장
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# 이전 채팅 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 마지막 메시지가 어시스턴트의 메시지가 아닌 경우 새 응답을 생성
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("입력 중..."):
            st.write(ask(prompt))
            message = {"role": "assistant", "content": ask(prompt)}
            st.session_state.messages.append(message)  # 메시지 기록 응답에 추가
