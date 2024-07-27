# imc.py

def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)
    return round(imc, 2)

def clasificacion_oms(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura_cm = float(input("Ingrese su altura en cm: "))
        
        imc = calcular_imc(peso, altura_cm)
        clasificacion = clasificacion_oms(imc)
        
        print(f"Su IMC es {imc}")
        print(f"La clasificación OMS es {clasificacion}")
        
    except ValueError:
        
        print("Por favor, ingrese valores numéricos válidos para peso y altura.")

