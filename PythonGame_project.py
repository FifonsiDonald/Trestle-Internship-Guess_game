import random
import streamlit as st
import matplotlib.pyplot as plt

# import pandas as pd

# import numpy as np

# import plotly.graph_objects as go

st.set_page_config(page_title="TrestleGuessGame")


session_state = st.session_state

# session_state.cache = True

st.markdown(

    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',

    unsafe_allow_html=True,

)

st.markdown(

    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',

    unsafe_allow_html=True,

)

st.markdown("""""", unsafe_allow_html=True)


hide_streamlit_style = """ 

            <style> 

     

                header{visibility:hidden;} 

                .main { 

                    margin-top: -120px; 

                    padding-top:10px; 

                } 

                #MainMenu {visibility: hidden;} 

                footer {visibility: hidden;} 

 
 

            </style> 

             

            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown(

    """ 

    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: orange"> 

    <a class="navbar-brand" href="#"  target="_blank"> <b>Trestle Python Track</b></a>   

    </nav> 
    

""",

    unsafe_allow_html=True,

)

session_state = st.session_state
if 'reply_count' not in session_state:
    session_state['reply_count'] = {
        'error': 0,
        'win': 0,
        'loss': 0
    }
reply_count = session_state['reply_count']
    

st.text(" \n ")
st.text(" \n ")
st.text(" \n ")
st.text(" \n ")
st.text(" \n ")
st.text(" \n ")

with st.form(key="Form"):

    st.header("Guess Game :dice")

    col1, col2 = st.columns(2)

    with col1:

        extent = st.number_input("Choose DIfficulty :sunglasses:", min_value=2, max_value=10)
    with col2:

        generator = random.randint(0, extent)

        input = st.text_input("Enter the Random Number above 2")

    button = st.form_submit_button("Click")
    

    if button:

        if int(input) > extent:
            st.write("Please input a digit within the chosen Dfifficulty")
            reply_count["error"]+=1

        elif int(input) == generator:

            st.write("Guess was correct", generator)
            reply_count["win"]+=1
            st.balloons()
        else:

            st.write("Guess was incorrect, guess number was", generator)
            reply_count["loss"]+=1
secButton = st.button("Game Stats")
if secButton:
    labels = reply_count.keys()
    values = reply_count.values()

    fig, ax = plt.subplots()
    ax.bar(labels, values)

    ax.set_title('Game Stats')
    ax.set_xlabel('')
    ax.set_ylabel(' ')
    plt.xticks(rotation=45)
    st.pyplot(fig)


    
   
    
