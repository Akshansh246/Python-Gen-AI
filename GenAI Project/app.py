from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.5-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Enter your question: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)


st.markdown(
    """
    <style>
        .stApp{ 
            background-image: url("https://images.unsplash.com/photo-1746563947316-6f4cc65a66fa?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");  
            background-size: cover;
            background-attachment: fixed; 
            font-family: 'Gill-Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;  
        }
        .stApp h2{ 
            margin-top: 40px;
            color: #fff;
            font-size: 50px;
            width: 100%;
            font-weight: bold;
        }
        .stApp input{
            background-color: black;
            font-size: 20px;
        }
        .stApp input::placeholder{
            color: white;
        }
        .stApp button{
            background-color: black;
            padding: 15px;
            border-radius: 15px;
        }
        .stApp label p{
            color: white;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .stApp button p{
            font-size: 20px;
            font-weight: bold;
        }
        .st-ae{
            height: 70px;
            margin-bottom: 20px;
        }
        .stAppHeader{
            height: fit-content;
            padding: 10px;
        }
    </style>
""",unsafe_allow_html=True)

st.markdown(
"""
    <script>
        document.querySelector("input").setAttribute("placeholder", "Enter your name");
        alert("Welcome to the App! Ask any question related to SQL database");
    </script>
""",unsafe_allow_html=True)