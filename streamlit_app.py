import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import functions as f
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='CommonGround', page_icon='🛫')
st.title('🛫 Welcome to CommonGround!')

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
with col4:
    passengers01 = st.selectbox("Travelers 1", options=[1,2,3,4,5,6])
    passengers02 = st.selectbox("Travelers 2", options=[1, 2, 3, 4, 5, 6])


# Título de la aplicación
st.header("Step 2: Choose dates and times")

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

Origins = [iata01,iata02]
Travelers = [passengers01,passengers01]
Departures_d = [datefrom01,datefrom02]
Arrivals_d = [dateto01,dateto02]
Departures_h = [hourfrom01,hourfrom02]
Arrivals_h = [hourto01,hourto01]

json = {
    "Origin": Origins,
    "Travelers":Travelers,
    "Departure_d": Departures_d,
    "Departures_h":Departures_h,
    "Arrivals_d": Arrivals_d,
    "Arrivals_h":Arrivals_h
}

st.write(json)


if st.button("Search options"):
    f.searcher(json)

import streamlit as st

# Definir la plantilla de las preguntas para los orígenes
preguntas_template = [
    "¿Cuál es el {ordinal} origen?",  # 1
    "¿Cuántas personas parten de este punto?",  # 2
    "¿Fecha de salida?",  # 3
    "¿Momento de salida?",  # 4
    "¿Fecha de llegada?",  # 5
    "¿Momento de llegada?"  # 6
]

# Inicializar el estado de la pregunta actual si no existe
if 'indice_pregunta' not in st.session_state:
    st.session_state.indice_pregunta = 0

# Inicializar el número de origen actual si no existe
if 'origen_actual' not in st.session_state:
    st.session_state.origen_actual = 1

# Inicializar el número de orígenes si no existe
if 'total_origenes' not in st.session_state:
    st.session_state.total_origenes = 0

# Inicializar un diccionario para almacenar las respuestas si no existe
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}


# Función para convertir número en ordinal en español
def numero_a_ordinal(n):
    ordinales = ['primer', 'segundo', 'tercer', 'cuarto', 'quinto', 'sexto', 'séptimo', 'octavo', 'noveno', 'décimo']
    if n <= len(ordinales):
        return ordinales[n - 1]
    return f'{n}º'  # Si excede, se usa una convención de número+º


# Función para manejar el avance de preguntas
def avanzar_pregunta():
    respuesta = st.session_state.respuesta_input

    # Validar que no esté vacía la respuesta antes de avanzar
    if not respuesta:
        st.warning("Por favor, responde a la pregunta antes de continuar.")
        return

    # Guardar la respuesta y avanzar
    pregunta_actual = st.session_state.indice_pregunta
    origen_actual = st.session_state.origen_actual
    st.session_state.respuestas[(origen_actual, pregunta_actual)] = respuesta

    # Si hemos completado todas las preguntas para el origen actual, pasamos al siguiente origen
    if pregunta_actual == len(preguntas_template):
        st.session_state.indice_pregunta = 1  # Volver a la primera pregunta del siguiente origen
        st.session_state.origen_actual += 1  # Pasar al siguiente origen
    else:
        st.session_state.indice_pregunta += 1  # Pasar a la siguiente pregunta


# Mostrar la pregunta actual y ajustar el tipo de input
indice = st.session_state.indice_pregunta
origen_actual = st.session_state.origen_actual

# Preguntar el número total de orígenes si aún no se ha hecho
if st.session_state.total_origenes == 0:
    st.session_state.total_origenes = st.number_input("¿Cuántos orígenes diferentes tenemos?", min_value=1, step=1)

# Si todavía hay orígenes que no han sido cubiertos, continuar con las preguntas
if origen_actual <= st.session_state.total_origenes:
    ordinal = numero_a_ordinal(origen_actual)
    st.write(preguntas_template[indice - 1].format(ordinal=ordinal))

    # Condicionales para definir diferentes tipos de input
    if indice == 2:  # Pregunta de número de personas
        st.number_input("Tu respuesta aquí:", key="respuesta_input", step=1)

    elif indice == 3:  # Fecha de salida
        st.date_input("Selecciona la fecha de salida:", key="respuesta_input")

    elif indice == 4 or indice == 6:  # Hora (momento de salida o llegada)
        st.time_input("Selecciona la hora:", key="respuesta_input")

    elif indice == 5:  # Fecha de llegada
        st.date_input("Selecciona la fecha de llegada:", key="respuesta_input")

    else:  # Cualquier otro input
        st.text_input("Tu respuesta aquí:", key="respuesta_input")

    # Botón para pasar a la siguiente pregunta
    st.button("Siguiente", on_click=avanzar_pregunta)

else:
    st.write("¡Gracias por responder todas las preguntas!")

# Mostrar las respuestas del usuario al final
if st.session_state.origen_actual > st.session_state.total_origenes:
    st.write("Tus respuestas fueron:")
    for origen in range(1, st.session_state.total_origenes + 1):
        ordinal = numero_a_ordinal(origen)
        st.write(f"Respuestas para el {ordinal} origen:")
        for i, pregunta in enumerate(preguntas_template, start=1):
            respuesta = st.session_state.respuestas.get((origen, i), '')
            st.write(f"{pregunta.format(ordinal=ordinal)}: {respuesta}")


















