import streamlit as st
import pandas as pd
import numpy as np
import base64

#st.image("back.jpg", use_column_width=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('back.jpg')
st.title('Game of Thrones - Episode Summarizer')

df = pd.read_csv('Season_Episode.csv')
seasons = df.columns.tolist()

season_radio = st.radio("Select a Season", seasons)
selected_season_episode_list = df[season_radio]

def remove_zeros(lst):
    return [x for x in lst if x != 0]

selected_season_episode_list=remove_zeros(selected_season_episode_list)

selected_episode = st.selectbox(f"Select value for {season_radio}", selected_season_episode_list)

submitted = st.button("Submit")

#if submitted == TRUE:
    

#selection_label = f"Season {season_radio}, Episode {selected_episode}"
out_text_temp = f"Episode Summary until Season {season_radio}, Episode {selected_episode}"

#st.text_input("Chosen Season and Episode", value=selection_label)
st.text_area(out_text_temp, value='', height=200)
