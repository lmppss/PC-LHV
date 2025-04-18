# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZkgJpsrPLf54vXV3wMqcJXu2RLl27OGj
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Título de la app
st.title("🔍 Predicción del Poder Calorífico (PC) del Carbón")

# Cargar el modelo .pkl
modelo = joblib.load("PC_0.8722_12.04.pkl")  # Asegúrate de que este archivo esté en el mismo directorio que el script

# Inputs del usuario (10 variables, en orden y con nombres exactos)
st.header("📥 Ingresar datos del análisis químico")

sio2 = st.number_input("SiO2 ash (%)", min_value=0.0)
al2o3 = st.number_input("Al2O3 ash (%)", min_value=0.0)
fe2o3 = st.number_input("Fe2O3 ash (%)", min_value=0.0)
cao = st.number_input("CaO ash (%)", min_value=0.0)
mgo = st.number_input("MgO ash (%)", min_value=0.0)
so3 = st.number_input("SO3 ash (%)", min_value=0.0)
na2o = st.number_input("Na2O ash (%)", min_value=0.0)
k2o = st.number_input("K2O ash (%)", min_value=0.0)
s_carbon = st.number_input("S carbón (%)", min_value=0.0)
cl_carbon = st.number_input("Cl carbón (%)", min_value=0.0)

# Crear DataFrame con nombres correctos
columnas = [
    'SiO2 ash (%)', 'Al2O3 ash (%)', 'Fe2O3 ash (%)', 'CaO ash (%)',
    'MgO ash (%)', 'SO3 ash (%)', 'Na2O ash (%)', 'K2O ash (%)',
    'S carbón (%)', 'Cl carbón (%)'
]

entrada = pd.DataFrame([[
    sio2, al2o3, fe2o3, cao, mgo, so3, na2o, k2o, s_carbon, cl_carbon
]], columns=columnas)

# Botón para predecir
if st.button("🔮 Predecir Poder Calorífico"):
    pc_predicho = modelo.predict(entrada)[0]
    st.success(f"🔥 Poder Calorífico Predicho: {pc_predicho:.2f} kcal/kg")