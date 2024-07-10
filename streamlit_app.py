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
st.set_page_config(page_title='Blowfish', page_icon='🐡')
st.title('🐡 Welcome to Blowfish!')



tabla = pd.read_csv("data/tabla_st_01.csv", encoding='utf-8')


# Inicializar sesión de estado
if "search_lines" not in st.session_state:
    st.session_state.search_lines = []

# Función para añadir una línea de búsqueda
def add_search_line():
    st.session_state.search_lines.append({
        "origin": "",
        "departure date": None,
        "arrival date": None,
        "class": ""
    })

# Función para eliminar una línea de búsqueda
def remove_search_line(index):
    st.session_state.search_lines.pop(index)

# Título de la aplicación
st.header("Step 1: Choose your starting points")

# Botones para añadir y eliminar líneas de búsqueda

if st.button("Add origin"):
    add_search_line()



# Mostrar las líneas de búsqueda
for index, search_line in enumerate(st.session_state.search_lines):
    cols = st.columns((1, 0.7, 0.7, 0.8, 1))
    search_line["origin"] = cols[0].selectbox(f"Origen {index+1}", tabla.Airport)
    search_line["departure date"] = cols[1].date_input(f"Fecha ida {index+1}", value=search_line["departure date"])
    search_line["arrival date"] = cols[2].date_input(f"Fecha regreso {index+1}", value=search_line["arrival date"])
    search_line["class"] = cols[3].selectbox(f"Clase {index+1}", ["Economy", "Business", "First"], index=0)
    if cols[4].button(" - ", key=f"remove_{index}"):
        remove_search_line(index)
        st.experimental_rerun()  # Recargar la página después de eliminar


# Botón para enviar el formulario
if st.button("Buscar vuelos"):
    # Aquí puedes procesar las búsquedas
    st.write("Búsquedas realizadas:")
    for search in st.session_state.search_lines:
        st.write(search)








