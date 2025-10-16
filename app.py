import streamlit as st
import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from hechos import Bienestar
from motor import AsistenteBienestar
from utils import calcular_imc

st.title("🧠 Asistente de Bienestar Personal")

with st.form("formulario_bienestar"):
    edad = st.number_input("Edad", min_value=0, max_value=120)
    sexo = st.selectbox("Sexo", ["M", "F", "Otro"])
    horas_sueño = st.slider("Horas de sueño por noche", 0, 12, 7)
    ejercicio_frecuencia = st.selectbox("Frecuencia de ejercicio", ["ninguno", "poco", "regular", "diario"])
    comidas_sanas = st.selectbox("¿Comés sano?", ["nunca", "a veces", "siempre"])
    vasos_agua = st.slider("Vasos de agua por día", 0, 10, 5)
    nivel_estrés = st.slider("Nivel de estrés (1–10)", 1, 10, 5)
    estado_animo = st.selectbox("¿Cómo te sentís?", ["feliz", "cansado", "estresado", "triste"])
    horas_trabajo = st.slider("Horas de trabajo/estudio por día", 0, 12, 6)
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)
    enviar = st.form_submit_button("Evaluar bienestar")

if enviar:
    engine = AsistenteBienestar()
    engine.reset()
    engine.declare(Bienestar(
        edad=edad,
        sexo=sexo,
        horas_sueño=horas_sueño,
        ejercicio_frecuencia=ejercicio_frecuencia,
        comidas_sanas=comidas_sanas,
        vasos_agua=vasos_agua,
        nivel_estrés=nivel_estrés,
        estado_animo=estado_animo,
        horas_trabajo=horas_trabajo,
        peso=peso,
        altura=altura
    ))
    engine.run()

    st.subheader("🌈 Resumen de bienestar:")
    for r in engine.recomendaciones:
        st.write("- " + r)

    imc, clasificacion = calcular_imc(peso, altura)
    if imc:
        st.info(f"📏 Tu IMC es {imc:.1f} → {clasificacion}")
    else:
        st.warning("No se pudo calcular el IMC por falta de datos.")

    if not engine.recomendaciones:
        st.success("¡Tu nivel de bienestar es alto, mantené tus hábitos!")
    else:
        st.info("→ Consejo general: hacé pequeñas mejoras en tu rutina y revisá cómo te sentís en una semana.")


