def validar_datos_antropometricos(peso, altura):
    if peso <= 0 or altura <= 0:
        return False, "⚠️ Peso y altura deben ser mayores a cero."
    if peso > 300 or altura > 2.5:
        return False, "⚠️ Los valores ingresados parecen fuera de rango. Revisalos."
    return True, "✅ Datos válidos para calcular IMC."

def calcular_imc(peso, altura):
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
    return imc, f"📏 Tu IMC es {imc:.1f} → {clasificacion}"
