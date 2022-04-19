import streamlit as st
import  numpy as np

st.set_page_config(layout="wide")

st.title('Streamlit Layout App demo')

# Places text/image displays inside a collapsible container box
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')

st.sidebar.header('Input details')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', '🍣Sushi', '🌯Burrito', 'Lasagna', '🍔Hamburger', '🍕Pizza', 'Chesssy Nacchos', '🍜Noodles'])
user_likes = st.sidebar.selectbox('Your favorite indoor/outdoor game?', ['', '♟Chess', '🏸Badminton', '🎾Tennis', '🏓Ping Pong', '⚽Football', '🃏Cards', '⛳Golf'])


st.header('Output')

# Creates a tabular space within which contents can be placed inside
col1, col2, col3, col4 = st.columns(4)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')

with col4:
  if user_likes != '':
    st.write(f' *{user_likes}* is your favorite **game!**')
  else:
    st.write('👈 Please choose your favorite *game*!')


# Insert a multi-element container 
with st.container():
    st.write("This is inside the container")

    # Call any Streamlit command including custom components
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
st.image('https://blog.streamlit.io/content/images/size/w2000/2022/03/snowflake_streamlit-1.gif', width=400)
