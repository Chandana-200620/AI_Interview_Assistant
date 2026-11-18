
import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI ASSISTANT', page_icon='😍', layout='centered')
st.title('AI INTERVIEW ASSISTANT')
st.caption('Practice and prepare for your placements here')
st.caption('Launched by Chandana HL')
try:
  client=Groq(api_key=st.secrets['GROQ_API_KEY'])
except(KeyError,FileNotFoundError):
  st.error("API key is missing. Add it on advanced settings")
  st.stop
role=st.selectbox('Job Title', ['Machine learning Engineer', 'Data Analyst', 'Developer', 'Senior Manager','HR','Other'])
if role=='Other':
  st.text_input('Enter your Job Title', 'XXXXXXX')
model=st.selectbox('Model',['openai/gpt-oss-20b','openai/gpt-oss-120b'])
level=st.selectbox('Difficulty level',['Beginner','Intermediate','Advanced'])
mode=st.radio('Activity',['Generate questions','Evaluate answers','Improve the answers','Generate code'])
if mode=='Generate questions':
  count=st.slider("Number of questions",1,10,5)
elif mode=='Generate code':
  topic=st.selectbox('Topics',['SQL','AIML','PYTHON','DSA','C++','C','JAVA','HTML'])
  count=st.slider("Number of questions",1,10,5)
else:
  question=st.text_area('Enter question here')
  answer=st.text_area('Enter your answer',height=160)
  
