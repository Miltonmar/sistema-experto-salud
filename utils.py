def calcular_imc(peso, altura):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return imc, "Bajo peso"
        elif imc < 25:
            return imc, "Peso saludable"
        elif imc < 30:
            return imc, "Sobrepeso"
        else:
            return imc, "Obesidad"
    return None, "Datos insuficientes"
