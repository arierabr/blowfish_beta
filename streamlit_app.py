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
col1, col2, col3 = st.columns(3)

# Add content to the first column
with col1:
    country01 = st.selectbox("Country 1", country_df)


# Add content to the second column
with col2:
    city01_df = tabla[tabla["Country"] == country01]["City"].unique()
    city01 = st.selectbox("City 1", city01_df)


# Add content to the third column
with col3:
    iata01_df = tabla[tabla["City"]==city01]["Code"]
    iata01 = st.selectbox("Airport 1", iata01_df)
























