import streamlit as st
from logic import play_game

st.set_page_config(page_title='NOT-Akinator', layout='centered')
st.title("🧠 Not-Akinator: Kasoti-style Guessing Game")

mode = st.radio("Choose your role: ", ["I'll guess", "The app guesses"])
category = st.selectbox("Choose what to guess: ", ["Persons", "Places", "Things"])
difficulty = st.selectbox("Choose your difficulty: ", ["Easy", "Medium", "Hard"])

if st.button("Start Game"):
  play_game(mode, category, difficulty)
