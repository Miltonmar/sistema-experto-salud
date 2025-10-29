# 🧠 Sistema Experto de Evaluación de Bienestar Personal

Este proyecto implementa un sistema experto para evaluar el bienestar físico y emocional de una persona, utilizando **Streamlit** para la interfaz de usuario y **Experta** como motor de inferencia basado en reglas.

---

## 📋 Descripción

El sistema permite a los usuarios ingresar datos sobre sus hábitos diarios (sueño, hidratación, alimentación, ejercicio, estrés, estado emocional, carga laboral y datos antropométricos). A partir de un conjunto de reglas predefinidas, el sistema:

- Genera recomendaciones personalizadas para mejorar el bienestar.
- Evalúa el estado general del usuario (saludable, leve, moderado o crítico).
- Calcula el Índice de Masa Corporal (IMC) con observaciones según género.

---

## ⭐ Características

- **Interfaz Intuitiva:** Desarrollada con Streamlit para una experiencia clara y amigable.
- **Motor de Reglas:** Utiliza Experta para aplicar lógica declarativa sobre los datos ingresados.
- **Evaluación Multidimensional:** Considera sueño, hidratación, alimentación, ejercicio, estrés, estado emocional y carga laboral.
- **Cálculo de IMC:** Incluye validación de datos y observaciones específicas por género.
- **Mensajes Empáticos:** Las recomendaciones se presentan con emojis y lenguaje positivo.

---

## 🧠 Reglas de Evaluación

El motor de reglas (`AsistenteBienestar`) aplica las siguientes validaciones:

- **Sueño:** Menos de 5 horas → crítico; entre 5 y 6 → moderado; más de 9 → leve.
- **Hidratación:** Menos de 3 vasos → crítico; entre 3 y 5 → moderado.
- **Ejercicio:** "ninguno" → moderado; "poco" → leve.
- **Alimentación:** "nunca" → crítico; "a veces" → leve.
- **Estrés:** ≥8 → crítico; entre 6 y 7 → moderado.
- **Estado emocional:** "triste" o "estresado" → moderado.
- **Carga laboral:** más de 10 horas → moderado.
- **Combinaciones negativas:** como no hacer ejercicio + mala alimentación → crítico.

El estado final se determina por la cantidad y severidad de los puntajes acumulados.

---

## ▶️ Cómo Ejecutar el Sistema

Para ejecutar este sistema experto en tu máquina local:

1. **Clonar el repositorio** o guardar los archivos en una carpeta:

```
app.py  
motor.py  
hechos.py  
utils.py  
requirements.txt
```

2. **Instalar dependencias** (usando pip):

```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador en: [http://localhost:8501](http://localhost:8501)

---

## 🧱 Estructura del Código

| Archivo           | Descripción                                                                 |
|-------------------|------------------------------------------------------------------------------|
| `app.py`          | Interfaz principal con Streamlit. Recoge datos, ejecuta el motor y muestra resultados. |
| `motor.py`        | Define el motor de inferencia `AsistenteBienestar` con reglas declarativas. |
| `hechos.py`       | Define la clase `Bienestar` que representa los hechos del usuario.          |
| `utils.py`        | Contiene funciones auxiliares como el cálculo de IMC y validaciones.        |
| `requirements.txt`| Lista de dependencias necesarias para ejecutar el sistema.                  |

---

## 🌐 URL de Despliegue

> [https://sistema-experto-salud-zasmz4h3e76aqwffrc65yz.streamlit.app/](https://sistema-experto-salud-zasmz4h3e76aqwffrc65yz.streamlit.app/)
