def validar_datos_antropometricos(peso, altura):
    if peso <= 0 or altura <= 0:
        return False, "⚠️ Peso y altura deben ser mayores a cero."
    if peso > 300 or altura > 2.5:
        return False, "⚠️ Los valores ingresados parecen fuera de rango. Revisalos."
    return True, "✅ Datos válidos para calcular IMC."

def calcular_imc(peso, altura, sexo):
    valido, mensaje = validar_datos_antropometricos(peso, altura)
    if not valido:
        return None, mensaje

    imc = peso / (altura ** 2)
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Peso saludable"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    observacion = ""
    if sexo == "F" and imc >= 25:
        observacion = " (en mujeres, el IMC elevado puede tener más impacto metabólico)"
    elif sexo == "M" and imc < 18.5:
        observacion = " (en varones, el bajo peso puede afectar la masa muscular)"

    return imc, f"📏 Tu IMC es {imc:.1f} → {clasificacion}{observacion}"
