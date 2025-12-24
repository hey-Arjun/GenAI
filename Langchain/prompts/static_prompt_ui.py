# StaticPrompt

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.header('Research Tool')

user_input = st.text_input('Enter your Prompt')

if st.button('Summarize'):
    st.text('some random text')