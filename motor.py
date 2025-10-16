import collections
import collections.abc
collections.Mapping = collections.abc.Mapping

from experta import KnowledgeEngine, Rule, AND, MATCH, TEST, P
from hechos import Bienestar

class AsistenteBienestar(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recomendaciones = []

    @Rule(Bienestar(horas_sueño=P(lambda x: x < 6)))
    def sueño_poco(self):
        self.recomendaciones.append("😴 Dormís poco, tratá de descansar al menos 7 horas.")

    @Rule(Bienestar(vasos_agua=P(lambda x: x < 5)))
    def poca_agua(self):
        self.recomendaciones.append("💧 Estás tomando poca agua, intentá llegar a 8 vasos diarios.")

    @Rule(Bienestar(ejercicio_frecuencia=MATCH.ef), TEST(lambda ef: ef in ["ninguno", "poco"]))
    def ejercicio_insuficiente(self, ef):
        self.recomendaciones.append("💪 Deberías incorporar algo de actividad física.")

    @Rule(Bienestar(comidas_sanas=MATCH.cs), TEST(lambda cs: cs in ["nunca", "a veces"]))
    def dieta_mejorable(self, cs):
        self.recomendaciones.append("🥗 Intentá comer más frutas, verduras y menos procesados.")

    @Rule(Bienestar(nivel_estrés=P(lambda x: x > 7)))
    def estres_alto(self):
        self.recomendaciones.append("😓 Tu nivel de estrés es alto. Tomate pausas, respirá y dormí mejor.")

    @Rule(Bienestar(estado_animo=MATCH.ea), TEST(lambda ea: ea in ["triste", "cansado"]))
    def animo_bajo(self, ea):
        self.recomendaciones.append("🧘 Buscá actividades que te gusten o salí a caminar.")

    @Rule(AND(Bienestar(nivel_estrés=P(lambda x: x > 7)), Bienestar(horas_sueño=P(lambda x: x < 6))))
    def estres_sueño(self):
        self.recomendaciones.append("💡 El estrés alto puede estar relacionado con la falta de sueño.")

    @Rule(AND(Bienestar(ejercicio_frecuencia="ninguno"), Bienestar(comidas_sanas="nunca")))
    def malos_habitos(self):
        self.recomendaciones.append("💡 Tus hábitos pueden afectar tu salud. Comenzá con pequeños cambios.")

