import streamlit as st
from openai import OpenAI
from streamlit_chat import message
import json

API_KEY = st.secrets['API_KEY']

client = OpenAI(
    api_key=API_KEY
)

# JSON 파일 열기
with open('./data.json', 'r') as file:
    data = json.load(file)

# 질의응답 함수
@st.cache_data(show_spinner=False)
def ask(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= data['data'] + [
            {
                "role": "user",
                "content": f'{user_input}'
            }
        ],
        temperature=0.8,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].message.content

st.image("https://www.kgu-bigdata.com/default/img/main/logo.png")
st.header("🤖 경기대 빅데이터센터 챗봇(Demo)")
st.info("'gpt-3.5-turbo'를 기반으로 만들어진 챗봇입니다.", icon="📃")

# 채팅 메시지 기록 초기화
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 경기대 빅데이터센터에 대해 궁금한 점이 있으신가요? 도움이 필요하시면 무엇이든 말씀해주세요."}
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
