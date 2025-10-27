from experta import KnowledgeEngine, Rule, AND, MATCH, TEST, P
from hechos import Bienestar

class AsistenteBienestar(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recomendaciones = []
        self.puntajes = {"saludable": 0, "leve": 0, "moderado": 0, "critico": 0}
        self.estado_final = "No evaluado"

    @Rule(Bienestar(horas_sueño=P(lambda x: x < 5)))
    def sueño_critico(self):
        self.recomendaciones.append("😴 Dormís muy poco. Intentá priorizar el descanso.")
        self.puntajes["critico"] += 1

    @Rule(Bienestar(horas_sueño=P(lambda x: 5 <= x < 7)))
    def sueño_moderado(self):
        self.recomendaciones.append("😴 Tu descanso es justo. Apuntá a 7–9 horas por noche.")
        self.puntajes["moderado"] += 1

    @Rule(Bienestar(horas_sueño=P(lambda x: x > 9)))
    def sueño_excesivo(self):
        self.recomendaciones.append("🛌 Dormís muchas horas. Si te sentís cansado igual, revisá tu rutina o consultá con un profesional.")
        self.puntajes["leve"] += 1

    @Rule(Bienestar(vasos_agua=P(lambda x: x < 3)))
    def agua_critica(self):
        self.recomendaciones.append("💧 Estás muy deshidratado. Tomá al menos 6 vasos por día.")
        self.puntajes["critico"] += 1

    @Rule(Bienestar(vasos_agua=P(lambda x: 3 <= x < 6)))
    def agua_moderada(self):
        self.recomendaciones.append("💧 Podés mejorar tu hidratación. Apuntá a 6–8 vasos diarios.")
        self.puntajes["moderado"] += 1

    @Rule(Bienestar(ejercicio_frecuencia=MATCH.ef), TEST(lambda ef: ef == "ninguno"))
    def sin_ejercicio(self, ef):
        self.recomendaciones.append("💪 No estás haciendo ejercicio. Comenzá con caminatas o estiramientos.")
        self.puntajes["moderado"] += 1

    @Rule(Bienestar(ejercicio_frecuencia=MATCH.ef), TEST(lambda ef: ef == "poco"))
    def poco_ejercicio(self, ef):
        self.recomendaciones.append("💪 Podés sumar más actividad física a tu rutina.")
        self.puntajes["leve"] += 1

    @Rule(Bienestar(comidas_sanas=MATCH.cs), TEST(lambda cs: cs == "nunca"))
    def dieta_critica(self, cs):
        self.recomendaciones.append("🥗 Tu alimentación es muy pobre. Incorporá frutas y verduras.")
        self.puntajes["critico"] += 1

    @Rule(Bienestar(comidas_sanas=MATCH.cs), TEST(lambda cs: cs == "a veces"))
    def dieta_mejorable(self, cs):
        self.recomendaciones.append("🥗 Podés mejorar tu dieta. Evitá ultraprocesados.")
        self.puntajes["leve"] += 1

    @Rule(Bienestar(nivel_estrés=P(lambda x: x >= 8)))
    def estres_critico(self):
        self.recomendaciones.append("😓 Tu nivel de estrés es muy alto. Buscá pausas y técnicas de relajación.")
        self.puntajes["critico"] += 1

    @Rule(Bienestar(nivel_estrés=P(lambda x: 6 <= x < 8)))
    def estres_moderado(self):
        self.recomendaciones.append("😓 Tenés estrés moderado. Incorporá pausas activas.")
        self.puntajes["moderado"] += 1

    @Rule(Bienestar(estado_animo=MATCH.ea), TEST(lambda ea: ea in ["triste", "estresado"]))
    def animo_bajo(self, ea):
        self.recomendaciones.append("🧘 Tu estado emocional merece atención. Buscá actividades que te reconforten.")
        self.puntajes["moderado"] += 1

    @Rule(Bienestar(horas_trabajo=P(lambda x: x > 10)))
    def sobrecarga(self):
        self.recomendaciones.append("📚 Estás trabajando mucho. Intentá equilibrar tu rutina.")
        self.puntajes["moderado"] += 1

    @Rule(AND(Bienestar(ejercicio_frecuencia="ninguno"), Bienestar(comidas_sanas="nunca")))
    def malos_habitos(self):
        self.recomendaciones.append("⚠️ Tus hábitos pueden afectar tu salud. Comenzá con pequeños cambios.")
        self.puntajes["critico"] += 1

    def calcular_estado_final(self):
        if self.puntajes["critico"] >= 2:
            self.estado_final = "🔴 Riesgo crítico"
        elif self.puntajes["moderado"] >= 3:
            self.estado_final = "🟠 Riesgo moderado"
        elif self.puntajes["leve"] >= 2:
            self.estado_final = "🟡 Riesgo leve"
        else:
            self.estado_final = "🟢 Perfil saludable"
