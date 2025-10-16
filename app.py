import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
import streamlit as st
from experta import *

# ---- Definición de hechos ----
class Habitos(Fact):
    """Hechos sobre los hábitos del usuario"""
    pass

# ---- Sistema experto ----
class SistemaSalud(KnowledgeEngine):
    @Rule(Habitos(ejercicio='no', agua='poca'))
    def regla_1(self):
        self.resultado = "Deberías hacer más ejercicio y tomar más agua."

    @Rule(Habitos(ejercicio='sí', agua='poca'))
    def regla_2(self):
        self.resultado = "Vas bien con el ejercicio, pero te falta tomar más agua."

    @Rule(Habitos(ejercicio='no', agua='mucha'))
    def regla_3(self):
        self.resultado = "Tomás suficiente agua, pero te falta moverte más."

# ---- Interfaz Streamlit ----
st.title("🧠 Sistema Experto de Salud y Bienestar")

ejercicio = st.selectbox("¿Hacés ejercicio regularmente?", ["sí", "no"])
agua = st.selectbox("¿Tomás suficiente agua por día?", ["mucha", "poca"])

if st.button("Evaluar hábitos"):
    engine = SistemaSalud()
    engine.reset()
    engine.declare(Habitos(ejercicio=ejercicio, agua=agua))
    engine.run()

    resultado = getattr(engine, "resultado", "No se pudo generar una recomendación.")
    st.success(resultado)
