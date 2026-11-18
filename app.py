
import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI ASSISTANT', page_icon='😍', layout='centered')
st.title('AI INTERVIEW ASSISTANT')
st.caption('Practice and prepare for your placements here')
try:
  client=Groq(api_key=st.secrets['GROQ_API_KEY'])
except(KeyError,FileNotFoundError):
  st.error("API key is missing. Add it on advanced settings")
  st.stop
role=st.selectbox('Job Title', ['Machine learning Engineer', 'Data Analyst', 'Developer', 'Senior Manager','HR','Other'])
if role=='Other':
  st.text_input('Enter your Job Title', 'XXXXXXX')

