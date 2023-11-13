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
                - Introduction & Case Study

                3) 2일 ~ 3일차
                - 장소: 경기대 빅데이터 센터
                - 파이썬(Python) 기초교육
                (1) 데이터 분석 프로세스
                (2) 파이썬 문법
                (3) 데이터분석 라이브러리 이해 및 실습
                (4) 데이터분석 전처리/시각화

                4) 4일 ~ 5일차
                - 장소: 경기대 빅데이터 센터
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
                """
                },
            {
                "role": "user",
                "content": f'{user_input}'
                },
            ],
        temperature=1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].message.content

    return message

st.header("🤖 경기대 빅데이터센터 Chatbot(Demo)")
st.markdown("[홈페이지](https://www.kgu-bigdata.com/default/)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = ['안녕하세요! 빅데이터 캠프에 대해 궁금한 점이 있으신가요? 도움이 필요하시면 언제든지 말씀해주세요.']

if 'past' not in st.session_state:
    st.session_state['past'] = []

# 텍스트를 입력하여 봇과 대화 할 수 있는 폼 생성
# clear_on_submit 옵션을 통해서 submit 하면 폼의 내용이 지워짐
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('나:', '', key='input')
    submitted = st.form_submit_button('전송')

# 메시지를 입력 후 전송을 누를 경우
if submitted and user_input:
    output = ask(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# 저장된 대화 내용 보여주기
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
