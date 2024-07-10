import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='CoolSpot', page_icon='🛫')
st.title('🛫 Welcome to CoolSpot Searcher!')

#Data ----
tabla = pd.read_csv("data/tabla_st_01.csv", encoding='utf-8')
country_df = tabla.Country.unique()
#---------


# Título de la aplicación
st.header("Step 1: Choose your starting points")

# Create three columns
col1, col2, col3, col4 = st.columns(4)

# Add content to the first column
with col1:
    country01 = st.selectbox("Country 1", country_df)
    country02 = st.selectbox("Country 2", country_df)


# Add content to the second column
with col2:
    city01_df = tabla[tabla["Country"] == country01]["City"].unique()
    city01 = st.selectbox("City 1", city01_df)

    city02_df = tabla[tabla["Country"] == country02]["City"].unique()
    city02 = st.selectbox("City 2", city02_df)


# Add content to the third column
with col3:
    iata01_df = tabla[tabla["City"]==city01]["Code"]
    iata01 = st.selectbox("Airport 1", iata01_df)

    iata02_df = tabla[tabla["City"]==city02]["Code"]
    iata02 = st.selectbox("Airport 2", iata02_df)

# Add content to the forth column
with col3:
    passengers01 = st.selectbox("Travelers 1", options=[1,2,3,4,5,6])
    passengers02 = st.selectbox("Travelers 2", options=[1, 2, 3, 4, 5, 6])


# Título de la aplicación
st.header("Step 2: Choose the dates")

# Create three columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    datefrom01 = st.date_input("Departure day 1")
    datefrom02 = st.date_input("Departure day 2")

with col2:
    hourfrom01 = st.slider("Departure Hour 1", 0, 23, 12)
    hourfrom02 = st.slider("Departur Hour 2", 0, 23, 12)

with col3:
    dateto01 = st.date_input("Arrival day 1")
    dateto02 = st.date_input("Arrvival day 2")

with col4:
    hourto01 = st.slider("Arrival Hour 1", 0, 23, 12)
    hourto02 = st.slider("Arrival Hour 2", 0, 23, 12)
























