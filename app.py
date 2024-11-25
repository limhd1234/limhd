import os
from openai import OpenAI
import streamlit as st
os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)



st.title("관광지 추천")

contry = st.text_input("어떤 나라를 방문하고 싶으신가요?") 

if st.button("관광지 추천받기"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": contry,
            },
            {
                "role": "system",
                "content": "입력받은 나라에서 가장 인기있는 관광지를 알려줘"
            }
        ],
        model="gpt-4o",
    )
    result = chat_completion.choices[0].message.content
    st.write(result)