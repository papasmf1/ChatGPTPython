#이 파일을 실행할 때는 cmd로 커맨드창을 오픈해서 아래와 같이 입력합니다.
#streamlit run Chap11_chatgpt_pandasAI_streamlit.py 

import streamlit as st 
import pandas as pd 
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import matplotlib


matplotlib.use("TkAgg")

#내가 사용하는 Open AI Key로 변경해야 합니다. 
llm = OpenAI(api_token="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")

st.title("PandasAI를 사용한 프롬프트 기반의 분석")

uploaded_file = st.file_uploader("분석을 위한 CS파일을 업로드하세요!", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = SmartDataframe(df, config={"llm":llm})
    st.write(df.head(3))

    prompt = st.text_area("프롬프트를 입력하세요:")

    if st.button("생성하기"):
        if prompt:
            with st.spinner("PandasAI가 답변을 생성중입니다..."):
                st.write(df.chat(prompt))
        else:
            st.warning("프롬프트에 입력하세요:")





