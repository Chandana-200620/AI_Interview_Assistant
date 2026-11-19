
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
  st.stop()
role=st.selectbox('Job Title', ['Machine learning Engineer', 'Data Analyst', 'Developer', 'Senior Manager','HR','Other'])
if role=='Other':
  st.text_input('Enter your Job Title', 'XXXXXXX')
gen_model=st.selectbox('Model',['openai/gpt-oss-20b','openai/gpt-oss-120b'])
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
if st.button('Generate AI Response', type='primary'):
  if mode in ['Evaluate answers','Improve the answers'] and (not question.strip()) or (not answer.strip()):
    st.warning('Please enter question and answer')
    st.stop()
  topics='Topic is' + topic + 'Difficulty is' + level
  if mode=='Generate questions':
    task='Generate '+str(count)+' frequently asked interview questions in which 3 are theory and 2 are problammatic.Do not give answers instead give hints.'
  elif mode=='Generate code':
    task='Generate '+str(count)+' frequently asked coding questions which are helpful for placements and which are tricky on topic' + topic + ' and give hints to solve them.'
  elif mode=='Evaluate answers':
    task='Question: ' + question + ' My answer: ' + answer + ' Evaluate this based on concepts,relevance and communication. Give the rating for each answer.'
  elif mode=='Improve the answers':
    task='Question ' + question + ' My answer: ' + answer + ' Improve the answer by considering accuracy,length of words used for better explaination, choice of words.'
  background= 'Job role: ' +role+'Difficulty level: '+level
  with st.spinner('Generating your answer.....'):
      try:
        esponses=client.chat.completions.create(
          model=gen_model,
          messages=[{'role':'system',
                     'content':'Act as a senior interviewer,both HR and Technical'},
                    {'role':'user',
                     'content':background+task}
                   ],
          temperature:0.7,
          max_tokens=1800
        )
      except Exception as e:
        st.error ("API connection was unsuccessfull!")
        st.info("Please check your API key and rate limits")
      
      

  
  

