import requests
import json
import streamlit as st
import os
import pandas as pd
from io import StringIO

url = "https://assignment2-isd4ai77qq-uc.a.run.app/"

st.title('Amazing Question Answering Thing!')

if st.button('Available Models'):
    newurl = url+'models'
    response = requests.request("GET", newurl)
    models = response.json()
    # st.success(models)
    for i in models:
        st.success(i['name'])


name = st.text_input('name')
tokenizer = st.text_area('tokenizer')
model = st.text_area('model')

if st.button('Add the Model'):
    newurl = url + 'models'
    payload = json.dumps({
        "name": name,
        "tokenizer": tokenizer,
        "model": model
        })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("PUT", newurl, headers=headers, data=payload)
    st.success("Successfully added new model '{}'".format(response.json()[-1]['name']))

st.write('Select a model to delete from the list')
all_models= url + 'models'
response = requests.request("GET", all_models)
models = response.json()
model_list = []
for i in models:
    model_list.append(i['name'])
option = st.selectbox('Select', model_list)
st.write('You selected:', option)

if st.button('Delete the selected model'):
    updated_url = url+'models'+"?model="+option
    response1 = requests.request("DELETE", updated_url)
    st.success("Successfully deleted model '{}'".format(option))

# Inputs
question = st.text_input('Question')
context = st.text_area('Context')


# Execute question answering on button press
if st.button('Answer Question'):
    newurl = url + 'answer'
    payload = json.dumps({
        "question": question,
        "context": context
        })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", newurl, headers=headers, data=payload)
    answer = response.json()['answer']
    st.success(answer)


uploaded_file = st.file_uploader('File uploader')

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    answer_tabel = []
    for index, row in dataframe.iterrows():
        newurl = url + 'answer'
        question = row['question']
        context = row['context']
        payload = json.dumps({
            "question": question,
            "context": context
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", newurl, headers=headers, data=payload)
        answer = response.json()['answer']
        row['final_answer'] = answer
        answer_tabel.append(answer)
    dataframe["final_answer"] = answer_tabel
    st.table(dataframe)

